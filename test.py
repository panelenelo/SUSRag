from icecream import ic
from functions.load_documents import load_single_document
from functions.splitting import split_documents
from functions.embedding import create_embedding_model
from functions.vector_store import create_chunk_ids
from functions.vector_store import db_object
from functions.querys import query_rag
from functions.querys import get_answer

from langchain_community.document_loaders import PyPDFLoader
import config

def main():
    
    #results = db.similarity_search_with_score("Qual o alvo glicêmico em pacientes críticos?", k=5)
    query = "Qual o alvo glicêmico em pacientes críticos?"
    
    prompt = query_rag(query)
    print(f"Prompt:\n{prompt}\n")
    answer = get_answer(prompt)
    print(f"\nAnswer:\n{answer.pretty_print()}")
   

    

    



if __name__ == "__main__":
    main()

