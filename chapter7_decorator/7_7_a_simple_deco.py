# coding=gbk
import time


def clock(func):
    def clocked(*args):  # 定义内部函数clocked，它可以接收任意多个定位参数
        # nonlocal func
        t0 = time.perf_counter()
        result = func(*args)  # 这行代码可以用是因为clocked的闭包中包含自由变量func
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ",".join(repr(arg) for arg in args)
        print("[%0.8fs] %s(%s) -> %r" % (elapsed, name, arg_str, result))
        return result
    return clocked  # 返回内部函数，取代被修饰的函数。


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n - 1)


if __name__ == "__main__":
    print("*" * 40, "Calling snooze(.123)")
    snooze(0.123)
    print("*" * 40, "Calling factorial(6)")
    print("6! = ", factorial(6))
