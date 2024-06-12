def ordenacion_radixsort(vector):
    ndig = calcular_numero_maximo_de_digitos(vector)
    peso = 1

    for i in range(ndig):
        urnas = [[] for _ in range(10)]  # Crear urnas vacías para cada dígito (0-9)

        for num in vector:
            d = (num // peso) % 10  # Determinar el dígito actual
            urnas[d].append(num)    # Agregar el número en la urna correspondiente al dígito

        j = 0
        while j < 10 and not urnas[j]:  # Buscar la primera urna no vacía
            j += 1

        for r in range(j + 1, 10):  # Enlazar urnas vacías con urnas no vacías
            urnas[j].extend(urnas[r])

        # Recorrer la lista-urna resultante de la concatenación
        r = 0
        for num in urnas[j]:
            vector[r] = num
            r += 1

        peso *= 10

    return vector

def calcular_numero_maximo_de_digitos(vector):
    maximo = max(vector)
    digitos = 0
    while maximo > 0:
        maximo //= 10
        digitos += 1
    return digitos

# Ejemplo de uso:
vector = [110010, 10100, 1010, 101000]
print("Vector original:", vector)
vector_ordenado = ordenacion_radixsort(vector)
print("Vector ordenado:", vector_ordenado)