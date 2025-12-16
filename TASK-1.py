CODE:
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract all links
links = [a['href'] for a in soup.find_all('a', href=True)]
print(links)



NOTES:
- BeautifulSoup (bs4)
- Best for small to medium scraping tasks.
- Works with requests or urllib to fetch HTML.
