from tkinter import *
def ventana1_programa():
    ventana= Tk()
    ventana.title("TP Grupal Parte 1 - Grupo: ESPADACHINES ")
    ventana.resizable(0,0)
    ventana.iconbitmap("espadachines.ico")
    miFrame=Frame(ventana, width=600, height=350)
    miFrame.pack()
    miFrame.config(bg="LightSeaGreen")
    miImagen=PhotoImage(file="mensajeoculto.png")
    posicionimagen=Label(miFrame,image=miImagen).place(x=380,y=200)
    texto1era_ventana(miFrame,ventana)
    ventana.mainloop()
    

def texto1era_ventana(miFrame,ventana):
    texto_bienvenida= Label(miFrame, text="Bienvenido a la aplicación de mensajes secretos del grupo Espadachines.",bg="LightSeaGreen",font= ("Comic Sans MS",13))
    texto_bienvenida.place(x=0, y=50)
    texto_para_cerrar= Label(miFrame, text="Para continuar presione continuar, de lo contrario cierre la ventana.",bg="LightSeaGreen",font= ("Comic Sans MS",13))
    texto_para_cerrar.place(x=0, y=80)
    botonEnviar = Button(ventana,text="continuar", command=cifrados)
    botonEnviar.place (x=250, y=125)
    texto= Label(miFrame, text="Construido por : Leandro Sebastian Ramos",bg="LightSeaGreen",font= ("Comic Sans MS",13))
    texto.place(x=20, y=170)
    nombre2= Label(miFrame, text="Juan Martin Diaz",bg="LightSeaGreen",font= ("Comic Sans MS",13))
    nombre2.place(x=150, y=195)
    nombre3= Label(miFrame, text="Ruth Giselle Duarte Orue",bg="LightSeaGreen",font= ("Comic Sans MS",13))
    nombre3.place(x=150, y=225)
    nombre4= Label(miFrame, text="Iñaki Vydra",bg="LightSeaGreen",font= ("Comic Sans MS",13))
    nombre4.place(x=150, y=255)


def cifrados():
    nuevaVentana = Toplevel()
    nuevaVentana.title("Opciones de Cifrado")
    nuevaVentana.iconbitmap("espadachines.ico")
    nuevaVentana.resizable(0,0)
    marcoOpciones = Frame(nuevaVentana, width=300, height=300)
    marcoOpciones.pack()
    texto_mensaje = Label(marcoOpciones, text="Ingrese un mensaje")
    texto_mensaje.grid(row=0, column=0, padx=5, pady=5)
    entrada_mensaje = Entry(marcoOpciones)
    entrada_mensaje.grid(row=0, column=1, padx=5, pady=5)
    texto_clave = Label(marcoOpciones, text='Clave')
    texto_clave.grid(row=1, column=0, padx=5, pady=5)
    entrada_clave = Entry(marcoOpciones)
    entrada_clave.grid(row=1, column=1, padx=5, pady=5)
    mensaje_resultado = Label(marcoOpciones, text="Mensaje resultado:")
    mensaje_resultado.grid(row=4, column=0, padx=5, pady=5)
    texto_resultado = Label(marcoOpciones)
    texto_resultado.grid(row=4, column=1, padx=5, pady=5)
    boton_cifrado_cesar = Button(marcoOpciones, text="Cifrar mensaje César", command= lambda : texto_resultado.configure(text=cifrado_cesar(entrada_mensaje.get(), int(entrada_clave.get()))))
    boton_cifrado_cesar.grid(row=2, column=0, padx=5, pady=5)
    boton_descifrado_cesar = Button(marcoOpciones, text="Descifrar mensaje César", command= lambda : texto_resultado.configure(text=cifrado_cesar(entrada_mensaje.get(), -int(entrada_clave.get()))))
    boton_descifrado_cesar.grid(row=3, column=0, padx=5, pady=5)
    boton_cifrado_atbash = Button(marcoOpciones, text="Cifrar mensaje Atbash", command= lambda : texto_resultado.configure(text=cifrado_atbash(entrada_mensaje.get())))
    boton_cifrado_atbash.grid(row=2, column=1, padx=5, pady=5)
    boton_descifrado_atbash = Button(marcoOpciones, text="Descifrar mensaje Atbash", command= lambda : texto_resultado.configure(text=cifrado_atbash(entrada_mensaje.get())))
    boton_descifrado_atbash.grid(row=3, column=1, padx=5, pady=5)


def cifrado_cesar(cadena, clave):
    """
    Esta función recibe una cadena de caracteres y una clave numérica entera y devuelva la cadena cifrada mediante el cifrado cesar.
    Letras con tildes, ñ y otros símbolos se mantienen igual.
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
    
