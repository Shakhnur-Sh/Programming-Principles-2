# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# The parent class is the class being inherited from, also called the base class.
# The child class is the class that inherits from another class, also called the derived class.
# Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname() # Output: John Doe


# Now we can create a class named Student, which will inherit the properties and methods from the Person class:
# Create a class named Student, which will inherit the properties and methods from the Person class:
class Student(Person):
  pass


# Use the Student class to create an object, and then execute the printname method:
x = Student("Mike", "Olsen")
x.printname()



class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname() # Output: Mike Olsen