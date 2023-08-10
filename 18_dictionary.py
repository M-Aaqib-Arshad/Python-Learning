# difference between empty set and dictionary 
a = {}     # is a empty diction
b =  set()  # is a empty set 

print("Type of A is ",a,type(a)) 
print("Type of b is ",b,type(b)) 




dic = {
    1 : "Aaqib",
    2 : "Zohaib",
    3 : "Ali",
    4 : "Moeed"
}

print(dic[4])
print(dic[1])

marks = {
    "Aaqib" : 49,
    "Zohaib": 45,
    "Moeed" : 42,
    "Ali Faizan": 47
}

marks["Bilal"] = 45

print(marks)
print(marks["Aaqib"]) # gives an error if does not exist

# get method prevents from error it gives none if value does not present

print(marks.get("ali Faizan")) # none  # in this case dictionary is case sensitive
print(marks.get("Ali Faizan")) # 47  # case sensitive
