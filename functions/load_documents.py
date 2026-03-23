import config
from langchain_community.document_loaders import PyPDFDirectoryLoader

def load_documents():
    loader = PyPDFDirectoryLoader(config.DATA_PATH)
    docs = loader.load()
    return docs