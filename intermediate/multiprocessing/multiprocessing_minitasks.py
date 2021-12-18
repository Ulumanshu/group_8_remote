import timeit
import requests
from pprint import pprint
import threading
from timer_decorator import timing
from typing import List


URLS = [
    "https://jsonplaceholder.typicode.com/comments/1",
    "https://jsonplaceholder.typicode.com/comments/2",
    "https://jsonplaceholder.typicode.com/comments/3"
]


class ThreadWithReturnValue(threading.Thread):
    def __init__(self, target, args=(), kwargs=None):
        if kwargs is None:
            kwargs = {}
        self.target = target
        self.args = args
        self.kwargs = kwargs
        self.result = []
        super().__init__()

    def run(self):
        self.result = self.target(*self.args, **self.kwargs)

    def join(self, timeout=None) -> List:
        super().join(timeout)
        return self.result


def crawl(url):
    res = []
    try:
        result = requests.get(url).text
        res.append(result)

    except requests.exceptions.RequestException:
        print("Error with URL check!")

    return res


@timing
def wo_threading_func(urls):
    res = []
    for url in urls:
        subres = crawl(url)
        res.extend(subres)

    return res


@timing
def with_threading_func(urls):
    res = []
    threads = []
    for url in urls:
        th = ThreadWithReturnValue(target=crawl, args=(url, ))
        th.start()
        threads.append(th)

    for th in threads:
        res.extend(th.join())

    return res


if __name__ == "__main__":
    crawl_no_thread_results = wo_threading_func(URLS)
    crawl_with_threads_results = with_threading_func(URLS)

    pprint(crawl_no_thread_results, indent=4)
    pprint(crawl_with_threads_results, indent=4)
    # Pamodifikuoti metodus with_threading_func ir wo_threading_func bei crawl taip,
    # kad jie grazintu ka nuskaite internete kokia nors forma, ir su tredais ir be
    # (threading clase join metodo paveldejimas)
