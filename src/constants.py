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

query_params = {
    "primary_keyword": ["Python", "JavaScript", "React.js", "Fullstack", "Node.js"],
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
    "employment": ["remote", "parttime", "office"],
    "company_type": ["agency", "outsource", "outstaff", "product", "startup"],
    "english_level": [
        "no_english",
        "basic",
        "pre",
        "intermediate",
        "upper",
        "fluent",
        "proficient",
        "native",
    ],
    "salary": [500, 10000],  # step - 500
}
