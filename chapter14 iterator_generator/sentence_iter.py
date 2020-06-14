# coding=gbk
import re

RE_WORD = re.compile("\w+")


class Sentence:
    """
    Ϊ��ʹ��SentenceΪ�ɵ����Ķ�����Ҫʵ��__iter__��������__iter__������Ҫ����һ��������
    """
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return "Sentence(%s)" % repr(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceIterator:
    """
    ��������Ҫʵ��__next__��__iter__��������
    """
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self


if __name__ == "__main__":
    sentence = Sentence("I love you so much.")
    for word in sentence:
        print(word)
    print(list(sentence))
