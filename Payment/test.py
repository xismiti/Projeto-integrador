print("pick a number, 1 or 2")
a = None
while a not in (1, 2):

    a = int(input("> "))

    if a == 1:
        print("this")
    if a == 2:
        print("that")
    else:
        print("you have made an invalid choice, try again.")
