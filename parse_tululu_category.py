import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def fantasy_urls():
    fantasy_book_ids = []
    for page_id in range(1, 2):
        url = 'https://tululu.org/l55/'
        payload = {'id': page_id}
        response = requests.get(url, params=payload)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        book_cards = soup.find_all(class_='d_book')
        book_hrefs = [card.find('a')['href'] for card in book_cards]
        book_ids = [book_href[2:] for book_href in book_hrefs]
        fantasy_book_ids.extend(book_ids)
    return fantasy_book_ids