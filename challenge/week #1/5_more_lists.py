name_list = ["Rakeeb", "Nirvana"]
# list creates a new object for list
another_list = list(name_list)

print("List 1: {}".format(name_list))
print("List 2: {}".format(another_list))

if name_list == another_list:
    print("lists are equal")

another_list.sort(reverse=True)
print("updated list: {}".format(another_list))

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7]

numbers = [even, odd]


for number_set in numbers:
    print(number_set)
    for value in number_set:
        print(value)
