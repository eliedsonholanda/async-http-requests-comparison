import time
import asyncio
import httpx

async def fetch_data(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response

async def async_requests(urls):
    tasks = [fetch_data(url) for url in urls]
    await asyncio.gather(*tasks)

def sync_requests(urls):
    for url in urls:
        httpx.get(url)

if __name__ == "__main__":
    urls = ["https://jsonplaceholder.typicode.com/posts/1"] * 5

    start_time_sync = time.time()
    sync_requests(urls)
    end_time_sync = time.time()

    loop = asyncio.get_event_loop()
    start_time_async = time.time()
    loop.run_until_complete(async_requests(urls))
    end_time_async = time.time()

    print(f"Tempo gasto em requisições síncronas: {end_time_sync - start_time_sync} segundos")
    print(f"Tempo gasto em requisições assíncronas: {end_time_async - start_time_async} segundos")
