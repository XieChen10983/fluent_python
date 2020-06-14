s = "caf$"
print(len(s))
b = s.encode("utf8")
print(b)
print(len(b))
s = b.decode("utf8")
print(s)
