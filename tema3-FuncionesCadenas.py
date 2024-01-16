texto = "Universidad tecnologica de leon"

#mayusculas
print(texto.upper())

#minusculas
print(texto.lower())

#primera letra en mayuscula
print(texto.capitalize())

#primera letra de cada palabra en mayuscula
print(texto.title())

#reemplazar
print(texto.replace("tecnologica", "nacional"))

#contar
print(texto.count("tecnologica"))

#encontrar
print(texto.find("tecnologica"))

#comparar
print(texto.startswith("Universidad"))
print(texto.endswith("leon"))

#separar
print(texto.split(" "))

#unir
print(" ".join(texto))