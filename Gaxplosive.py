import csv,os,time
from funciones import *


gaspeque=12500
gasgrande=25500


while True:
    os.system("cls")
    print("Bienvenido a Gaxplosive")
    time.sleep(1)
    os.system("cls")
    print("1. Registrar Pedido")
    print("2. Listar todos los pedidos")
    print("3. Buscar pedido por rut")
    print("4. imprimir hoja de ruta")
    print("5. SALIR")
    while True:
        
        try:
            opc=int(input("Elija una opcion: "))
            if opc in (1,2,3,4,5):
                break
            else:
                print("ERROR! Elija Número Valido")
        except:
            print("ERROR! ingrese número entero")

    os.system("cls")
    if opc==1:
        opcion_1()
        time.sleep(1)
    elif opc==2:
        opcion_2()
        time.sleep(1)
    elif opc==3:
        opcion_3()
        time.sleep(1)
    elif opc==4:
        pass
    else:
        print("HAS ELEGIDO SALIR :c")
        time.sleep(1)
        print("Adios..")
        break
        

