nl=[]
for element in range(2000, 3201):
    if (element%7==0) and (element%5!=0):
        nl.append(str(element))
print (','.join(nl))