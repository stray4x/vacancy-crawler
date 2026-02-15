import json
from datetime import datetime
from pathlib import Path

from utils.args import ARG_LIMIT, ARG_PATH


def save_to_json(data: dict, recommended_vacancies: list[dict]):
    filename = f"djinni_{datetime.today().strftime('%d%m%y_%H%M%S')}.json"
    output_dir = Path(ARG_PATH)
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
                )[:ARG_LIMIT],
            },
            f,
            ensure_ascii=False,
            indent=4,
        )


def print_result(jobs_total: int, recommended_vacancies: list[dict]):
    print(f"[+] Total jobs: {jobs_total}\n")
    for idx, job in enumerate(recommended_vacancies, 1):
        print(f"[+] {job['title']}")
        print(f"    {job['link']}\n")
