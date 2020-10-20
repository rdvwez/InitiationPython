chaine = "avec python je progresse vite en programmation"
tab = list()

# affichage de la chaine en majuscule et normale
print(chaine.upper())
print(chaine)
# print(chaine.split())

# cassage de la chaine
for mot in chaine.split():
    tab.append(mot)

print(tab)

# reconstruction de la chaine
chaine2 = "-".join(tab)
print(chaine2)

# creation de la chaine en metant les underscore à la place des espaces 
chaine3 =  "_".join(tab)
print(chaine3)

chaine4 = "python"
print(chaine4)
print(chaine4[0])
print(chaine4[-2])

# application de slicing
chaine5 = "abcdefghijklmnopqrstuvwxyz"
print(chaine5[0:6])
print(chaine5[12:18])
print(chaine5[0:10])
print(chaine5[17:26])
print(chaine5[1:25:2])
print(chaine5[0:10:2])

# concatenation
chaien_a = "abcde"
chaien_b = "hijklm"
chaien_c = chaien_a +"-"+chaien_b
print(chaien_c)

