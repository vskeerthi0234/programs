a=[4,0,5,0,1,9,0,0]
n=len(a)
j=0
for i in range(0,n):
    if a[i]!=0:
        a[j]=a[i]
        j+=1
while j<n:
    a[j]=0
    j+=1
print()
    
    
