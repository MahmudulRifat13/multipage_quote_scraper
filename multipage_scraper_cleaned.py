import requests
from bs4 import BeautifulSoup
import csv
import time
import random

def scrape_page(url):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url,headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.find_all("div", class_="quote")

page = 1

with open("cleaner_quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author", "Tags"])

    while True:
        url=f"https://quotes.toscrape.com/page/{page}/"

        try:
            quotes = scrape_page(url)
        except Exception as e:
            print("Error on page", page, ":", e)
            break

        if not quotes:
            break

        for q in quotes:
            text = q.find("span", class_="text").text
            author = q.find("small", class_="author").text
            tags = ", ".join([tag.text for tag in q.find_all("a", class_="tag")])

            writer.writerow([text, author, tags])

        print(f"Page {page} done")
        page += 1
        time.sleep(random.uniform(1, 3))