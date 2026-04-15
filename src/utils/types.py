from typing import TypedDict


# TODO: relete
class DataDict(TypedDict):
    jobs_total: int
    max_applications: int
    total_applications: int
    recommended_vacancies: list[dict]
    stack_statistics: dict[str, int]


class StatsData(TypedDict):
    jobs_total: int
    max_applications: int
    total_applications: int
    stack_statistics: dict[str, int]


class RecommendationsData(TypedDict):
    jobs_total: int
    recommended_vacancies: list[dict]
