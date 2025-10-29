import requests
from bs4 import BeautifulSoup

url = "https://example.com"
resp = requests.get(url)
resp.raise_for_status()

soup = BeautifulSoup(resp.text, "html.parser")
print(soup.title.text)
