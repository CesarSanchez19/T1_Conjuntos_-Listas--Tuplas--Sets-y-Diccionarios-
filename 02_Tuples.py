### MENÚ INTERACTIVO DE TUPLAS EN PYTHON ###

# Funcion
def acceder_elemento(tupla):
    print("\n--- Ejecutando: Acceder un elemento ---")
    while True:
        indice = int(input("Ingrese el índice del elemento a acceder: "))
        if 0 <= indice < len(tupla):
            print("El elemento en el índice", indice, "es:", tupla[indice])
            break
        else:
            print("Índice fuera de rango. Intente nuevamente.")

# Función para intentar agregar un elemento a una tupla (y dejar que el error se imprima como normalmente lo haría Python)
def agregar_elemento(tupla):
    print("\n--- Ejecutando: Agregar un elemento ---")
    n = (input("Ingrese el elemento a agregar: "))
    n = convertir_elemento(n)
    try:
        tupla.append(n)  # Intentar modificar la tupla
    except AttributeError as e:
        print(e)  # Imprime el error tal como aparece en la consola
    
    print("\nContinuamos con el menú...\n")  # Continuamos con el menú

# Función para buscar un elemento en la tupla
def contar_elemento(tupla):
    print("\n--- Ejecutando: Contar un elemento ---")
    while True:
        n = input("Ingrese el elemento que desea contar: ")
        n = convertir_elemento(n)
        if n in tupla:
            print("El elemento", n, "aparece", tupla.count(n), "veces en la tupla.")
            break
        else:
            print("El elemento", n, "no está en la tupla. Intente nuevamente.")    

# Funcion buscar un elemento dentro de la tupla
def buscar_elemento(tupla):
    print("\n--- Ejecutando: Buscar un elemento ---")
    while True:
        n = input("Ingrese el elemento que desea buscar: ")
        n = convertir_elemento(n)
        if n in tupla:
            print("El elemento", n, "se encuentra en el índice", tupla.index(n))
            break
        else:
            print("El elemento", n, "no está en la tupla. Intente nuevamente.")

# Función para buscar un elemento en la tupla
def convertir_tupla_a_lista(tupla):
    print("\n--- Ejecutando: Convertir la tupla en lista ---")
    lista = list(tupla)
    print("La tupla ha sido convertida en lista:", lista)
    print(type(lista))
    return lista

# Funcion convertir elementos en numeros o cadenas de texto de una lista
def convertir_tupla(tupla):
    if all(elemento.isdigit() for elemento in tupla):  # Verifica si todos los elementos son números
        return tuple(map(int, tupla))  # Convierte a enteros
    else:
        return tuple(map(str, tupla))  # Mantiene como cadenas

# Convierte en un elemento en numero o string dentro de la lista
def convertir_elemento(n):
    if n.isdigit():  
        return int(n)  
    else:
        return str(n)

# Función para nuestro menú interactivo
def menu():
    print("\n--- Ejecutando: Menú interactivo de tuplas ---")
    tupla = tuple((input("Ingresar los elementos de la tupla separados por espacio: ").split()))
    tupla = convertir_tupla(tupla)
    print("\n--- creando tupla ---")
    while True:
        print("\n ### Menú interactivo de tupla en Python ###")
        print("\nLa tupla actual es:", tupla)
        
        opcion = input("\n1. Acceder un elemento\n2. Agregar un elemento\n3. Contar un elemento\n4. Buscar un elemento\n5. Convertir la tupla en lista\n0. Salir\nSeleccione una opción: ")
        
        # Opciones del menú
        if opcion == "1":
            acceder_elemento(tupla)
        elif opcion == "2":
            agregar_elemento(tupla)
        elif opcion == "3":
            contar_elemento(tupla)
        elif opcion == "4":
            buscar_elemento(tupla)
        elif opcion == "5":
            convertir_tupla_a_lista(tupla)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

menu()
