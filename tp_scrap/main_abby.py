import requests
from readability import Document
from markdownify import markdownify as md
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()


def main():
    url = "https://scie-cablage.com"
    response = requests.get(url, verify=False)

    categories_file = os.getenv("CATEGORIES_FILE", "categories.txt")

    with open(categories_file, "r", encoding="utf-8") as file:
        categories = file.read().splitlines()

    # print(response.text)
    # with open("scie-cablage.html", "w", encoding="utf-8") as file:
    #     file.write(response.text)
    doc = Document(response.text)
    clean_html = doc.summary()
    markdown = md(clean_html)
    with open("scie-cablage.md", "w", encoding="utf-8") as file:
        file.write(markdown)

    headers = {
        "Content-Type": "application/json",
        "X-ABBY-Key": os.getenv("ABBY_API_KEY"),
    }


    data = {
        "model": "gemma-4-26b-a4b-it",
        "messages": [
            {
                'role': 'user',
                'content': (
                    f'You are a website categorizer. Categorize the content of {url} '
                    f'into EXACTLY ONE of these categories: {categories}.\n\n'
                    f'RULES:\n'
                    f'- Respond with ONLY the category name, nothing else.\n'
                    f'- No explanation, no punctuation, no preamble.\n'
                    f'- Output must match exactly one of the provided categories.'
                )
            },
            {
                'role': 'user',
                'content': 'Here the content of the website in markdown format:\n\n' + markdown + '\n\nGive me the most relevant category.',
            }
        ],
        "temperature": 0.1,  # baisse la température pour plus de déterminisme
        "max_tokens": 50,    # limite physique : impossible de déborder
    }

    response = requests.post(
        "http://localhost:8080/v1/chat/completions", headers=headers, json=data)
    pprint(response.json())


if __name__ == '__main__':
    main()
