# to create a set
mySet = {1,1,1,2,2,3,4,4,4,4,5,5,5,5,5,5}
print(mySet)

# to add items
mySet.add(6)
print(mySet)

# to remove items
set1 = mySet
set2 = {3,4,5,6,7,8}

# to show the difference
diff = set2.difference(set1)
print(diff)

# to show the symmetric difference
symmetric = set1.symmetric_difference(set2)
print(symmetric)
