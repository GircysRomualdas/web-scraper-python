from urllib.parse import urlparse

def normalize_url(raw_url):
    url = urlparse(raw_url)
    full_path = f"{url.hostname}{url.path}".rstrip("/")
    return full_path
