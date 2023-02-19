x = lambda a: a-5
print(x(10))
x = lambda a, b: a*b

def fun(x):
    return lambda a: a-x

v = fun(4)
print(v(5))
