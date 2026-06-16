# Create a set of 6 students (with 2 duplicates)
students = {"Rahul", "Priya", "Amit", "Sneha", "Rahul", "Priya"}

# Print set (duplicates are automatically removed)
print("Students Set:", students)

# Add 2 new students
students.add("Rohan")
students.add("Anjali")

print("Updated Set:", students)

# Create a dictionary of 4 students with their marks
marks = {
    "Rahul": 82,
    "Priya": 68,
    "Amit": 55,
    "Sneha": 76
}

# Loop through dictionary and display result
for student, score in marks.items():
    print(student, "-", score, ":")

    if score >= 75:
        print("Distinction")
    elif score >= 60:
        print("Pass")
    else:
        print("Fail")