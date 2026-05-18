import httpx
from readability import Document
from markdownify import markdownify as md
import csv
import asyncio
from dotenv import load_dotenv
import os
import time

load_dotenv()

CONCURRENCY = int(os.getenv('CONCURRENCY_LIMIT', 3))


async def get_content(client_http, domain, markdown_dir, html_dir, semaphore):

    async with semaphore:
        r = await client_http.get(f'https://{domain}/')
        print(domain, r.status_code)

        doc = Document(r.text)
        clean_html = doc.summary()
        markdown = md(clean_html)


        with open(f"{markdown_dir}/{domain}.md", "w", encoding="utf-8") as file:
            file.write(markdown)

        with open(f"{html_dir}/{domain}.html", "w", encoding="utf-8") as file:
            file.write(r.text)


async def main():
    get_content_tasks = []

    # Limiter le nombre de tâches concurrentes à 3
    semaphore = asyncio.Semaphore(CONCURRENCY)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    }
    markdown_dir = "markdown_files"
    html_dir = "html_files"
    start_time = time.time()

    # Créer un dossier pour stocker les fichiers markdown, s'il n'existe pas déjà
    os.makedirs(markdown_dir, exist_ok=True)
    os.makedirs(html_dir, exist_ok=True)

    sites_web_societes = os.getenv(
        'SITES_WEB_SOCIETES_FILE', "sites_web_societes.csv")
    # ouvrir le fichier en mode lecture, avec gestion automatique de la fermeture.'r' par défaut
    with open(sites_web_societes) as file:
        # créer un objet DictReader pour lire le fichier CSV en utilisant le point-virgule comme séparateur
        reader = csv.DictReader(file, delimiter=';')

        async with httpx.AsyncClient(verify=False, follow_redirects=True, headers=headers, limits=httpx.Limits(max_connections=CONCURRENCY*5), timeout=httpx.Timeout(5.0)) as network_client:
            for row in reader:
                if "." in row['domain']:
                    domain = row['domain']
                    get_content_tasks.append(get_content(
                        network_client, domain, markdown_dir, html_dir, semaphore))
                    # await get_content(network_client, domain, markdown_dir)

            # Exécuter toutes les tâches de récupération de contenu en parallèle
            await asyncio.gather(*get_content_tasks)

    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")


if __name__ == '__main__':
    asyncio.run(main())
