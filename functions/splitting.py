from functions.load_documents import load_directory
from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents():    

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=130,
        add_start_index=True,
    )
    
    try:
        docs = load_directory()
    except Exception as e:
        print(f"Error loading documents: {e}")
        exit(1)

    try:
        chunks = text_splitter.split_documents(docs)
    except Exception as e:
        print(f"Error splitting documents: {e}")
        exit(1)

    return chunks

