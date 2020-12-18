import os
os.system('cls')
#commit
lista=[]
lista2=[]     # lista declarada para pasarsela al jugador 2.
listaDisparosJ1=[]
listaDisparosJ2=[]
listaLetras=["a","b","c","d","e","f","g","h","i","j"]
dictDianas1={}
dictDianas2={} #o contador al num de dianas para ganar o listaDianas.pop/remove>len.lista==0
numero=10
contadorjugador1=0
contadorjugador2=0  #15/12/2020  variable declarada para limitar barcos jugador2
contadorBarco1,contadorBarco2,contadorBarco3,contadorBarco4 = 0,0,0,0
contadorBarco5,contadorBarco6,contadorBarco7,contadorBarco8 = 0,0,0,0 #segunda declaración de variables para referirnos a la cantidad de barcos del jugador 2
def mostrarBienvenida():
    print("---------------------------------------------------------------------")
    # print(chr(27)+"[1;33m")  AQUI FALTA INDICAR EL FINAL DEL CHR ETC PARA QUE NO MODIFIQUE DE COLOR TODO LO QUE PRINTEA LA TERMINAL, COMO SI FUERA UN TAG DE HTML

    print("+++++++++++++++++ Bienvenido a Battleship en Python +++++++++++++++++")
    print("---------------------------------------------------------------------")
    print("+++++++++++++++++++++++ Para 2 jugadores <3 ++++++++++++++++++++++++")#<3
    print("\n")


def validarCoordenada(coordenada):
    while coordenada.lower() not in lista:
        print("Esa casilla está ocupada o no existe(smh), prueba otra vez: ")
        coordenada=str(input())
    return coordenada.lower()

def hacerTablero(lista,listaLetras):
    for i in listaLetras:
        for j in range(1,numero+1):
            lista_posiciones = (i+str(j))   # aqui convertimos la cadena de 1-10 a str para poder referirnos a la posicion en el tablero de forma visual
            lista.append(lista_posiciones)

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
        elif lista[i] == "X":
            print("|X|",end="  ")
        elif lista[i] == "O":
            print("|O|",end="  ")   #he quitado las barras para que se vea mejor el AGUA, pero podemos buscar algo mas guay.
        else:
            print("|_|",end="  ")
    print("\n")

def evaluarBarcos(lista,opcion,dictDianas):
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
                colocarBarco(lista,longitud,dictDianas)
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if longitud == 2 and contadorBarco2 <= 2: #aqui se evalua la cantidad de barcos colocados, permitimos 2 barcos de 1
            if contadorBarco2 == 2:
                print("Ya has colocado todo los barcos de esta medida.")
            else:
                contadorBarco2+=1       #******** aqui ira una vez la llamada en caso de poder ser
                colocarBarco(lista,longitud,dictDianas)
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if longitud == 3 and contadorBarco3 <= 2: #aqui se evalua la cantidad de barcos colocados, permitimos 2 barcos de 1
            if contadorBarco3 == 2:
                print("Ya has colocado todo los barcos de esta medida.")
            else:
                contadorBarco3+=1       #******** aqui ira una vez la llamada en caso de poder ser
                colocarBarco(lista,longitud,dictDianas)
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if longitud == 4 and contadorBarco4 <= 2: #aqui se evalua la cantidad de barcos colocados, permitimos 2 barcos de 1
            if contadorBarco4 == 2:
                print("Ya has colocado todo los barcos de esta medida.")
            else:
                contadorBarco4+=1       #******** aqui ira una vez la llamada en caso de poder ser
                colocarBarco(lista,longitud,dictDianas)
    
    
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
                colocarBarco(lista,longitud,dictDianas)
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if longitud == 2 and contadorBarco6 <= 2: 
            if contadorBarco6 == 2:
                print("Ya has colocado todo los barcos de esta medida.")
            else:
                contadorBarco6+=1       
                colocarBarco(lista,longitud,dictDianas)
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if longitud == 3 and contadorBarco7 <= 2: 
            if contadorBarco7 == 2:
                print("Ya has colocado todo los barcos de esta medida.")
            else:
                contadorBarco7+=1       #******** aqui ira una vez la llamada en caso de poder ser
                colocarBarco(lista,longitud,dictDianas)
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if longitud == 4 and contadorBarco8 <= 2: #aqui se evalua la cantidad de barcos colocados, permitimos 2 barcos de 1
            if contadorBarco8 == 2:
                print("Ya has colocado todo los barcos de esta medida.")
            else:
                contadorBarco8+=1       #******** aqui ira una vez la llamada en caso de poder ser
                colocarBarco(lista,longitud,dictDianas)
    
    return lista            #informarse sobre si la devolucion de cuenta1 incrementa

