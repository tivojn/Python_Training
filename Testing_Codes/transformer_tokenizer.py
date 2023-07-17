from transformers import AutoTokenizer

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# The text to count tokens for
text = """From that day forth, Luna became a guardian of the Whispering Woods, a symbol of hope and compassion. Visitors from far and wide came seeking her wisdom and blessings. She never forgot the value of kindness, for it was her pure heart that had unlocked the magic within the forest and the spirits that dwelled there."""

# Encode the text to count tokens
encoded = tokenizer.encode(text)

# Count the number of tokens
num_tokens = len(encoded)

print(f"Number of tokens in the text: {num_tokens}")

