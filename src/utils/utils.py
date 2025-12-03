from utils.constants import QUERY_PARAMS


def generate_url(keyword: str, exp_level: str):
    exp_level_params = ""

    for item in QUERY_PARAMS["exp_level"]:
        exp_level_params += f"&exp_level={item}"

        if item == exp_level:
            break

    return f"https://djinni.co/jobs/?primary_keyword={keyword}{exp_level_params}"


def get_options_list(arr: list[str]):
    result = ""
    for idx, keyword in enumerate(arr, start=1):
        result += f"\n{idx}. {keyword}"

    return result
