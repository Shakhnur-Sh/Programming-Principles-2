class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name) # Emil
print(p1.age) # 36



# Without the __init__() function, we would have to set the properties manually like this:
class Person:
  pass

p1 = Person()
p1.name = "Tobias"
p1.age = 25

print(p1.name) # Tobias
print(p1.age) # 25



# The __init__() function is called automatically every time the class is being used to create a new object.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 28)

print(p1.name) # Linus
print(p1.age) # 28



class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age) # Emil 18
print(p2.name, p2.age) # Tobias 25



# The __init__() function can take as many arguments as you want, but the first argument must always be self.
# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name) # Linus
print(p1.age) # 30
print(p1.city) # Oslo
print(p1.country) # Norway