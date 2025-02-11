from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_hostname: str = "postgres"
    database_port: str = "5433"
    database_username: str = "postgres"
    database_password: str = "password"
    database_name: str = "provimate"
    secret_key: str = "secret"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    use_credentials: bool = True
    validate_certs: bool = True
    portal_path: str = "http://localhost"

    class Config:
        env_file = ".env"

settings = Settings()
