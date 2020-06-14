# coding=gbk
"""
把句子划分为单词序列
"""
import re

RE_WORD = re.compile("\w+")


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, item):
        return self.words[item]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return "Sentence(%s)" % repr(self.text)


if __name__ == "__main__":
    sentence = Sentence("I love you so much.")
    for word in sentence:
        print(word)
    print(list(sentence))
