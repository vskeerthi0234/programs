'''
class parent:
    def __init__(self,a,b):
        self.a1=a
        self.b2=b
class child(parent):
    def cal(self):
        add=self.a1+self.b2
        print(add)
obj=child(10,20)
obj.cal()'''


#multiple inheritance

class A:
    m1=int(input("m1 marks"))
    m2=int(input("m2 marks"))
    m3=int(input("m3 marks"))
class B:
    sub=input("name of sub:")
class c(A,B):
    def tot(self):
        tot_mrks=self.m1+self.m2+self.m3
        print(tot_mrks)
obj=c()
obj.tot()


#constructor overloading
'''class check:
    def add(self,a):
        print(a)
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
obj=check()
obj.add(5)
obj.add(5,6)
obj.add(2,3,5)'''

