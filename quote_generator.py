# embeddings.py
from dotenv import load_dotenv
import os
from huggingface_hub import login
from langchain_community.vectorstores import Chroma
from sentence_transformers import SentenceTransformer
import json

# Load environment variables from .env file
load_dotenv()

# Log in to Hugging Face using the token from .env
login(token=os.getenv("HUGGING_FACE_TOKEN"))

# Load service data from JSON
with open("data/services.json", "r") as f:
    service_data = json.load(f)

# Load embeddings model from Hugging Face
embedding_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Define a custom embedding function
class CustomEmbeddingFunction:
    def __init__(self, model):
        self.model = model

    def embed_documents(self, texts):
        return self.model.encode(texts)

# Create an instance of the custom embedding function
embedding_function = CustomEmbeddingFunction(embedding_model)

# Create Chroma DB
vector_db = Chroma.from_texts(
    texts=[s["name"] for s in service_data],
    embedding=embedding_function,  # Pass the custom embedding function
    metadatas=service_data
)