

def primerTablero(lista1):
    print("---------------------------------------------------------------------")
    print("+++++++++++++++++Bienvenido a battleship en python+++++++++++++++++++")
    print("---------------------------------------------------------------------")
    print("+++++++++++++++vamos a jugar con un tablero de 10x10+++++++++++++++++")
    print("\n")
    for i in range(numero):
        for j in range(numero):
           print("|_|",end="  ")
           listabarco = [i,j]
           lista1.append(listabarco)
        print("\n")


    # lista1[00]= "B"
    # if lista1[00]== "B":
    #     print("avanzas")
    # print(lista1)


def colocarBarco(lista2):
    print("Di de que largo quieres colocar el barco (1,2,3 o 4): ")
    largo=int(input())
    while 0> largo > 4 :
        print("No puedes exceder de 4, prueba otra vez: ")
        largo=int(input())
    
    cuenta1 = cuenta2 = cuenta3 = cuenta4 = 0
    if largo == 1 and cuenta1 <= 2: #aqui se evalua la cantidad de barcos colocados, permitimos 2 barcos de 1
        cuenta1+=1
    if largo == 2 and cuenta2 <= 2: #aqui se evalua la cantidad de barcos colocados, permitimos 2 barcos de 2
        cuenta2+=1
    if largo == 3 and cuenta3 <= 2: #aqui se evalua la cantidad de barcos colocados, permitimos 2 barcos de 3
        cuenta2+=1
    if largo == 4 and cuenta2 <= 1: #aqui se evalua la cantidad de barcos colocados, permitimos 2 barcos de 1
        cuenta2+=1
    i=0
    while i < largo:
        print("introduce la ",i+1," coordenada:")
        coordenada=int(input())
        while lista2[coordenada] == "B":
            print("esta coordenada esta ocupada, introduce otra: ")
            coordenada=int(input())
        lista2[coordenada] = "B"
        i+=1
    print(lista2)

def dibujarTablero(listaImp):
    for i in range(len(listaImp)):
        if i%numero == 0:
            print("\n")
        if listaImp[i] == "B":
            print("|B|",end="  ")
        else:
            print("|_|",end="  ")
    print("\n")

def mostrarMenu(lista):
    salir = False
    while salir == False:
        
        print("Que quieres hacer?")
        print("opcion 1: ver el tablero ")
        print("opcion 2: colocar barco ")
        opcion=int(input())
        if opcion == 1:
            dibujarTablero(lista)
        if opcion == 2:
            colocarBarco(lista)
        if opcion == 3:
            salir = True
    
        

lista=[]
numero=10
primerTablero(lista)
mostrarMenu(lista)        

