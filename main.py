from semantic_search import process_document

file_source = "./semantic_search/codewave-com-insights-build-ai-agents-beginners-guide-.pdf"

def semantic_search(source: str):

    # load pdf document
    long_docs = process_document.load_pdf_file(source=source)
    if long_docs is None:
        print("Could not load the document....skipping splitting")
        return []
    
    # split pdf document
    chunks = process_document.split_document(docs=long_docs)

    # creating embedding and storing to vector_db persist memory of chomadb
    vector_store = process_document.create_vector_embedding(chunks=chunks)

    return None

def search_internal_db(user_query: str):
    return process_document.search_vector_db(query=user_query)


if __name__ == "__main__":
    semantic_search(source=file_source)
    
    user_query = input("What do you want to search about AI agents today?\n>>> ")
    
    try:
        search_results = search_internal_db(user_query=user_query)
        
        if search_results:
            # Safely print the first result
            print(f"\nFound {len(search_results)} results. Best match:")
            print(search_results[0].page_content[:500]) # Print first 500 chars
        else:
            print("The search returned no results.")
            
    except Exception as e:
        print(f"An error occurred during execution: {e}")