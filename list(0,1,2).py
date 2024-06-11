l=[2,1,0,1,1,2,0,0]
n=len(l)
c_0=0
c_1=0
c_2=0
for i in range(n):
    if l[i]==0:
        c_0+=1
    elif l[i]==1:
        c_1+=1
    else:
        c_2+=1
j=0

while c_0>0:
    l[j]=0
    j=j+1
    c_0=c_0-1

while c_1>0:
    l[j]=1
    j=j+1
    c_1=c_1-1

while c_2>0:
    l[j]=2
    j=j+1
    c_2=c_2-1
print(l)


