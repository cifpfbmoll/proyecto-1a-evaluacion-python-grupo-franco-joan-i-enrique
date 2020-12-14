import os
os.system('cls')
lista=[]
listaLetras=["a","b","c","d","e","f","g","h","i","j"]
numero=10
def bienvenida():
    print("---------------------------------------------------------------------")
    print("+++++++++++++++++ Bienvenido a Battleship en Python +++++++++++++++++++")
    print("---------------------------------------------------------------------")
    print("+++++++++++++++todos los tableros de battleship son de 10x10 Francisco, por eso se llama battleship, porque ya tiene unas reglas predefinidas que lo identifican como battleship y no como la ruka (: +++++++++++++++++")#<3
    print("\n")

def hacerTablero(lista,listaLetras):
    for i in listaLetras:
        for j in range(1,numero+1):
            print("|_|",end="  ")
            lista_posiciones = (i+str(j))
            lista.append(lista_posiciones)
        print("\n")
    print(lista)#print extra para ver la lista mientras trabajamos en el código

def mostrarTablero(lista):
    for i in range(len(lista)):
        if i%numero == 0:
            print("\n")
        if lista[i] == "B":
            print("|B|",end="  ")
        else:
            print("|_|",end="  ")
    print("\n")

def colocarBarco(lista):
    print("Elige la longitud del barco que quieres colocar (1, 2, 3 o 4): ")
    longitud=int(input())
    while 0> longitud > 4 :
        print("Whoops, respuesta incorrecta. Inténtalo otra vez: ")
        longitud=int(input())
    
    # cuenta1 = cuenta2 = cuenta3 = cuenta4 = 0
    # if longitud == 1 and cuenta1 <= 2: #aqui se evalua la cantidad de barcos colocados, permitimos 2 barcos de 1
    #     cuenta1+=1
    # if longitud == 2 and cuenta2 <= 2: #aqui se evalua la cantidad de barcos colocados, permitimos 2 barcos de 2
    #     cuenta2+=1
    # if longitud == 3 and cuenta3 <= 2: #aqui se evalua la cantidad de barcos colocados, permitimos 2 barcos de 3
    #     cuenta2+=1
    # if longitud == 4 and cuenta2 <= 1: #aqui se evalua la cantidad de barcos colocados, permitimos 2 barcos de 1
    #     cuenta2+=1
    i=0
    while i < longitud:
        print("Introduce la coordenada",i+1,": ")
        coordenadaBarco=str(input())
        while coordenadaBarco.lower() not in lista:
            print("Esa casilla está ocupada o no existe(smh), prueba otra vez: ")
            coordenadaBarco=str(input())
        lista[lista.index(coordenadaBarco.lower())]="B"
        i+=1
    print(lista)#print extra para ver la lista mientras trabajamos en el código


def mostrarMenu(lista):
    menuOn = True
    while menuOn:
        print("¿Qué quieres hacer?")
        print("1: Ver el tablero \n2: Colocar barco ")
        opcion=int(input())
        if opcion == 1:
            mostrarTablero(lista)
        if opcion == 2:
            colocarBarco(lista)
        if opcion == 3:
            menuOn = False
bienvenida()
hacerTablero(lista,listaLetras)
mostrarMenu(lista)
