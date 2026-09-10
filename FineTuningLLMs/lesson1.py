import ollama

response = ollama.chat(
    model="llama3.2",
    messages= [
        {
            "role": "user",
            "context": "Explain what a Python Function is"
        }
    ]
)