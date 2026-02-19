import streamlit as st
import os
import sys

# Add the project root to the python path so we can import modules
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.rag import RAGPipeline
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fix for Streamlit Cloud: Load secrets into os.environ
try:
    if "GOOGLE_API_KEY" in st.secrets:
        os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]
except Exception:
    pass # Run locally using .env if no secrets found

# Page Config
st.set_page_config(
    page_title="Policy Assistant RAG",
    page_icon="🤖",
    layout="centered"
)

# Header
st.title("🤖 Policy Assistant")
st.markdown("Ask me anything about our Refund, Shipping, or Cancellation policies!")

# Check API Key
if not os.getenv("GOOGLE_API_KEY"):
    st.error("⚠️ GOOGLE_API_KEY not found! Please check your .env file.")
    st.stop()

# Check for ChromaDB and Ingest if missing (Cloud Deployment Fix)
chroma_dir = os.path.join(os.path.dirname(__file__), "..", "chroma_db")
if not os.path.exists(chroma_dir):
    st.warning("⚠️ Vector Store not found. Running ingestion... (This happens once)")
    from src.ingest import ingest
    with st.spinner("Ingesting policy documents..."):
        try:
            ingest()
            st.success("Ingestion complete! Reloading...")
            st.rerun()
        except Exception as e:
            st.error(f"Ingestion failed: {e}")

# Initialize RAG Pipeline (Cached to avoid reloading on every rerun)
@st.cache_resource
def get_rag_pipeline():
    return RAGPipeline()

try:
    rag = get_rag_pipeline()
except Exception as e:
    st.error(f"Error initializing RAG Pipeline: {e}")
    st.stop()

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am the Policy Assistant. I am here to help you with questions about our Refund, Shipping, and Cancellation policies. How can I assist you today?"}
    ]

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("What is the refund policy?"):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Assistant Response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # We can modify RAGPipeline to return just the answer or answer + context
                # For now using generic run() which includes print statements we don't see here
                # But it returns the answer string.
                response = rag.run(prompt)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"An error occurred: {e}")
