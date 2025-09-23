import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
import os
from .categories import categories_list


folder = os.path.join(os.getcwd(),"chromaInit")


_embeddings = None
def get_embeddings():
    global _embeddings
    if _embeddings is None:
        print("Loading embedding model...")
        _embeddings = embedding_functions.HuggingFaceEmbeddingFunction(
            model_name="sentence-transformers/paraphrase-MiniLM-L3-v2"  # smaller model
        )
    return _embeddings



client = chromadb.PersistentClient(path=folder)

collection = client.get_or_create_collection("categories")
collection.upsert(
   documents = categories_list
,
     ids=[str(i) for i,element in enumerate(categories_list)]
 )
element=collection.get(ids=[str(i) for i,element in enumerate(categories_list)])