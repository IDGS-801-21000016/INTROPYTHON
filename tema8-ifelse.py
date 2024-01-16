mensaje = "Dame un número: "
num = input(mensaje)
mensaje = "Dame otro número: "
num2 = input(mensaje)

if num > num2:
  print(f"El número {num} es mayor que {num2}")
elif num < num2:
  print(f"El número {num} es menor que {num2}")
else:
  print(f"El número {num} es igual que {num2}")

print("---------------- Pedir una edad y decir si es mayor de edad ----------------")

mensaje = "Dame tu edad: "
edad = int(input(mensaje))

if edad >= 18:
  print(f"La edad {edad} es mayor de edad")
else:
  print(f"La edad {edad} es menor de edad")
