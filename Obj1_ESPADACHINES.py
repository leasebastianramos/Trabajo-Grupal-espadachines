# Escribir una función que reciba el mensaje a cifrar (cadena de caracteres) y la clave de
# cifrado, y devuelva el mensaje cifrado, mediante el cifrado césar. Probarla utilizando doctest,
# con al menos 10 casos diferentes.

import doctest

def cifrado_cesar(cadena, clave):
    # Esta función recibe una cadena de caracteres y una clave numérica entera y devuelva la cadena cifrada mediante el cifrado cesar.
    # Letras con tildes, ñ y otros símbolos se mantienen igual.
    """
    >>> cifrado_cesar('az09', 0)
    'az09'
    >>> cifrado_cesar('abc0123', 1)
    'bcd1234'
    >>> cifrado_cesar('bc123', -1)
    'ab012'
    >>> cifrado_cesar('hola mundo', 3)
    'krod pxqgr'
    >>> cifrado_cesar('krod pxqgr', 23)
    'hola mundo'
    >>> cifrado_cesar('krod pxqgr', -3)
    'hola mundo'
    >>> cifrado_cesar('HOLA MUNDO', 3)
    'KROD PXQGR'
    >>> cifrado_cesar('hola mundo1', 33)
    'ovsh tbukv4'
    >>> cifrado_cesar('ñ!"·$%&/()áèü', 31)
    'ñ!"·$%&/()áèü'
    >>> cifrado_cesar(cifrado_cesar('abcñ$0123', 31), -31)
    'abcñ$0123'
    """
    mensaje_cifrado = ""
    inicio_numeros = ord('0')
    fin_numeros = ord('9')
    inicio_mayusculas = ord('A')
    fin_mayusculas = ord('Z')
    inicio_minusculas = ord('a')
    fin_minusculas = ord('z')
    rango_numeros = 10
    rango_letras = 26

    for caracter in cadena:
        codigo_unicode = ord(caracter)
        if codigo_unicode>=inicio_numeros and codigo_unicode<=fin_numeros:
            caracter_nuevo = chr(inicio_numeros+(codigo_unicode-inicio_numeros+clave)%rango_numeros)
        elif codigo_unicode>=inicio_mayusculas and codigo_unicode<=fin_mayusculas:
            caracter_nuevo = chr(inicio_mayusculas+(codigo_unicode-inicio_mayusculas+clave)%rango_letras)
        elif codigo_unicode>=inicio_minusculas and codigo_unicode<=fin_minusculas:
            caracter_nuevo = chr(inicio_minusculas+(codigo_unicode-inicio_minusculas+clave)%rango_letras)
        else:
            caracter_nuevo = caracter
        mensaje_cifrado += caracter_nuevo
    return mensaje_cifrado
