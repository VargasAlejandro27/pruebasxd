#ejercicio 4 

def numero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error al convertir, solo ingrese números.")

def creararreglo():
    tamano = numero ("Ingrese el tamaño del arreglo: ")
    while tamano <= 0:
        print ("El tamaño del arreglo tiene que ser un numero positivo")
        tamano = numero ("Ingrese el tamaño del arreglo: ")
    arreglo = [0]*tamano

    for i in range (tamano):
        valor = numero (f"Ingrese el valor para la posicion {i}: ")
        arreglo[i]= valor
    return arreglo

def imprimirarreglo (arreglo):
    print("El arreglo es:", arreglo)

def contar(arreglo, numero):
    contador = 0
    for elemento in arreglo:
        if elemento== numero:
            contador+=1
    return contador

print("Bienvenido al contador :D")

arreglo= creararreglo()
imprimirarreglo (arreglo)

buscador= numero("ingrese el numero que desea buscar en el arreglo: ")
numeroigual=contar(arreglo, buscador)

print (f"el numero {buscador}, aparece {numeroigual} veces en el arreglo")
