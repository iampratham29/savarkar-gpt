import pdf_loader
import embedding_utils
import ethical_layer
import config
from chromadb.errors import InvalidCollectionException

def main():
    """Main function to orchestrate the process."""
    pdf_path = "Essentials of Hindutva.pdf"  # Replace with the path to your PDF
    collection_name = "my_knowledge_base"  # Name for your ChromaDB collection

    # 1. Load and Chunk the PDF
    pdf_text = pdf_loader.get_pdf_text(pdf_path)
    if pdf_text is None:
        return  # Exit if PDF loading failed

    text_chunks = pdf_loader.split_text_into_chunks(pdf_text)

    # 2. Initialize Embedding Manager and Create/Load Chroma Collection
    embedding_manager = embedding_utils.EmbeddingManager()
    try:
        collection = embedding_manager.create_collection(collection_name)
    except InvalidCollectionException:
    # If the collection doesn't exist, create it
        collection = embedding_manager.chroma_client.create_collection(
        name=collection_name, embedding_function=embedding_manager.embedding_function
        )

    # 3. Add Chunks to the Chroma Collection (if it's empty)
    if collection.count() == 0: # Check if collection is empty
        embedding_manager.add_to_collection(collection, text_chunks, [f"doc_{i}" for i in range(len(text_chunks))])
        print("Added documents to the collection.")
    else:
        print("Collection already contains documents. Skipping addition.")


    # 4.  User Interaction Loop
    while True:
        query = input("Ask a question (or type 'exit'): ")
        if query.lower() == "exit":
            break

        # 5. Retrieve Relevant Documents
        results = embedding_manager.query_collection(collection, query)
        # Flatten the list of lists into a single list of strings
        context = "\n".join([" ".join(doc) if isinstance(doc, list) else doc for doc in results['documents']])

        # 6. Create Prompt for Ollama

        prompt = f"Context:\n{context}\n\nQuestion: {query}\n\nAnswer:"

        # 7. Generate Response with Ethical Constraints
        response = ethical_layer.generate_safe_response(prompt)
        print(f"Answer: {response}\n")

if __name__ == "__main__":
    main()