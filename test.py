from icecream import ic
from functions.load_documents import load_single_document
from functions.splitting import split_documents
from functions.embedding import create_embedding_model
from functions.vector_store import create_chunk_ids
from functions.vector_store import db_object
from langchain_community.document_loaders import PyPDFLoader
import config

def main():
    
    db = db_object()
    #results = db.similarity_search_with_score("Qual o alvo grlicêmico em pacientes críticos?", k=5)
    results = db._collection.count()
    ic(results)

    

    
    

    



if __name__ == "__main__":
    main()

