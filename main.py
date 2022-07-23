import random

lool = random.randint(1, 25)

print(lool)

lol = int(input())


if lol == lool:
    print("Wygrales!")
else:
    print("sprobuj ponownie")
    while True:
        lol = int(input())
        while lol > lool:
            print("Liczba jest Mniejsza!")
            break
        while lol < lool:
            print("Liczba jest Wieksza!")
            break
        if lol == lool:
            print("Wygrałeś!")
            print("Wygrałeś!")
            print("Wygrałeś!")
            print("Wygrałeś!")
            print("Wygrałeś!")
            break
