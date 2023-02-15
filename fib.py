# Fibonacci

num = int(input("Enter a number:  "))

a = 0
b = 1
c = 0
if num < 1:
    print("Number should be grater than 0")
elif num == 1:
    print(0)
else:
    for i in range(num):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
