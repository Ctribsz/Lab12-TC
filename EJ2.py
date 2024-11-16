# Lista utilizada para el ejercicio 2
EJ2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Función del ejercicio 2
def calcular_potencias(lista_numeros, potencia):
    """
    Calcula la potencia n-ésima de cada elemento en una lista de enteros.

    :param lista_numeros: Lista de enteros a elevar a la potencia
    :param potencia: Potencia a la que se elevarán los elementos
    :return: Lista con los resultados
    """
    return list(map(lambda x: x ** potencia, lista_numeros))

# Imprimir resultado del ejercicio 2
resultado_ej2 = calcular_potencias(EJ2, 3)

print("\n" + "="*30)
print("Resultado del Ejercicio 2:")
print(f"Potencia 3 de la lista {EJ2}:")
print(resultado_ej2)
print("="*30)
