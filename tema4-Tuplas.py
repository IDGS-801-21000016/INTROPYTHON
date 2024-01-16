'''
Las tuplas son inmutables, es decir, no se pueden modificar
'''

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(tupla[-2])
print(tupla[2:5])

for valor in tupla:
    print(valor)


tuplasVariosDatos = (1, "hola", 3.4, True,13.4j)
print(tuplasVariosDatos)

# Convertir una tupla en lista
lista = list(tuplasVariosDatos)
print(lista)

# Convertir una lista en tupla
tupla = tuple(lista)
print(tupla)


variasTuplas = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
a, b, c = variasTuplas

print(a)
print(b)
print(c)


#agregar elementos a una tupla
tupla = (1, 2, 3, 4, 5)
lista = list(tupla)
lista.append(6)
tupla = tuple(lista)

tuplaNuevo = tupla + (7, 8, 9)
print(tuplaNuevo)