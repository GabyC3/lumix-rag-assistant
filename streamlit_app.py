import streamlit as st

from src.services.document_service import DocumentService

st.set_page_config(
    page_title="Lumix AI Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Lumix AI ")

st.write("Sistema de consulta inteligente basado en documentación.")

service = DocumentService()

documents = service.load()

st.success(f"Se cargaron {len(documents)} páginas.")

pdfs = sorted(
    set(
        doc.metadata["source"].split("\\")[-1]
        for doc in documents
    )
)

st.subheader("Documentos encontrados")

for pdf in pdfs:
    st.write(f" {pdf}")