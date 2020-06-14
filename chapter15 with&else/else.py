# coding=gbk
"""
for/else、while/else、try/else的语句关系密切，else子句的行为如下：
    1. for
        仅当for循环运行完毕时（即for循环没有被break语句中止）才运行else模块
    2. while
        仅当while循环因为条件为假值而退出时（即while循环没有被break语句中止）才运行else模块
    3. try
        仅当try模块没有抛出异常才运行else模块
    在所有情况下，如果异常或者return、break、continue语句导致控制权跳到了复合语句的主块之外，else子句也会被跳过
"""

my_list = ["apple", "pineapple", "peach", "bear", "strawberry", ]
for item in my_list:
    if item == "banana":
        break
else:
    raise ValueError("No banana flavor found")
