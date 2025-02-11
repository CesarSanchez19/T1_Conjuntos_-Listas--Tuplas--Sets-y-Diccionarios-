### MENÚ INTERACTIVO DE LISTAS EN PYTHON ###

# Funciones del menú #

# Función para agregar un elemento a la lista 
def agregar_elemento(lista):
    print("\n--- Ejecutando: Agregar un elemento ---")  
    n = int(input("Ingrese el elemento a agregar: "))
    lista.append(n)
    print("Este elemento ha sido agregado:", n, "\nY por lo tanto, la nueva lista es", lista)

# Función para insertar un elemento en la lista en una posición válida
def insertar_elemento(lista):
    print("\n--- Ejecutando: Insertar un elemento ---")
    while True:
        posicion = int(input("Ingrese la posición: "))
        if 0 <= posicion <= len(lista):  
            n = int(input("Ingrese el elemento: "))
            lista.insert(posicion, n)
            print("Este elemento ha sido insertado:", n, "\nY por lo tanto, la nueva lista es", lista)
            break  
        else:
            print("Posición fuera de rango. Intente nuevamente.")


# Función para eliminar un elemento de la lista
def eliminar_elemento(lista):
    print("\n--- Ejecutando: Eliminar un elemento ---")
    while (True):
        n = int(input("Ingrese el elemento a eliminar: "))
        if n in lista:
            lista.remove(n)
            print("Este elemento ha sido eliminado:", n, "\nY por lo tanto, la nueva lista es", lista)
            break
        else:
            print("El elemento no está en la lista.")

# Función para encontrar un elemento en la lista y mostrar su posición
def encontrar_elemento(lista):
    print("\n--- Ejecutando: Encontrar un elemento ---")
    while True:
        n = int(input("Ingrese el elemento a buscar: "))
        if n in lista:
            indice = lista.index(n)  
            print("El elemento", n, "está en la lista y está ubicado en el índice:", indice)
            break  
        else:
            print("El elemento", n, "no está en la lista. Intente nuevamente.")

# Función para contar un elemento en la lista
def contar_elemento(lista):
    print("\n--- Ejecutando: Contar un elemento ---") 
    n = int(input("Ingrese el elemento a contar: "))
    print("El elemento", n, "aparece", lista.count(n), "veces en la lista.")

# Función para ordenar la lista
def ordenar_lista(lista):
    print("\n--- Ejecutando: Ordenar la lista ---") 
    lista.sort()
    print("La lista ha sido ordenada:", lista)

# Función para invertir la lista
def invertir_lista(lista):
    print("\n--- Ejecutando: Invertir la lista ---") 
    lista.reverse()
    print("La lista ha sido invertida:", lista)

# Función para vaciar o limpiar la lista
def limpiar_lista(lista):
    print("\n--- Ejecutando: Limpiar la lista ---")  
    lista.clear()
    print("La lista ha sido vaciada:", lista)

# Función para nuestro menú interactivo
def menu():
    print("### Menú interactivo de listas en Python ###")
    lista = list(map(int, input("Ingrese los elementos de la lista separados por espacio: ").split()))
    while True:
        print("\n ### Menú interactivo de listas en Python ###")
        print("\nLa lista actual es:", lista)
        
        opcion = input("\n1. Añadir un elemento\n2. Insertar un elemento\n3. Eliminar un elemento\n4. Encontrar un elemento\n5. Contar un elemento\n6. Ordenar la lista\n7. Invertir la lista\n8. Limpiar o vaciar la lista\n0. Salir\nSeleccione una opción: ")
        
        # Opciones del menú
        if opcion == "1":
            agregar_elemento(lista)
        elif opcion == "2":
            insertar_elemento(lista)
        elif opcion == "3":
            eliminar_elemento(lista)
        elif opcion == "4":
            encontrar_elemento(lista)
        elif opcion == "5":
            contar_elemento(lista)
        elif opcion == "6":
            ordenar_lista(lista)
        elif opcion == "7":
            invertir_lista(lista)
        elif opcion == "8":
            limpiar_lista(lista)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

menu()
