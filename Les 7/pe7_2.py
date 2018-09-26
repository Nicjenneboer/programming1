infile = open("Kaartnummers.txt", "r")
kaartnummers = infile.read().strip().split("\n")
for i in kaartnummers:
    print("{} {} {}".format(i.split(",")[1], "heeft kaartnummer: ", i.split(",")[0]))
infile.close()