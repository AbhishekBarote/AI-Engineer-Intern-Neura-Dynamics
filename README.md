# Policy Assistant RAG (Gemini Flash Edition)

A Retrieval-Augmented Generation (RAG) system that answers customer questions based on company policy documents, powered by **Google Gemini**.

## Features
- **Document Chunking**: Loads and chunks markdown policy documents.
- **Vector Search**: Uses ChromaDB and **Google Generative AI Embeddings** (`models/gemini-embedding-001`).
- **Structured Prompts**: Uses a refined prompt template to ensure grounded, polite, and accurate answers.
- **Evaluation**: Includes a script to evaluate performance on a set of test questions.
- **LLM**: Uses **Gemini 2.5 Flash** (`models/gemini-2.5-flash`).
- **User Interface**: Web-based chat interface using **Streamlit**.

## Setup

1.  **Clone the repository**:
    ```bash
    git clone <repo_url>
    cd <repo_name>
    ```

2.  **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # Windows
    # source venv/bin/activate # Linux/Mac
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment**:
    Create a `.env` file in the root directory and add your Google API key:
    ```
    GOOGLE_API_KEY=AIzaSy...
    ```

## Usage

1.  **Ingest Data** (First run only):
    Load the policy documents into the vector store:
    ```bash
    python src/ingest.py
    ```

2.  **Run the Web Interface**:
    Start the Streamlit app:
    ```bash
    streamlit run src/app.py
    ```

3.  **Run CLI Assistant**:
    ```bash
    python src/main.py
    ```

4.  **Evaluate**:
    Run the evaluation script:
    ```bash
    python src/evaluate.py
    ```
