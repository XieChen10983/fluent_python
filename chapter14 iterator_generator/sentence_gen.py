# coding=gbk
import re

RE_WORD = re.compile("\w+")


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return "Sentence(%s)" % repr(self.text)

    def __iter__(self):
        """
        for word in self.words:  迭代self.words
            yield word  产出当前的word
        return 此语句不是必要的，这个函数可以直接落空，自动返回
        :return:
        """
        for word in self.words:
            yield word
        return


if __name__ == "__main__":
    sentence = Sentence("I love you so much.")
    for word in sentence:
        print(word)
    print(list(sentence))
