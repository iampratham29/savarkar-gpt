import ethical_layer
from flask import Flask, request, jsonify
import pdf_loader
import embedding_utils
from chromadb.errors import InvalidCollectionException

app = Flask(__name__)

# Initialize ChromaDB collection
pdf_path = "Essentials of Hindutva.pdf"
collection_name = "my_knowledge_base"

embedding_manager = embedding_utils.EmbeddingManager()

try:
    pdf_text = pdf_loader.get_pdf_text(pdf_path)
    if pdf_text is None:
        raise Exception("Failed to load the PDF.")
    text_chunks = pdf_loader.split_text_into_chunks(pdf_text)
    collection = embedding_manager.create_collection(collection_name)
    if collection.count() == 0:
        embedding_manager.add_to_collection(collection, text_chunks, [f"doc_{i}" for i in range(len(text_chunks))])
except InvalidCollectionException:
    collection = embedding_manager.chroma_client.create_collection(
        name=collection_name, embedding_function=embedding_manager.embedding_function
    )

# API Endpoint for querying the bot
@app.route("/query", methods=["POST"])
def query_bot():
    data = request.get_json()
    query = data.get("query", "")
    if not query:
        return jsonify({"error": "Query is required"}), 400

    # Query the collection
    results = embedding_manager.query_collection(collection, query)
    context = "\n".join([" ".join(doc) if isinstance(doc, list) else doc for doc in results['documents']])
    prompt = f"Context:\n{context}\n\nQuestion: {query}\n\nAnswer:"

    # answer = f"[Your bot's response to '{query}']"  # Replace with your bot's logic
    answer = ethical_layer.generate_safe_response(prompt)
        
    return jsonify({"context": context, "answer": answer})

if __name__ == "__main__":
    app.run(debug=True)