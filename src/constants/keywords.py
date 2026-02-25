from constants.categories import FULLSTACK, JAVASCRIPT, NODEJS, PYTHON, REACT

KEYWORDS = {
    # ---------------------------------------------------------------------------
    # JavaScript
    # ---------------------------------------------------------------------------
    "typescript": {"categories": [REACT, FULLSTACK, JAVASCRIPT, NODEJS], "weight": 3},
    "react": {"categories": [REACT, FULLSTACK, JAVASCRIPT], "weight": 2},
    "next.js": {"categories": [REACT, FULLSTACK, JAVASCRIPT], "weight": 2},
    "redux": {"categories": [REACT, JAVASCRIPT], "weight": 1},
    "zustand": {"categories": [REACT, JAVASCRIPT], "weight": 1},
    "react-query": {"categories": [REACT, JAVASCRIPT], "weight": 1},
    "tailwind": {"categories": [REACT, FULLSTACK], "weight": 1},
    "material ui": {"categories": [REACT], "weight": 1},
    "electron": {"categories": [JAVASCRIPT], "weight": 2},
    "vue": {"categories": [JAVASCRIPT, FULLSTACK], "weight": 2},
    "angular": {"categories": [JAVASCRIPT, FULLSTACK], "weight": 2},
    "jest": {"categories": [JAVASCRIPT, REACT, NODEJS], "weight": 1},
    "trpc": {"categories": [JAVASCRIPT, FULLSTACK], "weight": 1},
    # ---------------------------------------------------------------------------
    # Node.js
    # ---------------------------------------------------------------------------
    "node": {"categories": [NODEJS, FULLSTACK], "weight": 3},
    "express": {"categories": [NODEJS, FULLSTACK], "weight": 2},
    "nest": {"categories": [NODEJS, FULLSTACK], "weight": 2},
    "fastify": {"categories": [NODEJS], "weight": 2},
    "mongoose": {"categories": [NODEJS], "weight": 1},
    "prisma": {"categories": [NODEJS, FULLSTACK], "weight": 1},
    "typeorm": {"categories": [NODEJS], "weight": 1},
    "drizzle": {"categories": [NODEJS], "weight": 1},
    "sequelize": {"categories": [NODEJS], "weight": 1},
    # ---------------------------------------------------------------------------
    # Python
    # ---------------------------------------------------------------------------
    "python": {"categories": [PYTHON], "weight": 3},
    "django": {"categories": [PYTHON], "weight": 2},
    "drf": {"categories": [PYTHON], "weight": 2},
    "fastapi": {"categories": [PYTHON], "weight": 2},
    "flask": {"categories": [PYTHON], "weight": 2},
    "celery": {"categories": [PYTHON], "weight": 1},
    "sqlalchemy": {"categories": [PYTHON], "weight": 1},
    # ---------------------------------------------------------------------------
    # Databases / Infra
    # ---------------------------------------------------------------------------
    "postgres": {"categories": [NODEJS, PYTHON, FULLSTACK], "weight": 1},
    "mysql": {"categories": [NODEJS, PYTHON, FULLSTACK], "weight": 1},
    "mongodb": {"categories": [NODEJS, FULLSTACK], "weight": 1},
    "graphql": {"categories": [NODEJS, FULLSTACK], "weight": 1},
    "docker": {"categories": [NODEJS, PYTHON, FULLSTACK], "weight": 1},
    "aws": {"categories": [NODEJS, PYTHON, FULLSTACK], "weight": 1},
    "websocket": {"categories": [NODEJS], "weight": 1},
    "redis": {"categories": [NODEJS, PYTHON], "weight": 1},
    "rabbitmq": {"categories": [NODEJS, PYTHON], "weight": 1},
    "kafka": {"categories": [NODEJS, PYTHON], "weight": 1},
    "kubernetes": {"categories": [NODEJS, PYTHON], "weight": 1},
}
