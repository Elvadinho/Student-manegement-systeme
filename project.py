# Initialising the class Student
class Student:

    # Instantiate Constructor
    def __init__(self, id, name, gender):
        self.id= id
        self.name= name
        self.gender= gender
    
    # Function to create and add a new student
    def add_student(self,id, Name, Gender):
        obj=Student(id, Name, Gender)
        stud_list.append(obj)

    # To display the Student list
    def view_student(self, obj):
        print("ID : ",obj.id)
        print("Name : ",obj.name)
        print("Gender : ",obj.gender)
        print("\n")

    # To update a student's information
    def update(self):
        pass

    # To remove a student
    def delete(self, delete):
        del stud_list[delete]
        
# Initiasialising the class Subject
class Subject:

    def __init__(self, id, name, coef):
        self.id=id
        self.name=name
        self.coef=coef
    
    def add_subject(self, id, name, coef):
        subj=Subject(id, name, coef)
        stud_list.append(subj)

    def view_subject(self, subj):
        print("Subject ID : ",subj.id)
        print("Subject Name : ",subj.name)
        print("Coefficient : ",subj.coef)
        print("\n")

    def delete(self, delete):
        del subj_list[delete]

    def check_if_passed():
        pass
####
# List of students
stud_list=[]

# An object of student class
obj= Student(0,'','')

obj.add_student(1,"ANANTIA TEMGOUA",'M')
obj.add_student(2,"Vanessa MANESSONG",'F')
obj.add_student(3,"TEMGOUA PAPA",'M')

####
# List of subjects
subj_list=[]

# An object of subject class
subj= Subject(0,'',0)

subj.add_subject(101,"Math ", 5)
subj.add_subject(102,"Chemistry ", 2)
subj.add_subject(103,"Biology ", 3)


print("Operations that can be used: ")
print("1.Accept Student details\n2.Display Student Details\n3.Delete Details of Student\n4.Update Student Details\n5.Exit")

while 1==1:

    ch=int(input("Enter choice: "))
    if(ch==1):
        id=int(input("Enter your id "))
        name=input("Enter your name ")
        gender=input("Enter your gender ")

        obj.add_student(id,name,gender)

    elif(ch==2):
        print("\n List of Students")
        for i in range(stud_list.__len__()):
            obj.view_student(stud_list[i])

    elif(ch==3):
        deletion=int(input('Enter the ID of the student you want to delete: '))
        obj.delete(deletion)
        print("\nList after deletion")
        for i in range(stud_list.__len__()):
            obj.view_student(stud_list[i])

    elif(ch==4):
        stud=int(input('Enter the ID of the student you want to update: '))
        obj.update

    else:
        print("Thank You ! ")

