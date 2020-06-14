# coding=gbk
"""
此代码探究可迭代对象与迭代器的对比
"""

s = "ABC"  # 字符串“ABC”为可迭代对象，其背后是有迭代器的。
for char in s:
    print(char)

# 下面构建一个迭代器
it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        del it
        break
