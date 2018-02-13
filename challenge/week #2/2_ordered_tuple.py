# appending is not possible on tuples?

metallica = "Ride the Lightning", "Metallica", 1984
metallica_list = ["Ride the Lightning", "Metallica", 1984]


imelda = "More Mayhem", "Imelda May", 2011, (
    [
        (1, "Pulling the Rug"),
        (2, "Psycho"),
        (3, "Mayhem")
    ]
)

title, artist, year, tracks = imelda

tracks.append((4, "Kentish"))

for song in tracks:
    order, name = song
    print("#{} track: \t{}".format(order, name))










