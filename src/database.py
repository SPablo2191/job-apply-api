from odmantic import AIOEngine
from src.config import settings as global_settings
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient(global_settings.mongodb_url)
engine = AIOEngine(client=client, database=global_settings.mongodb_database)
