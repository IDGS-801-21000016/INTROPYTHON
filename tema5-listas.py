'''
listas es una secuencia de elementos que pueden ser de diferentes tipos de datos
'''

# listas

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# acceder a un elemento de la lista
print(lista[0])

# acceder a un elemento de la lista
print(lista[-1])

# acceder a un elemento de la lista
print(lista[2:5])

# acceder a un elemento de la lista
print(lista[2:])
print(lista[:5])

# agregar un elemento a la lista
lista.append(11)
print(lista)

# agregar un elemento a la lista
lista.insert(0, 90)
print(lista)

# agregar varios elementos a la lista
lista.extend([12, 13, 14])
print(lista)

# eliminar un elemento de la lista
lista.remove(14)
print(lista)

# eliminar el ultimo elemento de la lista
lista.pop()
print(lista)

# eliminar un elemento de la lista
del lista[0]
print(lista)

# eliminar un elemento de la lista
del lista[0:2]

# eliminar todos los elementos de la lista
lista.clear()

print(lista)

lista2 = ["esmeralda", "jonathan", "Yuri", "jorge", "javier"]
print(lista2)

lista3 = lista + lista2
print(lista3)

lista4 = [3,10,34,1,5,7,9,2,4,6,8]

# ordenar una lista
lista4.sort()

print(lista4)

# ordenar una lista de forma inversa
lista4.reverse()
print(lista4)