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

def get_html(url):
    res = requests.get(url, headers={"User-Agent": "BootCrawler/1.0"})

    if res.status_code > 399:
        raise Exception(f"response status code: {res.status_code}")

    content_type = res.headers.get("content-type", "")
    if "text/html" not in content_type:
        raise Exception(f"response content type is not HTML.")

    return res.text

def crawl_page(base_url, current_url=None, page_data=None):
    if current_url is None:
        current_url = base_url
    if page_data is None:
        page_data = {}

    base_url_obj = urlparse(base_url)
    current_url_obj = urlparse(current_url)
    if current_url_obj.netloc != base_url_obj.netloc:
        return page_data

    nor_url = normalize_url(current_url)

    if nor_url in page_data:
        return page_data

    print(f"crawling {current_url}")
    html = safe_get_html(current_url)
    if html is None:
        return page_data

    data = extract_page_data(html, current_url)

    page_data[nor_url] = data

    next_urls = get_urls_from_html(html, base_url)
    for next_url in next_urls:
        page_data = crawl_page(base_url, next_url, page_data)

    return page_data

def safe_get_html(url):
    try:
        return get_html(url)
    except Exception as e:
        print(f"{e}")
        return None
