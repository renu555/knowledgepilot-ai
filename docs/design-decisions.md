# Design Decisions

## DD-001
We chose Ollama because the application must run entirely on-premises without sending organizational data to external cloud services.

---

## DD-002
The LLM interaction is isolated in a dedicated client module to support replacing the inference engine in the future with minimal code changes.

---

## DD-003
Configuration is stored separately from application logic so models and runtime settings can be changed without modifying the application code.