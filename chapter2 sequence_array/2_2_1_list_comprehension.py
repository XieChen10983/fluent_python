# coding=gbk
"""
[���ʽ(Ԫ��) for Ԫ�� in Ԫ���б�]  �б��Ƶ�ͨ�����������µ��б���������̫�������迼����forѭ��д��
�б��Ƶ���python3�в����ܵ�ͬ�������ĸ��ţ�������python2�л��ܵ��Ƶ����ʽ���ͬ�������ĸ���
"""

"""-----------------------------------�б��Ƶ���append�ıȽ�-------------------------------------"""
symbols = "$%^&*("
# codes = []
# for symbol in symbols:
#     codes.append(ord(symbol))
codes = [ord(symbol) for symbol in symbols]
print(codes)

"""-----------------------------------�����б��Ƶ���map/filter�ıȽ�---------------------------------------"""
symbols = "LJLKGE$"
beyond_ascii = [ord(symbol) for symbol in symbols if ord(symbol) > 73]
# beyond_ascii = list(filter(lambda c: c > 73, map(ord, symbols)))
print(beyond_ascii)

"""-----------------------------------�ѿ�����-------------------------------------"""
colors = ["black", "white"]
sizes = ["S", "M", "L"]
# ���color��size�����Ⱥ�˳���Ǻ���for size in sizes for color in colors���Ⱥ�˳������ģ�����ǰ��ľ����ģ�����
t_shirts = [(color, size) for size in sizes for color in colors]
print(t_shirts)
