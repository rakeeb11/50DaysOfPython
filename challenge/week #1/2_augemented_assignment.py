number = "9, 223, 372, 036"
cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        """cleanedNumber = cleanedNumber + number[i] # normal assignment"""
        # augmented assignment -> +=, -=, *=, & /=, <<= >>= |=
        cleanedNumber += number[i]

newNumber = int(cleanedNumber)
print("new number: {}".format(cleanedNumber))

x = 23
x += 1
print(x)

x -= 4
print(x)

x *= 5
print(x)

x /= 5
print(x)