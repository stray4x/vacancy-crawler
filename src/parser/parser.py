import asyncio
import random
from parser.output import print_result, save_to_json

from playwright.async_api import ElementHandle, Page, async_playwright

from constants.keywords import KEYWORDS
from constants.parser import PAGE_SIZE, VACANCY_LIST_SELECTORS
from utils.args import ARG_HEADLESS, ARG_OUT

recommended_vacancies: list[dict] = []


async def parse_job_item(li_element: ElementHandle, kewords: list[str]):
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

        for keyword in kewords:
            if keyword in text:
                vacancy["score"] += KEYWORDS[keyword]["weight"]

        recommended_vacancies.append(vacancy)


async def parse_page_list(page: Page, kewords: list[str]):
    await page.wait_for_selector(VACANCY_LIST_SELECTORS["job_link"])
    await asyncio.sleep(random.uniform(1, 7))

    job_items = await page.query_selector_all(VACANCY_LIST_SELECTORS["job_item"])

    for li in job_items:
        await parse_job_item(li, kewords)


async def run_parser(url: str, keywords: list[str]):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=ARG_HEADLESS)
        page = await browser.new_page()

        total_pages = 0

        await page.goto(url, timeout=60000)
        await page.wait_for_selector(VACANCY_LIST_SELECTORS["jobs_total"])
        await asyncio.sleep(random.uniform(0.1, 2))

        data = {"jobs_total": 0}

        try:
            total_jobs = int(
                await page.inner_text(VACANCY_LIST_SELECTORS["jobs_total"])
            )
            total_pages = (int(total_jobs) + PAGE_SIZE - 1) // PAGE_SIZE

            data["jobs_total"] = total_jobs
        except Exception as e:
            print(e)

        await parse_page_list(page, keywords)

        if total_pages > 1:
            for current_page in range(2, total_pages):
                new_url = f"{url}&page={current_page}"

                await page.goto(new_url, timeout=60000)
                await parse_page_list(page, keywords)
                await asyncio.sleep(random.uniform(1, 5))

        match ARG_OUT:
            case "file":
                save_to_json(data, recommended_vacancies)
            case "print":
                print_result(data["jobs_total"], recommended_vacancies)
            case "both":
                save_to_json(data, recommended_vacancies)
                print_result(data["jobs_total"], recommended_vacancies)

        await browser.close()

        print("done")
