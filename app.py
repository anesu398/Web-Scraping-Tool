import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url

    def scrape(self):
        try:
            # Send a GET request to the URL
            response = requests.get(self.url)

            # Check if request was successful
            if response.status_code == 200:
                # Parse HTML content
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Extract relevant information from the page
                # (Example: Extracting titles of all articles)
                articles = soup.find_all('article')
                titles = [article.find('h2').text.strip() for article in articles]

                return titles
            else:
                print("Error: Unable to fetch data from the provided URL.")
                return None
        except Exception as e:
            print(f"Error: {e}")
            return None

# Example usage:
if __name__ == "__main__":
    url = "https://www.zillow.com"
    scraper = WebScraper(url)
    scraped_data = scraper.scrape()
    if scraped_data:
        print("Scraped data:")
        for title in scraped_data:
            print("- " + title)
