shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

for item in shopping_list:
    if item == 'spam':
        continue
    print("Buy {}".format(item))

for item in shopping_list:
    if item == 'spam':
        print("Break away found spam")
        break
    print("Buy {}".format(item))
else:
    # else can be used with for as well
    # executed when break is not reached
    print("Didn't find spam")
