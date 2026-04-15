import json
from datetime import datetime
from pathlib import Path
from typing import cast
from utils.args import ARG_LIMIT, ARG_PATH, ARG_STATS
from utils.types import StatsData, RecommendationsData


def sort_vacancies(recommended_vacancies: list[dict]):
    return sorted(
        recommended_vacancies,
        key=lambda x: x["score"],
        reverse=True,
    )[:ARG_LIMIT]


def sort_stack_stats(stats: dict[str, int]) -> dict[str, int]:
    return dict(sorted(stats.items(), key=lambda x: x[1], reverse=True))


def save_stats_to_json(data: StatsData):
    filename = f"djinni_stats_{datetime.today().strftime('%d%m%y_%H%M%S')}.json"
    result = {
        **data,
        "stack_statistics": sort_stack_stats(data["stack_statistics"]),
        "avg_applications": (
            data["total_applications"] / data["jobs_total"]
            if data["jobs_total"] > 0
            else 0
        ),
    }
    _write_json(result, filename)


def save_recommendations_to_json(data: RecommendationsData):
    filename = f"djinni_vrecs_{datetime.today().strftime('%d%m%y_%H%M%S')}.json"
    result = {
        **data,
        "recommended_vacancies": sort_vacancies(data["recommended_vacancies"]),
    }
    _write_json(result, filename)


def save_to_json(data: StatsData | RecommendationsData):
    if ARG_STATS:
        save_stats_to_json(cast(StatsData, data))
    else:
        save_recommendations_to_json(cast(RecommendationsData, data))


def _write_json(result: dict, filename: str):
    output_dir = Path(ARG_PATH)
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(output_dir / filename, mode="w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)


def print_result(data: StatsData | RecommendationsData):
    if ARG_STATS:
        _print_stats(cast(StatsData, data))
    else:
        _print_recommendations(cast(RecommendationsData, data))


def _print_stats(data: StatsData):
    print(f"[+] Total jobs: {data['jobs_total']}")
    print(f"[+] Max applications per job: {data['max_applications']}")
    print(f"[+] Total applications: {data['total_applications']}")
    if data["jobs_total"] > 0:
        print(
            f"[+] Average applications per job: {data['total_applications'] / data['jobs_total']:.2f}\n"
        )

    sorted_stats = sort_stack_stats(data["stack_statistics"])
    for idx, (tech, count) in enumerate(sorted_stats.items(), 1):
        print(f"[{idx}] {tech}: {count} vacancies")


def _print_recommendations(data: RecommendationsData):
    sorted_vacancies = sort_vacancies(data["recommended_vacancies"])
    for idx, job in enumerate(sorted_vacancies, 1):
        print(f"[+] {job['title']}")
        print(f"    {job['link']}\n")
