# declaracion de una lista para almacenar los numeros
numeros=[]

#Carga de los numeros en la lista 

for i in range(5):

    try:
        num=int(input("Ingrese un numero entero "))
        #agregamos el numero a la lista  
        numeros.append(num)

    # si el valor ingresado no es un numero entero capturamos
    # la excepcion y solicitamos un nuevo ingreso de valor
       
    except ArithmeticError:

        num=int(input("Error de formato, por favor ,ingrese un numero entero "))
  
     

#Suma de los numeros


#Calculo del promedio
   

#encontrando el maximo  de los numeros  



# Mostramos la suma, el promerdio ,el maximo y el minimo
# de los numeros de la lista

print("La suma de los numeros es ",str(Suma(numeros)))
print("El promedio de los numeros es ",str(Promedio(numeros)))
print("El mayor  de los numeros es ",str(Maximo(numeros)))
print("El menor de los numeros es ",str(Minimo(numeros)))