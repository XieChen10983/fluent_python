# coding=gbk
"""
�˴���̽���ɵ���������������ĶԱ�
"""

s = "ABC"  # �ַ�����ABC��Ϊ�ɵ��������䱳�����е������ġ�
for char in s:
    print(char)

# ���湹��һ��������
it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        del it
        break
