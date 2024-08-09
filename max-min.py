lista = [53,41,76,83,94,15,27,36,60]


n = len(lista)
print(n)

max = lista[0]
min = lista[0]
for i in range(0,n,1):
    
    if max < lista[i]:
        max = lista[i]
    if min > lista[i]:
        min = lista[i]
        

print("Max:", max)
print("Min:", min)
