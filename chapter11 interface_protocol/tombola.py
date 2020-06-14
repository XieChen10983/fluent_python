# coding=gbk
import abc


class Tombola(abc.ABC):
    """
    Tombola����������ĸ������������������ǳ��󷽷���
        .load(...):��Ԫ�ط�������
        .pick():������������ó�һ��Ԫ�أ�����ѡ�е�Ԫ��
    ���������Ǿ��巽����
        .loaded():���������������һ��Ԫ�أ�����True��
        .inspect():����һ������Ԫ�飬�������е�����Ԫ�ع��ɣ������޸����������ݣ��ڲ���˳�򲻱�����
    """

    @abc.abstractmethod
    def load(self, iterable):
        """�ӿɵ������������Ԫ��"""

    @abc.abstractmethod
    def pick(self):
        """
        ���ɾ��Ԫ�أ�Ȼ���䷵�ء�
        ���ʵ��Ϊ�գ��������Ӧ���׳���LookupError����
        :return:
        """

    def loaded(self):
        """���������һ��Ԫ�أ����ء�True�������򷵻ء�False��"""
        return bool(self.inspect())

    def inspect(self):
        """����һ������Ԫ�飬�ɵ�ǰԪ�����"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))
