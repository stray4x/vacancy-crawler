import json
from datetime import datetime
from pathlib import Path


from utils.args import ARG_LIMIT, ARG_PATH, ARG_STACK_STAT
from utils.types import DataDict


def sort_vacancies(recommended_vacancies: list[dict]):
    return sorted(
        recommended_vacancies,
        key=lambda x: x["score"],
        reverse=True,
    )[:ARG_LIMIT]


def sort_stack_stats(stats: dict[str, int]) -> dict[str, int]:
    return dict(sorted(stats.items(), key=lambda x: x[1], reverse=True))


def save_to_json(data: DataDict):

    result = dict(data)

    if ARG_STACK_STAT:
        filename = f"djinni_stats_{datetime.today().strftime('%d%m%y_%H%M%S')}.json"
        result["stack_statistics"] = sort_stack_stats(data["stack_statistics"])
        del result["recommended_vacancies"]
    else:
        filename = f"djinni_vrecs_{datetime.today().strftime('%d%m%y_%H%M%S')}.json"
        result["recommended_vacancies"] = sort_vacancies(data["recommended_vacancies"])
        del result["stack_statistics"]

    output_dir = Path(ARG_PATH)
    output_dir.mkdir(parents=True, exist_ok=True)
    file_path = output_dir / filename

    with open(
        file_path,
        mode="w",
        encoding="utf-8",
    ) as f:
        json.dump(
            result,
            f,
            ensure_ascii=False,
            indent=4,
        )


def print_result(data: DataDict):
    print(f"[+] Total jobs: {data['jobs_total']}\n")

    if ARG_STACK_STAT:
        sorted_stats = sort_stack_stats(data["stack_statistics"])
        for idx, (tech, count) in enumerate(sorted_stats.items(), 1):
            print(f"[{idx}] {tech}: {count} vacancies")
    else:
        sorted_vacancies = sort_vacancies(data["recommended_vacancies"])
        for idx, job in enumerate(sorted_vacancies, 1):
            print(f"[+] {job['title']}")
            print(f"    {job['link']}\n")
