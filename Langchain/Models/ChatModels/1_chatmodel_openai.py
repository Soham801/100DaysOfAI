from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

results = model.invoke("What is Neural Networks? Answer in 5 points like a physics teacher who is driving a car")

print(results.content)