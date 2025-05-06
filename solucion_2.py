##declaramos las variables:

##string_1 y string_2 = textos q el usuario introducirá

string_1 = input('escribe un texto cualquiera ')
string_2 = input('escribe otro texto cualquiera :3 ')

##string_final = la cadena q se le retornará al usuario al final del programa, de momento se deja vacía
##para luego empezar a agregarle las letras una a una

string_final = ''

##primero es necesario determinar cuál es la cadena más larga, eso se realiza extrayendo la longitud de
## cada una con la función len() (pasándole entre paréntesis la cadena a extraer su longitud) y comparándolas
## con la función max() (pasándole entre parentesis las dos longitudes separadas por ,)

##(la función max retorna el valor de la longitud más larga y almacenamos esa longitud en la variable
## longitud_mayor)

longitud_mayor = max(len(string_1), len(string_2))

##inicializamos un bucle for q inicie en 0 (este parámetro se sobreentiende si solo se le pasa un número
##  a range()) y finalice en la longitud mayor (sin incluir este valor)

for i in range(longitud_mayor):

    ##en cada iteración se realizan las siguientes dos acciones:

    ##si el número actual del bucle for (i) es menor a la longitud de la primera cadena...

    if i < len(string_1):

        ##le añade el caracter correspondiente a ese índice (índice i) de la cadena 1 a la cadena final

        string_final += string_1[i]

    ##si el número actual del bucle for (i) es menor a la longitud de la segunda cadena...

    if i < len(string_2):

        ##le añade el caracter correspondiente a ese índice (índice i) de la cadena 2 a la cadena final

        string_final += string_2[i]

## mostramos la cadena final y termina el programa

print(f'string entrelazado {string_final}')