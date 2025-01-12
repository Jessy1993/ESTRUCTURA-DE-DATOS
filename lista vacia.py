# Crear una lista vacía para almacenar los números ganadores
numeros_ganadores = []

# Preguntar al usuario por 6 números ganadores
for i in range(6):
    numero = int(input(f'Introduce el número ganador {i+1}: '))
    numeros_ganadores.append(numero)

# Ordenar la lista de menor a mayor
numeros_ganadores.sort()

# Mostrar los números ganadores ordenados
print('Los números ganadores ordenados son:')
print(numeros_ganadores)
