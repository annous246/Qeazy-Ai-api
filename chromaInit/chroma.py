import chromadb
from chromadb.utils import embedding_functions
import os
from .categories import categories_list

folder = os.path.join(os.getcwd(), "chromaInit")

# Globals
client = None
collection = None
_embeddings = None

def get_embeddings():
    global _embeddings
    if _embeddings is None:
        print("Loading embedding model...")
        _embeddings = embedding_functions.HuggingFaceEmbeddingFunction(
            model_name="sentence-transformers/paraphrase-MiniLM-L3-v2"  # smaller model
        )
    return _embeddings

def get_collection():
    global client, collection
    if client is None:
        client = chromadb.PersistentClient(path=folder)
    if collection is None:
        collection = client.get_or_create_collection(
            name="categories",
            embedding_function=get_embeddings()
        )
        # Only insert docs if empty
        if collection.count() == 0:
            collection.upsert(
                documents=categories_list,
                ids=[str(i) for i in range(len(categories_list))]
            )
    return collection
