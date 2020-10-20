# recuperation de la donnée
var = input('entrer quelque chose au clavier\n')

# fonction testan la conversion en int
def testconversion(donnee):
    try:
        var = int(donnee)
        return True
    except:
        return False

# affichage des resultats selon le cas
if testconversion(var):
    print("C’est un chiffre")
elif isinstance(var, (str)):
    taille = len(var)
    if taille == 1:
        print("C’est une lettre")
    else:
        print("C’est une chaine de caractères")
else: 
    print("C’est autre chose")
    
