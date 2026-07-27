from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from src.config.settings import *

class Manager:

    def __init__(self):

        self.embedding = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL
        )

        self.db = Chroma(
            persist_directory=str(VECTOR_DB_PATH),
            embedding_function=self.embedding
        )

    def get_retriever(self):

        return self.db.as_retriever(
            search_kwargs={
                "k": TOP_K
            }
        )