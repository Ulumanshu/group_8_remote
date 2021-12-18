import timeit
import requests


def crawl(url, dest):
    try:
        result = requests.get(url).text
        with open(dest, "a") as f:
            f.write(result)

    except requests.exceptions.RequestException:
        print("Error with URL check!")


def wo_threading_func(urls):
    for url in urls:
        crawl(url, "without_threads.txt")


def with_threading_func(urls):
    import threading

    threads = []
    for url in urls:
        th = threading.Thread(target=crawl, args=(url, "with_threads.txt"))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()


if __name__ == "__main__":
    pass
    # Pamodifikuoti metodus with_threading_func ir wo_threading_func bei crawl taip,
    # kad jie grazintu ka nuskaite internete kokia nors forma, ir su tredais ir be
    # (threading clase join metodo paveldejimas)