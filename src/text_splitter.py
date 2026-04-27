from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    documents = splitter.create_documents([text])

    return documents