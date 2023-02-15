# Palindrome

str_n = input("Enter a string or number: ")

str_rev = str_n[::-1]

if str_rev == str_n:
    print("Palindrome")
else:
    print("Not Palindrome")

# temp = ""
# for i in str_n:
#     temp = i + temp
#
# if temp == str_n:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
