class MyClass:
  x = 5

print(MyClass) # <class '__main__.MyClass'>


#Create an object named p1, and print the value of x:
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x) # 5


#Delete the p1 object:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1

print(p1) # NameError: name 'p1' is not defined


#Create three objects from the MyClass class:
class MyClass:
  x = 5

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x) # 5
print(p2.x) # 5
print(p3.x) # 5

# having an empty class definition like this, would raise an error without the pass statement
class Person:
  pass