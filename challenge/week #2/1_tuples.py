# immutable list of data

t = "a", "b", "c"  # a tuple

print(t)

print("a", "b", "c")  # individual strings
print(("a", "b", "c"))  # also a tuple

welcome = "Welcome to my Nightmare", "Alice Cooper", 1957
bad = "Bad Company", "Bad Company", 1974
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)

# metallica[0] = "Master of Puppets" cannot assign
metallica = "Master of Puppets", metallica[1], metallica[2]  # can reassign
# rhs is evaluated first that's why this reassignment is possible

# tuples are for heterogeneous items

title, artist, year = metallica
print(title)
print(artist)
print(year)

# unpacking the tuple!