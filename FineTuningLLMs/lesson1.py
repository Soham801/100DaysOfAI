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
                       "content": prompt
               }
            ],
            options= {
                "temperature": 0.7,
            }
    )

print("\nPrompt:")
print(prompt)

print("\nResponse:")
print(response["message"]["content"])

print("-" * 120)