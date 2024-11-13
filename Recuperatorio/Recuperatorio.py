import random
from os import system

COL_NUMERO_LISTA=0
COL_VOTOS_MAÑANA=1
COL_VOTOS_TARDE=2
COL_VOTOS_NOCHE=3
COL_PORCENTAJE=4

def inicializar_matriz(cant_filas: int, cant_columnas: int, valor_inicial) -> list:
    matriz = []
    for i in range(cant_filas):
        fila = [valor_inicial] * cant_columnas
        matriz += [fila]
    return matriz

def cargar_votos(matriz_votos):
#funcion para ingresar los datos de las listas y la cantidad de votos
    for i in range(len(matriz_votos)):
        numero_lista = int(input("Ingrese numero de lista (3 cifras): "))
        while numero_lista<100 or numero_lista >999 :
            print("Error: Debe tener 3 cifras.")
            numero_lista = int(input("Ingrese numero de lista (3 cifras): "))
        
        
        votos_mañana = int(input("Ingrese la cantidad de votos del turno mañana: "))
        while  votos_mañana <0:
            print("Error: Debe ser un numero entero y positivo.")
            votos_mañana = int(input("Ingrese la cantidad de votos del turno mañana: "))
        
        
        votos_tarde = int(input("Ingrese la cantidad de votos del turno tarde: "))
        while votos_tarde <0:
            print("Error: Debe ser un numero entero y positivo.")
            votos_tarde = int(input("Ingrese la cantidad de votos del turno tarde: "))

        votos_noche = int(input("Ingrese la cantidad de votos del turno noche: "))
        while votos_noche <0:
            print("Error: Debe ser un numero entero y positivo.")
            votos_noche = int(input("Ingrese la cantidad de votos del turno noche: "))

        
        matriz_votos[i][COL_NUMERO_LISTA] = numero_lista
        matriz_votos[i][COL_VOTOS_MAÑANA] = votos_mañana
        matriz_votos[i][COL_VOTOS_TARDE] = votos_tarde
        matriz_votos[i][COL_VOTOS_NOCHE] = votos_noche

    calcular_porcentajes(matriz_votos)
    
def calcular_porcentajes(matriz_votos):
    # Calcular porcentaje de votos
    total_votos = 0
    for i in range(len(matriz_votos)):
        total_votos += matriz_votos[i][COL_VOTOS_MAÑANA] + matriz_votos[i][COL_VOTOS_TARDE] + matriz_votos[i][COL_VOTOS_NOCHE]
    

    for i in range(len(matriz_votos)):
        total_lista = matriz_votos[i][COL_VOTOS_MAÑANA] + matriz_votos[i][COL_VOTOS_TARDE] + matriz_votos[i][COL_VOTOS_NOCHE]
        if total_votos > 0:
            porcentaje = (total_lista / total_votos) * 100
        else:
            porcentaje = 0
        matriz_votos[i][COL_PORCENTAJE] = porcentaje



def mostrar_votos(lista: list) -> list:
#mostrar resultado de todas las listas
    print("---")
    for fil in range(len(lista)):

        print(f"Numero de lista: {lista[fil][COL_NUMERO_LISTA]}")
        print(f"Votos turno mañana: {lista[fil][COL_VOTOS_MAÑANA]}")
        print(f"Votos turno tarde: {lista[fil][COL_VOTOS_TARDE]}")
        print(f"Votos turno noche: {lista[fil][COL_VOTOS_NOCHE]}")
        print(f"El porcentaje de votos es del {lista[fil][COL_PORCENTAJE]}%")
        print("----------")


def ordenar_mayor_menor(matriz_votos, columna) -> bool:
#ordena la columna que quieras de mayor a menor
    for fil_i in range(len(matriz_votos)-1):
        for fil_j in range(fil_i + 1,len(matriz_votos)):
        
            if matriz_votos[fil_i][columna] < matriz_votos[fil_j][columna]:
            
                aux = matriz_votos[fil_i]
                matriz_votos[fil_i] = matriz_votos[fil_j]
                matriz_votos[fil_j] = aux

def mostrar_turno_mas_votado(matriz_votos):
    #el turno que mas votos recibio entre todas las listas
    total_mañana=0
    total_tarde=0
    total_noche=0

    for i in range(len(matriz_votos)):
        total_mañana+= matriz_votos[i][COL_VOTOS_MAÑANA]
        total_tarde+= matriz_votos[i][COL_VOTOS_TARDE]
        total_noche+= matriz_votos[i][COL_VOTOS_NOCHE]
    
    if total_mañana>=total_tarde and total_mañana>=total_noche:
        print("El turno donde mas se voto es el turno mañana")
    if total_tarde>=total_mañana and total_tarde>=total_noche:
        print("El turno donde mas se voto es el turno tarde")   
    if total_noche>=total_tarde and total_noche>=total_mañana:
        print("El turno donde mas se voto es el turno noche")

