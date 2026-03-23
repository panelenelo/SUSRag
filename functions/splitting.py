import functions.load_documents as ld
from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents():    

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True,
        )
    
    docs = ld.load_documents()
    split_docs = text_splitter.split_documents(docs)

    return split_docs
