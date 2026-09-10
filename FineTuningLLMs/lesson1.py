import ollama

response = ollama.chat(
    model="llama3.2",
    messages= [
        {
            "role": "user",
            "content": "Explain what a Python Function is"
        }
    ]
)

print(response["message"]["content"])