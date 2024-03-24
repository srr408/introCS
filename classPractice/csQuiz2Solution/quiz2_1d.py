# if a list is sorted in ascending order, any two elements chosen from list, L, must satisfy the property L[i+1]>=L[i], where is a valid index.
#so we check if this property is held in the list.

def isSorted(inputList:list[int])->bool:
    for i in range(len(inputList)-1):
        if inputList[i+1]<inputList[i]:
            return False

    return True

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
print(isSorted(list))
sort(list)
print(isSorted(list))