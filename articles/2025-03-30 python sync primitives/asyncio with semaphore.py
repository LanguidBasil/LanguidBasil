from collections.abc import Iterable
import asyncio
import itertools
import aiohttp

async def make_request_async(semaphore: asyncio.Semaphore, urls: Iterable[str]) -> None:
    async with semaphore:
        for url in urls:
            async with aiohttp.request("get", url):
                ...

async def async_main() -> None:
    urls = [f"https://jsonplaceholder.typicode.com/todos/{i}" for i in range(1, 201)]
    task_count = 10

    s = asyncio.Semaphore(value=task_count)
    _ = await asyncio.gather(
        *[
            make_request_async(s, urls_batch)
            for urls_batch in itertools.batched(urls, len(urls) // task_count)
        ]
    )

if __name__ == "__main__":
    asyncio.run(async_main())
