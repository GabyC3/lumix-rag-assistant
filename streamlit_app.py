import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from src.rag.rag_pipeline import RAGPipeline

st.set_page_config(
    page_title="Lumix AI Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("Lumix AI ")

question = st.text_input(
    "Realiza una consulta"
)

if question:

    rag = RAGPipeline()

    answer, docs = rag.ask(question)

    st.subheader("Respuesta")

    st.write(answer)

    st.divider()

    st.subheader("Documentos utilizados")

    for doc in docs:

        st.caption(
            doc.metadata["source"]
        )