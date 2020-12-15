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
# def dentroTablero(coordenada,lista): #esto es una trolleada no se que hago pls help
#     while coordenada.lower() not in lista:
#         print("Esa casilla está ocupada o no existe(smh), prueba otra vez: ")
#         coordenada=str(input())
#     return coordenada
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

    i=0
    listaCoordenadas=[]
    while i < longitud:
        if longitud==1:
            disposicionBarco=None
        elif longitud>1 and i==0:
            disposicionBarco=input("¿Colocar barco en horizontal o vertical? (ej: H o V)") #Pendiente de terminar. Se puede meter while para que respuesta sea h o v.
        print("Introduce la coordenada",i+1,": ")
        coordenadaBarco=str(input())
        while coordenadaBarco.lower() not in lista:
            print("Esa casilla está ocupada o no existe(smh), prueba otra vez: ")
            coordenadaBarco=str(input())
        #franco=True  inicio para el bucle de comprobar si cabe y cambiar a false cuando termine
        while longitud==2 and i==0 and (lista[lista.index(coordenadaBarco.lower())+1]=="B" and lista[lista.index(coordenadaBarco.lower())-1]=="B"):
            coordenadaBarco=str(input("Noob, el barco no cabe, prueba en otro sitio: "))
            #acho mi puta vida en bicicleta sería mas facil, 
            #METER FUNCION COMPARAR SI CASILLA VALIDA OTRA VEZ.
            while coordenadaBarco.lower() not in lista:
                print("Esa casilla está ocupada o no existe(smh), prueba otra vez: ")
                coordenadaBarco=str(input())
        while longitud==3 and i==0 and (lista[lista.index(coordenadaBarco.lower())+1]=="B" and lista[lista.index(coordenadaBarco.lower())-1]=="B") or (lista[lista.index(coordenadaBarco.lower())+2]=="B" and (lista[lista.index(coordenadaBarco.lower())-1]=="B") and (lista[lista.index(coordenadaBarco.lower())-2]=="B" and lista[lista.index(coordenadaBarco.lower())+1]=="B")):
            coordenadaBarco=str(input("Noob, el barco no cabe, prueba en otro sitio: "))
            #acho mi puta vida en bicicleta sería mas facil, 
            #METER FUNCION COMPARAR SI CASILLA VALIDA OTRA VEZ.
            while coordenadaBarco.lower() not in lista:
                print("Esa casilla está ocupada o no existe(smh), prueba otra vez: ")
                coordenadaBarco=str(input())

        if i==0:
            listaCoordenadas.append(lista.index(coordenadaBarco.lower()))
        if longitud>1 and disposicionBarco=="H" or disposicionBarco=="h": 
        # ////////////////////////////
        #He tenido que usar una funcion de listas llamada sorted() para que la lista que contiene las coordenadas de los barcos de longitud 2-4 esté ordenada de menor a mayor numero y tomen como referencia las contiguas a las esquinas, sumando +1/+10(es decir comprobar la casilla a la derecha) a la posicion [-1] que tras hacer un sorted siempre será el indice mas a la derecha o mas abajo y sumando -1/-10 a la posicion [0] que siempre será el indice mas pequeño
        # ///////////////////////////
        #HACER FUNCION DEL WHILE? pero seguro que las variables dejan de mantener los datos...........
            while (i>0) and (lista.index(coordenadaBarco.lower())!=(sorted(listaCoordenadas)[0])-1 and lista.index(coordenadaBarco.lower())!=(sorted(listaCoordenadas)[-1])+1):
                coordenadaBarco=str(input("¡Las casillas deben ser contiguas! Prueba otra vez: "))
                print(lista, listaCoordenadas)
                print(coordenadaBarco)
                while coordenadaBarco.lower() not in lista:
                    print("Esa casilla está ocupada o no existe(smh), prueba otra vez: ")
                    coordenadaBarco=str(input())
                print(coordenadaBarco)
        elif longitud>1 and disposicionBarco=="V" or disposicionBarco=="v":
            while (i>0) and (lista.index(coordenadaBarco.lower())!=(sorted(listaCoordenadas)[0])-10 and lista.index(coordenadaBarco.lower())!=(sorted(listaCoordenadas)[-1])+10):
                coordenadaBarco=str(input("¡Las casillas deben ser contiguas! Prueba otra vez: "))
                print(lista, listaCoordenadas)
                print(coordenadaBarco)
                while coordenadaBarco.lower() not in lista: #pasar esto a funcion
                    print("Esa casilla está ocupada o no existe(smh), prueba otra vez: ")
                    coordenadaBarco=str(input())
                print(coordenadaBarco)
        if i>0 and longitud>1:
            listaCoordenadas.append(lista.index(coordenadaBarco.lower()))
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
        # if opcion == 3:
        #     menuOn = False
bienvenida()
hacerTablero(lista,listaLetras)
mostrarMenu(lista)
