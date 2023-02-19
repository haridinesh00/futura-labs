import re

x = "Hello"
y = re.findall("lo", x)
print(y)
z = re.search("lo", x)
w = re.split("e", x)
print(z)
print(w)

e = "Hello, today is gjhgjhg khkjhkj"
g = re.split("\s", e)
print(g)

f = re.sub("o", "i", e)
print(f)
