import os
os.system('cls')
#commit
lista=[]

lista2=[]     # lista instanciada para pasarsela al jugador 2.
listaLetras=["a","b","c","d","e","f","g","h","i","j"]
numero=10
contadorJugador1=0
contadorJugador2=0  #15/12/2020  variable instanciada para limitar barcos jugador 2
contadorBarco1 = contadorBarco2 = contadorBarco3 = contadorBarco4 = 0
contadorBarco5 = contadorBarco6 = contadorBarco7 = contadorBarco8 = 0 #segunda instanciacion de variables para referirnos a la cantidad de barcos del jugador 2
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
            lista_posiciones = (i+str(j))   # aqui convertimos la cadena de 1-10 a str para poder referirnos a la posicion en el tablero de forma visual
            lista.append(lista_posiciones)
        print("\n")
    print(lista)#print extra para ver la lista mientras trabajamos en el código

def mostrarTablero(lista):
    listaFila = ["A","B","C","D","E","F","G","H","I","J"]   #esta lista se utilizara para imprimir a principio de linea las letras para el tablero
    x=0     #este auxiliar lo coloco aqui para poder referirme a la posicion de la lista que quiero que se imprima, asi puedo ir imprimiendo las filas
    for i in range(10):
            print("  ",i+1,end=" ")
    for i in range(len(lista)):
        if i%numero == 0:
            print("\n")
        if i == 0 or i%10 == 0:
            print (listaFila[x],end=" ")
            x+=1            #aqui incrementando la variable de fila para ir a la siguiente letra
        if lista[i] == "B":
            print("|B|",end="  ")
        else:
            print("|_|",end="  ")
    print("\n")

def colocarBarco(lista,opcion):
    print(opcion)
    global contadorBarco1,contadorBarco2,contadorBarco3,contadorBarco4
    global contadorBarco5,contadorBarco6,contadorBarco7,contadorBarco8 
    ### 15/12/2020 !enrique!, es necesario colocar mas variables para el control de contadorbarco para el jugador 2, ya que pasandole la lista ya sabe a cual se esta refiriendo, pero nos queda el problema de limitar los barcos del segundo jugador si necesitas aclaracion sobre esta parte dime cosas.
    if opcion ==2:  #<------  15/12/2020  aqui traigo el numero de la opcion desde el menu, para saber que camino cogemos, digamos si es el colocar barco del jugador 1 o del jugador 2
        print("Elige la longitud del barco que quieres colocar (1, 2, 3 o 4): ")
        longitud=int(input())
        while 0> longitud > 4 :
            print("Whoops, respuesta incorrecta. Inténtalo otra vez: ")
            longitud=int(input())
        #Comentario antiguo 11/12/2020 enrique, me da la impresion que tendremo que hacer otra funcion en este punto, ya que si lo dejamos asi, tendremos que copiar la funcion todo el rato dentro de la evaluacion de la longitud y cantidad de barcos.   ********
        
        if longitud == 1 and contadorBarco1 <= 2: #aqui se evalua la cantidad de barcos colocados, permitimos 2 barcos de 1
            if contadorBarco1 == 2:
                print("Ya has colocado todo los barcos de esta medida.")
            else:   #15/12/2020 ----- finalmente he decidido ponerlo dentro, es mas facil y ahorramos vueltas al programa de evaluar condiciones
                contadorBarco1+=1       #******** aqui ira una vez la llamada en caso de poder ser
                llamaBarco(lista,longitud)
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if longitud == 2 and contadorBarco2 <= 2: #aqui se evalua la cantidad de barcos colocados, permitimos 2 barcos de 1
            if contadorBarco2 == 2:
                print("Ya has colocado todo los barcos de esta medida.")
            else:
                contadorBarco2+=1       #******** aqui ira una vez la llamada en caso de poder ser
                llamaBarco(lista,longitud)
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if longitud == 3 and contadorBarco3 <= 2: #aqui se evalua la cantidad de barcos colocados, permitimos 2 barcos de 1
            if contadorBarco3 == 2:
                print("Ya has colocado todo los barcos de esta medida.")
            else:
                contadorBarco3+=1       #******** aqui ira una vez la llamada en caso de poder ser
                llamaBarco(lista,longitud)
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if longitud == 4 and contadorBarco4 <= 2: #aqui se evalua la cantidad de barcos colocados, permitimos 2 barcos de 1
            if contadorBarco4 == 2:
                print("Ya has colocado todo los barcos de esta medida.")
            else:
                contadorBarco4+=1       #******** aqui ira una vez la llamada en caso de poder ser
                llamaBarco(lista,longitud)
    
    
    if opcion ==4:  #<------  15/12/2020  aqui traigo el numero de la opcion desde el menu, para saber que camino cogemos, digamos si es el colocar barco del jugador 1 o del jugador 2
        print("Elige la longitud del barco que quieres colocar (1, 2, 3 o 4): ")
        longitud=int(input())
        while 0> longitud > 4 :
            print("Whoops, respuesta incorrecta. Inténtalo otra vez: ")
            longitud=int(input())
        
        if longitud == 1 and contadorBarco5 <= 2: #aqui se evalua la cantidad de barcos colocados, permitimos 2 barcos de 1
            if contadorBarco5 == 2:
                print("Ya has colocado todo los barcos de esta medida.")
            else:   #15/12/2020 ----- finalmente he decidido ponerlo dentro, es mas facil y ahorramos vueltas al programa de evaluar condiciones
                contadorBarco5+=1       #******** aqui ira una vez la llamada en caso de poder ser
                llamaBarco(lista,longitud)
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if longitud == 2 and contadorBarco6 <= 2: 
            if contadorBarco6 == 2:
                print("Ya has colocado todo los barcos de esta medida.")
            else:
                contadorBarco6+=1       
                llamaBarco(lista,longitud)
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if longitud == 3 and contadorBarco7 <= 2: 
            if contadorBarco7 == 2:
                print("Ya has colocado todo los barcos de esta medida.")
            else:
                contadorBarco7+=1       #******** aqui ira una vez la llamada en caso de poder ser
                llamaBarco(lista,longitud)
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if longitud == 4 and contadorBarco8 <= 2: #aqui se evalua la cantidad de barcos colocados, permitimos 2 barcos de 1
            if contadorBarco8 == 2:
                print("Ya has colocado todo los barcos de esta medida.")
            else:
                contadorBarco8+=1       #******** aqui ira una vez la llamada en caso de poder ser
                llamaBarco(lista,longitud)
    
    return lista            #informarse sobre si la devolucion de cuenta1 incrementa

