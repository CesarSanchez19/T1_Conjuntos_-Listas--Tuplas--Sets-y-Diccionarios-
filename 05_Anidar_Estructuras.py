### MENÚ INTERACTIVO DE ANIDACIÓN DE ESTRUCTURAS EN PYTHON ###

# Función para agregar un elemento a la lista anidada (tupla y diccionario).
def agregar_elemento(lista_anidada):
    print("\n--- Ejecutando: Agregar un elemento ---")
    n = input("Ingrese el elemento que desea agregar: ")
    n = convertir_elemento(n)

    while True:
        print("\n--- Elige dónde quieres agregar el elemento ---")
        seleccion = input("\n1. Agregar en la tupla\n2. Agregar en el diccionario\n0. Salir\nSeleccione una opción: ")

        if seleccion == "1":
            tupla_temp = list(lista_anidada[0])  
            tupla_temp.append(n)  
            lista_anidada[0] = tuple(tupla_temp)  
            print(f"\nNueva tupla actualizada: {lista_anidada[0]}")
            break
        
        elif seleccion == "2":
            diccionario = lista_anidada[1]  
            clave = input("Ingrese la clave para este nuevo valor: ")
            diccionario[clave] = n  
            print(f"\nNuevo diccionario actualizado: {diccionario}")
            break

        elif seleccion == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

# Función para acceder a un elemento en la lista anidada (tupla y diccionario).
def acceder_elemento(lista_anidada):
    print("\n--- Ejecutando: Acceder a un elemento ---")
    n = input("Ingrese el elemento que desea buscar: ")
    n = convertir_elemento(n)

    if len(lista_anidada) < 2:
        print("\nError: La estructura de `lista_anidada` no es válida.")
        return

    while True:
        print("\n--- Elige dónde quieres buscar el elemento ---")
        seleccion = input("\n1. Buscar en la tupla\n2. Buscar en el diccionario\n0. Salir\nSeleccione una opción: ")

        if seleccion == "1":
            tupla = lista_anidada[0]
            if n in tupla:
                indice = tupla.index(n)
                print(f"\nEl elemento '{n}' está en la tupla en el índice {indice}. En la primera fila {lista_anidada[0]}")
                break
            else:
                print(f"\nEl elemento '{n}' no está en la tupla.")

        elif seleccion == "2":
            diccionario = lista_anidada[1]
            if n in diccionario:
                valor = diccionario[n]
                print(f"\nLa clave '{n}' está en el diccionario con el valor '{valor}'. En la segunda fila {lista_anidada[1]}")
                break
            else:
                print(f"\nLa clave '{n}' no está en el diccionario.")

        elif seleccion == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

# Función para modificar un elemento en la lista anidada (tupla y diccionario).
def modificar_elemento(lista_anidada):
    print("\n--- Ejecutando: Modificar un elemento ---")
    n = input("Ingrese el elemento que desea modificar: ")
    n = convertir_elemento(n)

    if len(lista_anidada) < 2:
        print("\nError: La estructura de `lista_anidada` no es válida.")
        return

    while True:
        print("\n--- Elige dónde quieres modificar el elemento ---")
        seleccion = input("\n1. Modificar en la tupla\n2. Modificar en el diccionario\n0. Salir\nSeleccione una opción: ")

        if seleccion == "1":
            tupla = lista_anidada[0]
            if n in tupla:
                indice = tupla.index(n)
                nuevo_valor = input(f"\nIngrese el nuevo valor para reemplazar '{n}': ")
                nuevo_valor = convertir_elemento(nuevo_valor)
                tupla_temp = list(tupla)
                tupla_temp[indice] = nuevo_valor
                lista_anidada[0] = tuple(tupla_temp)
                print(f"\nTupla actualizada: {lista_anidada[0]}")
                break
            else:
                print(f"\nEl elemento '{n}' no está en la tupla.")

        elif seleccion == "2":
            diccionario = lista_anidada[1]
            if n in diccionario:
                nuevo_valor = input(f"\nIngrese el nuevo valor para la clave '{n}': ")
                diccionario[n] = convertir_elemento(nuevo_valor)
                print(f"\nDiccionario actualizado: {lista_anidada[1]}")
                break
            else:
                print(f"\nLa clave '{n}' no está en el diccionario.")

        elif seleccion == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

# Función para eliminar un elemento en la lista anidada (tupla y diccionario).
def eliminar_elemento(lista_anidada):
    print("\n--- Ejecutando: Eliminar un elemento ---")
    n = input("Ingrese el elemento que desea eliminar: ")
    n = convertir_elemento(n)

    if len(lista_anidada) < 2:
        print("\nError: La estructura de `lista_anidada` no es válida.")
        return

    while True:
        print("\n--- Elige dónde quieres eliminar el elemento ---")
        seleccion = input("\n1. Eliminar en la tupla\n2. Eliminar en el diccionario\n0. Salir\nSeleccione una opción: ")

        if seleccion == "1":
            tupla = lista_anidada[0]
            if n in tupla:
                tupla_temp = list(tupla)
                tupla_temp.remove(n)  # Elimina el primer elemento que coincida
                lista_anidada[0] = tuple(tupla_temp)
                print(f"\nTupla actualizada: {lista_anidada[0]}")
                break
            else:
                print(f"\nEl elemento '{n}' no está en la tupla.")

        elif seleccion == "2":
            diccionario = lista_anidada[1]
            if n in diccionario:
                del diccionario[n]  # Elimina la clave y su valor
                print(f"\nDiccionario actualizado: {lista_anidada[1]}")
                break
            else:
                print(f"\nLa clave '{n}' no está en el diccionario.")

        elif seleccion == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

# Función para convertir elementos en números o cadenas de texto de una lista.
def convertir_tupla(tupla):
    if all(elemento.isdigit() for elemento in tupla):  # Verifica si todos los elementos son números
        return tuple(map(int, tupla))  # Convierte a enteros
    else:
        return tuple(map(str, tupla))  # Mantiene como cadenas

# Función para convertir los elementos en números o cadenas
def convertir_elemento(n):
    return int(n) if n.isdigit() else str(n)

# Función para el menú interactivo
def menu():
    print("\n--- Ejecutando: Menú interactivo de estructuras anidadas ---")
    
    print("\n--- Creando: Lista anidada con tupla y diccionario ---")
    tupla = convertir_tupla(tuple(input("Primero, ingrese los elementos de la tupla separados por espacio: ").split()))
    diccionario = {}
    
    items = input("Segundo, ingrese las claves y valores del diccionario separados por espacio (ejemplo: nombre:yair apellido:guzman): ").split()
    
    for par in items:
        if ":" in par: 
            clave, valor = par.split(":")
            diccionario[convertir_elemento(clave.strip())] = convertir_elemento(valor.strip())
        else:
            print(f"Formato incorrecto en '{par}'. Use clave:valor.")

    lista_anidada = [tupla, diccionario]
    
    print("\n--- Lista anidada creada ---")
    print(lista_anidada)
    
    while True:
        print("\n### Menú interactivo de estructuras anidadas en Python ###")
        print(f"Lista anidada actual: {lista_anidada}")
        
        opcion = input("\n1. Agregar un elemento\n2. Acceder a un elemento \n3. Modificar un elemento\n4. Eliminar un elemento\n0. Salir\nSeleccione una opción: ")
        
        if opcion == "1":
            agregar_elemento(lista_anidada)
        elif opcion == "2":
            acceder_elemento(lista_anidada)
        if opcion == "3":
            modificar_elemento(lista_anidada)
        elif opcion == "4":
            eliminar_elemento(lista_anidada)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu()
