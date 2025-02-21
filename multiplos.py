"""
Inserta el encabezado aquí y escribe tu código abajo
"""

# Entradas
número1 = int(input("Ingrese un número: "))
número2 = int(input("Ingrese otro número: "))

# Proceso
if número2 == 0:
    resultado = "No se puede dividir por cero."
elif número1 % número2 == 0:  
    resultado = "El " + str(número1) + " es múltiplo de " + str(número2)
else:  
    resultado = "El " + str(número1) + " no es múltiplo de " + str(número2)

# Salida
print(resultado)