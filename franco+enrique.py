import os
os.system('cls')
#commit
lista=[]
listaDisparosJ1=[]
dictDianas1={}
dictDianas2={} #o contador al num de dianas para ganar o listaDianas.pop/remove>len.lista==0
#si convierto listasDianas en diccionarios, puedo almacenar A1:INDICE(=0) y cuando el enemigo hace diana, uso el indice como referencia para cambiar mi tablero con una X y lo borro para seguir contando hasta 0 y ver quien gana.

lista2=[]     # lista declarada para pasarsela al jugador 2.
listaDisparosJ2=[]
listaLetras=["a","b","c","d","e","f","g","h","i","j"]
numero=10
contadorJugador1=0
contadorJugador2=0  #15/12/2020  variable declarada para limitar barcos jugador 2
contadorBarco1 = contadorBarco2 = contadorBarco3 = contadorBarco4 = 0
contadorBarco5 = contadorBarco6 = contadorBarco7 = contadorBarco8 = 0 #segunda declaración de variables para referirnos a la cantidad de barcos del jugador 2
def bienvenida():
    print("---------------------------------------------------------------------")
    # print(chr(27)+"[1;33m")
    print("+++++++++++++++++ Bienvenido a Battleship en Python +++++++++++++++++")
    print("---------------------------------------------------------------------")
    print("++++++++++++++++++++++++++tablero de 10x10 ++++++++++++++++++++++++++")#<3
    print("\n")

def hacerTablero(lista,listaLetras):
    for i in listaLetras:
        for j in range(1,numero+1):
            lista_posiciones = (i+str(j))   # aqui convertimos la cadena de 1-10 a str para poder referirnos a la posicion en el tablero de forma visual
            lista.append(lista_posiciones)
    # print(lista)#print extra para ver la lista mientras trabajamos en el código

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

def colocarBarco(lista,opcion,dictDianas):
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
                llamarBarco(lista,longitud,dictDianas)
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if longitud == 2 and contadorBarco2 <= 2: #aqui se evalua la cantidad de barcos colocados, permitimos 2 barcos de 1
            if contadorBarco2 == 2:
                print("Ya has colocado todo los barcos de esta medida.")
            else:
                contadorBarco2+=1       #******** aqui ira una vez la llamada en caso de poder ser
                llamarBarco(lista,longitud,dictDianas)
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if longitud == 3 and contadorBarco3 <= 2: #aqui se evalua la cantidad de barcos colocados, permitimos 2 barcos de 1
            if contadorBarco3 == 2:
                print("Ya has colocado todo los barcos de esta medida.")
            else:
                contadorBarco3+=1       #******** aqui ira una vez la llamada en caso de poder ser
                llamarBarco(lista,longitud,dictDianas)
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if longitud == 4 and contadorBarco4 <= 2: #aqui se evalua la cantidad de barcos colocados, permitimos 2 barcos de 1
            if contadorBarco4 == 2:
                print("Ya has colocado todo los barcos de esta medida.")
            else:
                contadorBarco4+=1       #******** aqui ira una vez la llamada en caso de poder ser
                llamarBarco(lista,longitud,dictDianas)
    
    
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
                llamarBarco(lista,longitud,dictDianas)
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if longitud == 2 and contadorBarco6 <= 2: 
            if contadorBarco6 == 2:
                print("Ya has colocado todo los barcos de esta medida.")
            else:
                contadorBarco6+=1       
                llamarBarco(lista,longitud,dictDianas)
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if longitud == 3 and contadorBarco7 <= 2: 
            if contadorBarco7 == 2:
                print("Ya has colocado todo los barcos de esta medida.")
            else:
                contadorBarco7+=1       #******** aqui ira una vez la llamada en caso de poder ser
                llamarBarco(lista,longitud,dictDianas)
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if longitud == 4 and contadorBarco8 <= 2: #aqui se evalua la cantidad de barcos colocados, permitimos 2 barcos de 1
            if contadorBarco8 == 2:
                print("Ya has colocado todo los barcos de esta medida.")
            else:
                contadorBarco8+=1       #******** aqui ira una vez la llamada en caso de poder ser
                llamarBarco(lista,longitud,dictDianas)
    
    return lista            #informarse sobre si la devolucion de cuenta1 incrementa

