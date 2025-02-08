def matriz_inversa():
    try:
        print("Ingrese las dimensiones del arreglo que desea invertir.")
        
        while True:
            try:
                filas = int(input(">> Ingrese la cantidad de filas: \n"))
                columnas = int(input(">> Ingrese la cantidad de columnas: \n"))
                if filas <= 0 or columnas <= 0:
                    print("El número de filas y columnas debe ser mayor que 0. Intente nuevamente.")
                    continue
                if filas != columnas:  
                    print("Para poder calcular la inversa, la matriz debe ser cuadrada (mismo número de filas y columnas).")
                    continue
                break
            except ValueError:
                print("Error: Por favor ingrese un número entero válido para las dimensiones.")
        
        matriz = [[0] * columnas for _ in range(filas)]
        
        for i in range(filas):
            for j in range(columnas):
                while True:
                    try:
                        valor = int(input(f">> Ingrese el valor para la posición ({i}, {j}): "))
                        matriz[i][j] = valor
                        break
                    except ValueError:
                        print("Error: Por favor ingrese un número entero válido para los elementos de la matriz.")
        
        matriz_invertida = [[0] * columnas for _ in range(filas)]
        for i in range(len(matriz)-1, -1, -1):
            for j in range(len(matriz[i])-1, -1, -1):
                matriz_invertida[filas-1-i][columnas-1-j] = matriz[i][j]
        
        print("\nMatriz original:")
        for fila in matriz:
            print(fila)

        print("\nMatriz invertida:")
        for fila in matriz_invertida:
            print(fila)

    except Exception as e:
        print(f"Error inesperado: {e}")

matriz_inversa()
