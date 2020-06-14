# coding=gbk

registry = set()


def register(activate=True):
    def decorate(func):
        print("running register(activate=%s) -> decorate(%s)" % (activate, func))
        if activate:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    return decorate


@register(activate=False)
def f1():
    print("running f1()")


@register()
def f2():
    print("running f2()")


# @register()
def f3():
    print("running f3()")


f1()
f2()
f3()
print(registry)
