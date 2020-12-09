
def crearTablero(num,listaTab):
    for i in range(num):
        print("\n")
        for j in range(num):
            print("|_|",end="")
            posicion=[i],[j]
            listaTab.append(posicion)
    print("\n")        


def introducirCoordenada(lista):
    print("vamos a colocar el barco de 4")
    print("Introduce coordenada para colocar el barco con los numeros seguidos, por ejemplo, si quieres colocarlos en la posicion fila 1, columna 1, escribe: 11")  
    contador=0
    while contador < 4:
        print("Introduce ",contador+1,"coordenada: ")
        posiBarco=int(input())
        lista[posiBarco] = "B"
        contador+=1
    print(lista)

numero=int(input("Introduce un numero para filas y columnas: "))
lista=[]
posicion =[],[]
crearTablero(numero,lista)
introducirCoordenada(lista)
imprimeConBarco(lista)
# colocarBarco(lista,posicion)
# print(lista)