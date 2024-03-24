#A function assigns each input one output.

def insertionSort(numbers:list[int])->None:

    for i in range (1,len(numbers)):
        j=i-1
        key=numbers[i]
        while j>=0 and numbers[j]>key:
            numbers[j+1]=numbers[j]
            j-=1
        numbers[j+1]=key

if __name__ == "__main__":
    numbers=[x for x in range(10,0,-1)]
    print(numbers)
    insertionSort(numbers)
    print(numbers)

