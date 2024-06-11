'''def factorial(n): 
    fact=1
    if(n==0 or n==1):
        return fact
    while n>0:
        digit=n%10
        fact=fact*(factorial(n-1))
        n=n//10
num=int(input("enter a number"))
print(factorial(num))'''

def fact(n):
    if n==0:
        return 1 
    return n * fact(n-1)
#print(fact(n))
num=int(input())
temp=num
sum=0
while num>0:
    digit=num%10
    sum=sum+fact(digit)
    num=num//10
print(sum)
if(sum==temp):
    print("The given number is strong number")
else:
    print("the given number is not a strong number")

'''def factorial(n):
    fact=1
    sum=0
    temp=n
    digit=n%10 
    while n>0:
        fact=fact*factorial(digit-1)
        return fact
    sum=sum+fact
    n=n//10
    if(sum==temp):
       print("strong")
    else:
       print("not strong")
num=int(input("enter a number"))
print(factorial(num))'''