# Find Strings whose alternate characters are vowels.Given a list as ['EUTOPIA','COMPUTER','SUOIDEA','AIEEE','CHICKEN','EMELIA','BURGER','ONES','PUPPY','ZEBRA']
# write a program that prints all elements of the above-given list whose elements have alternative vowels.
# Expected output-['EUTOPIA','SUOIDEA','AIEEE','EMELIA','ONES']

inp = ['EUTOPIA','COMPUTER','SUOIDEA','AIEEE','CHICKEN','EMELIA','BURGER','ONES','PUPPY','ZEBRA']
arr = []

#inp = list(input("Enter a list of strings : ").split())

vowel = ['A', 'E', 'I', 'O', 'U','a','e','i','o','u']

for i in inp:
    for j in range(len(i)-2):
        if i[j] in vowel and i[j+2] in vowel:
            arr.append(i)
arr = list(set(arr))
print(arr)
