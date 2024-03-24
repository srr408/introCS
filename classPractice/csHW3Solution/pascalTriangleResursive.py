def pascalTriangle(n:int)->list[list:int]:
    """
    :param n: Int -- Levels of pascal triangle

    :return: List[List[Int]] -- a list of sublists, which contains pascal values.
    """
    if n==0:
        return [[1]]
    previous=pascalTriangle(n-1)
    return previous+[[1]+[previous[-1][i]+previous[-1][i+1] for i in range(len(previous[-1])) if (i)!=len(previous[-1])-1]+[1]]


print(pascalTriangle(8))