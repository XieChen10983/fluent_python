# coding=gbk
"""
�˴���̽�����������������
"""
b = [6]  # ��bΪȫ�ֱ���
# print(id(b))
# b[0] += 1
# print(id(b))


def f1(a):
    print(a)
    print(b)


f1(3)


def f2(a):
    print(a)
    print(b)  # ��b�ں��������и�ֵ��Ϊ�ֲ�����
    b = 9


f2(3)
