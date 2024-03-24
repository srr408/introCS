N=int(input("Please enter a positive integer: "))

for i in range(1,N+1):
	print(" "*(N-i),end="")
	print("*"*i)
