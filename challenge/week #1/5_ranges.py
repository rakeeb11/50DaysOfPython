print(range(10))

# iteration with range is a better choice
numbers = list(range(10))
print(numbers)

even_numbers = list(range(0, 10, 2))
odd_numbers = list(range(1, 10, 2))

print(even_numbers)
print(odd_numbers)


alphabets = "abcdefghijklmnopqrstuvwxyz"
print(alphabets.index('e'))

small_decimals = range(0, 10)
print(small_decimals.index(3))

odd = range(1, 1000, 2)
print(odd[2])

sevens = range(7, 100, 7)
print(sevens)