import os
import streamlit as st
from dotenv import load_dotenv

# Load .env (for local development)
load_dotenv()


# ---------- API KEY LOADERS ----------

def get_secret(key_name: str):
    # 1. Try Streamlit secrets (for deployed app)
    try:
        value = st.secrets[key_name]
        if value:
            return value
    except Exception:
        pass

    # 2. Try environment variables (for local)
    value = os.getenv(key_name)
    if value:
        return value

    # 3. Not found
    st.error(f"{key_name} not found! Set it in Streamlit secrets or .env file.")
    st.stop()


# ---------- LOAD KEYS ----------

GROQ_API_KEY = get_secret("GROQ_API_KEY")
HF_TOKEN = get_secret("HUGGINGFACEHUB_API_TOKEN")


# ---------- CONFIG ----------

VIDEO_ID = "qYNweeDHiyU"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "llama-3.1-8b-instant"