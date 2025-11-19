students = {"Harry": 82, "John": 71, "Mavi": 67}

# to add a student and their score
students["Jack"] = 99
print(students)

# to change a student's score
students["John"] = 92
print(students)

# to delete a student
del students["Mavi"]
print(students)

# to show a student and their score
print("Harry got: ", students["Harry"])


# NEW STUDENTS
# students with their scores
newStudents = ["Messi", "Ronaldo", "Neymar"]
marks = [99, 98, 97]

# to show their scores
marksheet = dict(zip(newStudents, marks))
print("new students marksheet", marksheet)
