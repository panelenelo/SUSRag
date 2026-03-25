import config
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.document_loaders import PyPDFLoader


def load_directory():

    try:
        loader = PyPDFDirectoryLoader(config.DATA_PATH)
    except Exception as e:
        print(f"Error loading documents: {e}")
        exit(1)

    docs = loader.load()

    print(f"Number of documents loaded: {len(docs)}")

    return docs

def load_single_document():

    try:
        loader = PyPDFLoader(config.DATA_PATHtwo)
    except Exception as e:
        print(f"Error loading document: {e}")
        exit(1)

    docs = loader.load()

    print(f"Number of documents loaded: {len(docs)}")

    return docs
