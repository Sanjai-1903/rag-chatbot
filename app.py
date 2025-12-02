import requests
from document import search

API_KEY = "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"

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "HTTP-Referer": "http://localhost",   # required
    "X-Title": "RAG Project",             # required
    "Content-Type": "application/json"
}
userinput=input("enter the question: ")
def chat(userinput):
    context=search(userinput)
    prompt_context=f"context:{context}\n\n userinput:{userinput}"
    data = {
        "model": "meta-llama/llama-3.1-70b-instruct:free ",   # must include provider prefix on OpenRouter
        "messages": [
            {
                "role": "user",
                "content": prompt_context
                
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    return (response.json()["choices"][0]["message"]["content"])

print(chat("what is the usage area"))