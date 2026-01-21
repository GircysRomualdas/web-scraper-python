import asyncio
import aiohttp
from urllib.parse import urlparse
from crawl import normalize_url, extract_page_data, get_urls_from_html

class AsyncCrawler:
    def __init__(self, base_url, max_concurrency, max_pages):
        self.base_url = base_url
        self.max_pages = max_pages
        self.should_stop = False
        self.all_tasks = set()
        self.base_domain = urlparse(base_url).netloc
        self.page_data = {}
        self.lock = asyncio.Lock()
        self.max_concurrency = max_concurrency
        self.semaphore = asyncio.Semaphore(max_concurrency)
        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()

    async def add_page_visit(self, normalized_url):
        async with self.lock:
            if self.should_stop:
                return False

            if normalized_url in self.page_data:
                return False

            if self.max_pages and len(self.page_data) >= self.max_pages:
                self.should_stop = True
                print("Reached maximum number of pages to crawl.")
                return False

            self.page_data[normalized_url] = None
            return True

    async def get_html(self, url):
        async with self.session.get(url, headers={"User-Agent": "BootCrawler/1.0"}) as res:
            if res.status > 399:
                return None

            content_type = res.headers.get("content-type", "")
            if "text/html" not in content_type:
                return None

            return await res.text()


    async def crawl_page(self, current_url):
        if self.should_stop:
            return

        current_task = asyncio.current_task()
        self.all_tasks.add(current_task)

        try:
            base_url_obj = urlparse(self.base_url)
            current_url_obj = urlparse(current_url)
            if current_url_obj.netloc != base_url_obj.netloc:
                return

            normalized_url = normalize_url(current_url)

            if not await self.add_page_visit(normalized_url):
                return

            print(f"crawling {current_url}")

            async with self.semaphore:
                html = await self.get_html(current_url)

                if html is None:
                    return

                data = extract_page_data(html, current_url)

                async with self.lock:
                    self.page_data[normalized_url] = data

                next_urls = get_urls_from_html(html, self.base_url)
                tasks = []
                for next_url in next_urls:
                    task = asyncio.create_task(self.crawl_page(next_url))
                    self.all_tasks.add(task)
                    tasks.append(task)

                await asyncio.gather(*tasks, return_exceptions=True)
        finally:
            self.all_tasks.remove(current_task)


    async def crawl(self):
        try:
            await self.crawl_page(self.base_url)
        except asyncio.CancelledError:
            pass
        return self.page_data

async def crawl_site_async(base_url, max_concurrency, max_pages):
    async with AsyncCrawler(base_url, max_concurrency, max_pages) as crawler:
        return await crawler.crawl()
