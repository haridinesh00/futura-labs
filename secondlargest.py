# Find second largest number
# inp = []
# inp = list(map(int, input("Enter a list of numbers: ").split()))
#
# inp.sort()
# print(inp)
# print("Second largest number is :", inp[-2])

new_arr = []
n = int(input("Enter the limit : "))
print("Enter the numbers: ")
for i in range(n):
    new_arr.append(int(input()))
new_arr.sort()
print("Second largest number is : ", new_arr[-2])
