import requests
from readability import Document
from markdownify import markdownify as md

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
if __name__ == '__main__':
    main()