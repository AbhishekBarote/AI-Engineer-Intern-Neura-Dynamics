import os
import sys
from dotenv import load_dotenv

# Add the project root to the python path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.rag import RAGPipeline

load_dotenv()

def main():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY not found. Please set it in your .env file.")
        return

    rag = RAGPipeline()
    print("Welcome to the Policy Assistant! (Type 'quit' to exit)")
    
    while True:
        query = input("\nAsk a question: ")
        if query.lower() in ["quit", "exit", "bye"]:
            break
        
        try:
            answer = rag.run(query)
            print(f"\nAnswer:\n{answer}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
