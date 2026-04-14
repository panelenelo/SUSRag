from langchain_core.prompts import ChatPromptTemplate
from functions.embedding import create_embedding_model
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama



PROMPT_TEMPLATE = """
You are a highly precise and strict assistant. Your sole purpose is to answer the user's question based EXCLUSIVELY on the provided context.

Follow these rules strictly:
1. Do not use any outside knowledge, prior training data, or personal assumptions to answer the question.
2. If the answer cannot be explicitly found within the provided context, you must state exactly: "I cannot answer this question based on the provided documents." Do not attempt to guess or provide a partial answer from outside knowledge.
3. Do not add conversational filler. Be direct and concise.

Context:
{context}

---

Question: 
{question}

Answer:
"""

def query_rag(query_text: str):

    embedding_funtion = create_embedding_model()
    db = Chroma(
        collection_name     = "SusDiabetes",
        embedding_function  = embedding_funtion,
        persist_directory   = "./chroma_langchain_db",
    )

    results = db.similarity_search_with_score(query_text, k=5)
    context_text = "\n---\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    return prompt


def get_answer(prompt: str):
    model = ChatOllama(model="qwen3.5:4b")
    response_text = model.invoke(prompt)
    return response_text