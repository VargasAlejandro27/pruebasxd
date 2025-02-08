#EJERICIO 2 

def numero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error al convertir, solo ingrese números.")

def crear_matriz(nombre_matriz):
    filas = numero(f"Ingrese la cantidad de filas para la matriz {nombre_matriz}: ")
    columnas = numero(f"Ingrese la cantidad de columnas para la matriz {nombre_matriz}: ")
    matriz = [[0 for _ in range(columnas)] for _ in range(filas)]
    for fila in range(filas):
        for columna in range(columnas):
            matriz[fila][columna] = numero(f"Ingrese el valor de la matriz {nombre_matriz} en la posición ({fila}, {columna}): ")
    return matriz

def imprimirmatriz(matriz):
    for fila in matriz:
        print (fila)

def encontrarminymax(matriz):
    # Inicializamos minimo y maximo con el primer elemento de la matriz
    minimo = matriz[0][0]
    maximo = matriz[0][0]
    for fila in matriz:
        for numero in fila:
            if numero < minimo:
                minimo = numero
            if numero > maximo:
                maximo = numero
    return minimo, maximo

nombre_matriz = "A"
matriz = crear_matriz(nombre_matriz)
print("\nMatriz generada:")
imprimirmatriz(matriz)

minimo, maximo = encontrarminymax(matriz)
print(f"\nNúmero más pequeño en la matriz: {minimo}")
print(f"Número más grande en la matriz: {maximo}")





