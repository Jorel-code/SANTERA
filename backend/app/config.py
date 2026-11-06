import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-change-me")

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg://santera:santera@localhost:5432/santera_dev"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False