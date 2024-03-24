userStr=input("Please insert a string: ")

vowel=0
listVowels='aeiou'
for char in userStr:
    if char in listVowels:
        vowel+=1

print(f"There are {vowel} vowels in the word {userStr}")
