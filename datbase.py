from pymongo import MongoClient,ASCENDING
from pymongo.collection import Collection
from config import settings

client:MongoClient|None=None



def connect()->None:
    global client
    client=MongoClient(settings.database_url,serverSelectionTimeoutMS=5000)#establishing connection to the MongoDB server using the provided database URL. The serverSelectionTimeoutMS parameter specifies the maximum time (in milliseconds) to wait for a server selection before throwing an error. In this case, it is set to 5000 milliseconds (5 seconds).
    col=get_collection()#getting the collection from the database. This will also trigger a server selection to ensure that the connection is established.
    col.create_index([("title", ASCENDING)])#creating an index on the "title" field of the collection. The index is created in ascending order (ASCENDING). The unique=True parameter ensures that the values in the "title" field are unique across all documents in the collection. If a document with a duplicate title is inserted, it will raise an error.
    col.create_index([("completed", ASCENDING)])


def get_collection() -> Collection:
    db = get_client()[settings.database_name]
    return db[settings.collection_name]


def get_client()->MongoClient:
    if client is None:
       connect()
    return client

def disconnect() -> None:
    global client
    if client is not None:
        client.close()
        client = None
        

