# coding=gbk
import re

RE_WORD = re.compile("\w+")


class Sentence:
    """
    为了使得Sentence为可迭代的对象，需要实现__iter__方法，而__iter__方法需要调用一个迭代器
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
    迭代器需要实现__next__、__iter__两个方法
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
