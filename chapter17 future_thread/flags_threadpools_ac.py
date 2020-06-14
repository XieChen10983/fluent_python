# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/3/26 16:48
filename(文件名): flags_threadpools_ac.py
function description(功能描述):用submit方法和as_completed方法来代替future中的map方法
...
"""
from flags_threadpools import *
from concurrent import futures


def download_many(cc_list):
    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            to_do.append(future)
            msg = "Scheduled for {}: {}"
            print(msg.format(cc, future))

        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            msg = "{} result: {!r}"
            print(msg.format(future, res))
            results.append(res)

    return len(results)


if __name__ == "__main__":
    main(download_many)
