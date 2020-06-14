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
        for word in self.words:  ����self.words
            yield word  ������ǰ��word
        return ����䲻�Ǳ�Ҫ�ģ������������ֱ����գ��Զ�����
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
