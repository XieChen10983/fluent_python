# coding=gbk
"""
for/else��while/else��try/else������ϵ���У�else�Ӿ����Ϊ���£�
    1. for
        ����forѭ���������ʱ����forѭ��û�б�break�����ֹ��������elseģ��
    2. while
        ����whileѭ����Ϊ����Ϊ��ֵ���˳�ʱ����whileѭ��û�б�break�����ֹ��������elseģ��
    3. try
        ����tryģ��û���׳��쳣������elseģ��
    ����������£�����쳣����return��break��continue��䵼�¿���Ȩ�����˸�����������֮�⣬else�Ӿ�Ҳ�ᱻ����
"""

my_list = ["apple", "pineapple", "peach", "bear", "strawberry", ]
for item in my_list:
    if item == "banana":
        break
else:
    raise ValueError("No banana flavor found")
