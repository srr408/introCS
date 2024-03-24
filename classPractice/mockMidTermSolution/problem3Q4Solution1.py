#this is a less pythonic way of solving the problem
userStr=input("Please insert a string: ")

vowel=0
for char in userStr:
    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
        vowel+=1

print(f"There are {vowel} vowels in the word {userStr}")