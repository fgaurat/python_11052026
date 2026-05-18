import requests
from pprint import pprint
import json
import sys
from bs4 import BeautifulSoup

def extract_homepage_signals(html: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    
    signals = {
        "title": None,
        "meta_description": None,
        "og_description": None,
        "h1": [],
        "h2": [],
        "h3": [],
        "p": [],
        "json_ld": [],
        "body_text": None,
    }
    
    # Title
    if soup.title and soup.title.string:
        signals["title"] = soup.title.string.strip()
    
    # Metas
    for name, key in [("description", "meta_description"), 
                       ("og:description", "og_description")]:
        tag = soup.find("meta", attrs={"name": name}) or \
              soup.find("meta", attrs={"property": name})
        if tag and tag.get("content"):
            signals[key] = str(tag["content"]).strip()
    
    # Headings
    for level in ["h1", "h2", "h3"]:
        signals[level] = [
            h.get_text(strip=True) 
            for h in soup.find_all(level) 
            if h.get_text(strip=True)
        ][:10]  # max 10 par niveau
    
    # JSON-LD (Organization, LocalBusiness, etc.)
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string or "")
            signals["json_ld"].append(data)
        except (json.JSONDecodeError, TypeError):
            pass
    
    return signals



def abby_classify(html, categories, api_key):
    json_content = json.dumps(extract_homepage_signals(html))
    # print(extract_homepage_signals(html))
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
                'content': 'Here the content of the website in json format:\n\n' + json_content + '\n\nGive me only the most relevant category.',
            }
        ],
        "temperature": 0.1,  # baisse la température pour plus de déterminisme
        # "max_tokens": 500,    # limite physique : impossible de déborder
    }

    response = requests.post(
        "http://localhost:8080/v1/chat/completions", headers=headers, json=data)

    return response.json()
