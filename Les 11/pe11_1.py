
try:
    personen = int(input("Hoeveel personen gaan er mee op reis?: "))
    if personen > 0:
        print(4356 / personen)
    else:
        print(" - Negatieve getallen zijn niet toegestaan!")
except ValueError:
    print(" - Gebruik cijfers voor het invoeren van het aantal!")
except ZeroDivisionError:
    print(" - Delen door nul kan niet!")
except:
    print (" - Onjuiste invoer!")