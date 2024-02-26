print('Hello World')
print("Hello World")
print('''Hello world''')  #Used for multiline
print("What's upf?")


# String behaves like an array

a = "Hello, World"

print(a[0],a[1])


# String Looping 

b = "Banana"
name = 'aaqib'

for x in b:
    print(x)
# Length of a String 
print(len(b))

# String Slicing 

print(b[0:3])
print(b[-4:-1])
print(b[0:])

# String Methods
print(name.capitalize()) # First letter only
# print(name.center) 
print(name.upper())      # All letters are Capitalize
print(name.count('a'))      # Count All the numbers of character which you want to find

print(name.isalnum())   # True
print(name.isalpha())   # True
print(name.isascii())   # True
print(name.isdigit())   # Fales

print(a.strip()) # returns "Hello, World!" Remove white spaces

print(a.replace("H", "J"))  # Replace the H with J

print(a.split(",")) # returns ['Hello', ' World!'] Sperates if on the basis of commas or sperator

# Concatination 

greetings = "Hi!"
name = " Aaqib"

c = greetings + name
print(c)

# Format method to concate string with number
age = 20
text = "Hello, I am Aaqib and i am {age} year old"
print(text) #Hello, I am Aaqib and i am {age} year old
text = "Hello, I am Aaqib and i am {} year old"

print(text.format(age))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# Escape Characters 
txt = "We are the so-called \"Vikings\" from the north."
print(txt) 
