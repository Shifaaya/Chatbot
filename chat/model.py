from transformers import pipeline
import torch

torch.set_num_threads(4)
print("CPU threads:", torch.get_num_threads())

chatbot = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct",
) 
print("Qwen device:", chatbot.device)