##By Fernando Socasi

def crear_arreglo(tamano):
    if tamano <=0:
        raise ValueError("El tamaño del arreglo debe ser de un numero entero positivo")
    arreglo = [0]* tamano
    for i in range(tamano):
        arreglo[i]=int(input(f"Ingrese el número para la posicion {i+1}:"))
    return arreglo

def calcular_promedio(arreglo):
    suma = 0
    contador = 0
    for numero in arreglo:
        suma += numero
        contador += 1
    if contador == 0:
        return 0 
    return suma / contador

def imprimir_arreglo(arreglo):
    print("Arreglo:", end=" ")
    for numero in arreglo:
        print(numero, end=" ")
    print() 

def main():
    tamano = int(input("Ingrese el tamaño del arreglo: "))
    arreglo = crear_arreglo(tamano)
    imprimir_arreglo(arreglo)
    promedio = calcular_promedio(arreglo)
    print("El promedio es:", promedio)

if _name_ == "_main_":
    main()