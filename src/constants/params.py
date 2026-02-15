from constants.categories import FULLSTACK, JAVASCRIPT, NODEJS, PYTHON, REACT


MAX_PARAMS_LIMIT = 20

QUERY_PARAMS: dict[str, list] = {
    "primary_keyword": [
        JAVASCRIPT,
        FULLSTACK,
        NODEJS,
        REACT,
        PYTHON,
    ],
    "exp_level": [
        "no_exp",
        "1y",
        "2y",
        "3y",
        "4y",
        "5y",
        "6y",
        "7y",
        "8y",
        "9y",
        "10y",
    ],
    "salary": [500, 10000],  # step - 500
    "company_type": ["agency", "outsource", "outstaff", "product", "startup"],
    "employment": ["remote", "parttime", "office"],
    "english_level": [
        {
            "No English": "no_english",
            "Beginner": "basic",
            "Pre-Intermediate": "pre",
            "Intermediate": "intermediate",
            "Upper-Intermediate": "upper",
            "Fluent (Advanced)": "fluent",
            "Proficient": "proficient",
            "Native": "native",
        }
    ],
}

ASK_OPTIONS = {
    # multiple options
    "primary_keyword": QUERY_PARAMS["primary_keyword"],
    "exp_level": QUERY_PARAMS["exp_level"],
    "company_type": QUERY_PARAMS["company_type"],
    "english_level": list(QUERY_PARAMS["english_level"][0].keys()),
    # single option
    "salary": [
        str(QUERY_PARAMS["salary"][0] + i)
        for i in range(0, QUERY_PARAMS["salary"][1], 500)
    ],
    "employment": QUERY_PARAMS["employment"],
}