def mostrar_no_te_voto_nadie(matriz_votos):
    #los que recibieron menos del 5% de los votos
    total_votos = 0
    for i in range(len(matriz_votos)):
        total_votos += matriz_votos[i][COL_VOTOS_MAÑANA] + matriz_votos[i][COL_VOTOS_TARDE] + matriz_votos[i][COL_VOTOS_NOCHE]
    bandera=False
    print("Las listas que recibieron menos del 5% de los votos:")
    for i in range(len(matriz_votos)):
        total_lista = matriz_votos[i][COL_VOTOS_MAÑANA] + matriz_votos[i][COL_VOTOS_TARDE] + matriz_votos[i][COL_VOTOS_NOCHE]
        
        if total_votos > 0:
            porcentaje = (total_lista / total_votos) * 100
        else:
            porcentaje = 0
            
        matriz_votos[i][COL_PORCENTAJE] = porcentaje
        
#verificar cuales recibieron menos del 5% de votos
        if porcentaje < 5:
            print(f"Lista {matriz_votos[i][COL_NUMERO_LISTA]} con {porcentaje}% de los votos")
            bandera=True

    if bandera==False:
        print("Ninguna lista tiene menos del 5%")

        


def hacer_ballotage(matriz_votos):
    #calcular el total de votos de la primera vuelta
    total_votos = 0
    for i in range(len(matriz_votos)):
        total_votos += (matriz_votos[i][COL_VOTOS_MAÑANA] + matriz_votos[i][COL_VOTOS_TARDE] +  matriz_votos[i][COL_VOTOS_NOCHE])

    #ordenar la matriz para tener a los dos candidatos mas votados al principio
    ordenar_mayor_menor(matriz_votos, COL_PORCENTAJE)
    
    #verificar si el candidato con mas votos supera el 50%
    if (matriz_votos[0][COL_PORCENTAJE] > 50):
        print(f"No hay Ballotage, el ganador es la lista {matriz_votos[0][COL_NUMERO_LISTA]}")
    else:
        print("Hay Ballotage")
        #la cantidad de votos en total
        votos_totales_segunda_vuelta = 0
        for i in range(len(matriz_votos)):
            votos_totales_segunda_vuelta += (matriz_votos[i][COL_VOTOS_MAÑANA] + matriz_votos[i][COL_VOTOS_TARDE] +  matriz_votos[i][COL_VOTOS_NOCHE])
        
        #votos aleatorios de la segunda vuelta
        candidato_1 = random.randint(0, votos_totales_segunda_vuelta)
        candidato_2 = votos_totales_segunda_vuelta - candidato_1

        # mostrar el ganador de la segunda vuelta
        if candidato_1 > candidato_2:
            print(f"Ganador por Ballotage es la lista {matriz_votos[0][COL_NUMERO_LISTA]}")
        else:
            print(f"Ganador por Ballotage es la lista {matriz_votos[1][COL_NUMERO_LISTA]}")


def pausar():
    system("pause")

def limpiar_pantalla():
    system("cls")

def ejecutar_menu():
    matriz_votos = inicializar_matriz(2, 5, 0)
    votos_cargados = False
    while True:
        
        limpiar_pantalla()

        print("--- Menu ---")
        print("1. Cargar Votos")
        print("2. Mostrar Votos")
        print("3. Ordenar votos turno mañana")
        print("4. No te voto nadie")
        print("5. Turno en el que mas se voto")
        print("6. Ballotage")
        print("7. Salir")
        
        opcion = input("Elegir opcion (1-7): ")
        
        if opcion == '1':
            cargar_votos(matriz_votos)
            votos_cargados=True 
        elif (opcion == "2" and votos_cargados == False) or (opcion == "3" and votos_cargados == False) or (opcion == "4" and votos_cargados == False) or (opcion == "5" and votos_cargados == False) or (opcion == "6" and votos_cargados == False):
            print("Primero debes cargar los votos")
        elif opcion == '2':
            mostrar_votos(matriz_votos)
        elif opcion == '3':
            ordenar_mayor_menor(matriz_votos, COL_VOTOS_MAÑANA)
            mostrar_votos(matriz_votos)
        elif opcion == '4':
            mostrar_no_te_voto_nadie(matriz_votos)
        elif opcion == '5':
            mostrar_turno_mas_votado(matriz_votos)
        elif opcion == '6':
            hacer_ballotage(matriz_votos)
        elif opcion =='7':
            print("Fin del programa")
            break
        else:
            print("Ingresar una opcion valida.")

        pausar()


ejecutar_menu()
