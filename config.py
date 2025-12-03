import os
from dotenv import load_dotenv

load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

class Config:
    deepseek_api_key = DEEPSEEK_API_KEY

config_obj = Config()