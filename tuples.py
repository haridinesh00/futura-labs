a = (5, 6, 7)

a = list(a)
a[1] = 8
a.append(9)
a.remove(8)
a = tuple(a)
print(a)

i = 0
while i < len(a):
    print(a[i])
    i = i + 1

b = (1, 2, 3)

c = a + b
print(c)