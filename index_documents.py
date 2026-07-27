from src.services.document_service import DocumentService
from src.vector.manager import Manager

print("Cargando documentos...")

service = DocumentService()

chunks = service.process()

print(f"{len(chunks)} chunks generados")

print("Creando base vectorial...")

db = Manager()

db.create_vectorstore(chunks)

print("Indexación finalizada.")