# Armstrong number

num = input("Enter a number : ")
sum = 0
for i in num:
    sum = sum + (int(i)**3)
if sum == int(num):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
