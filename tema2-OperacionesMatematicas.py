num1 = 20

num2 = 10

# Suma
print(f"La suma es: {num1 + num2}")

# Resta
print(f"La resta es: {num1 - num2}")

# Multiplicacion
print(f"La multiplicacion es: {num1 * num2}")

# Division
print(f"La division es: {num1 / num2}")

# Division entera
print(f"La division entera es: {num1 // num2}")

# Modulo
print(f"El modulo es: {num1 % num2}")

# Potencia
print(f"La potencia es: {num1 ** num2}")


# concatenacion de cadenas

texto1 = "Hola"
texto2 = "Mundo"
textoFinal = texto1 + " " + texto2
print(textoFinal)

print("El resuludo es %s %s" % (texto1, texto2))

saludoFinal = "El resuludo es {} {}".format(texto1, texto2)
print(saludoFinal)

saludoFinal = "El resuludo 2 es {x} {y}".format(x=texto1, y=texto2)
print(saludoFinal)

saludoFinal = f"El resuludo 3 es {texto1} {texto2}"
print(saludoFinal)
