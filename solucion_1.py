##declaramos las variables:

## n = número q el usuario introducirá

n = int(input('introduce un número entero positivo '))

##sum = la suma q se irá acumulando en el for q viene a continuación...

sum = 0

##inicializamos un bucle for q recorrerá los números desde 1 hasta el q el usuario ingresó más 1

##(esto último porq hay q recordar q el segundo parámetro del range del bucle for no incluye el número 
##  especificado: en este caso va desde 1 incluyendo al 1, hasta n+1 sin incluirlo)

for i in range(1, n+1):

    # En cada iteración del bucle se le suma el número actual al q equivale i

    sum += i

##mostramos la suma y termina el programa (si se coloca una f antes de las comillas de una cadena, se
## pueden concatenar variables pasándoselas a python entre llaves {})

print(f'la suma de los números enteros positivos desde 1 hasta {n} es {sum}')