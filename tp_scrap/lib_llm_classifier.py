import requests
from pprint import pprint


def abby_classify(html, categories, api_key):
    headers = {
        "Content-Type": "application/json",
        "X-ABBY-Key": api_key,
    }


    data = {
        "model": "gemma-4-26b-a4b-it",
        "messages": [
            {
                'role': 'user',
                'content': (
                    f'You are a website categorizer. Categorize the content '
                    f'into EXACTLY ONE of these categories: {categories}.\n\n'
                    f'RULES:\n'
                    f'- Respond with ONLY the category name, nothing else.\n'
                    f'- No explanation, no punctuation, no preamble.\n'
                    f'- Output must match exactly one of the provided categories.'
                )
            },
            {
                'role': 'user',
                'content': 'Here the content of the website in html format:\n\n' + html + '\n\nGive me the most relevant category.',
            }
        ],
        "temperature": 0.1,  # baisse la température pour plus de déterminisme
        "max_tokens": 50,    # limite physique : impossible de déborder
    }

    response = requests.post(
        "http://localhost:8080/v1/chat/completions", headers=headers, json=data)
    pprint(response.json())
