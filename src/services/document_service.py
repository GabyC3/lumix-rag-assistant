from src.chunking.text_chunker import TextChunker
from src.config.settings import DOCUMENTS_PATH
from src.loaders.pdf_loader import PDFLoader


class DocumentService:

    def __init__(self):

        self.loader = PDFLoader(DOCUMENTS_PATH)
        self.chunker = TextChunker()

    def process(self):

        documents = self.loader.load_documents()

        chunks = self.chunker.split(documents)

        return chunks