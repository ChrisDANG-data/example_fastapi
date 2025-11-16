from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_username:str
    database_password:str
    database_port:str
    database_hostname:str
    database_name:str
    fastapi_secretkey:str
    fastapi_algorithm:str
    fastapi_expire_time:int

    class Config:
        env_file=".env"

settings =Settings()

        
