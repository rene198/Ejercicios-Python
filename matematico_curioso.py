'''
Creado: x Equipo de 5°2°: De la Cruz, Silisque, Buendia. 
Fecha: 10/05/2021
'''
num = int(input("Ingrese un numero: "))
contador = 1
may = 0
while num != 1:
    if num > may:
        may = num
    if num %2==0:
        num = num /2
    else:
        num = (num*3)+1
    print(int(num),end=' ')
    contador = contador+1
print("\nLa cantidad de numeros en la secuencia es: ",int(contador))
print("El numero mayor es de: ",int(may))
