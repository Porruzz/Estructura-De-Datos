def agregar_apartamentos(conjunto_residencial):
    # Definimos las letras que identificarán a las torres
    letras = ['A', 'B', 'C', 'D', 'E', 'F']

    # Recorremos cada letra para crear las torres y sus pisos
    for letra in letras:
        # Creamos una lista para representar cada torre
        torre = [letra, []]

        # Creamos los 6 pisos para cada torre
        for piso in range(1, 7):
            # Creamos una lista de identificadores de apartamentos para cada piso
            apartamentos = [f"{letra}{piso:03d}" for _ in range(1, 7)]
            # Agregamos la lista de apartamentos al piso actual de la torre
            torre[1].append(apartamentos)

        # Agregamos la torre con sus pisos al conjunto residencial
        conjunto_residencial.append(torre)

def generar_facturacion_torre_piso(conjunto_residencial, letra_torre, numero_piso):
    # Buscamos la torre en el conjunto residencial
    for torre in conjunto_residencial:
        if torre[0] == letra_torre:  # Si la letra de la torre coincide
            piso = torre[1][numero_piso - 1]  # Obtenemos el piso específico
            # Mostramos el listado de facturación por consola
            print(f"Listado de facturación - Torre {letra_torre}, Piso {numero_piso}:")
            for apartamento in piso:
                print(f"Apartamento: {apartamento}, Monto a pagar: $250000")
            # Borramos la información de facturación del piso después de mostrarla en la consola
            piso.clear()
            return

# Crear el conjunto residencial
conjunto_residencial = []

# Agregar los apartamentos al conjunto residencial
agregar_apartamentos(conjunto_residencial)

# Generar la facturación para una torre y un piso específico
generar_facturacion_torre_piso(conjunto_residencial, 'C', 6)
generar_facturacion_torre_piso(conjunto_residencial, "F", 5)
