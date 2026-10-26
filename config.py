import os
from dotenv import load_dotenv

load_dotenv()
class Setting:
    database_url=os.getenv("MONGO_URI")
    database_name=os.getenv("MONGO_DATABASE")
    collection_name=os.getenv("COLLECTION_NAME")

settings=Setting()
print(settings.database_url,settings.database_name,settings.collection_name)
