#without recursion
print("factorial of a positive integer without recursion")
x=int(input("enter a positive number:"))
fact=1
for i in range(1,x+1):
    fact*=i
print("factorial of given integer",x," is:",fact)
#with recursion
print("factorial of a given integer with recursion")
y=int(input("enter a positive integer:"))
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
print("factorial of given integer",y," is:",fact(y))
