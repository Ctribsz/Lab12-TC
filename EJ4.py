# Listas utilizadas para el ejercicio 4
EJ4_original = ['rojo', 'verde', 'azul', 'amarillo', 'gris', 'blanco', 'negro']
EJ4_eliminar = ['amarillo', 'café', 'blanco']
# Función del ejercicio 4
def eliminar_elementos(lista_original, elementos_a_eliminar):
    """
    Elimina elementos indicados de una lista.

    :param lista_original: Lista de elementos originales
    :param elementos_a_eliminar: Lista de elementos a eliminar
    :return: Lista con los elementos restantes
    """
    return list(filter(lambda x: x not in elementos_a_eliminar, lista_original))

# Imprimir resultado del ejercicio 4
resultado_ej4 = eliminar_elementos(EJ4_original, EJ4_eliminar)

print("\n" + "="*30)
print("Resultado del Ejercicio 4:")
print("Lista original:")
print(EJ4_original)
print("\nElementos a eliminar:")
print(EJ4_eliminar)
print("\nLista resultante:")
print(resultado_ej4)
print("="*30)
