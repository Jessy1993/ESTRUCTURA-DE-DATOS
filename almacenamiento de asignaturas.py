# Crear una lista con las asignaturas del curso
asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']

# Crear una lista vacía para almacenar las notas
notas = []

# Preguntar al usuario la nota de cada asignatura
for asignatura in asignaturas:
    nota = float(input(f'¿Qué nota has sacado en {asignatura}? '))
    notas.append(nota)

# Mostrar las asignaturas con sus respectivas notas
for i in range(len(asignaturas)):
    print(f'En {asignaturas[i]} has sacado {notas[i]}')
