import asyncio
import json
import random
from datetime import datetime
from pathlib import Path

from playwright.async_api import Page, async_playwright, ElementHandle

from constants.keywords import KEYWORDS
from constants.parser import PAGE_SIZE, VACANCY_LIST_SELECTORS

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

    print(f"job items: {len(job_items)}")

    for li in job_items:
        await parse_job_item(li, kewords)


async def run_parser(url: str, keywords: list[str]):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        total_pages = 0

        print(f"Opening {url}")
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

        filename = f"report_{datetime.today().strftime('%d-%m-%y')}.json"
        output_dir = Path("output")
        output_dir.mkdir(parents=True, exist_ok=True)
        file_path = output_dir / filename

        with open(
            file_path,
            mode="w",
            encoding="utf-8",
        ) as f:
            json.dump(
                {
                    **data,
                    "recommended_vacancies": sorted(
                        recommended_vacancies,
                        key=lambda x: x["score"],
                        reverse=True,
                    )[:15],
                },
                f,
                ensure_ascii=False,
                indent=4,
            )

        await browser.close()

        print("done")
