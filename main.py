print("Hello World")
a = [1, 2, 3, 4, 5]
a.insert(1, 5)
print(a)
a.append(56)
print(a)
b = [5, 6, 7, 8]

a.extend(b)
print(a)
a.remove(6)
print(a)
a.pop(1)
print(a)
a.pop()
print(a)
del a[2]
print(a)

# a = sorted(a)
# print(a)
a.sort()
print(a)

c = ["Hello", "Apple", "Balloon"]
c.sort()
print(c)

e = c.copy()
print(e)
e  = c + e
print(e)