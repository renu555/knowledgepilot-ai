What is an API?
Application Program Interface which helps in communication between two running applications based on defined set of rules. 
Why doesn't Python directly talk to the AI model?
Python does not directly talk to AI model because AI model needs a runtime interface like Ollama.
AI models are large binary files containing neural network weights. Python cannot execute them directly. A runtime such as Ollama loads the model into memory, manages inference, tokenization, and exposes an API for applications.
What is localhost?
Localhost refers to the current computer. It is accessed using the IP address 127.0.0.1 and allows applications running on the same machine to communicate over the network without using the internet.
Why does Ollama expose an API?
Ollama exposes an HTTP API so that external applications (such as Python programs, web applications, or desktop applications) can send prompts to the model and receive generated responses.
What would happen if Ollama wasn't running?
python would not be able to send request to AI model qwen and error would be there like Connection refused or cannot connect to localhost