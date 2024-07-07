'''n = input("Enter a string:")
l = len(n)
flag = True
i = 0

while i < l:
    if n[i] !=n[l - 1 - i]:
        flag = False
        break
    i+=1
if flag:
    print("Palindrome")
else:
    print("Not a palindrome")'''


n = input("Enter a string:")
#rev = ''.join(reversed(n))
#print(rev)
m=n[::-1]
print(m)
if(n==m):
    print("yes")
else:
    print("no")