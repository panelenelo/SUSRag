from icecream import ic
from functions.load_documents import load_single_document
from functions.splitting import split_documents
from functions.embedding import create_embedding_model
from functions.vector_store import create_chunk_ids
from langchain_community.document_loaders import PyPDFLoader
import config

def main():
    chunks = split_documents()
    id_chunks = create_chunk_ids(chunks)


    print(f"number of chunks: {len(chunks)}")
    print(f"number of chunk IDs: {len(id_chunks)}")

    print(f"First chunk metadata: {id_chunks[10:]}")

    
    

    



if __name__ == "__main__":
    main()

