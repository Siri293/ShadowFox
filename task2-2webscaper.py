import requests
from bs4 import BeautifulSoup

# Step 1: Website URL
url = "https://quotes.toscrape.com"

# Step 2: Send a request to the website
response = requests.get(url)

# Step 3: Check if response is OK
if response.status_code == 200:
    # Step 4: Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 5: Find all quote blocks
    quotes = soup.find_all('div', class_='quote')

    # Step 6: Loop through each quote and extract data
    for i, quote in enumerate(quotes, 1):
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        print(f"{i}. {text} — {author}")
else:
    print("Failed to load the page")
