# Escribir una función que reciba el mensaje a cifrar (cadena de caracteres), y devuelva el
# mensaje cifrado, mediante el cifrado atbash. Probarla utilizando doctest, con al menos 10
# casos diferentes.

import doctest

def cifrado_atbash(cadena):
    # Función que recibe una cadena y devuelve el mensaje codficado mediante el cifrado atbash.
    # Letras con tildes, ñ y otros símbolos se mantienen igual.
    """
    >>> cifrado_atbash('hola mundo')
    'SLOZ ÑFNWL'
    >>> cifrado_atbash('SLOZ ÑFNWL')
    'hola mundo'
    >>> cifrado_atbash('abcd')
    'ZYXW'
    >>> cifrado_atbash('0123456789')
    '9876543210'
    >>> cifrado_atbash('ZYWV')
    'abde'
    >>> cifrado_atbash('mÑ')
    'Ñm'
    >>> cifrado_atbash('nN')
    'Nn'
    >>> cifrado_atbash('hólá múndó')
    'SóOá ÑúNWó'
    >>> cifrado_atbash('!"·$%&/')
    '!"·$%&/'
    >>> cifrado_atbash(cifrado_atbash('ZZalgoritmoüÑá09$'))
    'ZZalgoritmoüÑá09$'
    """
    letras = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    numeros = '0123456789'
    mensaje_cifrado = ""
    for caracter in cadena:
        if caracter in numeros:
            caracter_nuevo = numeros[(len(numeros)-1)-int(caracter)]
        elif caracter in letras:
            caracter_nuevo = letras[(len(letras)-1)-letras.index(caracter)]
        else:
            caracter_nuevo = caracter
        mensaje_cifrado += caracter_nuevo
    return mensaje_cifrado
