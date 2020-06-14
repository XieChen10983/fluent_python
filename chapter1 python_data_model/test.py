# coding=gbk
import numpy as np
from functools import reduce
"""
直接使用np.convolve在次数超过13之后会出现bug
"""

# poly = np.convolve(poly, [1, 13])
# print(poly)


def convolve(a: iter, b: iter):
    a.reverse()
    b.reverse()
    new_len = (len(a) - 1) + (len(b) - 1) + 1
    conv = np.zeros(shape=(new_len, ))
    for i, ele_a in enumerate(a):
        for j, ele_b in enumerate(b):
            conv[i + j] += ele_a * ele_b
    conv = list(conv)
    conv = [int(ele) for ele in conv]
    conv.reverse()
    return conv


poly = [1, 1]
for i in range(2, 21):
    poly = convolve(poly, [1, i])
# poly = np.array(poly)
an = reduce(convolve, [[1, i] for i in range(1, 21)])
print("an = ", an)
roots = np.roots(an)
an[1] += 0.0001
roots_2 = np.roots(an)
print(roots)
print(roots_2)
print(abs(roots_2 - roots))
