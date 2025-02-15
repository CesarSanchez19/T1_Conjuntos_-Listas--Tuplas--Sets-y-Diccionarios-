### MENÚ INTERACTIVO DE DICCIONARIOS EN PYTHON ###

# Función para agregar un par clave-valor al diccionario
def agregar_pares(diccionario):
    print("\n--- Procesando: Añadir un nuevo par clave-valor ---")
    clave = input("\nIngrese una nueva clave que desea agregar a este diccionario: ")
    valor = input(f"Ingrese el valor para la clave '{clave}' que desea asignar: ")
    diccionario[convertir_elemento(clave)] = convertir_elemento(valor)
    print(f"\nEste es el nuevo clave-valor ({clave} : {diccionario[clave]}) agregado a este diccionario: {diccionario}")

# Función para modificar un par clave-valor existente del diccionario
def modificar_pares(diccionario):
    print("\n--- Procesando: Modificar un par clave-valor ---")
    while(True):
        clave = input("\nIngrese la clave que desea modificar dentro del diccionario: ")
        if clave in diccionario:
            valor = input(f"Ingrese el nuevo valor de la clave '{clave}' que desea asignar: ")
            diccionario[clave] = convertir_elemento(valor)
            print(f"\nEste es el nuevo clave-valor ({clave} : {diccionario[clave]}) fue modificado dentro de este diccionario: {diccionario}")
            break
        else:
            print(f"\nLa clave '{clave}' no existe dentro del diccionario.")

# Función para eliminar un par clave-valor existente del diccionario
def eliminar_pares(diccionario):
    print("\n--- Procesando: Eliminar un par clave-valor ---")
    while(True):
        clave = input("\nIngrese la clave que desea eliminar del diccionario: ")
        if clave in diccionario:
            del diccionario[clave]
            print(f"\nEl clave '({clave})' fue eliminado de este diccionario: {diccionario}")
            break
        else:
            print(f"\nLa clave '{clave}' no existe dentro del diccionario.")

# Función para verificar un par clave-valor dentro del diccionario
def verificar_pares(diccionario):
    print("\n--- Procesando: Verificar un par clave-valor ---")
    clave = input("\nIngrese la clave que desea verificar dentro de este diccionario: ")
    if clave in diccionario:
        print(f"\nEl clave-valor ({clave} : {diccionario[clave]}) fue encontrado dentro de este diccionario: {diccionario[clave]}")
    else:
        print(f"\nLa clave '{clave}' no existe dentro del diccionario.")

# Función para obtener los valores o claves que contenga el diccionario
def obtener_pares(diccionario):
    print("\n--- Procesando: Obtener valores o claves ---")
    while(True):
        print("\n¿Qué deseas obtener del diccionario?")
        seleccion = input("\n1. Obtener claves\n2. Obtener valores \n0. Salir\nSeleccione una opción: ")
        if seleccion == "1":
            print(f"Estas son las claves que contiene este diccionario: {diccionario.keys()}")
        elif seleccion == "2":
            print(f"Estos son los valores que contiene este diccionario: {diccionario.values()}")
        elif seleccion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Función para convertir los elementos en números o cadenas
def convertir_elemento(n):
    if n.isdigit():
        return int(n)
    else:
        return str(n)

# Función para el menú interactivo
def menu():
    print("\n--- Ejecutando: Menú interactivo de Diccionario ---")
    diccionario = {}
    items = input("Ingrese las claves y valores del diccionario separados por espacio (ejemplo: nombre:yair apellido:guzman): ").split()
    for par in items:
        clave, valor = par.split(":")
        diccionario[convertir_elemento(clave.strip())] = convertir_elemento(valor.strip())
    print("\n--- Diccionario Creado ---")
    while True:
        print("\n### Menú interactivo de diccionarios en Python ###")
        print(f"Diccionario actual: {diccionario}")
        
        opcion = input("\n1. Añadir un nuevo par clave-valor\n2. Modificar el valor de una clave\n3. Eliminar un par clave-valor existente\n4. Verificar un par clave-valor\n5. Obtener valores o claves\n0. Salir\nSeleccione una opción: ")
        
        if opcion == "1":
            agregar_pares(diccionario)
        elif opcion == "2":
            modificar_pares(diccionario)
        elif opcion == "3":
            eliminar_pares(diccionario)
        elif opcion == "4":
            verificar_pares(diccionario)
        elif opcion == "5":
            obtener_pares(diccionario)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu()
