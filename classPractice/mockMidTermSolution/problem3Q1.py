int1=int(input("Please enter first integer: "))
int2=int(input("Please enter second integer: "))
int3=int(input("Please enter a third integer: "))

#min function takes input min(x0,x1,x2,...,xn) and returns the smallest value
# from the given inputs.
for i in range(1,min(int1,int2,int3)):
    if int1%i==0 and int2%i==0 and int3%i==0:
        print(i)