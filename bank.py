# Deposit and withdrawal
inp = []
balance = 0
n = int(input("Enter the number of transactions : "))
for i in range(n):
    inp.append(list(input().split()))
# print(inp)

arr_len = len(inp)
# print(arr_len)
for j in range(arr_len):
    if inp[j][0] == 'D' or inp[j][0] == 'd':
        balance = balance + int(inp[j][1])
    elif inp[j][0] == 'W' or inp[j][0] == 'w':
        balance = balance - int(inp[j][1])
    else:
        print("Mistake in entered data, enter D for deposit and W for withdrawal")
print("Balance is ", balance)
