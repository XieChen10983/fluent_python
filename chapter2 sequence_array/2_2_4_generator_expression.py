# coding=gbk
"""
1. ���������ʽ���������˵�����Э�飬�����������Ԫ�أ��������Ƚ���һ���������б�Ȼ���ٰ�����б���
    ��ĳ�����캯���С����������ʽ���ַ�ʽ��Ȼ�ܹ���ʡ�ڴ档
2. ���������ʽ���﷨���б��Ƶ���ֻ࣬�����ѷ����Ż���Բ���š�
"""

"""-------------------------���������ʽ��ʼ��Ԫ��---------------------------"""
symbols = "ldkjk"
ascii_symbols = tuple(ord(symbol) for symbol in symbols)
print(ascii_symbols)

"""-------------------------���������ʽ��ʼ������---------------------------"""
import array
array1 = array.array("I", (ord(symbol) for symbol in symbols))
print(array1)

"""-------------------------���������ʽ����ѿ�����------------------------"""
colors = ["black", "white"]
sizes = ["L", "M", "S"]
for t_shirt in ([color, size] for color in colors for size in sizes):
    # �˴��������һ���������б�����һ��Ԫ��һ��Ԫ�����ɣ���colors��sizes�ϴ�ʱ�����Խ�ʡ�ڴ�
    print(t_shirt)

colors = ("black", "white")
print(print("color %s/%s" % colors))

import numpy as np
