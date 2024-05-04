from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os
load_dotenv()

class Settings(BaseSettings):
     version : str = os.getenv('VERSION','0.0.0')
     api_version : str = os.getenv('API_VERSION','v1')
     mongodb_database: str =  os.getenv('MONGODB_DB_NAME','db')
     mongodb_url : str = os.getenv('MONGODB_URI','mongodb://localhost:27017')

settings = Settings()
