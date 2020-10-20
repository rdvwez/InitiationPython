tab_a = [15,20,5,14,1,0,19,26,4,6,5]
tab_b = [3,26,18,3,7,6,9,20,8,1,23]

tab_c = list()

i= 0
while i <11:
    if tab_a[i] < tab_b[i]:
        tab_c.append(tab_b[i])
    else:
        tab_c.append(tab_a[i])
    i+=1


print(tab_c)