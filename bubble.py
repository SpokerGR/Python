lista = [6,8,2,7,9,4,5,3,1]

def bubble(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if lista[j] < lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]


print("First : ",lista)        
bubble(lista)
print("Last : ",lista)
