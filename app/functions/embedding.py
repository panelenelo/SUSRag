from langchain_ollama import OllamaEmbeddings


# Use maybe qwen embedding
def create_embedding_model():
    
    embeddings = OllamaEmbeddings(
        model="qwen3-embedding",
    )

    return embeddings
    
