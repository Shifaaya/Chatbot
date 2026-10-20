from openai import OpenAI

client=OpenAI()

response=client.responses.create(model="gpt-5.6-luna", input="Hello! Explain what python is in one sentence")

print(response.output_text)