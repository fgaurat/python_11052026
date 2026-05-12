import requests
from readability import Document
from markdownify import markdownify as md
from ollama import chat

def main():
    url = "https://scie-cablage.com"
    response = requests.get(url,verify=False)


    with open("categories.txt", "r", encoding="utf-8") as file:
        categories = file.read().splitlines()


    # print(response.text)
    # with open("scie-cablage.html", "w", encoding="utf-8") as file:
    #     file.write(response.text)
    doc = Document(response.text)
    clean_html = doc.summary()
    markdown = md(clean_html)
    with open("scie-cablage.md", "w", encoding="utf-8") as file:
        file.write(markdown)

    response = chat(model='gemma3', messages=[
        {
            'role': 'system',
            'content': f'You are a helpful assistant that categorizes the content of the website {url} into the following categories: {categories}.'
        },
    {
        'role': 'user',
        'content': 'Here the content of the website in markdown format:\n\n' + markdown,
    },
    ])
    print(response.message.content)        
if __name__ == '__main__':
    main()