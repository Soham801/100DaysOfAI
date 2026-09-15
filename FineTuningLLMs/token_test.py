from transformers import AutoTokenizer

tokernizer = AutoTokenizer.from_pretrained(
    "meta-llama/Llama-3.2-1B"
)

text = "Hello, How are you?"

tokens = tokernizer.tokenize(text)
token_ids = tokernizer.encode(text)

print("Text: ")
print(text)