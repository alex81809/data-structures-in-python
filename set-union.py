# first set
set1 = {"blue", "green", "red", "yellow"}

# second set
set2 = {"purple", "green", "blue", "orange"}

# union takes both common and uncommon values
union = set1.union(set2)
print(union)

# intersection takes only the common values between both of the sets
inter = set1.intersection(set2)
print(inter)
