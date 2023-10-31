from tkinter import *
from tkinter import messagebox
import doctest

COLOR = "#47A2AF"
FUENTE=("Comic Sans MS",12)

def ventana1_programa():
    """
    Esta funcion se encarga de crear la primera ventana.
    """
    ventana= Tk()
    ventana.title("TP Grupal Parte 1 - Grupo: ESPADACHINES ")
    ventana.resizable(0,0)
    ventana.iconbitmap("espadachines.ico")
    miFrame=Frame(ventana, width=600, height=350)
    miFrame.pack()
    miFrame.config(bg=COLOR)
    miImagen=PhotoImage(file="mensajeoculto.png")
    posicionimagen=Label(miFrame,image=miImagen)
    posicionimagen.place(x=380,y=200)
    texto1era_ventana(miFrame,ventana)
    ventana.mainloop()
    
def abrir_ventana2(ventana):
    """
    Esta funcion hace que se cierre la primera ventana luego de apretar continuar.
    """
    ventana.destroy()
    ventana2()
    
def texto1era_ventana(miFrame,ventana):
    """
    Esta funcion muestra los mensajes de la primera ventana que ve el usuario y tiene el boton para despues de apretarlo
    lo desplaze a la segunda ventana.
    """
    texto_bienvenida= Label(miFrame, text="Bienvenido a la aplicación de mensajes secretos del grupo Espadachines.",bg=COLOR,font= (FUENTE))
    texto_bienvenida.place(x=0, y=50)
    texto_para_cerrar= Label(miFrame, text="Para continuar presione continuar, de lo contrario cierre la ventana.",bg=COLOR,font= (FUENTE))
    texto_para_cerrar.place(x=0, y=80)
    botonEnviar = Button(ventana,text="Continuar",font= ("Comic Sans MS",13), command=lambda:abrir_ventana2(ventana))
    botonEnviar.place (x=250, y=125)
    texto= Label(miFrame, text="Construido por : Leandro Sebastian Ramos",bg=COLOR,font= (FUENTE))
    texto.place(x=20, y=170)
    nombre2= Label(miFrame, text="Juan Martin Diaz",bg=COLOR,font= (FUENTE))
    nombre2.place(x=150, y=195)
    nombre3= Label(miFrame, text="Ruth Giselle Duarte Orue",bg=COLOR,font= (FUENTE))
    nombre3.place(x=150, y=225)
    nombre4= Label(miFrame, text="Iñaki Vydra",bg=COLOR,font= (FUENTE))
    nombre4.place(x=150, y=255)


def reiniciar_ventana2(texto1, texto2, texto3):
    """
    Esta funcion reinicia la ventana 2.
    """
    cadena_vacia = ''
    texto1.delete(1.0, END)
    texto1.insert(END, cadena_vacia)
    texto2.config(state=NORMAL)
    texto2.delete(1.0, END)
    texto2.insert(END, cadena_vacia)
    texto2.config(state=DISABLED)
    texto3.delete(0, END)
    texto3.insert(0, cadena_vacia)


def ventana2():
    """
    Funcion que crea la segunda ventana luego de apretar continuar.
    """
    raiz_ventana2 = Tk()
    raiz_ventana2.title("Opciones de Cifrado")
    raiz_ventana2.resizable(0, 0)
    raiz_ventana2.config(bg=COLOR)
    raiz_ventana2.iconbitmap("espadachines.ico")
    ventana2_mensaje(raiz_ventana2)
    raiz_ventana2.mainloop()
    
def ventana2_mensaje(raiz_ventana2):
    """
    Esta funcion sirve para mostrar la entrada de los mensajes y mostrarlos.
    """
    frame_mensaje = Frame(raiz_ventana2, bg=COLOR,relief=SUNKEN,bd=10)
    frame_mensaje.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    texto_mensaje = Label(frame_mensaje, text="Mensaje:",bg=COLOR,font= FUENTE)
    texto_mensaje.grid(row=0, column=0, padx=5, pady=5,sticky='w')
    entrada_mensaje = Text(frame_mensaje,width=33, height=12)
    entrada_mensaje.grid(row=1, column=1, padx=5, pady=5)
    scroll=Scrollbar(frame_mensaje,command=entrada_mensaje.yview)
    scroll.grid(row=1, column=2, padx=5, pady=5,sticky="nsew")
    entrada_mensaje.config(yscrollcommand=scroll.set)
    frame_resultado = Frame(raiz_ventana2, bg=COLOR,relief=SUNKEN,bd=10)
    frame_resultado.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
    texto_mensaje = Label(frame_resultado, text="Resultado:",bg=COLOR,font= FUENTE)
    texto_mensaje.grid(row=0, column=0, padx=5, pady=5, sticky='w')
    resultado = Text(frame_resultado,width=73, height=12, state=DISABLED)
    resultado.grid(row=2, column=1, padx=5, pady=5)
    scroll=Scrollbar(frame_resultado,command=resultado.yview)
    scroll.grid(row=2, column=2, padx=5, pady=5,sticky="nsew")
    resultado.config(yscrollcommand=scroll.set)
    usuario_conf_ventana2(raiz_ventana2,entrada_mensaje,resultado)

