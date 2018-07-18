import time 
import sys

while True:
    print("--------------------------------MENU PRINCIPAL-------------------------------------")
    print("Eliga una opcion:")
    print("-----------------------------------------------------------------------------------")
    print('     "1".Acceder a menu Semanal')
    print('     "2".Acceder a menu Quincenal')
    print('     "3".Acceder a menu Semanal')
    print('     Para cerrar sesion: "Cerrar o s"')
    print("-----------------------------------------------------------------------------------")
    print("")
    orden = input("Escriba un parametro:  ") #Variable almacena el valor que se le de. A la espera de los valores ()
    print("")
    if orden == "1":    ###Opcion 1 para ejecutar el menu Semanal###
        print("===================================================================================")
        print(' Usted ha accedido exitosamente a la lista semanal!')
        print("===================================================================================")
        print('Si desea agregar o borrar elementos puede utilizar los parametros: add o del')
        print(' Para volver al menu principal escriba: salir')
        print("-----------------------------------------------------------------------------------")
        time.sleep(2)       ###Modulo (import time) agrega un descanzo antes de pasar a la siguiente linea de codigo##
        print(" Todos los elementos agregados:")    ###Mensaje para posteriormente mostrar todos los elementos de la lista###
        lista = ["PAN = $50","QUESO = $100"]    ##Lista que contiene todos los elementos de el MENU SEMANAL##
        maximoDeElementos = 20      ###Maximo de elementos (letras, espacios, caracteres especiales) que se puede agregar a una lista###
        print(lista)        ###Mostrar el contenido de la variable (LISTA)###
        while len(lista) < maximoDeElementos:   ###Bucle NUMERO 1 para la variable lista  y el numero maximo de elementos###
            opcion = input("Que desea hacer?    ")     ###variable (OPCION) que contiene una entrada de datos###
            if opcion == "add" or "ADD":    #Enunciado: (SI) el elemento agregado en la variable (OPCION) es igual a valor entero (ADD) ENTONCES haz esto...#
                agregar = input("Agrege un elemento:    ")  ##Variable que almacena los datos que se escriban##
                lista.append(agregar)   ##Ennunciado: Variable (LISTA) hacer (ANADIR) valor escrito en la variable aterior: AGREGAR ##
                print(lista)        ##Mostrar el contenido de la variable (LISTA)

            elif opcion == "del" or "DEL":  ###Ennunciado: (SI) el elemento escrito en la variable (OPCION) es igual a (del) o (DEL) entonces haz esto...###
                remover = input("Borre un elemento:     ") ###Variable (REMOVER) con una entrada de datos###
                lista.remove(remover)   ##Ennunciado: (LISTA) hacer (eliminar) elemento escrito en la variable anterior: REMOVER ##
                print(lista)    ##Mostrar el contenido de la variable (LISTA)

            elif opcion == "salir" or "s" or "SALIR" or "S":    ###Enunciado: (SI) el elemento escrito en la variable (OPCION) es igual a (salir) o (s) o (SALIR) o (S) entonces haz esto...###
                break   ###ROMPE ESTE BUCLE NUMERO 1. Si se ejecuta lo descrito en la linea anterior###

            else:       ###Si no se cumple nada de lo anteriormente mencionado entonces haz esto... ###
                print("Parametro incorrecto")       ###Mensaje de que se introdujo un paramentro mal###

    elif orden == "2":    ###Opcion 2 para ejecutar el menu Quincenal###
        print("=======================================================================")
        print(' Usted ha accedido exitosamente a la lista Quincenal!')
        print("=======================================================================")
        print('Si desea agregar o borrar elementos puede utilizar los parametros: add o del')
        print(' Para volver al menu principal escriba: salir')
        time.sleep(2)       ###Modulo (import time) agrega un descanzo antes de pasar a la siguiente linea de codigo##
        print(" Todos los elementos agregados:")    ###Mensaje para posteriormente mostrar todos los elementos de la lista###
        lista = ["PAN = $50","QUESO = $100"]    ##Lista que contiene todos los elementos de el MENU QUINCENAL##
        maximoDeElementos = 20      ###Maximo de elementos (letras, espacios, caracteres especiales) que se puede agregar a una lista###
        print(lista)        ###Mostrar el contenido de la variable (LISTA)###
        while len(lista) < maximoDeElementos:   ###Bucle NUMERO 1 para la variable lista  y el numero maximo de elementos###
            opcion = input("Que desea hacer?    ")     ###variable (OPCION) que contiene una entrada de datos###
            if opcion == "add" or "ADD":    #Enunciado: (SI) el elemento agregado en la variable (OPCION) es igual a valor entero (ADD) ENTONCES haz esto...#
                agregar = input("Agrege un elemento:    ")  ##Variable que almacena los datos que se escriban##
                lista.append(agregar)   ##Ennunciado: Variable (LISTA) hacer (ANADIR) valor escrito en la variable aterior: AGREGAR ##
                print(lista)        ##Mostrar el contenido de la variable (LISTA)

            elif opcion == "del" or "DEL":  ###Ennunciado: (SI) el elemento escrito en la variable (OPCION) es igual a (del) o (DEL) entonces haz esto...###
                remover = input("Borre un elemento:     ") ###Variable (REMOVER) con una entrada de datos###
                lista.remove(remover)   ##Ennunciado: (LISTA) hacer (eliminar) elemento escrito en la variable anterior: REMOVER ##
                print(lista)    ##Mostrar el contenido de la variable (LISTA)

            elif opcion == "salir" or "s" or "SALIR" or "S":    ###Enunciado: (SI) el elemento escrito en la variable (OPCION) es igual a (salir) o (s) o (SALIR) o (S) entonces haz esto...###
                break   ###ROMPE ESTE BUCLE NUMERO 1. Si se ejecuta lo descrito en la linea anterior###

            else:       ###Si no se cumple nada de lo anteriormente mencionado entonces haz esto... ###
                print("Parametro incorrecto")       ###Mensaje de que se introdujo un paramentro mal###

    elif orden == "3":
        print("=======================================================================")
        print(' Usted ha accedido exitosamente a la lista Mensual!')
        print("=======================================================================")
        print('Si desea agregar o borrar elementos puede utilizar los parametros: add o del')
        print(' Para volver al menu principal escriba: salir')
        time.sleep(2)       ###Modulo (import time) agrega un descanzo antes de pasar a la siguiente linea de codigo##
        print(" Todos los elementos agregados:")    ###Mensaje para posteriormente mostrar todos los elementos de la lista###
        lista = ["PAN = $50","QUESO = $100"]    ##Lista que contiene todos los elementos de el MENU MENSUALL##
        maximoDeElementos = 20      ###Maximo de elementos (letras, espacios, caracteres especiales) que se puede agregar a una lista###
        print(lista)        ###Mostrar el contenido de la variable (LISTA)###
        while len(lista) < maximoDeElementos:   ###Bucle NUMERO 1 para la variable lista  y el numero maximo de elementos###
            opcion = input("Que desea hacer?    ")     ###variable (OPCION) que contiene una entrada de datos###
            if opcion == "add" or "ADD":    #Enunciado: (SI) el elemento agregado en la variable (OPCION) es igual a valor entero (ADD) ENTONCES haz esto...#
                agregar = input("Agrege un elemento:    ")  ##Variable que almacena los datos que se escriban##
                lista.append(agregar)   ##Ennunciado: Variable (LISTA) hacer (ANADIR) valor escrito en la variable aterior: AGREGAR ##
                print(lista)        ##Mostrar el contenido de la variable (LISTA)

            elif opcion == "del" or "DEL":  ###Ennunciado: (SI) el elemento escrito en la variable (OPCION) es igual a (del) o (DEL) entonces haz esto...###
                remover = input("Borre un elemento:     ") ###Variable (REMOVER) con una entrada de datos###
                lista.remove(remover)   ##Ennunciado: (LISTA) hacer (eliminar) elemento escrito en la variable anterior: REMOVER ##
                print(lista)    ##Mostrar el contenido de la variable (LISTA)

            elif opcion == "salir" or "s" or "SALIR" or "S":    ###Enunciado: (SI) el elemento escrito en la variable (OPCION) es igual a (salir) o (s) o (SALIR) o (S) entonces haz esto...###
                break   ###ROMPE ESTE BUCLE NUMERO 1. Si se ejecuta lo descrito en la linea anterior###

            else:       ###Si no se cumple nada de lo anteriormente mencionado entonces haz esto... ###
                print("Parametro incorrecto")       ###Mensaje de que se introdujo un paramentro mal###

    elif orden == "cerrar" or "c" or "CERRAR" or "C":      ###Ennunciado: (SI) el elmento escrito en la variable (ORDEN) es igual a (cerrar) o (c) o (CERRAR) o (C) entonces haz esto...###
        print("Cerrando programa...")       ###Mensaje que informa que se esta cerrando el programa###
        time.sleep(2)       ###Modulo (import time) agrega un descanzo antes de pasar a la siguiente linea de codigo##
        sys.exit() #Parametro para cerrar el programa tecleando cer
    else:     ###Si no se cumple nada de lo anteriormente mencionado entonces haz esto... ###
        print("El elemento que ha introducido no existe. Intente nuevamente")   #Mensaje que saldra despues de la linea de codigo anterior#
