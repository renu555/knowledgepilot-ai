from ollama import chat
from backend.app.config.settings import MODEL_NAME


class LLMClient:
    def __init__(self, model=MODEL_NAME):
        self.model = model

    def ask(self, messages):
        response = chat(
            model=self.model,
            messages=messages
        )

        return response.message.content