from typing import TypedDict


class DataDict(TypedDict):
    jobs_total: int
    recommended_vacancies: list[dict]
    stack_statistics: dict[str, int]
