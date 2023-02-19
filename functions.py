# Functions

# Arbitrary argument
def hello(*x):
    print(x[1])

hello(1, 2, 3)

# Arbitrary keyword argument
def new(**x):
    print("Value is ", x["b"])

new(a=2, b=4, c=5)

def hai(x = 5):
    print("Input value is", x)
hai()

def books(x):
    for i in x:
        print(i)
x = [1, 2, 3, 4, 5]
books(x)

def library(x):
    return x
print(library(10))
