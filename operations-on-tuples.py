# tuples
marks = (56, 756, 234, 656, 546, 45)
print(marks)

# you can write different data types at the same time inside of the tuple
marks = (78, "codingal", False)

# nested tuples
marks = (56,(567567,234,"welcome"), [877, 345, 345, 345])
print(marks)

print(marks[1])
print(marks[1][2])

for i in marks:
    print("Hello", i)
