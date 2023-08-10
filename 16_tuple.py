tple = (1,4,5,6,7,8,99,9,4)

print(tple.count(4))
print(tple.index(4))

# You cannot change the tuple, allows duplicate values,
#  ordered means you can not change the order of any item

print(tple)


# you can change tuple with type casting 

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"  
x = tuple(y)

print(x)