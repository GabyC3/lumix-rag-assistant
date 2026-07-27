import streamlit as st

from src.rag.rag_pipeline import RAGPipeline
from src.config.settings import MODEL_NAME


class Chat:

    def __init__(self):

        if "messages" not in st.session_state:
            st.session_state.messages = []

        if "rag_pipeline" not in st.session_state:
            st.session_state.rag_pipeline = RAGPipeline()

        self.pipeline = st.session_state.rag_pipeline

    def render(self):

        st.title("Lumix AI")

        st.caption(
            "Asistente inteligente basado en documentación interna."
        )

        st.sidebar.markdown("### Estado")

        st.sidebar.success("Sistema operativo")

        st.sidebar.title("Lumix")

        st.sidebar.markdown("---")

        st.sidebar.write(f"Modelo: {MODEL_NAME}")

        if st.sidebar.button("🗑 Limpiar conversación"):

            st.session_state.messages = []

            st.rerun()


        for message in st.session_state.messages:

            with st.chat_message(message["role"]):

                st.markdown(message["content"])

                if (
                    message["role"] == "assistant" and "documents" in message):

                    st.markdown("---")

                    st.markdown("##### Documentos consultados")

                    shown = set()

                    for doc in message["documents"]:

                        source = doc.metadata.get("source","Documento")

                        if source not in shown:

                            st.write(f"• {source}")

                            shown.add(source)

        question = st.chat_input(
            "Escribe tu consulta..."
        )

        if question:

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": question
                }
            )

            with st.chat_message("user"):

                st.markdown(question)

            with st.chat_message("assistant"):

                with st.spinner("Consultando documentación..."):

                    try:

                       answer, docs = self.pipeline.ask(question)

                    except Exception as error:

                     answer = ("Ocurrió un error al consultar la documentación.")

                     docs = []

                     st.error(error)

                    st.markdown(answer)

                    if docs:

                        st.markdown("---")

                        st.markdown("##### Documentos consultados")

                        shown = set()

                        for doc in docs:

                            source = doc.metadata.get("source","Documento")

                            if source not in shown:

                                st.write(f"• {source}")

                                shown.add(source)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer,
                    "documents": docs
                }
            )