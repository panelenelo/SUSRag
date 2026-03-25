import argparse
from langchain_core.prompts import ChatPromptTemplate
from functions.embedding import create_embedding_model
from langchain_chroma import Chroma


PROMPT_TEMPLATE = """
    Answer the question based only on the following context:
    {context}
    ---
    Answer the question based on the above context: {question}
    """


def query_rag(query_text: str):

    embedding_funtion = create_embedding_model()
    db = Chroma(
        collection_name     = "SusDiabetes",
        embedding_function  = embedding_funtion,
        persist_directory   = "./chroma_langchain_db",
    )

    results = db.similarity_search_with_score(query_text, k=5)
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
