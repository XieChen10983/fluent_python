# coding=gbk
from abc import ABC, abstractmethod
from collections import namedtuple


Customer = namedtuple("Customer", "name fidelity")


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # 上下文
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, "__total"):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = "<Order total: {:.2f} dur: {:.2f}>"
        return fmt.format(self.total(), self.due())


class Promotion(ABC):
    @abstractmethod
    def discount(self, order):
        """返回折扣金额（正值）"""


class FidelityPromo(Promotion):  # 第一个具体的策略
    """为积分为1000或以上的顾客提供5%的折扣"""
    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):  # 第二个具体的策略
    """单个商品为20个或以上时提供10%的折扣"""
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount


class LargeOrderPromo(Promotion):  # 第三个具体策略
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0


def fidelity_promo(order):
    """积分为1000分以上的顾客提供5%的折扣"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    """单个商品为20个或以上时提供10%的折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


def large_order_promo(order):
    """订单中的不同商品达到10个或以上时提供7%的折扣"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0


# promos = [bulk_item_promo, fidelity_promo, large_order_promo]
promos = [globals()[name] for name in globals()
          if name.endswith("_promo")
          and name != "best_promo"]
print(promos)


def best_promo(order):
    return max([promo(order) for promo in promos])


joe = Customer("John Doe", 0)
ann = Customer("Ann Smith", 1100)
cart = [
    LineItem("banana", 4, 0.5),
    LineItem("apple", 10, 1.5),
    LineItem("watermelon", 5, 5.0)
]
# print(Order(joe, cart, FidelityPromo()))
# print(Order(ann, cart, FidelityPromo()))
print(Order(ann, cart, fidelity_promo))
print(Order(ann, cart, best_promo))
