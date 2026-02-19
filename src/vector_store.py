import os
import shutil
from typing import List
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

PERSIST_DIRECTORY = os.path.join(os.path.dirname(__file__), "..", "chroma_db")

def get_vector_store():
    embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
    vector_store = Chroma(
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=embeddings
    )
    return vector_store

def add_documents_to_store(documents: List[Document]):
    """
    Adds documents to the vector store.
    """
    vector_store = get_vector_store()
    vector_store.add_documents(documents)
    print(f"Added {len(documents)} documents to the store.")

def clear_store():
    """
    Clears the vector store by deleting the directory.
    """
    if os.path.exists(PERSIST_DIRECTORY):
        shutil.rmtree(PERSIST_DIRECTORY)
        print("Vector store cleared.")

def query_store(query: str, k: int = 3) -> List[Document]:
    """
    Queries the vector store for the top-k most similar documents.
    """
    vector_store = get_vector_store()
    results = vector_store.similarity_search(query, k=k)
    return results

if __name__ == "__main__":
    try:
        store = get_vector_store()
        print("Vector store initialized successfully.")
    except Exception as e:
        print(f"Failed to initialize vector store: {e}")
