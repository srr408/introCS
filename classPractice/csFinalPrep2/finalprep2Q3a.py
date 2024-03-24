def listOfNumbers(n:int)->list[int]:
    #list[int] means either your parameter or the return type is of the type list of itegers:
    #type annotation is a new feature in python. It's option.
    #So you can write, 
    #def listOfNumbers(n):
    #people who are comfortable with python, will use list comprehension here.

    numbers=[0]*n#creates a list of size n, with each entries being 0.
    for i in range(1,n+1):
        numbers[i]=i
    #using list comprehension
    #return [i for i in range(1,n+1)]
    #you can also solve this way but this should be the 'slowest' was to solve this problem
    #numbers=[]
    #for i in range(1,n+1):
    #   numbers.append(i)
    #return numbers
    return numbers



