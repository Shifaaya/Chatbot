from transformers import pipeline

chatbot = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct",
)

messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful and concise chatbot. "
            "Answer the user's questions directly. "
            "Use the conversation history when relevant."
        ),
    }
]

print("Chatbot ready! Type 'quit' to exit.\n")

while True:
    user_message = input("You: ")

    if user_message.lower() == "quit":
        print("Goodbye!")
        break

    messages.append({
        "role": "user",
        "content": user_message,
    })

    result = chatbot(
        messages,
        max_new_tokens=50,
        do_sample=True,
    )

    response = result[0]["generated_text"][-1]["content"]

    messages.append({
        "role": "assistant",
        "content": response,
    })

    print("Bot:", response)