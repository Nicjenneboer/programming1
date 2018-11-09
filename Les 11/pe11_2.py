import datetime
import csv

bestand = 'inloggers.csv'



with open(bestand, "w") as inlogCSV:
    writer = csv.writer(inlogCSV, delimiter=";")

    while True:
        date = datetime.datetime.now().strftime("%a %d %b at %H:%M")
        naam = input("Wat is je achternaam? ")
        if naam == "einde":
            break
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")
        writer.writerow((date, voorl, naam, gbdatum, email))

