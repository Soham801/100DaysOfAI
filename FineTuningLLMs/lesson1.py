import ollama

response = ollama.chat(
    model="llama3.2",
    messages= [
        {
            "role": "system",
            "content": '''
                        You are a Python tutor for beginners.
                        Always explain concept simply.
                        Always Provide a small example.

                        '''
        },
        {
            "role": "user",
            "content": "Explain Python Dictionaires."
        }
    ]
)

print(response["message"]["content"])

