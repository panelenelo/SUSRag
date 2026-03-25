from functions.embedding import create_embedding_model
from functions.splitting import split_documents
from langchain_chroma import Chroma


def add_to_chroma():

    vector_store = Chroma(
        collection_name     = "SusDiabetes",
        embedding_function  = create_embedding_model(),
        persist_directory   = "./chroma_langchain_db",
    )

    chunks = split_documents()
    chunk_ids = create_chunk_ids(chunks)

    try:
        inserted_ids = vector_store.add_documents(documents=chunks, ids=chunk_ids)
    except Exception as e:
        print(f"Error adding documents to vector store: {e}")
        exit(1)

    print(f"Inserted document IDs: {inserted_ids}")

    vector_store.persist()


def create_chunk_ids(chunks):
    
    # This will create IDs like "data/monopoly.pdf:6:2"
    # Page Source : Page Number : Chunk Index

    chunk_ids = []

    last_page_id = None
    current_chunk_index = 0

    for chunk in chunks:
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        current_page_id = f"{source}:{page}"

        # If the page ID is the same as the last one, increment the index.
        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0

        # Calculate the chunk ID.
        chunk_id = f"{current_page_id}:{current_chunk_index}"
        last_page_id = current_page_id

        chunk_ids.append(chunk_id)

    return chunk_ids

    
    
        