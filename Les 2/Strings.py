# 1. Hoeveel letters bevat de string 'Supercalifragilisticexpialidocious'?

print (len("Supercalifragilisticexpialidocious"))

# 2. Komt in 'Supercalifragilisticexpialidocious' de tekst 'ice' voor?

print ("ice" in "Supercalifragilisticexpialidocious")

# 3. Is het woord 'Antidisestablishmentarianism' langer dan 'Honorificabilitudinitatibus'?

print ("Antidisestablishmentarianism" > "Honorificabilitudinitatibus")

# 4. Welke componist komt in alfabetische volgorde het eerst: 'Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'? Welke het laatst?

x = ['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein']
print ("Eerst: " + sorted(x)[0] + " Laatst: " + sorted(x)[-1])

# Uitkomsten
# 1. 34
# 2. True
# 3. False
# 4. Eerst: Bartok Laatst: Buxtehude .
