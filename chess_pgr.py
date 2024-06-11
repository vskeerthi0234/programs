'''co=input("enter the cordinates")
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
        print("white")'''
e_r="bdfh"
o_c="1357"

e_c="2468"
o_c="aceg"
s=input()
if s[0] in e_c:
    if s[1] in e_r:
        print("black")
    else:
        print("white")
else:
    if s[1] in e_r:
        print("white")
    else:
        print("black")