#A function with one argument:
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil") # Emil Refsnes
my_function("Tobias") # Tobias Refsnes
my_function("Linus") # Linus Refsnes


#The parameter is the variable that is defined in the function definition.
#While the argument is the value that is passed to the function when it is called.
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument



#A function with two arguments:
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
# Emil Refsnes


#If you try to call the function with the wrong number of arguments, you will get an error
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")
# TypeError: my_function() missing 1 required positional argument: 'lname'


def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil") # Hello Emil
my_function("Tobias") # Hello Tobias
my_function() # Hello friend
my_function("Linus") # Hello Linus



def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden") # I am from Sweden
my_function("India") # I am from India
my_function() # I am from Norway
my_function("Brazil") # I am from Brazil



def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")
# I have a dog
# My dog's name is Buddy


def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")
# I have a dog
# My dog's name is Buddy



#When you call a function with arguments without using keywords, they are called positional arguments.
#The order matters with positional arguments.
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy") 
# I have a dog
# My dog's name is Buddy



#Positional arguments must come before keyword arguments:
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)
# I have a 5 year old dog named Buddy


#Sending a list as an argument:
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)
# apple
# banana
# cherry


#Sending a dictionary as an argument:
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)
# Name: Emil
# Age: 25



#To specify positional-only arguments, add ", /" after the arguments:
def my_function(name, /):
  print("Hello", name)

my_function("Emil")
#With ", /", you will get an error if you try to use keyword arguments:

#my_function(name = "Emil") # TypeError: my_function() got some positional-only arguments passed as keyword arguments: 'name'

#To specify that a function can have only keyword arguments, add "*," before the arguments:
def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")
#With "*,", you will get an error if you try to use positional arguments:



#Arguments before "/" are positional-only, and arguments after "*" are keyword-only:
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result) # 50