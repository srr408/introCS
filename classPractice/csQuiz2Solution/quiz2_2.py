#naive solution
def Sum3(inputList:list[int],target)->list[int]:
    for i in range(len(inputList)):
        for j in range(len(inputList)):
            for k in range(len(inputList)):
                if i != j and j!=k and i!=k and (inputList[i]+inputList[j]+ inputList[k]==target):
                    return [i,j,k]

print(Sum3([1,8,9,12,20],30))