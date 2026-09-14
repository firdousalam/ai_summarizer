import requests
from bs4 import BeautifulSoup


def fetch_article(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(
            f"Failed to fetch article. Status code: {response.status_code}")
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    article_text = " ".join([p.get_text() for p in paragraphs])
    return article_text
