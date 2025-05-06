##declaramos las variables:

##string_ingresado = texto q el usuario escribira

string_ingresado = input('escribe un texto cualquiera  ')

##contadores = se irán aumentando a medida q se encuentren vocales, consonantes o números
# ##(de momento inician en ceros)

contador_de_vocales = 0
contador_de_numeros = 0
contador_de_consonantes = 0

##vocales = un string con las posibles vocales, solo en minúsculas porque más tarde se convertirá la
## cadena ingresada a sólo minúsculas y no se tendrá q tener en cuenta las mayúsculas (incluimos vocales
##con tilde y la u con diéresis porque el programa las detecta como caracteres diferentes a sus versiones
##regulares)

vocales = 'aeiouáéíóúü'

##numeros = otro string, esta vez con todos los dígitos (numeros de una cifra) posibles

numeros = '0123456789'

##consonantes = un string con las posibles consonantes, solo en minúsculas porque más tarde se convertirá la
## cadena ingresada a sólo minúsculas y no se tendrá q tener en cuenta las mayúsculas

consonantes = 'bcdfghjklmnñpqrstvwxyz'

##se crea un bucle for q recorrerá cada caracter del string ingresado (convirtiendo este último a solo
##minúsculas con el método .lower() q retorna la misma cadena pero toda en minúsculas)

for caracter in string_ingresado.lower():

    ##con la funcionalidad in detectamos si el caracter actual del bucle se encuentra en el string de
    ##posibles vocales q creamos previamente

    if caracter in vocales:

        ##si es así le sumamos uno al contador de vocales, ya q quiere decir q encontramos una vocal
        ##en la cadena

        contador_de_vocales += 1

    ##si no se cumple lo anterior, con la funcionalidad in detectamos si el caracter actual 
    ##del bucle se encuentra en el string de posibles números q creamos previamente

    elif caracter in numeros:

        ##si es así le sumamos uno al contador de números, ya q quiere decir q encontramos un número
        ##en la cadena

        contador_de_numeros += 1

    ##si no se cumple todo lo anterior, con la funcionalidad in detectamos si el caracter actual del 
    #bucle se encuentra en el string de posibles consonantes q creamos previamente

    elif caracter in consonantes:

        ##si es así le sumamos uno al contador de consonantes, ya q quiere decir q encontramos una consonante
        ##en la cadena

        contador_de_consonantes += 1

##mostramos la cantidad de vocales, consonantes y números

##si no se encontró ninguna vocal, es decir el contador de vocales quedó en ceros...

if contador_de_vocales == 0:

    ##se muestra q no se encontró ninguna vocal

    print(f'no hay vocales en el texto ingresado... :sadfeis:')

##caso contrario...

else:

    ##se muestra la cantidad de vocales

    print(f'cantidad de vocales {contador_de_vocales}')

##si no se encontró ninguna consonante, es decir el contador de consonantes quedó en ceros...

if contador_de_consonantes == 0:

    ##se muestra q no se encontró ninguna consonante

    print(f'no hay consonantes en el texto ingresado... D:')

##caso contrario...

else:

    ##se muestra la cantidad de consonantes

    print(f'cantidad de consonantes {contador_de_consonantes}')

##si no se encontró ningún número, es decir el contador de números quedó en ceros...

if contador_de_numeros == 0:

    ##se muestra q no se encontró ningún número

    print(f'no hay números en el texto ingresado... :c')

##caso contrario...

else:

    ##se muestra la cantidad de números

    print(f'cantidad de numeros {contador_de_numeros}')