from typing import TypedDict


class StatsData(TypedDict):
    jobs_total: int
    max_applications: int
    median_applications: float
    total_applications: int
    stack_statistics: dict[str, int]


class RecommendationsData(TypedDict):
    jobs_total: int
    recommended_vacancies: list[dict]
