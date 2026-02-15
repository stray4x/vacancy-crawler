from urllib.parse import quote_plus

from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from constants.params import MAX_PARAMS_LIMIT, QUERY_PARAMS
from constants.keywords import KEYWORDS


def ask_options(message: str, options: list[str], total_selected: int) -> list[str]:
    if total_selected >= MAX_PARAMS_LIMIT:
        return []
    remaining = MAX_PARAMS_LIMIT - total_selected

    transformer = (
        lambda res: f"Total params: {len(res) + total_selected} / {MAX_PARAMS_LIMIT}"
    )

    result: list[str] = inquirer.checkbox(
        message=message,
        choices=[Choice(value=option, name=option) for option in options],
        validate=lambda res: len(res) <= remaining,
        invalid_message=f"{MAX_PARAMS_LIMIT} params maximum",
        transformer=transformer,
    ).execute()

    if None in result:
        return []

    return result


SKIP_OPTION = "-- skip --"


def ask_single_option(message: str, options: list, total_selected: int) -> str | None:
    if total_selected >= MAX_PARAMS_LIMIT:
        return None

    choices = [SKIP_OPTION] + options

    def transformer(res) -> str:
        if res != SKIP_OPTION:
            current_total = total_selected + 1
        else:
            current_total = total_selected

        return f"Total params: {current_total} / {MAX_PARAMS_LIMIT}"

    result = inquirer.select(
        message=message,
        choices=choices,
        transformer=transformer,
    ).execute()

    if result == SKIP_OPTION:
        return None

    print(result)

    return result


def get_keywords_for_categories(categories: list[str]) -> list[str]:
    result: list[str] = []

    for keyword, meta in KEYWORDS.items():
        if any(cat in meta["categories"] for cat in categories):
            result.append(keyword)

    return result


def ask_keywords(categories: list[str]):

    choices = get_keywords_for_categories(categories)

    result: list[str] = inquirer.checkbox(
        message="Keywords for recommendations",
        choices=[Choice(value=option, name=option) for option in choices],
        validate=lambda res: len(res) >= 1,
        invalid_message="Pick at least 1",
    ).execute()

    return result


def print_summary(**kwargs):
    print("\nChosen options:")

    for label, value in kwargs.items():
        if value is None or (isinstance(value, list) and not value):
            continue

        display = ", ".join(value) if isinstance(value, list) else str(value)
        print(f"{label.replace('_', ' ')}: {display}")


def confirm(message: str) -> bool:
    return input(f"{message} (y/n): ").lower() == "y"


# todo:rewrite


def generate_url(
    primary_keyword: list[str],
    exp_level: list[str],
    salary: str | None,
    company_type: list[str],
    employment: str | None,
    english_level: list[str],
) -> str:
    selections = {
        "primary_keyword": primary_keyword,
        "exp_level": exp_level,
        "salary": salary,
        "company_type": company_type,
        "employment": employment,
        "english_level": english_level,
    }

    query_parts = []

    for key, value in selections.items():
        if value is None or (isinstance(value, list) and not value):
            continue

        if isinstance(value, list):
            for item in value:
                if key == "english_level":
                    mapped = QUERY_PARAMS["english_level"][0].get(item)
                    if mapped:
                        query_parts.append(f"{key}={quote_plus(mapped)}")
                else:
                    query_parts.append(f"{key}={quote_plus(item)}")
        else:
            query_parts.append(f"{key}={quote_plus(str(value))}")

    query_string = "&".join(query_parts)

    return f"https://djinni.co/jobs/?{query_string}"