def llamarBarco(lista,longitud,dictDianas):       #comentalo enrique!
    if longitud==1:
        disposicionBarco=None #no hace falta usar vert/horiz para los de 1
    elif longitud>1:
        disposicionBarco=input("¿Colocar barco en horizontal o vertical? (ej: H o V): ") #Pendiente de terminar. Se puede meter while para que respuesta sea h o v obligatoriamente.

    inicioBarco=True
    #meto coord.inic y final en el while, solo sales del bucle si has puesto de 1 ficha correctamente o si has puesto correctamente la inic y final de long 2-4. >>>>

    while inicioBarco:
        print("Introduce la coordenada inicial del barco")
        coordenadaInicial=str(input())
        while coordenadaInicial.lower() not in lista:         #mirar franco convertir en funcion
            print("Esa casilla está ocupada o no existe(smh), prueba otra vez: ")
            coordenadaInicial=str(input())
        if longitud==1:
            # listaDianas.append(lista[lista.index(coordenadaInicial.lower())])
            dictDianas[coordenadaInicial.lower()]=(lista.index(coordenadaInicial.lower()))
            lista[lista.index(coordenadaInicial.lower())]="B"
            print(dictDianas)
              #si es un barco de 1, al pasar el while que comprueba la casilla dentro del tablero y disponible pues la asigna como "B" y sale de la función.
            inicioBarco=False


# OK, Agárrate Franco, hago lo mismo que en el viejo método:
# Almaceno los indices de coordenada inic y fin en >listaInicioFinal<, las ordeno con sorted(). (posición 0 es el indice mas pequeño y posicion 1 es el grande). Y lo uso para hacer comprobaciones de la distancia que hay entre ambas puntas del barco.
        elif longitud>1:
            listaInicioFinal=[] #solo para comprobar cosas, 159 y 160 hacen esto
            listaInicioFinal.append(lista.index(coordenadaInicial.lower()))
            print("Introduce la coordenada final del barco")
            coordenadaFinal=str(input())
            while coordenadaFinal.lower() not in lista:
                print("Esa casilla está ocupada o no existe(smh), prueba otra vez: ")
                coordenadaFinal=str(input())
            # a partir de aqui vamos a comprobar que las posiciones esten a distancia de longitud
            # listaInicioFinal=[]   //descomentar y quitar lineas 151 y 152
            # listaInicioFinal.append(lista.index(coordenadaInicial.lower()))
            
            listaInicioFinal.append(lista.index(coordenadaFinal.lower()))
            print(listaInicioFinal)  #para ver qué hace el codigo, no es necesario el print.

            # distancia--> (indice de coordenada final == longitud-1  + indice de la coordenada inicial)
            #aqui tenemos un if para barcos en v y otro para horiz.
            # pero ambos comprueban que el barco sea correcto(la primera y la ultima estén a la distancia adecuada, si es un barco imposible te lleva al else que reinicia TODO el bucle y metes coord.inicio y final de nuevo)
            if disposicionBarco.lower()=="h" and (sorted(listaInicioFinal)[0])+(longitud-1)==sorted(listaInicioFinal)[-1]: 
                #este if podria ser una funcion porque se repite 2 veces (casi)
                if lista[sorted(listaInicioFinal)[0]+1]!="B" and lista[sorted(listaInicioFinal)[-1]-1]!="B":
                    for i in range(longitud):
                        # listaDianas.append(lista[sorted(listaInicioFinal)[0]+i])
                        dictDianas[lista[sorted(listaInicioFinal)[0]+i]]=(sorted(listaInicioFinal)[0]+i)
                        lista[sorted(listaInicioFinal)[0]+i]="B"
                    inicioBarco=False
                else:
                    print("Son barcos, no transformers, no los pongas encima de otros barcos. Vuelve a intentarlo")

            elif disposicionBarco.lower()=="v" and (sorted(listaInicioFinal)[-1])-sorted(listaInicioFinal)[0]==(longitud-1)*10:
                if lista[sorted(listaInicioFinal)[0]+10]!="B" and lista[sorted(listaInicioFinal)[-1]-10]!="B":
                    for i in range(longitud):
                        # listaDianas.append(lista[sorted(listaInicioFinal)[0]+i*10])
                        dictDianas[lista[sorted(listaInicioFinal)[0]+i*10]]=(sorted(listaInicioFinal)[0]+i*10)
                        lista[sorted(listaInicioFinal)[0]+i*10]="B"
                    inicioBarco=False
                else:
                    print("Son barcos, no transformers, no los pongas encima de otros barcos. Vuelve a intentarlo")


            else:
                print("FAIL! Vuelve a colocar el barco/El barco no cabe ahí, try again.")


