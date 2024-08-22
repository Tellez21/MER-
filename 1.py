# Ejercicio 1: Calcular el promedio de 5 notas de un estudiante.
notas = [float(input("Ingrese la nota {}: ".format(i+1))) for i in range(5)]
promedio = sum(notas) / len(notas)
print("El promedio de las notas es:", promedio)