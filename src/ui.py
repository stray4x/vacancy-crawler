from utils.utils import get_options_list


def print_summary(keyword: str, exp_level: str):
    print(
        f"""
Chosen options:

Category: {keyword}
Experience: {exp_level} and below
"""
    )


def ask_option(title: str, arr: list[str]) -> str:
    print(title + get_options_list(arr))
    idx = int(input("Enter a number: "))
    return arr[idx - 1]


def confirm(message: str) -> bool:
    return input(f"{message} (y/n): ").lower() == "y"
