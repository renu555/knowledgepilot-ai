from ollama import chat
question = input("Ask me anything: ")
response = chat(
    model="qwen2.5:3b",
    messages=[
        {
            "role": "user",
            "content": question
        }
    ]
)
print("\nAI:\n")
print(response.message.content)