# //////////////////////////////////////////////////////////////
    # CODIGO DEL MÉTODO ANTERIOR, MANTENER PORQUE REUTILIZO COSAS!!!
    #     while longitud==2 and i==0 and (lista[lista.index(coordenadaBarco.lower())+1]=="B" and lista[lista.index(coordenadaBarco.lower())-1]=="B"):
    #         coordenadaBarco=str(input("Noob, el barco no cabe, prueba en otro sitio: "))
    #         #METER FUNCION COMPARAR SI CASILLA VALIDA OTRA VEZ.
    #         while coordenadaBarco.lower() not in lista:
    #             print("Esa casilla está ocupada o no existe(smh), prueba otra vez: ")
    #             coordenadaBarco=str(input())
    #     while longitud==3 and i==0 and (lista[lista.index(coordenadaBarco.lower())+1]=="B" and lista[lista.index(coordenadaBarco.lower())-1]=="B") or (lista[lista.index(coordenadaBarco.lower())+2]=="B" and (lista[lista.index(coordenadaBarco.lower())-1]=="B") and (lista[lista.index(coordenadaBarco.lower())-2]=="B" and lista[lista.index(coordenadaBarco.lower())+1]=="B")):
    #         coordenadaBarco=str(input("Noob, el barco no cabe, prueba en otro sitio: "))
    #         #acho mi puta vida en bicicleta sería mas facil, 
    #         #METER FUNCION COMPARAR SI CASILLA VALIDA OTRA VEZ.
    #         while coordenadaBarco.lower() not in lista:
    #             print("Esa casilla está ocupada o no existe(smh), prueba otra vez: ")
    #             coordenadaBarco=str(input())

    #     if i==0:
    #         listaCoordenadas.append(lista.index(coordenadaBarco.lower()))
    #     if longitud>1 and disposicionBarco=="H" or disposicionBarco=="h": 
    #     # ////////////////////////////
    #     #He tenido que usar una funcion de listas llamada sorted() para que la lista que contiene las coordenadas de los barcos de longitud 2-4 esté ordenada de menor a mayor numero y tomen como referencia las contiguas a las esquinas, sumando +1/+10(es decir comprobar la casilla a la derecha) a la posicion [-1] que tras hacer un sorted siempre será el indice mas a la derecha o mas abajo y sumando -1/-10 a la posicion [0] que siempre será el indice mas pequeño
    #     # ///////////////////////////
    #     #HACER FUNCION DEL WHILE? pero seguro que las variables dejan de mantener los datos...........
    #         while (i>0) and (lista.index(coordenadaBarco.lower())!=(sorted(listaCoordenadas)[0])-1 and lista.index(coordenadaBarco.lower())!=(sorted(listaCoordenadas)[-1])+1):
    #             coordenadaBarco=str(input("¡Las casillas deben ser contiguas! Prueba otra vez: "))
    #             print(lista, listaCoordenadas)
    #             print(coordenadaBarco)
    #             while coordenadaBarco.lower() not in lista:
    #                 print("Esa casilla está ocupada o no existe(smh), prueba otra vez: ")
    #                 coordenadaBarco=str(input())
    #             print(coordenadaBarco)
    #     elif longitud>1 and disposicionBarco=="V" or disposicionBarco=="v":
    #         while (i>0) and (lista.index(coordenadaBarco.lower())!=(sorted(listaCoordenadas)[0])-10 and lista.index(coordenadaBarco.lower())!=(sorted(listaCoordenadas)[-1])+10):
    #             coordenadaBarco=str(input("¡Las casillas deben ser contiguas! Prueba otra vez: "))
    #             print(lista, listaCoordenadas)
    #             print(coordenadaBarco)
    #             while coordenadaBarco.lower() not in lista: #pasar esto a funcion
    #                 print("Esa casilla está ocupada o no existe(smh), prueba otra vez: ")
    #                 coordenadaBarco=str(input())
    #             print(coordenadaBarco)
    #     if i>0 and longitud>1:
    #         listaCoordenadas.append(lista.index(coordenadaBarco.lower()))
    #     lista[lista.index(coordenadaBarco.lower())]="B"
    #     i+=1
    # print(lista)#print extra para ver la lista mientras trabajamos en el código    
# //////////////////////////////////////////////////////

