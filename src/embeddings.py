import os

from langchain_huggingface import HuggingFaceEmbeddings
from config.config import EMBEDDING_MODEL, HF_TOKEN

os.environ["HF_TOKEN"] = HF_TOKEN

def load_embeddings():

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    return embeddings