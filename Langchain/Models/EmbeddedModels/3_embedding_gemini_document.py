from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2", dimensions=32
)

documents = [
    "Delhi is the capital of India"
    "Mumbai is the capital of Maharashtra"
    "Banglore is the capital of Karnataka"
]

results = embeddings.embed_documents(documents)
print(str(results))