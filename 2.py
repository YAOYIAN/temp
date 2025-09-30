import requests

url = "http://localhost:11434/api/generate"
payload = {
        "model": "deepseek-r1:70b",
    "prompt": "Why is the sky blue?",
    "stream": False
}

res = requests.post(url, json=payload)
print(res.json()["response"])
