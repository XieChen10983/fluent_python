# coding=gbk
import random
from tombola import Tombola


class LotteryBlower(Tombola):

    def __init__(self, iterable):
        self._balls = list(iterable)  # ��������Ԫ��ȸ����������ͣ����Ҵ��������������޸�����

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError("pick from empty LotterBlower")
        return self._balls.pop(position)

    def loaded(self):  # ���ǳ�������е�loaded���������������inspect������
        return bool(self._balls)

    def inspect(self):
        return tuple(sorted(self._balls))
