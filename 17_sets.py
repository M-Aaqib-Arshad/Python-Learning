set1 = {1,3,5,6,6,7}
set2 = {1,4,6,8,9,0}
set3 = {3,5,6}

print(set1)

# set1.remove(6) # remove 6 from set1

print(set1.union(set2))
print(set1.intersection(set2))

# update the set1 
# set1.intersection_update(set2)

x = set1.issuperset(set3)
print("set1 is super set of set3 :",x)  # true

y = set3.issubset(set1)
print("set3 is sub set of set1 :",y)  # true

z = set3.isdisjoint(set1)
print("set1 and set3 are disjoint sets  :",z) # False





 

print(set1)