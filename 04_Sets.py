### MENÚ INTERACTIVO DE CONJUNTOS EN PYTHON ###

### Funciones interactivas del menú ###

# Función que agrega elementos en cualquier conjunto
def agregar_elemento(conjunto_uno, conjunto_segundo):
    print("\n--- Ejecutando: agregar un elemento ---")
    n = input("Ingrese el elemento que desea agregar: ")
    n = convertir_elemento(n)
    
    while True:
        print("\n--- Seleccione a qué conjunto desea agregar el elemento: ---")
        print("1. Primer conjunto")
        print("2. Segundo conjunto")
        print("0. Salir")
        seleccion_uno = input("Seleccione una opción: ")

        if seleccion_uno == "1":
            conjunto_uno.add(n)
            print(f"El elemento {n} se agregó al primer conjunto: {conjunto_uno}")
            break
        elif seleccion_uno == "2":
            conjunto_segundo.add(n)
            print(f"El elemento {n} se agregó al segundo conjunto: {conjunto_segundo}")
            break
        elif seleccion_uno == "0":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Función para hacer una intersección de dos conjuntos
def interseccion_conjuntos(conjunto_uno, conjunto_segundo):
    interseccion = conjunto_uno.intersection(conjunto_segundo)
    print("La intersección de los conjuntos (uno & dos) es: ", interseccion)

# Función para unir dos conjuntos
def union_conjuntos(conjunto_uno, conjunto_segundo):
    union = conjunto_uno.union(conjunto_segundo)
    print("La unión de los conjuntos (uno | dos) es: ", union)

# Función que elimina elementos en cualquier conjunto
def eliminar_elemento(conjunto_uno, conjunto_segundo):
    print("\n--- Ejecutando: eliminando un elemento ---")
    n = input("Ingrese el elemento que desea eliminar: ")
    n = convertir_elemento(n)
    
    while True:
        print("\n--- Seleccione de qué conjunto desea eliminar el elemento: ---")
        print("1. Primer conjunto")
        print("2. Segundo conjunto")
        print("0. Salir")
        seleccion_dos = input("Seleccione una opción: ")

        if seleccion_dos == "1":
            if n in conjunto_uno:
                conjunto_uno.remove(n)
                print(f"El elemento {n} fue eliminado del primer conjunto: {conjunto_uno}")
                break
            else:
                print(f"El elemento {n} no se encuentra en el conjunto. Intente nuevamente.")

        elif seleccion_dos == "2":
            if n in conjunto_segundo:
                conjunto_segundo.remove(n)
                print(f"El elemento {n} fue eliminado del segundo conjunto: {conjunto_segundo}")
                break
            else:
                print(f"El elemento {n} no se encuentra en el conjunto. Intente nuevamente.")
        elif seleccion_dos == "0":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Función para verificar si un elemento está en un conjunto
def verificar_elemento(conjunto_uno, conjunto_segundo):
    print("\n--- Ejecutando: verificar un elemento ---")
    n = input("Ingrese el elemento que desea verificar: ")
    n = convertir_elemento(n)
    
    while True:
        print("\n--- Seleccione en qué conjunto desea verificar el elemento: ---")
        print("1. Primer conjunto")
        print("2. Segundo conjunto")
        print("0. Salir")
        seleccion_tres = input("Seleccione una opción: ")

        if seleccion_tres== "1":
            if n in conjunto_uno:
                print(f"El elemento {n} fue encontrado en el  primer conjunto: {conjunto_uno}")
                break
            else:
                print(f"El elemento {n} no se encuentra en el conjunto.")
        elif seleccion_tres == "2":
            if n in conjunto_segundo:
                print(f"El elemento {n} fue encontrado en el  primer conjunto: {conjunto_segundo}")
                break
            else:
                print(f"El elemento {n} no se encuentra en el conjunto.")
        elif seleccion_tres == "0":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Función para vaciar los conjuntos
def vaciar_conjuntos(conjunto_uno, conjunto_segundo):
    print("\n--- Ejecutando: vaciar los conjuntos ---")
    conjunto_uno.clear()
    conjunto_segundo.clear()
    print("Los conjuntos han sido vaciados.")

# Función para la diferencia de dos conjuntos
def diferencia_conjuntos(conjunto_uno, conjunto_segundo):
    diferencia = conjunto_uno.difference(conjunto_segundo)
    print("La diferencia de los conjuntos (uno - dos) es: ", diferencia)

# Función para convertir los elementos en números o cadenas
def convertir_conjuntos(conjuntos):
    if all(elemento.isdigit() for elemento in conjuntos):  
        return set(map(int, conjuntos))  
    else:
        return set(map(str, conjuntos))  

# Convierte un solo elemento en número o string
def convertir_elemento(n):
    return int(n) if n.isdigit() else str(n)

# Función para el menú interactivo
def menu():
    print("\n--- Ejecutando: Menú interactivo de Conjuntos (sets) ---")
    
    conjunto_uno = convertir_conjuntos(set(input("Ingrese los elementos del primer conjunto separados por espacio: ").split()))
    conjunto_segundo = convertir_conjuntos(set(input("Ingrese los elementos del segundo conjunto separados por espacio: ").split()))

    print("\n--- Conjuntos creados ---")
    
    while True:
        print("\n### Menú interactivo de conjuntos en Python ###")
        print(f"1er conjunto: {conjunto_uno}")
        print(f"2do conjunto: {conjunto_segundo}")
        
        opcion = input("\n1. Agregar un elemento\n2. Realizar una intersección de conjuntos\n3. Realizar la unión de conjuntos\n4. Eliminar un elemento\n5. Verificar un elemento\n6. Realizar diferencia de conjuntos\n7. Vaciar conjuntos\n0. Salir\nSeleccione una opción: ")
        
        if opcion == "1":
            agregar_elemento(conjunto_uno, conjunto_segundo)
        elif opcion == "2":
            interseccion_conjuntos(conjunto_uno, conjunto_segundo)
        elif opcion == "3":
            union_conjuntos(conjunto_uno, conjunto_segundo)
        elif opcion == "4":
            eliminar_elemento(conjunto_uno, conjunto_segundo)
        elif opcion == "5":
            verificar_elemento(conjunto_uno, conjunto_segundo)
        elif opcion == "6":
            diferencia_conjuntos(conjunto_uno, conjunto_segundo)
        elif opcion == "7":
            vaciar_conjuntos(conjunto_uno, conjunto_segundo)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu()
