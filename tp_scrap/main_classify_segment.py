from glob import glob
from dotenv import load_dotenv
import os
import csv
import lib_llm_classifier
from pprint import pprint

load_dotenv()

def main():
    categories_file = os.getenv("CATEGORIES_FILE", "categories.txt")

    with open(categories_file, "r", encoding="utf-8") as file:
        categories = file.read().splitlines()

    api_key = os.getenv("ABBY_API_KEY")

    html_files = glob('html_files/*.html')

    all_categories = []
    for html_file in html_files:
        # html_files/125_technideal.com.html
        file_director,file_name = html_file.split('/')
        code_client, domain = file_name.split('_')
        domain = domain.replace('.html', '')
        print(code_client)
        print(domain)
        category = "Industry"
        category_dict = {
            "code_client": code_client,
            "domain": domain,
            "category": category
        }
        all_categories.append(category_dict)
        # with open(html_file, 'r', encoding='utf-8') as f:
        #     html_content = f.read()
        # category = lib_llm_classifier.abby_classify(html_content, categories, api_key)
        # print(category['choices'][0]['message']['content'])
        # break


    # save in csv file
    with open('classified_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['code_client', 'domain', 'category']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=';')
        writer.writeheader()  # Write header only once
        writer.writerows(all_categories)







if __name__ == '__main__':
    main()