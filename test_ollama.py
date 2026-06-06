from ollama import Client

client = Client(host="http://192.168.1.120:11434")

response = client.chat(
    model="llama3.1:8b",
    messages=[
        {
            "role": "user",
            "content": "Scrivi solo la parola OK",
        }
    ],
)

print(response.message.content)