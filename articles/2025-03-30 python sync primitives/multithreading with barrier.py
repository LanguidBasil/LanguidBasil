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
