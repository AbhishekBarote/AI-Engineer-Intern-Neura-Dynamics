import os
from typing import List
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def load_documents(data_dir: str) -> List[Document]:
    """
    Loads all markdown files from the specified directory.
    """
    loader = DirectoryLoader(data_dir, glob="**/*.md", loader_cls=TextLoader)
    documents = loader.load()
    return documents

def chunk_documents(documents: List[Document], chunk_size: int = 500, chunk_overlap: int = 50) -> List[Document]:
    """
    Splits documents into smaller chunks.
    
    Rationale for chunk_size=500:
    - 500 characters is roughly 100-150 words, which is usually enough to capture a coherent policy clause 
      (e.g., "Refund Eligibility" or "Shipping Costs") without including too much irrelevant context.
    - Smaller chunks improve retrieval precision by ensuring the vector representation is focused on a specific topic.
    - Overlap of 50 ensures that sentences cut at the boundary are preserved in the next chunk.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""]
    )
    chunks = text_splitter.split_documents(documents)
    return chunks

if __name__ == "__main__":
    # Simple test
    data_path = os.path.join(os.path.dirname(__file__), "..", "data")
    if os.path.exists(data_path):
        docs = load_documents(data_path)
        print(f"Loaded {len(docs)} documents.")
        chunks = chunk_documents(docs)
        print(f"Created {len(chunks)} chunks.")
        print(f"Sample chunk: {chunks[0].page_content}")
    else:
        print(f"Data directory not found at {data_path}")
