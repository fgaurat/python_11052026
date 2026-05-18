from glob import glob
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    categories_file = os.getenv("CATEGORIES_FILE", "categories.txt")

    with open(categories_file, "r", encoding="utf-8") as file:
        categories = file.read().splitlines()


    html_files = glob('html_files/*.html')

    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()

if __name__ == '__main__':
    main()