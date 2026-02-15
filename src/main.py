import asyncio
from parser.parser import run_parser

from constants.params import ASK_OPTIONS
from utils.utils import (
    ask_keywords,
    ask_options,
    ask_single_option,
    confirm,
    generate_url,
    print_summary,
)


def start():
    print("You can select up to 20 options in total.\n")
    total_selected = 0

    try:
        category = ask_options(
            "Category:", ASK_OPTIONS["primary_keyword"], total_selected
        )
        total_selected += len(category)

        exp_level = ask_options(
            "Experience level:",
            ASK_OPTIONS["exp_level"],
            total_selected,
        )
        total_selected += len(exp_level)

        salary = ask_single_option("Min Salary:", ASK_OPTIONS["salary"], total_selected)
        total_selected += 1 if salary is not None else 0

        company_type = ask_options(
            "Company Type:", ASK_OPTIONS["company_type"], total_selected
        )
        total_selected += len(company_type)

        employment = ask_single_option(
            "Employment Type:", ASK_OPTIONS["employment"], total_selected
        )
        total_selected += 1 if employment is not None else 0

        english_level = ask_options(
            "English Level:", ASK_OPTIONS["english_level"], total_selected
        )
        total_selected += len(english_level)

        keywords = ask_keywords(category)

        print_summary(
            Category=category,
            Experience_Level=exp_level,
            Salary_From=f"{salary}$" if salary else None,
            Company_Type=company_type,
            Employment=employment,
            English_Level=english_level,
            Keywords=keywords,
        )

        if confirm("Start parsing?"):
            url = generate_url(
                category, exp_level, salary, company_type, employment, english_level
            )

            asyncio.run(run_parser(url, keywords))
        else:
            print("exit")

    except Exception as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    start()
