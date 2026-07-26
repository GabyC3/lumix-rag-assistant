from src.loaders.pdf_loader import PDFLoader


class DocumentService:

    def __init__(self):

        self.loader = PDFLoader("data/documents")

    def load(self):

        return self.loader.load_documents()