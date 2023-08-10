lst = [2,5,1,6,1,2,4,5,"Aaqib"]

# In python, it can not change the string and in slicing python make a new string 
# but in list you can modify and change it.

print(lst)
print(type(lst)) 

# Methods

lst.remove("Aaqib")
print("After removing function",lst) 
# print(lst.count(1))

# lst.sort()
lst.pop()  #del the random one, and you can also give the index of item like lst.pop(3)
print("After pop function",lst) 

print("For we ",lst.pop())

lst.append(7)
print("After append function",lst) 

# lst.clear() Output empty list
lst.extend([8,9,0]) # you can also add tuple in the list
print("After extend function",lst) 

lst.insert(8,10)
print("After insert function",lst) 

print(lst.index(9))
print(lst)


# Slicing 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# changing the list 

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

del thislist[0]

print(thislist)


# Loops

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

for x in range(len(thislist)):
  print(thislist[x])


# while loop 
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
