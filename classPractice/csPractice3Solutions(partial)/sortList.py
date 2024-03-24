import copy

def sortList(unsortedList:list[int])->list[int]:
    
    for i in range(1,len(unsortedList)):
        key=unsortedList[i]
        j=i-1
        while j>=0 and key<unsortedList[j]:
            unsortedList[j+1]=unsortedList[j]
            j-=1
        unsortedList[j+1]=key
    #ans=copy.deepcopy(unsortedList)
    return unsortedList


print(sortList([10,-2,4,1,8]))

    