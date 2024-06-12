import random

class GrupoEstudiantes:
    def __init__(self, cantidad_estudiantes):
        self.codigo_estudiante = [0] * cantidad_estudiantes
        self.nombre_estudiante = list(map(lambda x: f"Estudiante-{x+1}", range(cantidad_estudiantes)))
        self.notas = [[0, 0, 0, 0] for _ in range(cantidad_estudiantes)]  # [corte1, corte2, corte3, nota_final]

    def llenar_datos_estudiantes(self):
        self.codigo_estudiante = list(map(lambda x: random.randint(1, 10), self.codigo_estudiante))
        self.notas = list(map(lambda x: [random.randint(0, 500) / 100, random.randint(0, 500) / 100, random.randint(0, 500) / 100, 0], self.notas))
        self.notas = list(map(lambda x: [x[0], x[1], x[2], self.calcular_nota_final(x[0], x[1], x[2])], self.notas))

    def calcular_nota_final(self, corte1, corte2, corte3):
        return round((corte1 * 0.3) + (corte2 * 0.3) + (corte3 * 0.4), 1)

    def buscar_estudiante(self, codigo):
        def busqueda_binaria(codigo, inicio, fin):
            if inicio > fin:
                return -1
            else:
                medio = (inicio + fin) // 2
                if self.codigo_estudiante[medio] == codigo:
                    return medio
                elif self.codigo_estudiante[medio] < codigo:
                    return busqueda_binaria(codigo, medio + 1, fin)
                else:
                    return busqueda_binaria(codigo, inicio, medio - 1)
        return busqueda_binaria(codigo, 0, len(self.codigo_estudiante) - 1)

    def mostrar_informe(self):
        self.ordenar_por_nota_final()
        print("{:<10} {:<15} {:<10} {:<10} {:<10} {:<10}".format("Código", "Nombre", "Corte 1", "Corte 2", "Corte 3", "Nota Final"))
        for codigo, nombre, notas in zip(self.codigo_estudiante, self.nombre_estudiante, self.notas):
            print("{:<10} {:<15} {:<10} {:<10} {:<10} {:<10}".format(codigo, nombre, notas[0], notas[1], notas[2], notas[3]))

    def ordenar_por_nota_final(self):
        self.codigo_estudiante, self.nombre_estudiante, self.notas = zip(*sorted(zip(self.codigo_estudiante, self.nombre_estudiante, self.notas), key=lambda x: x[2], reverse=True))

def main():
    cantidad_estudiantes = 10
    grupo = GrupoEstudiantes(cantidad_estudiantes)

    # Llenar datos de estudiantes y notas
    grupo.llenar_datos_estudiantes()

    # Mostrar informe final del curso
    grupo.mostrar_informe()

    # Buscar un estudiante por código
    codigo_buscado = int(input("\nIngrese el código del estudiante a buscar: "))
    pos = grupo.buscar_estudiante(codigo_buscado)
    if pos != -1:
        print("\nEstudiante encontrado:")
        print("Código:", grupo.codigo_estudiante[pos])
        print("Nombre:", grupo.nombre_estudiante[pos])
        print("Corte 1:", grupo.notas[pos][0])
        print("Corte 2:", grupo.notas[pos][1])
        print("Corte 3:", grupo.notas[pos][2])
        print("Nota Final:", grupo.notas[pos][3])
    else:
        print("\nESTUDIANTE NO REGISTRADO")

if __name__ == "__main__":
    main()
