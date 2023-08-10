class Employee:
     def __init__(self,fname,lname,salary,speciality,experience):
          
          self.fname = fname
          self.lname = lname
          self.salary = salary  
          self.speciality = speciality
          self.experience = experience
          
     def getSalary(self):
        print(self.salary)
   
    





harry = Employee("Harry","Porter","$4000","Programmer","2 Years")
Aaqib = Employee("Aaqib","Arshad","$5000","Data Analyst","3 Years")

print(harry, Aaqib)

# harry.fname = "Harry" 
# harry.lname = "Porter" 
# harry.salary = "40000"

print(harry.fname,Aaqib.fname)

Aaqib.getSalary()

