# Submission Guide

Here is the information you need to fill out your submission form.

## 1. GitHub Repository Link
I have prepared the code locally. You need to push it to your GitHub account:
1.  Create a new repository on GitHub (e.g., `policy-rag-assistant`).
2.  Run these commands in your terminal:
    ```bash
    git add .
    git commit -m "Final submission: RAG with Gemini Flash and Streamlit UI"
    git branch -M main
    git remote add origin https://github.com/<YOUR_USERNAME>/policy-rag-assistant.git
    git push -u origin main
    ```
3.  **Submit the link**: `https://github.com/<YOUR_USERNAME>/policy-rag-assistant`

## 2. Deployed Link
This requires deploying the app. The easiest way is **Streamlit Community Cloud**:
1.  Push your code to GitHub (step above).
2.  Go to [share.streamlit.io](https://share.streamlit.io/).
3.  Connect your GitHub account.
4.  Select your new repository (`policy-rag-assistant`).
5.  Set "Main file path" to `src/app.py`.
6.  **IMPORTANT**: In "Advanced settings" -> "Secrets", add your API key:
    ```
    GOOGLE_API_KEY=AIzaSy...
    ```
7.  Click **Deploy**.
8.  **Submit the link**: The URL Streamlit gives you (e.g., `https://policy-rag-assistant.streamlit.app`).

## 3. Loom Video Link
You need to record a short (1-2 min) video.
1.  Open [Loom](https://www.loom.com/).
2.  Record your screen showing the Streamlit app.
3.  **Demo Script**:
    *   **Intro**: "Hi, I built a Policy Assistant using Gemini Flash and Streamlit."
    *   **Greeting**: Type "Hey" -> Show it introduces itself.
    *   **Policy Question**: Type "What is the refund policy?" -> Show the answer.
    *   **Edge Case**: "How to travel to Mumbai?" -> Show it politely declines as out-of-scope.
4.  **Submit the link**: The link to your recorded video.

## 4. Additional Details (Project Summary)
You can likely copy this for the "Short Note" section:
> "I built a RAG system using LangChain and Google Gemini 2.5 Flash. I implemented a custom chunking strategy (500 chars) for policy documents and stored vectors in ChromaDB. I focused heavily on Prompt Engineering to ensure the bot handles greetings ('Hey') naturally and politely declines out-of-scope questions ('How to travel...'). The interface is built with Streamlit for a chat-like experience. I also included an automated evaluation script to test edge cases."
