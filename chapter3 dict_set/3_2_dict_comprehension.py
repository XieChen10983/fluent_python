# coding=gbk
"""
�ֵ��Ƶ����Դ��κ��Լ�ֵ����ΪԪ�صĿɵ��������й������ֵ�
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