def jugar(lista,lista2,dictDianas1,dictDianas2,listaDisparosJ1,listaDisparosJ2):
    jugar = True
    while jugar:
        turno1=True
        print("jugador 1: introduce coordenada donde disparar: ")
        while turno1:
            mostrarJuntos(lista,listaDisparosJ1)
            jugada1=str(input())
            while (jugada1.lower() not in lista2) and (jugada1.lower() not in dictDianas2) :         #mirar franco convertir en funcion
                print("Apunta mejor, te has salido del tablero. Prueba otra vez: ")
                jugada1=str(input())
            if jugada1.lower() in dictDianas2:
                listaDisparosJ1[listaDisparosJ1.index(jugada1.lower())]="X"
                lista2[dictDianas2[jugada1.lower()]]="X"
                dictDianas2.pop(jugada1.lower())
                print("¡Diana! ",end="")
                # print("tablero disparos1") QUITAR
                # print(listaDisparosJ1) QUITAR
                # mostrarTablero(listaDisparosJ1)  QUITAR, SOLO PRUEBAS!!
                if len(dictDianas2) == 0:
                    print("Victoria")
                    jugar=False
                    turno2=False
                else:
                    print("Dispara otra vez")
                
            else:
                listaDisparosJ1[listaDisparosJ1.index(jugada1.lower())]="O"
                print("Agua, no has hecho diana. ")
                turno1=False

        turno2=True
        print("jugador 2: introduce coordenada donde disparar: ")
        while turno2:
            mostrarJuntos(lista2,listaDisparosJ2)
            jugada2=str(input())
            while (jugada2.lower() not in lista) and (jugada2.lower() not in dictDianas1) :         #mirar franco convertir en funcion
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
                turno2=False
            mostrarTablero(listaDisparosJ2)

def mostrarJuntos(listaA,listaB): #no se puede usar la funcion mostrar tablero aqui dentro??? NI idea, es una pregunta.
    auxiliar=0
    listaFila = ["A","B","C","D","E","F","G","H","I","J"]   #esta lista se utilizara para imprimir a principio de linea las letras para el tablero
    x=0     #este auxiliar lo coloco aqui para poder referirme a la posicion de la lista que quiero que se imprima, asi puedo ir imprimiendo las filas
    for i in range(10):
        print("  ",i+1,end=" ")
    print(" ",end="")
    for i in range(10):
        print("  ",i+1,end=" ")
    print("\n")
    
    for i in range(101):
        # if i%numero == 0:
        #     print("\n")
        if i == 0 or i%10 == 0:
            print (listaFila[x],end=" ")    
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
                    print(listaFila[x],end=" ")
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
    global contadorJugador1
    global contadorJugador2
    menuOn = True
    while menuOn:
        print("¿Qué quieres hacer?")
        print("1: Ver tablero primer jugador \n2: Colocar barco primer jugador \n3: ver tablero segundo jugador \n4: colocar barco segundo jugador \n5: jugar  \n6: salir" )
        opcion=int(input())
        if opcion == 1:
            mostrarTablero(lista)
        if opcion == 2:
            if contadorJugador1 == 8:#15/12/2020  limita la cantidad de barcos a colocar, si pasa de 8 no te deja entrar.
                print("ya has colocado todos los barcos.")
            else:
                colocarBarco(lista,opcion,dictDianas1)
                contadorJugador1+=1
        if opcion == 3:         #15/12/2020   he creado dos opciones mas para crear segundo tablero. gracias a pasarle tablero a lista2 sabe a cual me estoy refiriendo.

            mostrarTablero(lista2)
        if opcion == 4:
            if contadorJugador2 == 8:
                print("ya has colocado todos los barcos")
            else:
                colocarBarco(lista2,opcion,dictDianas2)#15/12/2020 colocar barco en lista2 va a haber que mirarlo con cuidado, ya que utiliza los mismo contadores que jugador uno, por ahora... hay dos opciones: mirar como pasarle y reiniciar los contadores y que los tenga en cuenta por dentro cada vez(parece mas complicado, pero mas elegante), o repetir el codigo completo con otro nombre para colocar barcos(parece lo mas facil,pero menos elegante) ---- por ahora he hecho la segunda opción, asi mientras lo vamos terminando. nos acabamos refiriendo a los segundos contadores gracias tanto a la lista que se le pasa como a la opcion escogida en el menu( que tambien se le pasa).
                contadorJugador2+=1
        if opcion==5 :
            jugar(lista,lista2,dictDianas1,dictDianas2,listaDisparosJ1,listaDisparosJ2)
            # if contadorJugador1==8 and contadorJugador2==8:
                # jugar(dictDianas1,dictDianas2)
            # else:
            #     print("Todavia no habeis(puto enrique y el idioma) colocado todos los barcos")
            menuOn = False
        if opcion == 6:
            menuOn = False
        if opcion== 7:
            mostrarJuntos(lista,lista2)

bienvenida()
hacerTablero(lista,listaLetras)
hacerTablero(lista2,listaLetras)

hacerTablero(listaDisparosJ1,listaLetras)
hacerTablero(listaDisparosJ2,listaLetras)#hacer funcion o enchufar esta asignacion dentro de otra funcion como hacer tablero o jugar(se empieza a utilizar cuando se empieza a disparar y se usara tambien en mostrarJuntos mientras se juega). Quiero dos tableros vacios(con las 100 posiciones dentro) para almacenar los aciertos y fallos de cada jugador y mostrarselos mientras juega.

mostrarMenu(lista,lista2)
