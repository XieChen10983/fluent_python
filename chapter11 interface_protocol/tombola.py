# coding=gbk
import abc


class Tombola(abc.ABC):
    """
    Tombola抽象基类有四个方法，其中有两个是抽象方法。
        .load(...):把元素放入容器
        .pick():从容器中随机拿出一个元素，返回选中的元素
    另外两个是具体方法。
        .loaded():如果容器中至少有一个元素，返回True。
        .inspect():返回一个有序元组，由容器中的现有元素构成，不会修改容器的内容（内部的顺序不保留）
    """

    @abc.abstractmethod
    def load(self, iterable):
        """从可迭代对象中添加元素"""

    @abc.abstractmethod
    def pick(self):
        """
        随机删除元素，然后将其返回。
        如果实例为空，这个方法应该抛出“LookupError”。
        :return:
        """

    def loaded(self):
        """如果至少有一个元素，返回“True”，否则返回“False”"""
        return bool(self.inspect())

    def inspect(self):
        """返回一个有序元组，由当前元素组成"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))
