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
    count-=1
    temp//=10
print(sum)
if(n==sum):
    print("disarum")
else:
    print("not a disarum")
#135=1**1 + 3**2 + 5**3