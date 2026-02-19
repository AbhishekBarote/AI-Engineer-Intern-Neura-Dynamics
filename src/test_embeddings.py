import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

models_to_test = [
    "models/embedding-001",
    "models/text-embedding-004",
    "models/gemini-embedding-001"
]

for model in models_to_test:
    print(f"Testing model: {model}")
    try:
        result = genai.embed_content(
            model=model,
            content="Hello world",
            task_type="retrieval_document"
        )
        print(f"SUCCESS: {model}")
        break
    except Exception as e:
        print(f"FAILED: {model} - {e}")
