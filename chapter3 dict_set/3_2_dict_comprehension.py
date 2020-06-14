# coding=gbk
"""
字典推导可以从任何以键值对作为元素的可迭代对象中构建出字典
"""
DIAL_CODE = [(86, "China"),
             (91, "India"),
             (1, "United States"),
             (62, "Indonesia"),
             (55, "Brazil"),
             (92, "Pakistan"),
             (880, "Bangladesh"),
             (234, "Nigeria"),
             (7, "Russia"),
             (81, "Japan")]
country_code = {country: code for code, country in DIAL_CODE}
upper_code = {code: country.upper() for code, country in DIAL_CODE if code <= 66}
print(country_code.popitem())
print(country_code)
print(upper_code)
