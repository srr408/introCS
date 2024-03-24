import random

provinces=["Anhui", "Fuzhou","Gansu", "Guangdong","Guizhou"]
capitals=["Hefei","Fujian","Lanzhou","Guangzhou", "Guiyang"]

capitalOfProvinces={}
for i in range(len(provinces)):#remember, capitals[i] will give you capital of provinces[i].
    capitalOfProvinces[provinces[i]]=capitals[i]

flag=""

userName=input("Please enter your name: ")
print("Welcome {}!".format(userName))
score=0
correctGuess=0
wrongGuess=0
round=1
while flag!="EXIT":
    province=provinces[random.randint(0,len(provinces)-1)]
    correctAns=capitalOfProvinces[province]
    print("Round:{}".format(round))
    print("Score:{}".format(score))
    print("Correct Guesses:{}".format(correctGuess))
    print("Incorrect Guesses:{}".format(wrongGuess))
    print("Type EXIT to quit game")
    ans=input("Guess the capital of {}: ".format(province))
    if ans=="EXIT":
        flag="EXIT"
    elif ans.lower()==correctAns.lower():
            print("CORRECT!")
            score+=1
            correctGuess+=1
    else:
        print("WRONG! Better luck next time!")
        wrongGuess+=1
    round+=1
    
print("Thank you for playing{}! Your score is {}".format(userName,score))