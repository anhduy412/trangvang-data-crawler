from bs4 import BeautifulSoup
import requests

def fetch_content(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')