import streamlit as st

from src.transcript_loader import get_transcript
from src.text_splitter import split_text
from src.embeddings import load_embeddings
from src.vector_store import create_vector_store
from src.retriever import create_retriever
from src.llm_model import load_llm
from src.prompt_template import get_prompt
from src.rag_chain import build_chain



st.set_page_config(page_title="YouTube RAG Chatbot", layout="wide")

st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>YouTube Video Q&A Chatbot</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center;'>Ask questions from any YouTube video transcript</p>",
    unsafe_allow_html=True
)


# -----------------------------
# INPUT + BUTTON (SIDE BY SIDE)
# -----------------------------

col1, col2 = st.columns([2, 1])  # input wider, button smaller

with col1:
    video_id = st.text_input(
        "Enter YouTube Video ID",
        placeholder="Example: qYNweeDHiyU"
    )

with col2:
    st.write("")  # spacing to align button vertically
    process_btn = st.button("Process Video")


# -----------------------------
# CENTERED VIDEO PREVIEW
# -----------------------------

if video_id:
    st.markdown("---")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown("### Video Preview")
        st.video(f"https://www.youtube.com/watch?v={video_id}")



# -----------------------------
# PROCESS VIDEO
# -----------------------------

if process_btn:

    with st.spinner("Processing video transcript..."):

        transcript = get_transcript(video_id)

        docs = split_text(transcript)

        embeddings = load_embeddings()

        vector_store = create_vector_store(docs, embeddings)

        retriever = create_retriever(vector_store)

        model = load_llm()

        prompt = get_prompt()

        rag_chain = build_chain(retriever, prompt, model)

        st.session_state.rag_chain = rag_chain

        st.success("Video processed successfully!")


# -----------------------------
# CHAT INTERFACE (ChatGPT Style)
# -----------------------------

if "rag_chain" in st.session_state:

    st.markdown("---")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Show previous messages
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat input (bottom fixed)
    user_input = st.chat_input("Ask anything about the video...")

    if user_input:

        # Save user message
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        # Show user message
        with st.chat_message("user"):
            st.markdown(user_input)

        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):

                response = st.session_state.rag_chain.invoke(user_input)

                # If response is dict (LangChain), handle safely
                if isinstance(response, dict):
                    answer = response.get("answer", str(response))
                else:
                    answer = str(response)

                st.markdown(answer)

        # Save assistant response
        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })


# -----------------------------
# RESET BUTTON
# -----------------------------

if st.button("Refresh Chat"):
    st.session_state.messages = []
    st.rerun()