def twoSum(nums:list[int],target:int)->list[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]+nums[j]==target and i!=j:
                return [i,j]

#test cases:
print(twoSum([2,7,11,15,7],9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))