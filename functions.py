class college:
    def __init__(self,cse,aiml):
        self.cse1=cse
        self.aiml1=aiml
        print("this is constructor")
    def get_details(self,stud_name,stud_usn):
        print("enter your details")
        self.stud_name=input("enter you name")
        self.stud_usn=input("enter you USN")
        stud_sec=input("enter you section")
    def marks_details(self,m1,m2,m3):
        print("enter your marks")
        self.m1=int(input("enter sub1 marks"))
        self.m2=int(input("enter sub2 marks"))
        self.m3=int(input("enter sub3 marks"))
    def set_details(self):
        student_name=self.stud_name
        student_usn=self.stud_usn   
        total_marks=self.m1+self.m2+self.m3
        print("student name:",student_name)
        print("student USN:",student_usn)
        print("total marks:",total_marks)
        print("cse:",self.cse1)
        print("aiml:",self.aiml1)
clg=college(90,80)
clg.get_details("keerthi","harini")
clg.marks_details(10,20,30)
clg.set_details()