def llamaBarco(lista,longitud):       #comentalo enrique!
    i=0
    while i < longitud:
        print("Introduce la coordenada",i+1,": ")
        coordenadaBarco=str(input())
        while coordenadaBarco.lower() not in lista:
            print("Esa casilla está ocupada o no existe(smh), prueba otra vez: ")
            coordenadaBarco=str(input())
        lista[lista.index(coordenadaBarco.lower())]="B"
        i+=1
    return lista    

def mostrarMenu(lista,lista2):
    global contadorJugador1
    global contadorJugador2
    menuOn = True
    while menuOn:
        print("¿Qué quieres hacer?")
        print("1: Ver tablero primer jugador \n2: Colocar barco primer jugador \n3: ver tablero segundo jugador \n4: colocar barco segundo jugador \n5: salir" )
        opcion=int(input())
        if opcion == 1:
            mostrarTablero(lista)
        if opcion == 2:
            if contadorJugador1 == 8:#15/12/2020  limita la cantidad de barcos a colocar, si pasa de 8 no te deja entrar.
                print("ya has colocado todos los barcos.")
            else:
                colocarBarco(lista,opcion)
                contadorJugador1+=1
        if opcion == 3:         #15/12/2020   he creado dos opciones mas para crear segundo tablero. gracias a pasarle tablero a lista2 sabe a cual me estoy refiriendo.

            mostrarTablero(lista2)
        if opcion == 4:
            if contadorJugador2 ==8:
                print("ya has colocado todos los barcos")
            else:
                colocarBarco(lista2,opcion)#15/12/2020 colocar barco en lista2 va a haber que mirarlo con cuidado, ya que utiliza los mismo contadores que jugador uno, por ahora... hay dos opciones: mirar como pasarle y reiniciar los contadores y que los tenga en cuenta por dentro cada vez(parece mas complicado, pero mas elegante), o repetir el codigo completo con otro nombre para colocar barcos(parece lo mas facil,pero menos elegante) ---- por ahora he hecho la segunda opción, asi mientras lo vamos terminando. nos acabamos refiriendo a los segundos contadores gracias tanto a la lista que se le pasa como a la opcion escogida en el menu( que tambien se le pasa).
                contadorJugador2+=1
        if opcion == 5:
            menuOn = False

bienvenida()
hacerTablero(lista,listaLetras)
hacerTablero(lista2,listaLetras)
mostrarMenu(lista,lista2) 