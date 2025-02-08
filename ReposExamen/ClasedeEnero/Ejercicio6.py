def obtener_pares(arreglo):
    return [num for num in arreglo if num % 2 == 0]

def obtener_impares(arreglo):
    return [num for num in arreglo if num % 2 != 0]

def crear_arreglo():
    arreglo = []
    while True:
        try:
            tamano = int(input(">> ¿Cuántos elementos tendrá el arreglo? "))
            if tamano <= 0:
                print("El tamaño del arreglo debe ser mayor que 0. Intente nuevamente.")
                continue
            break
        except ValueError:
            print("Error: Por favor ingrese un número entero válido para el tamaño del arreglo.")

    for i in range(tamano):
        while True:
            try:
                valor = int(input(f">> Ingrese el valor para el elemento {i+1}: "))
                arreglo.append(valor)
                break
            except ValueError:
                print("Error: Por favor ingrese un número entero válido para el valor.")
    return arreglo

def imprimir_arreglo(arreglo):
    print("\nArreglo:")
    for num in arreglo:
        print(num)

def main():
    try:
        print("Creando el arreglo...")
        arreglo = crear_arreglo()
        imprimir_arreglo(arreglo)

        arreglo_pares = obtener_pares(arreglo)
        arreglo_impares = obtener_impares(arreglo)

        print("\nNúmeros pares en el arreglo:")
        imprimir_arreglo(arreglo_pares)

        print("\nNúmeros impares en el arreglo:")
        imprimir_arreglo(arreglo_impares)

    except Exception as e:
        print(f"Error inesperado: {e}")

main()
