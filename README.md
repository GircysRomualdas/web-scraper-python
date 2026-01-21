# Web scraper

A concurrent web crawler that collects page metadata and links starting from a given URL, then exports the results to `report.csv` for analysis.

This project is part of Boot.dev's [Build a Web Scraper in Python](https://www.boot.dev/courses/build-web-scraper-python) course.

---

## Requirements

- Python 3.12+
- uv (if not installed: `pip install uv`)

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
uv run main.py <url> <max_concurrency> <max_pages>
```

- `<url>` - The website address where the crawler begins its search.
- `<max_concurrency>` - Maximum number of concurrent requests.
- `<max_pages>` - Maximum number of pages to crawl.

#### Example
```bash
uv run main.py "https://blog.boot.dev/" 3 25
```

Output:
```
Starting crawl of: https://blog.boot.dev/
Max concurrency: 3, Max pages: 25
crawling https://blog.boot.dev/
crawling https://blog.boot.dev/news/bootdev-beat-2026-01/
crawling https://blog.boot.dev/news/bootdev-beat-2025-12/
crawling https://blog.boot.dev/jobs/supply-demand-broken-programming-education/
crawling https://blog.boot.dev/news/bootdev-beat-2025-11/
crawling https://blog.boot.dev/education/vibe-coding-hell/
crawling https://blog.boot.dev/news/bootdev-beat-2025-10/
crawling https://blog.boot.dev/news/bootdev-beat-2025-09/
crawling https://blog.boot.dev/create-a-course/
crawling https://blog.boot.dev/news/training-grounds-launch/
crawling https://blog.boot.dev/news/bootdev-beat-2025-08/
crawling https://blog.boot.dev/news/hackathon-2025/
crawling https://blog.boot.dev/news/bootdev-beat-2025-07/
crawling https://blog.boot.dev/news/bootdev-beat-2025-06/
crawling https://blog.boot.dev/education/is-boot-dev-free/
crawling https://blog.boot.dev/news/bootdev-beat-2025-05/
crawling https://blog.boot.dev/news/bootdev-beat-2025-04/
crawling https://blog.boot.dev/news/bootdev-beat-2025-03/
crawling https://blog.boot.dev/news/bootdev-beat-2025-02/
crawling https://blog.boot.dev/computer-science/18-months-with-gpt-4/
crawling https://blog.boot.dev/news/bootdev-beat-2025-01/
crawling https://blog.boot.dev/tutorials/python/lists/
crawling https://blog.boot.dev/tutorials/python/loops/
crawling https://blog.boot.dev/tutorials/python/functions/
crawling https://blog.boot.dev/tutorials/python/variables/
Reached maximum number of pages to crawl.

Found 25 pages:
Web scraper report written to report.csv
```
