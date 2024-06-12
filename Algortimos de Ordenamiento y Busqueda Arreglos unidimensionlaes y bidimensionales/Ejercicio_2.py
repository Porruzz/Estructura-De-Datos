import random

def llenar_datos_empleados(nomina):
    for i in range(len(nomina[0])):
        id_empleado = random.randint(1, 1000)
        nomina[0][i] = id_empleado
        nomina[1][i] = f"Empleado-{id_empleado}"
        nomina[2][i] = [
            random.randint(20000, 50000),  # Sueldo básico aleatorio
            random.randint(1000, 5000),    # Deducciones aleatorias
            0                               # Neto a pagar inicialmente en 0
        ]
        # Calcular neto a pagar
        nomina[2][i][2] = nomina[2][i][0] - nomina[2][i][1]

def quicksort(arr, inicio, fin):
    if inicio < fin:
        pivot = particion(arr, inicio, fin)
        quicksort(arr, inicio, pivot - 1)
        quicksort(arr, pivot + 1, fin)

def particion(arr, inicio, fin):
    pivot = arr[fin][2]
    i = inicio - 1
    for j in range(inicio, fin):
        if arr[j][2] >= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[fin] = arr[fin], arr[i + 1]
    return i + 1

def busqueda_binaria_recursiva(id_buscado, inicio, fin, nomina):
    if inicio > fin:
        return -1
    else:
        medio = (inicio + fin) // 2
        if nomina[0][medio] == id_buscado:
            return medio
        elif nomina[0][medio] < id_buscado:
            return busqueda_binaria_recursiva(id_buscado, medio + 1, fin, nomina)
        else:
            return busqueda_binaria_recursiva(id_buscado, inicio, medio - 1, nomina)

def buscar_empleado(id_empleado, nomina):
    pos = busqueda_binaria_recursiva(id_empleado, 0, len(nomina[0]) - 1, nomina)
    if pos != -1:
        print("Empleado encontrado:")
        print("Nombre:", nomina[1][pos])
        print("Sueldo Básico:", nomina[2][pos][0])
        print("Deducciones:", nomina[2][pos][1])
        print("Neto a Pagar:", nomina[2][pos][2])
    else:
        print("EMPLEADO NO REGISTRADO")

def mostrar_informe(nomina):
    quicksort(nomina[2], 0, len(nomina[2]) - 1)

    print("Informe de Nómina:")
    print("{:<15} {:<15} {:<15} {:<15} {:<15}".format("ID", "Nombre", "Sueldo Básico", "Deducciones", "Neto a Pagar"))
    for empleado in nomina[2]:
        idx = nomina[2].index(empleado)
        print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(nomina[0][idx], nomina[1][idx], empleado[0], empleado[1], empleado[2]))

def main():
    cantidad_empleados = 10
    nomina = [[0] * cantidad_empleados for _ in range(3)]  # 3 arreglos: ID, Nombre, Datos (sueldo, deducciones, neto)

    # Llenar datos de empleados
    llenar_datos_empleados(nomina)

    # Ordenar los datos de la nómina por ID de forma ascendente
    nomina[0].sort()

    # Mostrar informe de nómina
    mostrar_informe(nomina)

    # Buscar un empleado por ID
    id_buscado = int(input("\nIngrese el número de identificación del empleado a buscar: "))
    buscar_empleado(id_buscado, nomina)

if __name__ == "__main__":
    main()
