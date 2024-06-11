'''n=int(input("enter"))
for i in range(n+1):
    print(" * ")
    for j in range(i+1):
        print(" * ",end="")'''
co=input("enter the cordinates")
n=int(input("number"))
if((co=='a')or(co=='c')or(co=='e')or(co=='g')):
    if(n%2==0):
        print("white")
    else:
        print("black")
else:
    if(n%2==0):
        print("black")
    else:
        print("white")
        

