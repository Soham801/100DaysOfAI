# Import Libraries

from langchain_openai import OpenAI
from dotenv import load_dotenv

# Loaded the OpenAI API Key from .env file
load_dotenv()

# Created an OpenAI Object as llm
llm = OpenAI(model = 'gpt-3.5-turbo-instruct')

# Using that Object called the invoke function where we sent our prompt and got our response which will be stored in results
results = llm.invoke("What is the capital of India")

print(results)