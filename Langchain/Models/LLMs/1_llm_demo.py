# Import Libraries

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Loaded the OpenAI API Key from .env file
load_dotenv()

# Created an OpenAI Object as llm
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

# Using that Object called the invoke function where we sent our prompt and got our response which will be stored in results
results = llm.invoke("What is the capital of India")

print(results.content)