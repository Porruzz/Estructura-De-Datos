class Contenedor:
    def __init__(self, codigo, fila, columna, posicion):
        self.codigo = codigo
        self.fila = fila
        self.columna = columna
        self.posicion = posicion


class Nodo:
    def __init__(self, contenedor):
        self.contenedor = contenedor
        self.siguiente = None

class Bodega:
    def __init__(self):
        self.fila_actual = 1
        self.contenedores_en_fila = 0
        self.inicio = None

    def almacenar_contenedor(self, codigo):
        if self.contenedores_en_fila == 0 or self.contenedores_en_fila == 56:
            self.fila_actual += 1
            self.contenedores_en_fila = 0

        columna = self.contenedores_en_fila % 56 + 1
        posicion = self.contenedores_en_fila // 56 + 1

        contenedor = Contenedor(codigo, self.fila_actual, columna, posicion)
        nuevo_nodo = Nodo(contenedor)

        if self.inicio is None:
            self.inicio = nuevo_nodo
        else:
            actual = self.inicio
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

        self.contenedores_en_fila += 1

    def salida_contenedor_recursivo(self, nodo=None, codigo=None):
        if nodo is None:
            nodo = self.inicio

        if nodo is None:
            print("No hay contenedores en la bodega.")
            return

        if nodo.contenedor.codigo == codigo:
            print(f"Ubicación del contenedor {codigo}:")
            print(f"Fila: {nodo.contenedor.fila}")
            print(f"Columna: {nodo.contenedor.columna}")
            print(f"Posición: {nodo.contenedor.posicion}")
            return

        self.salida_contenedor_recursivo(nodo.siguiente, codigo)

 # Crear una instancia de la bodega
bodega = Bodega()

# Almacenar 504 contenedores
for i in range(1, 505):
    codigo = f"A{i:03d}"
    bodega.almacenar_contenedor(codigo)

# Ejemplo de salida de un contenedor
codigo_salida = "A123"
bodega.salida_contenedor_recursivo(codigo=codigo_salida)
codigo_salida = "A005"
bodega.salida_contenedor_recursivo(codigo=codigo_salida)