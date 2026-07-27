import streamlit as st

from src.chat import Chat

st.set_page_config(
    page_title="Lumix AI Assistant",
    page_icon="🤖",
    layout="wide"
)

Chat().render()