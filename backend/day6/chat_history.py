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

    if user_input == "/history":
        print("\nConversation History\n")

        for message in messages:
            print(f"{message['role']}: {message['content']}")
            print("_" * 40)

        continue

    if user_input == "/clear":
        messages = [
            {
        "role": "system",
        "content": "You are a helpful AI assistant."
            }
        ]

        print("Conversation cleared.\n")
        continue

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = client.ask(messages)

    print("Assistant:", response)

    messages.append({
        "role": "assistant",
        "content": response
    })