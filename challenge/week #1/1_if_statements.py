def startNameGame():
    name = input("What is your name?\n")
    age = int(input("How old are you {0}?\n".format(name)))

    if 20 <= age < 100:  # adult
        if age == 20:
            print("You are an adult {}. Welcome to adulthood".format(name))
        else:
            print("You are an adult {}".format(name))
    elif age > 12:  # child
        print("Hi there child!")
    elif 12 >= age >= 18:  # teenager
        print("Hi there teenager! {}".format(name))
    else:  # invalid age
        print("Invalid age {}".format(name))


def agedGreeting():
    age = int(input("How old are you?\n"))

    if (age < 16) or (age > 65):
        print("Enjoy your free time")
    else:
        print("Have a great day at work")


def booleansInPython():
    """
        FUN FACT: Python does not have a boolean data type!!
        true is 1 and false is 0

        bool() can evaluate a boolean condition
        Python has True and False only
    """
    x = 0

    if bool(x):
        print("true")

    x = input("enter something here:")
    if x:
        print("you entered '{}'".format(x))
    else:
        print("you did not enter anything")

    print(not True)
    print(not False)


def usingNot():
    name = "Rakeeb"
    letter = input("Enter a character: ")

    if letter not in name:
        print("I don't need that letter")
    else:
        print("Please give me a {}, Rakeeb".format(letter))


usingNot()
