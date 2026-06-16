# Parent Class
class Person:
    def walk(self):
        print("Person is walking")

    def talk(self):
        print("Person is talking")


# Child Class Teacher
class Teacher(Person):
    def teach(self):
        print("Teacher is teaching")


# Child Class Student
class Student(Person):
    def study(self):
        print("Student is studying")


# Creating objects
teacher = Teacher()
student = Student()

# Calling methods for Teacher
print("Teacher:")
teacher.walk()      # Inherited
teacher.talk()      # Inherited
teacher.teach()     # Own method

# Calling methods for Student
print("\nStudent:")
student.walk()      # Inherited
student.talk()      # Inherited
student.study()     # Own method