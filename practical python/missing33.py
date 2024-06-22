#Python dictionary with keys having multiple inputs
num=int(input("enter number of students :-"))
student={}
for i in range(num):
    roll=i+1
    name=input("enter student name :- ")
    marks =int(input("enter the marks :- "))
    student[roll]=[[name],[marks]]
print(student)