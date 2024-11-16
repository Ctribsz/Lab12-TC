# Lista utilizada para el ejercicio 1
EJ1 = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Apple', 'model': 2, 'color': 'Silver'},
    {'make': 'Huawei', 'model': 50, 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

# Funcion del ejercicio 1
def ordenar_diccionarios(lista_diccionarios, clave):
    """
    Ordena una lista de diccionarios según la clave proporcionada.

    :param lista_diccionarios: Lista de diccionarios a ordenar
    :param clave: Clave por la cual se ordenará la lista
    :return: Lista ordenada de diccionarios
    """
    return sorted(lista_diccionarios, key=lambda x: x[clave])

# Imprimir resultado del ejercicio 1
resultado = ordenar_diccionarios(EJ1, 'model')

print("\n" + "="*30)
print("Resultado del Ejercicio 1:")
print("Lista ordenada por 'model':")
for item in resultado:
    print(f"Make: {item['make']}, Model: {item['model']}, Color: {item['color']}")
print("\n" + "="*30)
