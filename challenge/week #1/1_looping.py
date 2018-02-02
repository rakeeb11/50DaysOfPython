for i in range(1, 5):  # from 1 to 4
    print("i is {}".format(i))

number = "123"  # with length 3

for i in range(0, len(number)):  # from 0 to 2
    if i + 1 != len(number):
        print(number[i], end='')
    else:
        print(number[i])

for index, char in enumerate(number):  # using enumerate to get index of loop as well
    if index + 1 != len(number):
        print(char, end='')
    else:
        print(char)

for index, name in enumerate(["rakeeb", "nirvana"]):
    print("index: {} value: {}".format(index, name))

for i in range(0, 50, 5):  # adding in delimiter? with 5
    print("i is {}".format(i))

for i in range(1, 4):  # multiplication table from 1 and 3
    for j in range(1, 11):
        print("{1:2} times {0:2} is {2:2}".format(i, j, i * j))
    print("-------------------------")
