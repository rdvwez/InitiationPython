serie_a = [1,5,1,6,8,4,5,9,5,6,1,1,4,7,6,2,5,6,0,0,7,8,5,6,1,2]

# affichage de la liste de depart
print(serie_a)

# triage de la liste
taille = len(serie_a)
i= 0
while i < taille:
    j = 0
    while j < taille-1:
        if serie_a[j] > serie_a[j+1]:
            temp = serie_a[j]
            serie_a[j] = serie_a[j+1]
            serie_a[j+1] = temp  
        j+=1
    i+=1
# affichafe de la miste triée
print(serie_a)
print("0 apparait: {}".format(serie_a.count(0)))
print("9 apparait: {}".format(serie_a.count(9)))


