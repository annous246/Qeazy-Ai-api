import chromadb
from chromadb.config import Settings
import os
from .categories import categories_list
folder = os.path.join(os.getcwd(),"chromaInit")
client = chromadb.PersistentClient(path=folder)

collection = client.get_collection("categories")
collection.upsert(
   documents = categories_list
,
     ids=[str(i) for i,element in enumerate(categories_list)]
 )
element=collection.get(ids=[str(i) for i,element in enumerate(categories_list)])