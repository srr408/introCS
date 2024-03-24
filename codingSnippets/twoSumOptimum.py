def twoSum(nums: list[int], target: int) -> list[int]:
        numbersInList={}
        for index in range(len(nums)):
            numbersInList[nums[index]]=index

        for i in range(len(nums)):
            j=numbersInList.get(target-nums[i])
            if j!=None and i!=j:
                return [i,j]

#test cases:
print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))