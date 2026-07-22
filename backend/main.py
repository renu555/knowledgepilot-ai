from backend.app.llm.client import LLMClient

client = LLMClient()

messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    }
]

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = client.ask(messages)

    print("\nAssistant:", response)

    messages.append({
        "role": "assistant",
        "content": response
    })