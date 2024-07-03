
clientes=[]
sectores=["santiago","colina", "pirque"]
import csv,os,time
gaspeque=12500
gasgrande=25500



def opcion_1 ():
    print("Has elegido registrar")
    rut=int(input("Escribe tu RUT: "))
    nombre=input("Escribe tu Nombre y apellido: ")
    direc=input("Escribe tu direccion: ")
    comu=comunacomprobador()
    galonpe=int(input("Cuantos galones pequeños deseas?: "))
    galongr=int(input("Cuantos galones grandes deseas?: "))
    total=galonpe*12500+galongr*25500
    pedido={"Nombre": nombre,
         "Rut": rut,
         "Comuna": comu,
         "Direccion": direc,
         "galon pequeño":galonpe,
         "galon grande": galongr,
         "Total a pagar":total
         }
    clientes.append(pedido)
    
    
    print("HAS REGISTRADO TÚ PEDIDO CON EXITO!!")

    


def opcion_2 ():
    print("los pedidos que han hecho son:")
    for p in range(len(clientes)):
        print(clientes[p])



def opcion_3 ():
    while True:
        rutverificador=int(input("ingrese su rut para ver pedidos: "))
        if rutverificador in clientes:
            pass         
        else:
            print("NO HAY PEDIDOS CON ESTE RUT")



def comunacomprobador ():
    
    while True:
        comuni=input("Escribe tu comuna: ")
        if comuni in sectores:
            print("ESTE SECTOR SI ESTA DISPONIBLE PARA ENTREGA")
            time.sleep(1)
            break
        else:
            print("NO ENTREGAMOS A ESTE SECTOR")
        


def opcion_4 ():
    print(sectores)
    comunaimpr=("ingrese el nombre de la comuna:")
    with open(comunaimpr+"csv","x",newline="") as archivo:
        escritor=csv.DictWriter(archivo,["Nombre",nombre]["Rut": rut]["Comuna": comu]["Direccion": direc]["galon pequeño":galonpe]["galon grande": galongr])
        escritor.writerows(clientes)
        
        
    











    print("IMPRIMIENDO")


