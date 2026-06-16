# Custom Exceptions
class InvalidAgeError(Exception):
    pass

class InvalidMarksError(Exception):
    pass

try:
    # Input from user
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))

    # Age validation
    if age < 15 or age > 30:
        raise InvalidAgeError("Invalid Age! Age must be between 15 and 30.")

    # Marks validation
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Invalid Marks! Marks must be between 0 and 100.")

    # Successful registration
    print("Student registered successfully!")

except InvalidAgeError as e:
    print(e)

except InvalidMarksError as e:
    print(e)