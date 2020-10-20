# recuperation de la donnée
var = input('entrer un nombre ou des caractères ')
tabType = {} 
# print(len(var))
i = 0
while i < len(var) :
    tabType[i] = type(var[i])
    # print(var[i])
    i +=1
print(tabType)