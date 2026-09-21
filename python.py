import random
pokusy = 0
cislo = random.randint(1, 100)

while True:
    try:
        usercislo = int(input("tvuj guess "))
    except ValueError:
        print("Zadej prosim cislo.")
        continue

    pokusy += 1

    if usercislo < cislo:
        print ("je vetsi")

    elif usercislo > cislo:
        print("je mensi")

    else:
        print("spravne")
        print("Pocet pokusu:", pokusy)
        break