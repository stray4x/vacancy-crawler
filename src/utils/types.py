from typing import TypedDict


class DataDict(TypedDict):
    jobs_total: int
    max_applications: int
    total_applications: int
    recommended_vacancies: list[dict]
    stack_statistics: dict[str, int]
