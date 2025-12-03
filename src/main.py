import asyncio
from parser.parser import run_parser

from ui import ask_option, confirm, print_summary
from utils.constants import QUERY_PARAMS
from utils.utils import generate_url


def start():
    try:
        keyword = ask_option(
            "Choose category you want to parse:", QUERY_PARAMS["primary_keyword"]
        )
        exp_level = ask_option(
            "Choose experience level (everything below will be included):",
            QUERY_PARAMS["exp_level"],
        )

        print_summary(keyword, exp_level)

        if confirm("Start parsing?"):
            url = generate_url(keyword, exp_level)

            asyncio.run(run_parser(url))
        else:
            print("exit")

    except Exception as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    start()
