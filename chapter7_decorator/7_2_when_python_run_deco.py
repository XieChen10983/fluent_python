# coding=gbk
"""
1. װ������һ���ؼ������ǣ������ڱ�װ�εĺ�������֮���������У�ͨ�����ڵ���ģ��ʱ�������ˡ�
2. ������װ���������뱻װ�εĺ�����ͬһģ���ж��塣ʵ������£�װ����ͨ����һ��ģ���ж���Ȼ��Ӧ�õ�����ģ�麯���С�
3. registerװ�������صĺ�����ͨ�������������ͬ��ʵ���ϣ������װ���������ڲ�����һ������Ȼ���䷵�ء�
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
