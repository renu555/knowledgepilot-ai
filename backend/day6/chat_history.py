from backend.app.llm.client import LLMClient

client = LLMClient()

messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    }
]

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "/exit":
        print("Goodbye!")
        break

    if user_input.lower() == "/history":
        print("\nConversation History:\n")

        for message in messages:
            print(f"{message['role'].capitalize()}: {message['content']}\n")

        continue

    if user_input.lower() == "/clear":
        messages = [
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            }
        ]
    if user_input.lower() == "/stats":
        system_count=0
        user_count=0
        assistant_count=0
        print("stats of the messages!")
        for message in messages:
            if(message['role']=='user'):
                user_count+=1
            elif(message['role']=='system'):
                system_count+=1
            else:
                assistant_count+=1                 

        print("User count: ", user_count)
        print("\nAssistant count: ", assistant_count)
        print("\nSystem count: ", system_count)
        continue

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