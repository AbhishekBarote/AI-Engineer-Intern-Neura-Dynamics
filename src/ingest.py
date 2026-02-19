import os
import sys
from dotenv import load_dotenv

# Add the project root to the python path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.data_processing import load_documents, chunk_documents
from src.vector_store import add_documents_to_store, clear_store

load_dotenv()

def ingest():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY not found in environment variables.")
        print("Please create a .env file with your API key.")
        return

    data_path = os.path.join(os.path.dirname(__file__), "..", "data")
    if not os.path.exists(data_path):
        print(f"Data directory not found at {data_path}")
        return

    # Clear existing store to avoid duplicates during dev
    print("Clearing existing vector store...")
    clear_store()

    print("Loading documents...")
    raw_docs = load_documents(data_path)
    print(f"Loaded {len(raw_docs)} documents.")

    print("Chunking documents...")
    chunks = chunk_documents(raw_docs)
    print(f"Created {len(chunks)} chunks.")

    print("Adding to vector store...")
    try:
        add_documents_to_store(chunks)
        print("Ingestion complete!")
    except Exception as e:
        print(f"Error during ingestion: {e}")

if __name__ == "__main__":
    ingest()
