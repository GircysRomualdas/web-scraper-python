import sys
import asyncio
from async_crawler import crawl_site_async
from csv_report import write_csv_report

async def main_async():
    if len(sys.argv) < 4:
        print("Usage: uv run main.py <URL> <max_concurrency> <max_pages>")
        sys.exit(1)
    if len(sys.argv) > 4:
        print("Too many arguments provided")
        sys.exit(1)

    base_url = sys.argv[1]

    try:
        max_concurrency = int(sys.argv[2])
        max_pages = int(sys.argv[3])
    except ValueError:
        print("max_concurrency and max_pages must be integers")
        sys.exit(1)

    print(f"Starting crawl of: {base_url}")
    print(f"Max concurrency: {max_concurrency}, Max pages: {max_pages}")

    page_data = await crawl_site_async(base_url, max_concurrency, max_pages)

    valid_pages = [p for p in page_data.values() if p is not None]
    print(f"\nFound {len(valid_pages)} pages:")

    write_csv_report(valid_pages)


if __name__ == "__main__":
    try:
        asyncio.run(main_async())
    except KeyboardInterrupt:
        print("\nCrawl interrupted by user")
