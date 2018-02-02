print("Hello World!")

# memory locations to store values


# multiple variable assignment :)
sarah, bob, mike = 16, 21, 17

sarah = bob = mike = 17

# strings have + and * operations
# arithmetic operators

# tuples cannot be modified -> immutable

# elif
# and | or

# Control statements
# break
# continue
# pass -> have nothing; filler

# try and except

"""
    Multi line comments
    :D 
    Hi
"""


def helloWorld():
    print("Hello World!")


helloWorld()


def greeting(name):
    print("Hi %s!" % name)


greeting("Rakeeb")


def returnAdd(a, b):
    return a + b


sum = returnAdd(3, 4)

print("sum %d" % sum)


# dir
# help
# eval
# exec
# str
# float
# int


# Object oriented programming

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        print("Your name is %s" % self.name)

    def getAge(self):
        print("Your age is %d" % self.age)


person = Person("Rakeeb", 25)
person.getName()
person.getAge()


# use self

# inheritance
class Parent:

    def __init__(self):
        print("This is a parent class")

    def parentFunc(self):
        print("This is the parent func")


class Child(Parent):

    def __init__(self):
        super().__init__()
        print("This is the child class")

    def childFunc(self):
        print("this is a child func")

    def parentFunc(self):
        print("this is call of parent from child func")


class Junior(Child):

    def __init__(self):
        super().__init__()


parent = Parent()
child = Child()
child.parentFunc()
