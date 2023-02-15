# Pyramid star pattern

limit = int(input("Enter a limit : "))

space = " "
spaces = limit - 1
for i in range(limit):
    print(spaces*space, end="")
    spaces = spaces - 1
    for j in range(i):
        print("* ", end="")
    print("")
