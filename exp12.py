import requests
from bs4 import BeautifulSoup


url = " http://quotes.toscrape.com"


response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    quotes = [quote.text.strip() for quote in soup.find_all("span", class_="text")]

    with open("scraped_data.txt", "w", encoding="utf-8") as file:
        for quote in quotes:
            file.write(quote + "\n")
    
    print("Data scraped and stored successfully in 'scraped_data.txt'!")
else:
    print(f"Failed to fetch page, status code: {response.status_code}")