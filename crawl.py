from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import requests

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

def get_urls_from_html(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all("a")
    urls = []

    for link in links:
        href = link.get("href")
        urls.append(urljoin(base_url, href))

    return urls

def get_images_from_html(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.find_all("img")
    urls = []

    for image in images:
        src = image.get("src")
        urls.append(urljoin(base_url, src))

    return urls

def extract_page_data(html, page_url):
    return {
        "url": page_url,
        "h1": get_h1_from_html(html),
        "first_paragraph": get_first_paragraph_from_html(html),
        "outgoing_links": get_urls_from_html(html, page_url),
        "image_urls": get_images_from_html(html, page_url)
    }
