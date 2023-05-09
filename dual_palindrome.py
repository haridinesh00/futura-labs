# check if palindrome

str_a = input("Enter first string : ")
str_b = input("Enter second string : ")

con_result = str_a + str_b
print("Entered string : ", con_result)
if(con_result[::-1] == con_result):
    print("Palindrome")
else:
    print("Not Palindrome")
