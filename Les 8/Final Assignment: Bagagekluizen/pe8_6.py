def menu():
    print("1: Ik wil weten hoeveel kluizen nog vrij zijn")
    print("2: Ik wil een nieuwe kluis")
    print("3: Ik wil even iets uit mijn kluis halen ")
    print("4: Ik geef mijn kluis terug\n")
    menukeuze = int(input("Kies een optie (1-4): "))

def toon_aantal_kluizen_vrij():
    file = open("kluizen.txt", "r+")
    len(file.readlines())
    file.close()

toon_aantal_kluizen_vrij()