# coding=gbk
"""
1. 装饰器的一个关键特性是，他们在被装饰的函数定义之后立即运行，通常是在导入模块时就运行了。
2. 此例中装饰器函数与被装饰的函数在同一模块中定义。实际情况下，装饰器通常在一个模块中定义然后应用到其他模块函数中。
3. register装饰器返回的函数与通过参数传入的相同。实际上，大多数装饰器会在内部定义一个函数然后将其返回。
"""

registry = []


def register(func):
    print("running register(%s)" % func)
    registry.append(func)
    return func


@register
def f1():
    print("running f1()")


@register
def f2():
    print("running f2()")


# @register
def f3():
    print("running f3()")


def main():
    print("running main()")
    print("registry -> ", registry)
    f1()
    f2()
    f3()


if __name__ == "__main__":
    main()
