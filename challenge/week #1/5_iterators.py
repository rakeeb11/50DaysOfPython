# Iterable

string = "1234567890"

for char in string:
    # an iterator is created from the string
    print(char)

custom_iterator = iter(string)
next(custom_iterator)

days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
day_iterator = iter(days)
for i in range(0, len(days)):
    day = next(day_iterator)
    print(day)