def usuario_conf_ventana2(raiz_ventana2,entrada_mensaje,resultado):
    """
    Esta funcion sirve para que el usuario pueda configurar el programa.
    """
    frame_modos = Frame(raiz_ventana2, bg=COLOR,relief=SUNKEN,bd=10)
    frame_modos.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
    texto_modo = Label(frame_modos, text="Elige el tipo de cifrado:",bg=COLOR,font= FUENTE)
    texto_modo.grid(row=0, column=0, columnspan=2, padx=5, pady=5)  
    boton_cifrar = Button(frame_modos,text="Cifrar",font= FUENTE, command= lambda: verificar_cifrado(variable_caja_cesar, entrada_mensaje.get("1.0", "end-1c"), entrada_clave.get(), resultado))
    boton_cifrar.grid(row=10, column=4, padx=5, pady=5)
    boton_descifrar = Button(frame_modos,text="Descifrar",font= FUENTE, command= lambda: verificar_cifrado(variable_caja_cesar, entrada_mensaje.get("1.0", "end-1c"), entrada_clave.get(), resultado, -1))
    boton_descifrar.grid(row=10, column=5, padx=5, pady=5)
    variable_caja_cesar = IntVar()
    caja_cesar = Checkbutton(frame_modos,text="Cesar",font= FUENTE, variable=variable_caja_cesar, bg=COLOR,command=lambda: caja_atbash.deselect())
    caja_cesar.grid(row=4, column=0, padx=5, pady=5, sticky='w')
    caja_cesar.select()
    caja_atbash = Checkbutton(frame_modos,text="Atbash",font= FUENTE,bg=COLOR,command=lambda: caja_cesar.deselect())
    caja_atbash.grid(row=4, column=3, padx=5, pady=5, sticky='w')
    texto_clave = Label(frame_modos, text="Clave del cifrado Cesar:",font= FUENTE,bg=COLOR)
    texto_clave.grid(row=8, column=0, padx=5, pady=5)
    entrada_clave=Entry(frame_modos)
    entrada_clave.grid(row=10, column=0, padx=5, pady=5)
    opciones_finales_ventana2(frame_modos,raiz_ventana2,entrada_mensaje,entrada_clave,resultado)

def opciones_finales_ventana2(frame_modos,raiz_ventana2,entrada_mensaje,entrada_clave,resultado):
    """
    Esta funcion sirve para que te limpie la pantalla del programa y para cerrarlo si apretan sus respectivos botones.
    """
    frame_opciones_extra=Frame(frame_modos,bg="blue",relief=SUNKEN,bd=5)
    frame_opciones_extra.place(x=0, y=190)
    boton_reiniciar = Button(frame_opciones_extra, text="Cifrar otro mensaje",font= FUENTE, command=lambda: reiniciar_ventana2(entrada_mensaje,resultado,entrada_clave))
    boton_reiniciar.grid(row=16, column=0,padx=5, pady=5)
    boton_salir = Button(frame_opciones_extra, text='Salir',font= FUENTE, command=raiz_ventana2.destroy)
    boton_salir.grid(row=16, column=3, padx=5, pady=5)
    
  
def verificar_cifrado(caja_cesar, entrada, clave, salida, descifrar=1):
    """
    Esta funcion verifica lo que escribio el usuario en caso de no haber escrito algo le saltara un mensaje de advertencia.
    """
    if caja_cesar.get()==1:
        if validar_clave(clave):
            salida.config(state=NORMAL)
            salida.delete(1.0, END)
            salida.insert(END, cifrado_cesar(entrada, descifrar*int(clave)))
            salida.config(state=DISABLED)
        else:
            if len(clave)==0:
                messagebox.showwarning("Clave Inválida", "Debe ingresar una clave para el cifrado César.")
            else:
                messagebox.showwarning("Clave Inválida", "La clave debe ser un número entero.")

    else:
        salida.config(state=NORMAL)
        salida.delete(1.0, END)
        salida.insert(END, cifrado_atbash(entrada))
        salida.config(state=DISABLED)


def validar_clave(clave):
    """
    Esta funcion valida que la clave que el ususario escribio sea un numero.
    """
    valida = False
    if len(clave)>0 and (clave.isnumeric() or (clave[0]=='-' and clave[1:].isnumeric())):
        valida = True
    return valida


def cifrado_cesar(cadena, clave):
    """
    Esta función recibe una cadena de caracteres y una clave numérica entera y devuelva la cadena cifrada mediante el cifrado cesar.
    Letras con tildes, ñ y otros símbolos se mantienen igual.
    
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
    
    INICIO_NUMEROS = ord('0')
    FIN_NUMEROS = ord('9')
    INICIO_MAYUSCULAS = ord('A')
    FIN_MAYUSCULAS = ord('Z')
    INICIO_MINUSCULAS = ord('a')
    FIN_MINUSCULAS = ord('z')
    RANGO_NUMEROS = 10
    RANGO_LETRAS = 26

    for caracter in cadena:
        codigo_unicode = ord(caracter)
        if codigo_unicode >= INICIO_NUMEROS and codigo_unicode <= FIN_NUMEROS:
            caracter_nuevo = chr(INICIO_NUMEROS+(codigo_unicode-INICIO_NUMEROS+clave)%RANGO_NUMEROS)
        elif codigo_unicode >= INICIO_MAYUSCULAS and codigo_unicode <= FIN_MAYUSCULAS:
            caracter_nuevo = chr(INICIO_MAYUSCULAS+(codigo_unicode-INICIO_MAYUSCULAS+clave)%RANGO_LETRAS)
        elif codigo_unicode >= INICIO_MINUSCULAS and codigo_unicode <= FIN_MINUSCULAS:
            caracter_nuevo = chr(INICIO_MINUSCULAS+(codigo_unicode-INICIO_MINUSCULAS+clave)%RANGO_LETRAS)
        else:
            caracter_nuevo = caracter
        mensaje_cifrado += caracter_nuevo
        
    return mensaje_cifrado



def cifrado_atbash(cadena):
    """
    Función que recibe una cadena y devuelve el mensaje codficado mediante el cifrado atbash.
    Letras con tildes, ñ y otros símbolos se mantienen igual.
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


def main():
    ventana1_programa()


if __name__=='__main__':
    main()
    