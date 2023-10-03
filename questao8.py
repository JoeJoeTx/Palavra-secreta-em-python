import random
lista = []


for i in range(100):
    lista.append(random.randint(0,100))



for i in range(len(lista)):
    menor = i

    for j in range(len(lista)):
        if lista[j] < lista[menor]:
            menor = j

        if lista[i] != lista[menor]:
            aux = lista[i]
            lista[i] = lista[menor]
            lista[menor] = aux

lista.reverse()
print(lista)