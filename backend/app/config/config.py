import os
from pydantic import  BaseSettings
#ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))


class Settings(BaseSettings):
    VERSION: str
    SERVICE_PORT:int
    

    # class Config:
    #     case_sensitive = True
    #     env_file = os.path.join(ROOT_DIR, ".env")

settings = Settings()