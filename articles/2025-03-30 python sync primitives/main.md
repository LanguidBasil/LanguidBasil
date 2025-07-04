
Напиши пост про задачку с url'ами

Локи (мьютексы), семафоры, барьеры. Краткий ликбез. GIL out of scope

Упомянуть что задачка попалась на собесе ... . Она заключается в ... . Нужно обработать все максимально быстро, не нагрузив при этом нашу сетевую карту. 

Когда лучше использовать мультипоточность, а не асинхронность? Например если нам нужен четкий процесс который всегда отрабатывает в указанное время, не дожидаясь своей очереди, например процесс по трекингу изменений в директории

Сказать что это все эффективно только для IO-bound задач и в будущем нужно будет также разобрать процессы. Вопросы про их синхронизацию тоже частые

---

мультипоточность с барьерной синхронизацией

```python
from collections.abc import Iterable
import threading
import itertools
import requests

def make_request_sync(barrier: threading.Barrier, urls: Iterable[str]) -> None:
    for url in urls:
        with requests.request("get", url):
            ...

    _ = barrier.wait()

if __name__ == "__main__":
    urls = [f"https://jsonplaceholder.typicode.com/todos/{i}" for i in range(1, 201)]
    thread_count = 10

    barrier = threading.Barrier(thread_count + 1) # все io потоки + главный
    for urls_batch in itertools.batched(urls, len(urls) // thread_count):
        threading.Thread(target=make_request_sync, args=(barrier, urls_batch)).start()

    _ = barrier.wait()
```

---

асинхронщина с семафорами

```python
from collections.abc import Iterable
import asyncio
import itertools
import aiohttp

async def make_request_async(semaphore: asyncio.Semaphore, urls: Iterable[str]) -> None:
    async with semaphore:
        for url in urls:
            async with aiohttp.request("get", url):
                ...

async def async_main():
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
```
