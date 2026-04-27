from config.config import VIDEO_ID

from src.transcript_loader import get_transcript
from src.text_splitter import split_text
from src.embeddings import load_embeddings
from src.vector_store import create_vector_store
from src.retriever import create_retriever
from src.llm_model import load_llm
from src.prompt_template import get_prompt
from src.rag_chain import build_chain


def main():

    print("Loading transcript...")

    transcript = get_transcript(VIDEO_ID)

    docs = split_text(transcript)

    embeddings = load_embeddings()

    vector_store = create_vector_store(docs, embeddings)

    retriever = create_retriever(vector_store)

    model = load_llm()

    prompt = get_prompt()

    rag_chain = build_chain(retriever, prompt, model)

    while True:

        question = input("\nAsk Question (type exit to quit): ")

        if question.lower() == "exit":
            break

        answer = rag_chain.invoke(question)

        print("\nAnswer:", answer)


if __name__ == "__main__":
    main()