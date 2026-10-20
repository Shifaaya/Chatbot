import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


model_name = "Qwen/Qwen2.5-0.5B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(model_name)


text = "I like Python"

tokens = tokenizer.tokenize(text)
token_ids = tokenizer.encode(text)

print("Tokens:")
print(tokens)

print("\nToken IDs:")
print(token_ids)


# Convert token IDs into a PyTorch tensor
input_ids = torch.tensor([token_ids])

# Get the embedding layer
embedding_layer = model.get_input_embeddings()

# Convert token IDs into embeddings
embeddings = embedding_layer(input_ids)


print("\nEmbedding shape:")
print(embeddings.shape)

print("\nFirst token embedding:")
print(embeddings[0][0])
