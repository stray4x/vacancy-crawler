import asyncio
import json
import random
from datetime import datetime
from pathlib import Path

from playwright.async_api import Page, async_playwright

from utils.constants import (
    PYTHON_KEYWORDS,
    VACANCY_DETAIL_SELECTORS,
    VACANCY_LIST_SELECTORS,
)

should_recommend = ["django", "drf", "postgres", "django rest framework"]

recommended_vacancies = set()


async def parse_vacancy_page(page: Page, data: dict, page_link: str):
    print(f"Parsing: {page_link}")
    await page.goto(page_link, timeout=60000)
    await page.wait_for_selector(VACANCY_DETAIL_SELECTORS["job_title"])
    await asyncio.sleep(random.uniform(1, 4))

    title = await page.inner_text(VACANCY_DETAIL_SELECTORS["job_title"])
    print(f"Vacancy: {title}")

    try:
        desc = await page.inner_text(VACANCY_DETAIL_SELECTORS["job_desc"])
    except Exception as e:
        print(e)
        desc = ""

    try:
        skills = await page.inner_text(VACANCY_DETAIL_SELECTORS["skills"])
    except Exception as e:
        print(e)
        skills = ""

    text = (desc + " " + skills).lower()

    for key in PYTHON_KEYWORDS:
        data.setdefault(key, 0)

        if key in text:
            data[key] += 1

    for key in should_recommend:
        if key in should_recommend:
            recommended_vacancies.add(page_link)


async def parse_page_list(page: Page, data: dict):
    await page.wait_for_selector(VACANCY_LIST_SELECTORS["job_link"])
    await asyncio.sleep(random.uniform(1, 7))

    vacancy_links: list[str] = await page.eval_on_selector_all(
        VACANCY_LIST_SELECTORS["job_link"],
        "elements => elements.map(el => el.href)",
    )

    for item in vacancy_links:
        await parse_vacancy_page(page, data, item)


async def run_parser(url: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        page_size = 15
        total_pages = 0

        print(f"Opening {url}")
        await page.goto(url, timeout=60000)

        await page.wait_for_selector("header div span")
        await asyncio.sleep(random.uniform(0.1, 2))

        data = {"jobs_total": 0}

        try:
            total_jobs = int(await page.inner_text("header div span"))
            total_pages = (int(total_jobs) + page_size - 1) // page_size

            data["jobs_total"] = total_jobs
        except Exception as e:
            print(e)

        await parse_page_list(page, data)

        if total_pages > 1:
            for current_page in range(2, total_pages):
                new_url = f"{url}&page={current_page}"
                await page.goto(new_url, timeout=60000)
                await parse_page_list(page, data)

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
                    "recommended_vacancies": list(recommended_vacancies),
                },
                f,
                ensure_ascii=False,
                indent=4,
            )

        await browser.close()

        print("done")
