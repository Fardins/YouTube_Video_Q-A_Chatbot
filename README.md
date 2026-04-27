# YouTube RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot built with LangChain and Streamlit that allows users to ask questions about YouTube video transcripts.

This application leverages advanced natural language processing to provide instant, accurate answers from video content without requiring users to watch the entire video. It supports multiple languages including English, Hindi, and Bangla, making it accessible to a diverse audience. The system uses HuggingFace embeddings for semantic understanding and Groq's LLaMA model for generating contextually relevant responses. With a modular architecture, it's easy to customize and extend for different use cases.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Example Usage](#example-usage)
- [Dependencies](#dependencies)
- [How It Works](#how-it-works)
- [Future Improvements](#future-improvements)
- [Author](#author)

## Features

- **YouTube Transcript Fetching**: Automatically retrieves transcripts from YouTube videos in multiple languages (English, Hindi, Bangla).
- **Text Processing**: Splits long transcripts into manageable chunks for better retrieval.
- **Embeddings**: Uses HuggingFace sentence transformers for generating text embeddings.
- **Vector Store**: Stores embeddings in FAISS for efficient similarity search.
- **LLM Integration**: Powered by Groq's LLaMA model for generating responses.
- **Interactive Chat Interface**: Streamlit-based UI for easy interaction.
- **Modular Architecture**: Clean separation of concerns with dedicated modules for each component.

## Project Structure

```
youtube_rag_langchain/
├── README.md
├── requirements.txt
├── streamlit_app.py          # Main Streamlit application
├── config/
│   └── config.py             # Configuration settings and API keys
└── src/
    ├── app.py                # (Optional) Additional app logic
    ├── embeddings.py         # Handles text embeddings using HuggingFace
    ├── llm_model.py          # Loads and configures the LLM (Groq)
    ├── prompt_template.py    # Defines the prompt template for the RAG chain
    ├── rag_chain.py          # Builds the RAG chain using LangChain
    ├── retriever.py          # Creates the retriever for document retrieval
    ├── text_splitter.py      # Splits text into chunks for processing
    ├── transcript_loader.py  # Fetches YouTube video transcripts
    └── vector_store.py       # Manages the FAISS vector store
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd youtube_rag_langchain
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Set up environment variables**:
   Create a `.env` file in the root directory with the following variables:
   ```
   HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
   GROQ_API_KEY=your_groq_api_key
   ```

2. **API Keys**:
   - **HuggingFace**: Get your token from [HuggingFace Hub](https://huggingface.co/settings/tokens)
   - **Groq**: Obtain your API key from [Groq Console](https://console.groq.com/)

3. **Configuration File**:
   The `config/config.py` file contains default settings. You can modify:
   - `EMBEDDING_MODEL`: Default is "sentence-transformers/all-MiniLM-L6-v2"
   - `LLM_MODEL`: Default is "llama-3.1-8b-instant"
   - `VIDEO_ID`: Example video ID for testing


## Example Usage

Here's a step-by-step example of using the YouTube RAG Chatbot:

1. **Start the app**:
   ```bash
   streamlit run streamlit_app.py
   ```
   Open the provided URL in your browser.

2. **Enter a Video ID**:
   Use a YouTube video ID like `dQw4w9WgXcQ` (Rick Astley - Never Gonna Give You Up).

3. **Process the Video**:
   Click "Process Video" to fetch the transcript, split it into chunks, generate embeddings, and set up the RAG chain.

4. **Ask Questions**:
   - Type: "What is the main topic of this video?"
   - The chatbot will retrieve relevant transcript sections and generate an answer using the LLM.

5. **Continue the Conversation**:
   Ask follow-up questions like "Can you explain the chorus lyrics?" to get more detailed responses based on the video content.

## Dependencies

Key dependencies include:
- `streamlit`: For the web interface
- `langchain`: Core framework for building the RAG chain
- `langchain-huggingface`: HuggingFace integrations
- `langchain-groq`: Groq LLM integration
- `faiss-cpu`: Vector database for similarity search
- `youtube-transcript-api`: For fetching YouTube transcripts
- `sentence-transformers`: For text embeddings
- `python-dotenv`: For environment variable management

See `requirements.txt` for the complete list.

## How It Works

1. **Transcript Loading**: Fetches the video transcript using YouTube Transcript API
2. **Text Splitting**: Breaks the transcript into smaller chunks for better processing
3. **Embedding Generation**: Converts text chunks into vector embeddings
4. **Vector Storage**: Stores embeddings in FAISS for efficient retrieval
5. **Retrieval**: Finds relevant document chunks based on user queries
6. **Generation**: Uses the LLM to generate answers based on retrieved context
7. **Chat Interface**: Provides an interactive UI for user interaction


## Future Improvements

- **Multi-Modal Support**: Integrate video/audio analysis alongside transcripts for richer context.
- **Advanced Chunking**: Implement semantic chunking instead of fixed-size splitting for better retrieval accuracy.
- **Model Flexibility**: Add support for multiple LLMs (OpenAI, Anthropic, etc.) with easy switching.
- **Persistent Storage**: Enable saving processed videos and chat histories to a database.
- **Batch Processing**: Allow processing multiple videos at once for comparative analysis.
- **UI Enhancements**: Add features like video timestamp links in responses and conversation export.
- **Performance Optimization**: Implement caching and async processing for faster response times.

## Author

**Md Atickur Rahman**  
email: atickft13129@gmail.com  
Data Scientist & ML Engineer
