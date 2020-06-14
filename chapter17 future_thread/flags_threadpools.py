# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/3/26 15:59
filename(文件名): flags_threadpools.py
function description(功能描述):利用futures进行多线程任务处理
...
"""
from concurrent import futures
from flags import save_flag, get_flag, show, main

MAX_WORKERS = 20


def download_one(cc):
    """
    下载一个图像的函数，这是在各个线程中执行的函数。
    :param cc:
    :return:
    """
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + ".gif")
    return cc


def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))
    # executor.__exit__方法会调用executor.shutdown(wait=True)方法，它会在所有线程都执行完毕之前阻塞线程
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(cc_list))  # download_one函数会在多个线程中并发调用，map返回一个生成器
    return len(list(res))


if __name__ == "__main__":
    main(download_many)
