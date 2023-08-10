lst = [2,5,1,6,1,2,4,5,"Aaqib"]

# In python, it can not change the string and in slicing python make a new string 
# but in list you can modify and change it.

print(type(lst)) 
print(lst)

# Methods

lst.remove("Aaqib")
# print(lst.count(1))

# lst.sort()
lst.pop()  # you can also give the index of item like lst.pop(3)
lst.append(7)
# lst.clear() Output empty list
lst.extend([8,9,0]) # you can also add tuple in the list

lst.insert(8,10)

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
