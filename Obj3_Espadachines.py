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
    texto_mensaje.grid(row=0, column=0)
    entrada_mensaje = Entry(marcoOpciones)
    entrada_mensaje.grid(row=0, column=1)
    texto_clave = Label(marcoOpciones, text='Clave')
    texto_clave.grid(row=1, column=0)
    entrada_clave = Entry(marcoOpciones)
    entrada_clave.grid(row=1, column=1)
    boton_cifrado_cesar = Button(marcoOpciones, text="Cifrar mensaje César")
    boton_cifrado_cesar.grid(row=2, column=0)
    boton_descifrado_cesar = Button(marcoOpciones, text="Descifrar mensaje César")
    boton_descifrado_cesar.grid(row=3, column=0)
    boton_cifrado_atbash = Button(marcoOpciones, text="Cifrar mensaje Atbash")
    boton_cifrado_atbash.grid(row=2, column=1)
    texto_vacio = Label(marcoOpciones)
    boton_descifrado_atbash = Button(marcoOpciones, text="Descifrar mensaje Atbash")
    boton_descifrado_atbash.grid(row=3, column=1)

def mensaje_atbash(mensaje, frame):
    texto = Label(frame, texto=cifrado_atbash(mensaje))
    texto.grid(row=4, column=0)


def cifrado_cesar(cadena, clave):
    """
    Esta función recibe una cadena de caracteres y una clave numérica entera y devuelva la cadena cifrada mediante el cifrado cesar.
    Letras con tildes, ñ y otros símbolos se mantienen igual.
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
    
