import time 
import sys

print("_______________________________________________________________________________")
print('-Para acceder al listado Semanal por favor escriba: 	 1.')
time.sleep(2)
print("_______________________________________________________________________________")
print('-Para acceder al listado Quincenal por favor escriba:  	 2.')
time.sleep(2)
print("_______________________________________________________________________________")
print('-Para acceder al listado Mensual por favor escriba:  	 3.')
time.sleep(2)
print("===============================================================================")
print('|||||||||||||||||Para finalizar el programa escriba: cerrar o c|||||||||||||||||')
print("===============================================================================")
orden = input("Escriba un parametro aqui:  ") #Se queda esperando que se teclee alguna orden (1,2,3 o cerrar)
cerrar = sys.exit() #Parametro para cerrar el programa tecleando cer

print("")
def Semanal():
	print("=======================================================================")
	print('	Usted ha accedido exitosamente a la lista semanal!')
	print("=======================================================================")
	print('Si desea agregar o borrar elementos puede utilizar los parametros: add o del')
	print('	Para volver al menu principal escriba: salir')
	time.sleep(2)
	print("	Todos los elementos agregados:")
	lista = ["PAN = $50","QUESO = $100"]
	print(lista)

def Quincenal():
	print("=======================================================================")
	print('	Usted ha accedido exitosamente a la lista Quincenal!')
	print("=======================================================================")
	print('Si desea agregar o borrar elementos puede utilizar los parametros: add o del')
	print('	Para volver al menu principal escriba: salir')
	time.sleep(2)
	print("	Todos los elementos agregados:")
	lista = ["Internet = $1000","Netflix = $500"]
	print(lista)

def Mensual():
	print("=======================================================================")
	print('	Usted ha accedido exitosamente a la lista Mensual!')
	print("=======================================================================")
	print('Si desea agregar o borrar elementos puede utilizar los parametros: add o del')
	print('	Para volver al menu principal escriba: salir')
	time.sleep(2)
	print("	Todos los elementos agregados:")
	lista = ["AGUA = $400","LUZ = $2000"]
	print(lista)

varSemanal = Semanal()
varQuincenal = Quincenal()
varMensual = Mensual()

While True:
	if orden == cerrar and c:
		print(cerrar)
	elif orden == 1:
		print(varSemanal)
	elif orden == 2:
		print(varSemanal)
	elif orden == 3:
		print(varQuincenal)
	else:
		print("El elemento que ha escrito no existe")