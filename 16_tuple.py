tple = (1,4,5,6,7,8,99,9,4)

print(tple.count(4))
print(tple.index(4))

# You cannot change the tuple, allows duplicate values,
#  ordered means you can not change the order of any item

print("Index of 5 in tuple :",tple.index(5))
print("Full Tuple is : ",tple)


# you can change tuple with type casting 

x = ("apple", "banana", "cherry")
y = list(x)
# y[1] = "kiwi"  
x = tuple(y)

print(x)


tup1 = (1,"Python",3)
tup2 = (4,"Python",78,False)

# for duplcating the tuple
print(tup1 * 2)
# You can add to tuples and output is new tuple
print(tup1 + tup2)

# Multiplication and addition simultanousely 

tup3 = (tup1 *2 + tup2)

print(tup3)

# tuple 4 
tup4 = (1,5,7,88,9,544,34,77)
# Maximum in tuple
print(max(tup4)) 
# Minmum from tuple
print(min(tup4))

