from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader


class PDFLoader:

    def __init__(self, documents_path: str):
        self.documents_path = Path(documents_path)

    def load_documents(self):

        documents = []

        pdf_files = list(self.documents_path.glob("*.pdf"))

        for pdf in pdf_files:

            loader = PyPDFLoader(str(pdf))

            documents.extend(loader.load())

        return documents