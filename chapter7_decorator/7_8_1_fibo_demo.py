# coding=gbk
"""
functools.lru_cacheʵ���˱����Ĺ��ܡ���Ѻ�ʱ�ĺ�������������������⴫����ͬ�Ĳ���ʱ�ظ����㡣
���治�������Ƶ�������һ��ʱ�䲻�õĻ���ᱻ�ӵ���
"""
import functools
import time


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(", ".join(repr(arg) for arg in args))
        if kwargs:
            pairs = ["%s=%r" % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(", ".join(pairs))
        arg_str = ", ".join(arg_lst)
        print("[%0.8fs] %s(%s) -> %r" % (elapsed, name, arg_str, result))
        return result
    return clocked


# @functools.lru_cache()  # ����仰��ܿ�
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == "__main__":
    print(fibonacci(30))
