# scraper/scraper.py
import requests
from bs4 import BeautifulSoup
from database.database import save_to_db
from utils.logger import log

# Example URL (Replace with your target website)
URL = "http://books.toscrape.com/catalogue/category/books_1/index.html"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def scrape():
    log("Starting web scraping...")
    response = requests.get(URL, headers=HEADERS)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        data = parse_data(soup)
        save_to_db(data)
        log("Scraping complete.")
    else:
        log(f"Failed to retrieve data. Status code: {response.status_code}")

def parse_data(soup):
    # Example: Extracting product names
    products = []
    for item in soup.select(".product-title"):
        products.append({"name": item.text.strip()})
    return products