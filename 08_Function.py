text = "We are learning Python"


def first_function():
    print(1,text)
    print(2,text)
    print(3,text)
    print(4,text)

#  call A Function
first_function()

# Function with Parameters
def Second_Function(Param):
    print(1,Param)
    print(2,Param)
    print(3,Param)
    print(4,Param)

Second_Function("We are leaning python")


# Function with if else 
required_age = 5

def Calculator(Student_age, required_age):
    if Student_age == required_age:
       print("You can join the School")

    elif Student_age > required_age:
       print("You Should go to School.")
    else :
       print("You are not able to go to school.")


age = int(input("What is your age? : "))

Calculator(age , required_age)


def Future_age(currentAge):
    return currentAge + 18 

new_age = Future_age(18)

print(new_age)