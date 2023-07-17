from tokenizers import Tokenizer, models, pre_tokenizers, decoders, trainers

# Create a Byte-level BPE tokenizer
tokenizer = Tokenizer(models.BPE())

# Customize the tokenizer settings (optional)
tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel()
tokenizer.decoder = decoders.ByteLevel()
tokenizer.trainer = trainers.BpeTrainer(special_tokens=["[PAD]", "[UNK]", "[CLS]", "[SEP]", "[MASK]"])

# The text to count tokens for
text = """From that day forth, Luna became a guardian of the Whispering Woods, a symbol of hope and compassion. Visitors from far and wide came seeking her wisdom and blessings. She never forgot the value of kindness, for it was her pure heart that had unlocked the magic within the forest and the spirits that dwelled there."""

# Encode the text to count tokens
encoded = tokenizer.encode(text)

# Count the number of tokens
num_tokens = len(encoded.tokens)

print(f"Number of tokens in the text: {num_tokens}")

