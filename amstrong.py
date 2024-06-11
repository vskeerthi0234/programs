n=int(input("enter a number"))
sum=0
count=0
temp=n
while(temp>0):
    count+=1
    temp=temp//10
temp=n
while(temp>0):
    dig=temp%10
    sum+=(dig**count)
    temp//=10
print(sum)
print(count)
if(n==sum):
    print("amstrong")
else:
    print("not a amstrong")