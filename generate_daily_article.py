import os
import datetime
import requests

# Hugging Face API token
HF_TOKEN = os.getenv("HF_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Generate article
today = datetime.datetime.now().strftime("%Y-%m-%d")
topic = "Simple health tips anyone can follow"
prompt = f"Write a 500-word friendly and SEO-optimized blog article about: {topic}. Include a catchy title and useful tips."

output = query({"inputs": prompt})
result = output[0]["generated_text"]

# Save article
filename = f"articles/{today}.html"
os.makedirs("articles", exist_ok=True)
with open(filename, "w", encoding="utf-8") as f:
    f.write(f"<html><head><title>{topic}</title></head><body><h1>{topic}</h1><p>{result}</p><hr><p><a href='/index.html'>Back to Home</a></p></body></html>")

print("✅ Article generated and saved:", filename)
