# multipage_quote_scraper
A Python-based web scraper that automates multi-page crawling and extracts, cleans, and structures quotes, authors, and tags into a CSV dataset using Requests and BeautifulSoup.

## 🚀 Features
- Scrapes data across multiple pages automatically (pagination handling)
- Extracts:
  - Quote text
  - Author name
  - Tags
- Cleans and formats extracted data for consistency
- Stores structured data in CSV format
- Handles request errors gracefully
- Uses custom headers to mimic real browser requests
- Implements random delays to avoid detection/blocking
- Automatically stops when no more pages are available

---

## 🛠️ Technologies Used
- Python
- requests
- BeautifulSoup (bs4)
- CSV module
- time & random (for rate limiting)

---

## ⚙️ How It Works
- Sends HTTP requests with custom headers
- Parses HTML content using BeautifulSoup
- Extracts required fields from each quote block
- Iterates through paginated pages until data ends
- Cleans and formats extracted values
- Writes structured data into a CSV file
- Adds delay between requests to simulate human behavior

---

## Output
CSV file with structured job data

---

## 📌 Key Highlights
- Multi-page scraping logic using loop control
- Data cleaning and formatting (tags joined properly)
- Error handling with try-except
- Rate limiting using random delays
- Clean and modular function design

---

## 🤝 Contribution
Feel free to fork this repository and improve it further.
