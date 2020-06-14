# coding=gbk
"""
对于之前的最佳策略课题，promos列表中的值使用promotion装饰器来填充。
1. 促销策略函数更容易添加到列表之中，只需要用@promotion函数装饰，而不用采用_promo结尾再判断append
2. 突出了被装饰的函数的作用，还便于临时禁用某个促销策略，只需要将装饰器注释掉
3. 促销折扣策略可以在其他模块中定义，在系统的任何地方都行，只需要用@promotion来装饰即可。
"""

promos = []


def promotion(promo_func):
    promos.append(promo_func)
    return promo_func


@promotion
def fidelity(order):
    """
    为积分为1000分以上的顾客提供5%的折扣。
    :param order:
    :return:
    """
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


@promotion
def bulk_item(order):
    """
    单个商品为20个或以上时提供折扣10%
    :param order:
    :return:
    """
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.tatal() * .1
    return discount


@promotion
def large_order(order):
    """
    订单中不同商品达到10个或以上时提供7%折扣
    :param order:
    :return:
    """
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0


def best_promo(order):
    """选择可用的最佳折扣"""
    return max(promo(order) for promo in promos)
