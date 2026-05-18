import requests
from dotenv import load_dotenv
import os


load_dotenv()

headers = {
    "Content-Type": "application/json",
    "X-ABBY-Key": os.getenv("ABBY_API_KEY"),
}


data={
    "model": "gemma-4-26b-a4b-it", 
    # "input":[
    #     {"role": "user", "content": "What is the capital of France?"}
    # ],
    "messages":[
        {"role": "user", "content": "What is the capital of France?"}
    ]
}

response = requests.post("http://localhost:8080/v1/chat/completions", headers=headers, json=data)
print(response.json())