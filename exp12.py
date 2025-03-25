import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "http://quotes.toscrape.com"

# Send GET request to the URL
response = requests.get(url)

# Check if the request was successful (Status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract quotes using the specific CSS class
    quotes = [quote.text.strip() for quote in soup.find_all("span", class_="text")]

    # Save the extracted quotes to a text file
    with open("scraped_data.txt", "w", encoding="utf-8") as file:
        for quote in quotes:
            file.write(quote + "\n")
    
    print("✅ Data scraped and stored successfully in 'scraped_data.txt'!")
else:
    print(f"❌ Failed to fetch page, status code: {response.status_code}")