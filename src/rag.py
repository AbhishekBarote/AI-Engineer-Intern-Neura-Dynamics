import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from src.vector_store import query_store
from src.prompts import IMPROVED_PROMPT

load_dotenv()

class RAGPipeline:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
    
    def generate_answer(self, query: str, context_docs) -> str:
        """
        Generates an answer using the LLM and the retrieved context.
        """
        context_text = "\n\n".join([doc.page_content for doc in context_docs])
        
        # Use improved prompt structure
        prompt_text = IMPROVED_PROMPT.format(context=context_text, question=query)
        
        messages = [
            SystemMessage(content="You are a helpful customer support assistant."),
            HumanMessage(content=prompt_text)
        ]
        
        response = self.llm.invoke(messages)
        return response.content
    
    def run(self, query: str):
        """
        End-to-end RAG flow: Retrieve -> Generate
        """
        print(f"Querying: {query}")
        retrieved_docs = query_store(query)
        print(f"Retrieved {len(retrieved_docs)} documents.")
        
        if not retrieved_docs:
            print("No documents found. Letting LLM handle it (potential greeting).")
            # Pass empty context to the LLM so it can use the prompt instructions (e.g. for greetings)
            return self.generate_answer(query, [])
            
        answer = self.generate_answer(query, retrieved_docs)
        return answer

if __name__ == "__main__":
    rag = RAGPipeline()
    print("RAG Pipeline initialized.")
