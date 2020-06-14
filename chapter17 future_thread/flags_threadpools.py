# coding=gbk
"""
author(����): Channing Xie(л�)
time(ʱ��): 2020/3/26 15:59
filename(�ļ���): flags_threadpools.py
function description(��������):����futures���ж��߳�������
...
"""
from concurrent import futures
from flags import save_flag, get_flag, show, main

MAX_WORKERS = 20


def download_one(cc):
    """
    ����һ��ͼ��ĺ����������ڸ����߳���ִ�еĺ�����
    :param cc:
    :return:
    """
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + ".gif")
    return cc


def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))
    # executor.__exit__���������executor.shutdown(wait=True)�����������������̶߳�ִ�����֮ǰ�����߳�
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(cc_list))  # download_one�������ڶ���߳��в������ã�map����һ��������
    return len(list(res))


if __name__ == "__main__":
    main(download_many)
