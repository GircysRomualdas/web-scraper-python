from urllib.parse import urlparse
from bs4 import BeautifulSoup

def normalize_url(raw_url):
    url = urlparse(raw_url)
    full_path = f"{url.hostname}{url.path}".rstrip("/")
    return full_path

def get_h1_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    h1 = soup.find("h1")
    return h1.get_text().strip() if h1 else ""

def get_first_paragraph_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    main = soup.find("main")
    p = main.find("p") if main else soup.find("p")
    return p.get_text().strip() if p else ""
