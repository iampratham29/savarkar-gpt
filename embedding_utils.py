from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.utils import embedding_functions
import config

class EmbeddingManager:
    def __init__(self, db_path=config.CHROMA_DB_PATH, embedding_model_name=config.EMBEDDING_MODEL):
        self.embedding_model = SentenceTransformer(embedding_model_name)
        self.chroma_client = chromadb.PersistentClient(path=db_path)
        self.embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=embedding_model_name)

    def create_collection(self, collection_name):
        """Creates a ChromaDB collection if it doesn't exist."""
        try:
            collection = self.chroma_client.get_collection(name=collection_name, embedding_function=self.embedding_function)
            print(f"Collection '{collection_name}' already exists. Using existing collection.")
            return collection
        except ValueError:  # Collection does not exist
            print(f"Creating new collection: '{collection_name}'")
            collection = self.chroma_client.create_collection(name=collection_name, embedding_function=self.embedding_function)
            return collection

    def embed_text(self, text):
        """Embeds a single piece of text."""
        return self.embedding_model.encode(text)

    def add_to_collection(self, collection, documents, ids):
        """Adds documents and their embeddings to the ChromaDB collection."""
        embeddings = [self.embed_text(doc) for doc in documents]
        collection.add(
            embeddings=embeddings,
            documents=documents,
            ids=ids
        )

    def query_collection(self, collection, query_text, n_results=5):
        """Queries the ChromaDB collection and returns the most relevant documents."""
        query_embedding = self.embed_text(query_text)
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )
        return results