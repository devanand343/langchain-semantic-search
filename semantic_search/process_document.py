from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

load_dotenv()

# Loads pdf file from target source
def load_pdf_file(source: str):
    """
    waits until the target pdf file is loaded using async.
    require vaiable source

    source: -> str (pdf file path)
    """
    print("loading pdf file...")
    try:
        loader = PyPDFLoader(file_path=source)
        return loader.load()
    except Exception as e:
        print("File loading issue....", e)

# splits any pdf file into small chunks
def split_document(docs: list[Document]) -> list[Document]:
    """
    takes list of Document object as docs and return list of Document objects in smaller sizes.
    docs: -> list[Document] (langchain core Document object)
    """
    print("splitting texts into smaller chunks....")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 700,
        chunk_overlap = 100,
        add_start_index = True
    )

    print("Chunking done")

    return text_splitter.split_documents(docs)

# using openai embeddings and Chromadb for vector embedding
def create_vector_embedding(chunks: list[Document]):
    """
    embed chunks and store into local storage in designatd path.
    the the folder exists, saves if not creates and then saves.
    this functions is for Chromadb vector embedding and takes list of Document objects and return a vector db 'chroma'
    chunks: -> list[Document] 
    """
    print("Creating vector embeddings...wait")
    model = OpenAIEmbeddings(model="text-embedding-3-large")
    try:
        vector_db = Chroma.from_documents(
            documents= chunks,
            embedding= model,
            persist_directory="./semantic_search/chroma_langchain_db",
            collection_name= "ai_agents_collection",
        )

        return vector_db
    except Exception as e:
        print("problem in vector embedding creation.\n", e) 

    

# run similarity search based on user query
def search_vector_db(query: str) -> list[Document]:

    """
    runs a similarity search on user query and return Document objects to 3 nearest results.
    query: -> str
    """
    print("retriving results for your query...\nwait...")
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

    vector_db = Chroma(
        persist_directory= "./semantic_search/chroma_langchain_db",
        embedding_function= embeddings,
        collection_name="ai_agents_collection"
    )

    search_results = vector_db.similarity_search(
        query= query,
        k=3
    )
    print("HERE ARE RESULTS I FOUND \n\n")
    return search_results


