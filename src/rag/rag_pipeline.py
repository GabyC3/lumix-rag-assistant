from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

from src.config.settings import *
from src.prompts.rag_prompt import RAG_PROMPT
from src.vector.manager import Manager


class RAGPipeline:

    def __init__(self):

        self.llm = ChatGoogleGenerativeAI(
            model=MODEL_NAME,
            temperature=0
        )

        self.retriever = Manager().get_retriever()

        self.chain = (
            RAG_PROMPT
            | self.llm
            | StrOutputParser()
        )

    def ask(self, question):

        docs = self.retriever.invoke(question)

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        answer = self.chain.invoke(
            {
                "context": context,
                "question": question
            }
        )

        return answer, docs