class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name) # Emil
print(p1.age) # 36


# Create a class named Person, with properties name and age, and a method that prints the name and age of the person in a sentence:
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand) # Toyota
print(car1.model) # Corolla


# Create a class named Person, with properties name and age, and a method that prints the name and age of the person in a sentence:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.age = 40

print(p1.age) # Output: 40


# Delete the age property from the p1 object:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Linus", 18)

del p1.age

print(p1.name) # Output: Linus
print(p1.age) # Output: AttributeError: 'Person' object has no attribute 'age'


# Create a class named Person, with properties name and age, and a method that prints the name and age of the person in a sentence:
class Person:
  species = "Human"  # Class property

  def __init__(self, name):
    self.name = name  # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name) # Output: Emil
print(p2.name) # Output: Tobias
print(p1.species) # Output: Human
print(p2.species) # Output: Human


# Class properties are shared by all instances of the class, while instance properties are unique to each instance. 
# You can access class properties using the class name or an instance of the class:
class Person:
  lastname = ""

  def __init__(self, name):
    self.name = name

p1 = Person("Linus")
p2 = Person("Emil")

Person.lastname = "Refsnes"

print(p1.lastname) # Output: Refsnes 
print(p2.lastname) # Output: Refsnes


# You can also delete properties from objects, and objects can also contain methods. 
# Methods in objects are functions that belong to the object.
class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")

p1.age = 25
p1.city = "Oslo"

print(p1.name) # Output: Tobias
print(p1.age) # Output: 25
print(p1.city) # Output: Oslo