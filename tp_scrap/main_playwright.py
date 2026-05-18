from playwright.sync_api import sync_playwright


def main():
    url = "https://sncf-voyageurs.com"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        page.goto(url,wait_until="networkidle") # wait until the network is idle (no more than 2 network connections for at least 500 ms)
        page.screenshot(path="screenshot-sncf-voyageurs.png")

if __name__ == '__main__':
    main()