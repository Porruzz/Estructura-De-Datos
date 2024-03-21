import random
# Metodo de ordenamiento de la Burbuja
def bubblesort(list_):
    # Identifica el tamaño de la lista
    length = len(list_) - 1

    # Bucle para el recorrido de la lista
    for i in range(0,length):
        print(f"Recorrido #{i + 1}")
        # Comparaciones e intercambios
        for j in range(0,length):
            print(f"comparación: {list_[j]} > {list_[j + 1]}")
            if list_[j] > list_[j + 1]:
                print(f"intercambiar: {list_[j]} * {list_[j + 1]}")
                aux = list_[j]
                list_[j] = list_[j + 1]
                list_[j + 1] = aux
    return list_
# Lista Vacia
list_ = []
# Rellenarla de numeros aleatorios
for i in range(5):
    num = random.randint(1, 100)
    list_.append(num)
# Imprimir resutados 
print("Antes de ordenar: ")
print(list_)
print("Despues de ordenar: ")
print(bubblesort(list_))