def colocarBarco(lista,longitud,dictDianas):       #comentalo enrique!
    if longitud==1:
        disposicionBarco=None #no hace falta usar vert/horiz para los de 1
    elif longitud>1:
        disposicionBarco=input("¿Colocar barco en horizontal o vertical? (ej: H o V): ") #Pendiente de terminar. Se puede meter while para que respuesta sea h o v obligatoriamente.

    inicioBarco=True
    #meto coord.inic y final en el while, solo sales del bucle si has puesto de 1 ficha correctamente o si has puesto correctamente la inic y final de long 2-4. >>>>

    while inicioBarco:
        print("Introduce la coordenada inicial del barco")
        coordenadaInicial=str(input()) 
        coordenadaInicial=validarCoordenada(coordenadaInicial)
        # while coordenadaInicial.lower() not in lista:         #mirar franco convertir en funcion
        #     print("Esa casilla está ocupada o no existe(smh), prueba otra vez: ")
        #     coordenadaInicial=str(input())
        if longitud==1:
            dictDianas[coordenadaInicial.lower()]=(lista.index(coordenadaInicial.lower()))
            lista[lista.index(coordenadaInicial.lower())]="B"
              #si es un barco de 1, al pasar el while que comprueba la casilla dentro del tablero y disponible pues la asigna como "B" y sale de la función.
            inicioBarco=False

# OK, Agárrate Franco, hago lo mismo que en el viejo método:
# Almaceno los indices de coordenada inic y fin en >listaInicioFinal<, las ordeno con sorted(). (posición 0 es el indice mas pequeño y posicion 1 es el grande). Y lo uso para hacer comprobaciones de la distancia que hay entre ambas puntas del barco.
        elif longitud>1:
            # listaInicioFinal=[] #solo para comprobar cosas, 159 y 160 hacen esto
            # listaInicioFinal.append(lista.index(coordenadaInicial.lower()))
            print("Introduce la coordenada final del barco")
            coordenadaFinal=str(input())
            coordenadaFinal=validarCoordenada(coordenadaFinal)
            # while coordenadaFinal.lower() not in lista:
            #     print("Esa casilla está ocupada o no existe(smh), prueba otra vez: ")
            #     coordenadaFinal=str(input())
            # a partir de aqui vamos a comprobar que las posiciones esten a la misma distancia que la longitud
            listaInicioFinal=[]   #//descomentar y quitar lineas 151 y 152
            listaInicioFinal.append(lista.index(coordenadaInicial.lower()))
            listaInicioFinal.append(lista.index(coordenadaFinal.lower()))

            # distancia--> (indice de coordenada final == longitud-1  + indice de la coordenada inicial)
            #aqui tenemos un if para barcos en v y otro para horiz.
            # pero ambos comprueban que el barco sea correcto(la primera y la ultima estén a la distancia adecuada, si es un barco imposible te lleva al else que reinicia TODO el bucle y metes coord.inicio y final de nuevo)
            if disposicionBarco.lower()=="h" and (sorted(listaInicioFinal)[0])+(longitud-1)==sorted(listaInicioFinal)[-1]:
                #este if podria ser una funcion porque se repite 2 veces (casi)
                if lista[sorted(listaInicioFinal)[0]+1]!="B" and lista[sorted(listaInicioFinal)[-1]-1]!="B":
                    for i in range(longitud):
                        dictDianas[lista[sorted(listaInicioFinal)[0]+i]]=(sorted(listaInicioFinal)[0]+i)
                        lista[sorted(listaInicioFinal)[0]+i]="B"
                    inicioBarco=False
                else:
                    print("Son barcos, no transformers, no los pongas encima de otros barcos. Vuelve a intentarlo")

            elif disposicionBarco.lower()=="v" and (sorted(listaInicioFinal)[-1])-sorted(listaInicioFinal)[0]==(longitud-1)*10:
                if lista[sorted(listaInicioFinal)[0]+10]!="B" and lista[sorted(listaInicioFinal)[-1]-10]!="B":
                    for i in range(longitud):
                        dictDianas[lista[sorted(listaInicioFinal)[0]+i*10]]=(sorted(listaInicioFinal)[0]+i*10)
                        lista[sorted(listaInicioFinal)[0]+i*10]="B"
                    inicioBarco=False
                else:
                    print("Son barcos, no transformers, no los pongas encima de otros barcos. Vuelve a intentarlo")


            else:
                print("FAIL! Vuelve a colocar el barco/El barco no cabe ahí, try again.")

