test = "test"
chaine = "blablablabla"

longueur = len(chaine)

type_longueur = type(longueur)
# type(type_longueur)
# print(type_longuur)

if type_longueur == int and longueur >= 8 :
     print("Le mot de passe est coresct, taille : {}".format(len(chaine)))
else:
    print("taille du mot de passe trop petit")