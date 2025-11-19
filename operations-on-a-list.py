fruits = ["Mango", "Banana", "Orange", "Apple", "Kiwi"]

# to show the amount of items 
print("The length of the list is: ", len(fruits))

# to show the first item
print("The first item of the list is: ", fruits[0])

# to show the last item
print("The last item of the list is: ", fruits[-3])

# to add an item
fruits.append("Coconut")
print(fruits)

# to remove an item
fruits.remove("Kiwi")
print(fruits)

# to sort the list
fruits.sort()
print(fruits)

# to remove an item by index
fruits.pop(2)
print(fruits)

# to switch or reverse items
fruits.reverse()
print(fruits)

# to multiply the items
print("Multiplication of the list: ", fruits * 2)

# to remove specific items from the list
sliced = fruits[1:4]
print(sliced)

# to clear out the entire list
sliced.clear()
print("clear function of the list: ", sliced)
