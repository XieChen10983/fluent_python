# coding=gbk


class A:
    def ping(self):
        print("ping:", self)


class B(A):
    def pong(self):
        print("pong:", self)


class C(A):
    def pong(self):
        print("PONG:", self)


class D(B, C):
    def ping(self):
        super(D, self).ping()
        print("post-ping:", self)

    def pingpong(self):
        self.ping()
        # super().ping()
        super(D, self).ping()
        self.pong()
        super(D, self).pong()
        C.pong(self)
