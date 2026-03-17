from embedding import embeddings
from langchain_chroma import Chroma

vector_store = Chroma(
    collection_name     = "SusDiabetes",
    embedding_function  = embeddings,
    persist_directory   = "./chroma_langchain_db",
)
