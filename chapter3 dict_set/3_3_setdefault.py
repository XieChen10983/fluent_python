# coding=gbk
"""
此代码测试字典中setdefault(key, default)的功能
在终端使用 “python 3_3_setdefault.py 文件名” 来运行代码
"""
import sys
import re

WORD_RE = re.compile(r'\w+')

index = {}
with open(sys.argv[1], encoding="utf-8") as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # 这其实是一种很不好的实现，这样写是为了证明论点
            # occurrences = index.get(word, [])
            # occurrences.append(location)
            # index[word] = occurrences

            # 下面一句话就可以完成上面三句话的内容
            index.setdefault(word, []).append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])
