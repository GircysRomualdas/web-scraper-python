# Web scraper

A web scraper that fetches web pages and processes their contents.

This project is part of Boot.dev's [Build a Web Scraper in Python](https://www.boot.dev/courses/build-web-scraper-python) course.

---

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (if not installed: `pip install uv`)

---

## Installation

1. Clone the repository.

2. Sync the environment.
```bash
uv sync
```

---

## Usage

### Run web scraper:
```bash
uv run main.py <url>
```

- `<url>` The website address where the crawler begins its search.

#### Example
```bash
uv run main.py "https://website2.com"
```

Output:
```
starting crawl of: https://website2.com
```
