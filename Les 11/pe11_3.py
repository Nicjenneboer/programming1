import csv
x = 0
with open("pe11_3.csv", "r") as CSVFile:
    reader = csv.reader(CSVFile, delimiter=";")

    for row in reader:
        if x < int(row[2]):
            x = int(row[2])
            y = row
    print ("De hoogste score is: {} op {} behaald door {}".format(y[2], y[1], y[0]))