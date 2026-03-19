# LangChain Semantic Search

A specialized tool that performs **Semantic Search** on PDF documents using LangChain and ChromaDB. Unlike traditional keyword search, this project uses vector embeddings to find information based on the actual meaning and context of the query.

---

## 🔍 Features

* **Contextual Retrieval:** Uses OpenAI embeddings to understand the "intent" behind a search.
* **Vector Database:** Utilizes `ChromaDB` for efficient storage and retrieval of document fragments.
* **LangChain Integration:** Built with the LangChain framework for modular document loading and processing.
* **PDF Processing:** Automated script to split, embed, and index PDF content.

---

## 🛠️ Installation & Setup

### 1. Clone the repository
```bash
git clone [https://github.com/devanand343/langchain-semantic-search.git](https://github.com/devanand343/langchain-semantic-search.git)
cd langchain-semantic-search
```

### 2. Create a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Environment Variables
Create a .env file in the root directory and add your API key:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```

## 💻 Usage

### 1. Process and Index Documents
Run the processing script to split your PDF and save them into the vector store:
```bash
python semantic_search/process_document.py
```

### 2. Run the Search
Use the main entry point to query your indexed data:
```bash
python main.py
```
## 📁 Project Structure

- `main.py`  
  The user interface / entry point for searching.

- `semantic_search/`  
  Contains core functionality for semantic retrieval.

  - `process_document.py`  
    Logic for loading and chunking PDFs.

  - `chroma_langchain_db/`  
    (Ignored in Git) Local storage for vector embeddings.

- `requirements.txt`  
  List of required libraries (`langchain`, `chromadb`, `openai`, etc.).

- `.env.example`  
  Template for configuration.
