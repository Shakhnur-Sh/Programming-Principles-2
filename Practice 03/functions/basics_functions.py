def my_function():
  print("Hello from a function")

my_function()
# Hello from a function


def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77)) # 25.0
print(fahrenheit_to_celsius(95)) # 35.0
print(fahrenheit_to_celsius(50)) # 10.0


def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message) # Hello from a function

# We can also call the function directly in the print statement
def get_greeting():
  return "Hello from a function"

print(get_greeting()) # Hello from a function


def my_function():
  pass