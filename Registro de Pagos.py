print("_______________________________________________________________________________")
print('-Para acceder al listado Semanal por favor escriba:      1.')
time.sleep(2)
print("_______________________________________________________________________________")
print('-Para acceder al listado Quincenal por favor escriba:    2.')
time.sleep(2)
print("_______________________________________________________________________________")
print('-Para acceder al listado Mensual por favor escriba:      3.')
time.sleep(2)
print("===============================================================================")
print('|||||||||||||||||Para finalizar el programa escriba: cerrar o c|||||||||||||||||')
print("===============================================================================")

orden = input("Escriba un parametro aqui:  ") #Se queda esperando que se teclee alguna orden (1,2,3 o cerrar)

print("")
if orden == "1":
    print("=======================================================================")
    print(' Usted ha accedido exitosamente a la lista semanal!')
    print("=======================================================================")
    print('Si desea agregar o borrar elementos puede utilizar los parametros: add o del')
    print(' Para volver al menu principal escriba: salir')
    time.sleep(2)
    print(" Todos los elementos agregados:")
    lista = ["PAN = $50","QUESO = $100"]
    print(lista)

elif orden == "2":
    print("=======================================================================")
    print(' Usted ha accedido exitosamente a la lista Quincenal!')
    print("=======================================================================")
    print('Si desea agregar o borrar elementos puede utilizar los parametros: add o del')
    print(' Para volver al menu principal escriba: salir')
    time.sleep(2)
    print(" Todos los elementos agregados:")
    lista = ["Internet = $1000","Netflix = $500"]
    print(lista)

elif orden == "3":
    print("=======================================================================")
    print(' Usted ha accedido exitosamente a la lista Mensual!')
    print("=======================================================================")
    print('Si desea agregar o borrar elementos puede utilizar los parametros: add o del')
    print(' Para volver al menu principal escriba: salir')
    time.sleep(2)
    print(" Todos los elementos agregados:")
    lista = ["AGUA = $400","LUZ = $2000"]
    print(lista)
elif orden == "cerrar" or "c":
    print("Cerrando programa...")
    time.sleep(2)
    sys.exit() #Parametro para cerrar el programa tecleando cer
else:
    print("El elemento que ha introducido no existe. Intente nuevamente")
