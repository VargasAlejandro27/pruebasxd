#by Fernando Socasi
try:
    tamaño = int(input("Ingrese el tamaño del arreglo: "))
    arreglo = [0] * tamaño
except ValueError:
    print("Ingrese solo numeros no letras")

for i in range(tamaño):
    try:
        nuevo_valor = int(input(f"Ingrese el numero entero {i+1}: "))
        arreglo[i]=nuevo_valor
    except ValueError:
        print("Ingrese un numero entero")
        break
suma = 0
for num in arreglo:
    suma += num
print("Se muestra su arreglo:", arreglo)
print("Se muestra la Suma de todos los elementos:", suma)
