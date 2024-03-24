def sort(unsortedList:list[int])->list[int]:#[12,-2,9,0]
    
    for i in range(1,len(unsortedList)):

        key=unsortedList[i]
        j=i-1

        while j>=0 and key<unsortedList[j]:
            unsortedList[j+1]=unsortedList[j]
            j-=1 #j=j-1, decrementing j
            unsortedList[j+1]=key
    
    return unsortedList

list=[12,-2,9,0]
print(sort(list))