def comenzarPartida(lista,lista2,dictDianas1,dictDianas2,listaDisparosJ1,listaDisparosJ2):
    jugar = True
    while jugar:
        turno1=True
        os.system('cls')
        mostrarJuntos(lista,listaDisparosJ1)
        print("Jugador 1: Introduce coordenada donde disparar: ")
        while turno1:
            jugada1=str(input(">"))
            while (jugada1.lower() not in lista2) and (jugada1.lower() not in dictDianas2) :
                print("Apunta mejor, te has salido del tablero. Prueba otra vez: ")
                jugada1=str(input())
            if jugada1.lower() in dictDianas2:
                listaDisparosJ1[listaDisparosJ1.index(jugada1.lower())]="X"
                lista2[dictDianas2[jugada1.lower()]]="X"
                dictDianas2.pop(jugada1.lower())
                print("¡Diana! ",end="")
                if len(dictDianas2) == 0:
                    print("Victoria")
                    jugar=False
                    turno2=False
                else:
                    print("Dispara otra vez")
                
            else:
                listaDisparosJ1[listaDisparosJ1.index(jugada1.lower())]="O"
                print("Agua, no has hecho diana. ")
                input("Press any key to continue.")
                turno1=False

        turno2=True
        os.system('cls')
        mostrarJuntos(lista2,listaDisparosJ2)
        print("Jugador 2: Introduce coordenada donde disparar: ")
        while turno2:
            jugada2=str(input(">"))
            while (jugada2.lower() not in lista) and (jugada2.lower() not in dictDianas1) :
                print("Apunta mejor, te has salido del tablero. Prueba otra vez: ")
                jugada2=str(input())
            if jugada2.lower() in dictDianas1:
                listaDisparosJ2[listaDisparosJ2.index(jugada2.lower())]="X"
                lista[dictDianas1[jugada2.lower()]]="X"
                dictDianas1.pop(jugada2.lower())
                print("Diana! ",end="")
                if len(dictDianas1) == 0:
                    print("Victoria")
                    jugar=False
                else:
                    print("Dispara otra vez")
            else:
                listaDisparosJ2[listaDisparosJ2.index(jugada2.lower())]="O"
                print("Agua, no has hecho diana. ")
                input("Press any key to continue.")
                turno2=False

