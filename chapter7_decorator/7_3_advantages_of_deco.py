# coding=gbk
"""
����֮ǰ����Ѳ��Կ��⣬promos�б��е�ֵʹ��promotionװ��������䡣
1. �������Ժ�����������ӵ��б�֮�У�ֻ��Ҫ��@promotion����װ�Σ������ò���_promo��β���ж�append
2. ͻ���˱�װ�εĺ��������ã���������ʱ����ĳ���������ԣ�ֻ��Ҫ��װ����ע�͵�
3. �����ۿ۲��Կ���������ģ���ж��壬��ϵͳ���κεط����У�ֻ��Ҫ��@promotion��װ�μ��ɡ�
"""

promos = []


def promotion(promo_func):
    promos.append(promo_func)
    return promo_func


@promotion
def fidelity(order):
    """
    Ϊ����Ϊ1000�����ϵĹ˿��ṩ5%���ۿۡ�
    :param order:
    :return:
    """
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


@promotion
def bulk_item(order):
    """
    ������ƷΪ20��������ʱ�ṩ�ۿ�10%
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
    �����в�ͬ��Ʒ�ﵽ10��������ʱ�ṩ7%�ۿ�
    :param order:
    :return:
    """
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0


def best_promo(order):
    """ѡ����õ�����ۿ�"""
    return max(promo(order) for promo in promos)
