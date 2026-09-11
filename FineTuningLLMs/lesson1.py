import ollama


prompts = [
    "Explain Python dictionaries.",
    "Explain Python dictionaries to a 10-year-old.",
    "Explain Python dictionaries like a university professor.",
    "Explain Python dictionaries using only a code example",
]


for prompt in prompts:

    response = ollama.chat(
        model="llama3.2",
            messages= [
               {
                       "role": "user",
                       "content": "Explain Python Dictionaires."
               }
    ]
    )

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

