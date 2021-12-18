import timeit
import requests

URLS = [
    "https://jsonplaceholder.typicode.com/comments/1",
    "https://jsonplaceholder.typicode.com/comments/2",
    "https://jsonplaceholder.typicode.com/comments/3"
]


def crawl(url):
    res = []
    try:
        result = requests.get(url).text
        res.append(result)

    except requests.exceptions.RequestException:
        print("Error with URL check!")

    return res


def wo_threading_func(urls):
    res = []
    for url in urls:
        subres = crawl(url)
        res.extend(subres)

    return res


def with_threading_func(urls):
    import threading
    res = []
    threads = []
    for url in urls:
        th = threading.Thread(target=crawl, args=(url, ))
        th.start()
        threads.append(th)

    for th in threads:
        res.extend(th.join() or "NONE")

    return res


if __name__ == "__main__":
    crawl_no_thread_results = wo_threading_func(URLS)
    crawl_with_threads_results = with_threading_func(URLS)

    print(crawl_no_thread_results)
    print(crawl_with_threads_results)
    # Pamodifikuoti metodus with_threading_func ir wo_threading_func bei crawl taip,
    # kad jie grazintu ka nuskaite internete kokia nors forma, ir su tredais ir be
    # (threading clase join metodo paveldejimas)
