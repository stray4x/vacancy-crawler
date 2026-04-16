import asyncio
import random
import re
from parser.output import print_result, save_to_json

from playwright.async_api import ElementHandle, Page, async_playwright

from constants.keywords import KEYWORDS
from constants.parser import PAGE_SIZE, VACANCY_LIST_SELECTORS
from utils.args import ARG_HEADLESS, ARG_OUT, ARG_STATS
from utils.types import StatsData, RecommendationsData

applications_count: list[int] = []

stats_data: StatsData = {
    "jobs_total": 0,
    "max_applications": 0,
    "median_applications": 0,
    "total_applications": 0,
    "stack_statistics": {},
}

recommendations_data: RecommendationsData = {
    "jobs_total": 0,
    "recommended_vacancies": [],
}


def calculate_median(values: list[int]) -> float:
    values = sorted(values)
    n = len(values)
    mid = n // 2

    if n % 2 == 0:
        return (values[mid - 1] + values[mid]) / 2
    else:
        return values[mid]


async def parse_job_applications(li_element: ElementHandle):
    views_block = await li_element.query_selector(
        VACANCY_LIST_SELECTORS["views_responses"]
    )

    if views_block:
        spans = await views_block.query_selector_all(".text-nowrap")

        if len(spans) >= 2:
            span_text = await spans[1].evaluate("el => el.textContent")
            match = re.search(r"\d+", span_text)

            if match:
                count = int(match.group())
                stats_data["total_applications"] += count
                applications_count.append(count)

                if count > stats_data["max_applications"]:
                    stats_data["max_applications"] = count


async def parse_recommendation(li_element: ElementHandle, keywords: list[str]):
    job_link_data = await li_element.eval_on_selector(
        VACANCY_LIST_SELECTORS["job_link"],
        "el => ({ href: el.href, text: el.innerText.trim() })",
    )

    link: str = job_link_data["href"]
    title = job_link_data["text"]

    desc_block = await li_element.query_selector(VACANCY_LIST_SELECTORS["job_desc"])

    if desc_block is not None:
        vacancy = {"title": title, "link": link, "score": 0}

        text: str = await desc_block.evaluate("el => el.textContent")
        text = text.lower()

        for keyword in keywords:
            if keyword in text:
                vacancy["score"] += KEYWORDS[keyword]["weight"]

        recommendations_data["recommended_vacancies"].append(vacancy)


async def parse_stack_stats(li_element: ElementHandle, keywords: list[str]):
    desc_block = await li_element.query_selector(VACANCY_LIST_SELECTORS["job_desc"])

    if desc_block is not None:
        await parse_job_applications(li_element)
        text: str = await desc_block.evaluate("el => el.textContent")
        text = text.lower()

        for keyword in keywords:
            if keyword in text:
                stats_data["stack_statistics"][keyword] = (
                    stats_data["stack_statistics"].get(keyword, 0) + 1
                )


async def parse_job_item(li_element: ElementHandle, keywords: list[str]):
    if ARG_STATS:
        await parse_stack_stats(li_element, keywords)
    else:
        await parse_recommendation(li_element, keywords)


async def parse_page_list(page: Page, keywords: list[str]):
    await page.wait_for_selector(VACANCY_LIST_SELECTORS["job_link"])
    await asyncio.sleep(random.uniform(1, 7))

    job_items = await page.query_selector_all(VACANCY_LIST_SELECTORS["job_item"])

    for li in job_items:
        await parse_job_item(li, keywords)


async def run_parser(url: str, keywords: list[str]):
    async with async_playwright() as p:
        print("Parsing...")

        browser = await p.chromium.launch(headless=ARG_HEADLESS)
        page = await browser.new_page()

        total_pages = 0

        await page.goto(url, timeout=60000)
        await page.wait_for_selector(VACANCY_LIST_SELECTORS["jobs_total"])
        await asyncio.sleep(random.uniform(0.1, 2))

        await parse_page_list(page, keywords)

        if total_pages > 1:
            for current_page in range(2, total_pages):
                new_url = f"{url}&page={current_page}"
                await page.goto(new_url, timeout=60000)
                await parse_page_list(page, keywords)
                await asyncio.sleep(random.uniform(1, 5))

        if len(applications_count) > 0:
            stats_data["median_applications"] = calculate_median(applications_count)
        data = stats_data if ARG_STATS else recommendations_data

        try:
            total_jobs = int(
                await page.inner_text(VACANCY_LIST_SELECTORS["jobs_total"])
            )
            total_pages = (total_jobs + PAGE_SIZE - 1) // PAGE_SIZE
            data["jobs_total"] = total_jobs
        except Exception as e:
            print(e)

        match ARG_OUT:
            case "file":
                save_to_json(data)
            case "print":
                print_result(data)
            case "both":
                save_to_json(data)
                print_result(data)

        await browser.close()
        print("done")
