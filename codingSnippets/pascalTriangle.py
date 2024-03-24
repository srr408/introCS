def pascalTriangle(n:int)->list[int]:
    baseCase=[[1]]
    if n==0:
        return baseCase
    for i in range(n):
        newLevel=[1]
        prevLevel=baseCase[-1]
        for j in range(len(prevLevel)-1):
            
             newLevel.append(prevLevel[j] +prevLevel[j+1])
        newLevel.append(1)
        baseCase.append(newLevel)
    return baseCase
            
    
print(pascalTriangle(5))