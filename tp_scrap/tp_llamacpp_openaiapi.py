from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8080/v1",
    api_key="sk-no-key-required",
)

response = client.chat.completions.create(
    model="gemma-4-26b-a4b-it",  # peu importe, llama-server ignore
    messages=[
        {"role": "user", "content": "What is the capital of France?"}
    ],
)
print(response.choices[0].message.content)