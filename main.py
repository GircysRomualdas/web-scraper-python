import sys
import asyncio
from async_crawler import crawl_site_async

async def main_async():
    if len(sys.argv) < 2:
        print("no website provided")
        sys.exit(1)

    if len(sys.argv) > 2:
        print("too many arguments provided")
        sys.exit(1)

    base_url = sys.argv[1]
    print(f"Starting crawl of: {base_url}")

    page_data = await crawl_site_async(base_url, 10)

    valid_pages = [p for p in page_data.values() if p is not None]
    print(f"Found {len(valid_pages)} pages:")
    for page in valid_pages:
        print(f"- {page['url']}: {len(page['outgoing_links'])} outgoing links")



if __name__ == "__main__":
    asyncio.run(main_async())
