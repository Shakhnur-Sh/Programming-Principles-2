#Return statement:
def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)
# 8


#A function that returns a list:
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0]) # apple
print(fruits[1]) # banana
print(fruits[2]) # cherry



#A function that returns a tuple:
def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x) # 10
print("y:", y) # 20



#A function that returns a dictionary:
def my_function():
  return {"name": "Emil", "age": 25}
person = my_function()
print("Name:", person["name"]) # Name: Emil
print("Age:", person["age"]) # Age: 25