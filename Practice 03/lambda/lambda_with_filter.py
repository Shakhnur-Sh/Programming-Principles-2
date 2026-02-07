numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers) # [1, 3, 5, 7]


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) # [2, 4, 6, 8]


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
greater_than_4 = list(filter(lambda x: x > 4, numbers))
print(greater_than_4) # [5, 6, 7, 8]


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
less_than_4 = list(filter(lambda x: x < 4, numbers))
print(less_than_4) # [1, 2, 3]