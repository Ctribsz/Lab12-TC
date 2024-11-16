# Matriz utilizada para el ejercicio 3
EJ3 = [
    [1, 2, 3, 1],
    [4, 5, 6, 0],
    [7, 8, 9, -1]
]

# Función del ejercicio 3
def calcular_transpuesta(matriz):
    """
    Calcula la matriz transpuesta de una matriz dada.

    :param matriz: Matriz representada como lista de listas
    :return: Matriz transpuesta como lista de listas
    """
    return list(map(list, zip(*matriz)))

# Imprimir resultado del ejercicio 3
resultado_ej3 = calcular_transpuesta(EJ3)

print("\n" + "="*30)
print("Resultado del Ejercicio 3:")
print("Matriz original:")
for fila in EJ3:
    print(fila)
print("\nMatriz transpuesta:")
for fila in resultado_ej3:
    print(fila)
print("="*30)
