'''def power(a,b):
    if b==0:
        return 1  
    return a*power(a,b-1)
print(power(2,3))'''

#num=int(input())
def add(num):
    if num==0:
        return 0
    return num%10+add(num//10)
print(add(123))