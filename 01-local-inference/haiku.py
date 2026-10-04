import ollama   # the library that talks to your local model

# Ask the model for a haiku. 'model' picks which brain to use;
# ':1b' is the small 1-billion version that fits 8 GB of RAM.
response = ollama.generate(
    model="llama3.2:1b",
    prompt="Write a poem about my girlfriend",
)

# The model's text comes back under the key 'response'. Print it.
print(response["response"])