def mostrarJuntos(listaA,listaB): #no se puede usar la funcion mostrar tablero aqui dentro??? NI idea, es una pregunta.
    auxiliar=0
    listaFila = ["A","B","C","D","E","F","G","H","I","J"]   #esta lista se utilizara para imprimir a principio de linea las letras para el tablero
    x=0     #este auxiliar lo coloco aqui para poder referirme a la posicion de la lista que quiero que se imprima, asi puedo ir imprimiendo las filas
    # print("                           TABLERO MIO                                                      TABLERO ENEMIGO       ")
    # print("\n")
    print("           ",end="")
    for i in range(10):
        print("  ",i+1,end=" ")
    print("            ",end="")
    for i in range(10):
        print("  ",i+1,end=" ")
    print("\n")
    
    for i in range(101):
        # if i%numero == 0:
        #     print("\n")
        if i == 0 or i%10 == 0:
            print ("          ",listaFila[x],end=" ")    
            if i>0 and i%10 == 0: 
                for j in range(10):
                    if listaB[j+auxiliar] == "B":
                        print("|B|",end="  ")
                    elif listaB[j+auxiliar] == "X":
                        print("|X|",end="  ")
                    elif listaB[j+auxiliar] == "O":
                        print("|O|",end="  ")
                    else:
                        print("|_|",end="  ")
                print("\n")
                x+=1            #aqui incrementando la variable de fila para ir a la siguiente letra
                auxiliar+=10
                if x<10:
                    print("          ",listaFila[x],end=" ")
        if i < 100:
            if listaA[i] == "B":
                print("|B|",end="  ")
            elif listaA[i] == "X":
                print("|X|",end="  ")
            elif listaA[i] == "O":
                print("|O|",end="  ")
            else:
                print("|_|",end="  ")
    


def mostrarMenu(lista,lista2):
    global contadorjugador1
    global contadorjugador2
    menuOn = True
    while menuOn:
        # print("¿Qué quieres hacer?")
        print("1: Ver tablero primer jugador \n2: Colocar barco primer jugador \n3: Ver tablero segundo jugador \n4: Colocar barco segundo jugador \n5: Jugar  \n6: Salir" )
        opcion=int(input())
        if opcion == 1:
            mostrarTablero(lista)
        if opcion == 2:
            if contadorjugador1 == 8:#15/12/2020  limita la cantidad de barcos a colocar, si pasa de 8 no te deja entrar.
                print("Ya has colocado todos los barcos.")
            else:
                evaluarBarcos(lista,opcion,dictDianas1)
                contadorjugador1+=1
        if opcion == 3:         #15/12/2020   he creado dos opciones mas para crear segundo tablero. gracias a pasarle tablero a lista2 sabe a cual me estoy refiriendo.

            mostrarTablero(lista2)
        if opcion == 4:
            if contadorjugador2 == 8:
                print("Ya has colocado todos los barcos")
            else:
                evaluarBarcos(lista2,opcion,dictDianas2)#15/12/2020 colocar barco en lista2 va a haber que mirarlo con cuidado, ya que utiliza los mismo contadores que jugador uno, por ahora... hay dos opciones: mirar como pasarle y reiniciar los contadores y que los tenga en cuenta por dentro cada vez(parece mas complicado, pero mas elegante), o repetir el codigo completo con otro nombre para colocar barcos(parece lo mas facil,pero menos elegante) ---- por ahora he hecho la segunda opción, asi mientras lo vamos terminando. nos acabamos refiriendo a los segundos contadores gracias tanto a la lista que se le pasa como a la opcion escogida en el menu( que tambien se le pasa).
                contadorjugador2+=1
        if opcion==5 :
            comenzarPartida(lista,lista2,dictDianas1,dictDianas2,listaDisparosJ1,listaDisparosJ2)
            # if contadorjugador1==8 and contadorjugador2==8:
                # comenzarPartida(dictDianas1,dictDianas2)
            # else:
            #     print("Todavia no habeis(puto enrique y el idioma) colocado todos los barcos")
            menuOn = False
        if opcion == 6:
            menuOn = False
        if opcion== 7:
            mostrarJuntos(lista,lista2)

mostrarBienvenida()
hacerTablero(lista,listaLetras)
hacerTablero(lista2,listaLetras)

hacerTablero(listaDisparosJ1,listaLetras)
hacerTablero(listaDisparosJ2,listaLetras)#hacer funcion o enchufar esta asignacion dentro de otra funcion como hacer tablero o jugarr(se empieza a utilizar cuando se empieza a disparar y se usara tambien en mostrarJuntos mientras se juega). Quiero dos tableros vacios(con las 100 posiciones dentro) para almacenar los aciertos y fallos de cada jugador y mostrarselos mientras juega.

mostrarMenu(lista,lista2)
