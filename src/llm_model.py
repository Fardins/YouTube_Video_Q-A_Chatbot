from langchain_groq import ChatGroq
from config.config import LLM_MODEL, GROQ_API_KEY


def load_llm():

    llm = ChatGroq(
        model=LLM_MODEL,
        api_key=GROQ_API_KEY,
        temperature=0.7,
        max_tokens=512 
    )

    return llm