from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=1.5
)

results = model.invoke("explain your opinion on recent fifa world cup final in 3 lines")

print(results.content)