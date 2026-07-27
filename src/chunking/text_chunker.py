from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.config.settings import (
    CHUNK_OVERLAP,
    CHUNK_SIZE
)


class TextChunker:

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )

    def split(self, documents):

        return self.splitter.split_documents(documents)