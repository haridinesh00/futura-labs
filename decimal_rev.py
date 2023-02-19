# Given a real number as a string 1.write a program to extract the parts before and after the decimal point 2.
# Form a new number by reversing their positions 3.print a meesage if the newly formed number is greater than the original number.
# eg:- "123.654" after extraction it would be 123 and 654 after reversing it would be 654.123

inp = input("Enter a number: ")
ext = inp.split('.')

#print(ext)
# print(ext)

print("Number before decimal point : ",ext[0], "\nNumber after decimal point : ", ext[1])

new_num = float(ext[1]+"."+ext[0])
print("New number : ", new_num)

if new_num > float(inp):
    print(new_num, "is greater than ", float(inp))
else:
    print(new_num, "is less than ", float(inp))
