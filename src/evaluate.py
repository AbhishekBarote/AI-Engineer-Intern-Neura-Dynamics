import os
import sys
from dotenv import load_dotenv

# Add the project root to the python path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.rag import RAGPipeline
from src.prompts import IMPROVED_PROMPT

load_dotenv()

EVALUATION_QUESTIONS = [
    # Answerable
    "What is the time window for a full refund on defective products?",
    "Do you ship to Canada?",
    "Can I cancel my order if it has already been shipped?",
    
    # Partially Answerable (Requires synthesis or inference)
    "I bought a shirt and changed my mind. What are the conditions for returning it?", 
    
    # Unanswerable / Edge Cases
    "Hey",
    "What do you do?",
    "Do you offer student discounts?",
    "What is the CEO's name?",
    "Can I return a gift card?"
]

def evaluate():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY not found. Please set it in your .env file.")
        return

    print("Initializing RAG Pipeline for Evaluation...")
    # Initialize with improved prompt logic if implemented, for now using default
    rag = RAGPipeline()
    
    # Override generate_answer to use improved prompt for evaluation if desired
    # For now, we'll keep the simple one in rag.py unless we refactor rag.py to accept prompts
    # Let's just run it as is.

    print(f"{'='*60}")
    print(f"Running Evaluation on {len(EVALUATION_QUESTIONS)} questions")
    print(f"{'='*60}\n")

    for i, question in enumerate(EVALUATION_QUESTIONS, 1):
        print(f"Question {i}: {question}")
        try:
            answer = rag.run(question)
            print(f"Answer:\n{answer}")
        except Exception as e:
            print(f"Error: {e}")
        print("-" * 60)

if __name__ == "__main__":
    evaluate()
