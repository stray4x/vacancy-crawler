# -------------------------------------------------------------------------------
# params
# -------------------------------------------------------------------------------


MAX_PARAMS_LIMIT = 20

QUERY_PARAMS: dict[str, list] = {
    "primary_keyword": [
        "JavaScript",
        "Fullstack",
        "Node.js",
        "React.js",
        "Python",
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

# -------------------------------------------------------------------------------
# parsing
# -------------------------------------------------------------------------------

VACANCY_LIST_SELECTORS = {
    "vacancies_count": "header span.fs-1.fw-bold.text-muted",
    "job_link": "a.job-item__title-link",
    "pagination": "ul.pagination",
    "page_link": "ul.pagination a.page-link",
}

VACANCY_DETAIL_SELECTORS = {
    "job_title": "header h1",
    "job_desc": ".job-post__description",
    "skills": "table.table",
}

PYTHON_KEYWORDS = [
    "python",
    "django",
    "fastapi",
    "fast api",
    "flask",
    "django rest framework",
    "drf",
    "celery",
    "kafka",
    "rabbitmq",
    "redis",
    "postgres",
    "mysql",
    "sql",
    "graphql",
    "selenium",
    "playwright",
    "aws",
    "docker",
    "websockets",
    "sqlalchemy",
]
