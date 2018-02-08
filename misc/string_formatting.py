__author__ = 'dev'

age = 24

# str functions
print("My age is " + str(age) + " years")

# replacement fields
print("my age is {0} years".format(age))

months = {"Jan", "March", "May", "July", "August", "October", "December"}

# replacement fields are efficient
print("""
    January: {0}
    Feb: {1}
    March: {2}
    April: {1}
""".format(31, 28, 30))

# old way!
print("my age is %d years" % age)

for i in range(1, 12):
    print("no. {} squared is {} and cubed is {}".format(i, i **2, i **3))

# string formatting operators


