from tkinter import *
from tkinter import messagebox

COLOR = "#47A2AF"

def ventana1_programa():
    ventana= Tk()
    ventana.title("TP Grupal Parte 1 - Grupo: ESPADACHINES ")
    ventana.resizable(0,0)
    ventana.iconbitmap("espadachines.ico")
    miFrame=Frame(ventana, width=600, height=350)
    miFrame.pack()
    miFrame.config(bg=COLOR)
    miImagen=PhotoImage(file="mensajeoculto.png")
    posicionimagen=Label(miFrame,image=miImagen).place(x=380,y=200)
    texto1era_ventana(miFrame,ventana)
    ventana.mainloop()
    

def texto1era_ventana(miFrame,ventana):
    texto_bienvenida= Label(miFrame, text="Bienvenido a la aplicación de mensajes secretos del grupo Espadachines.",bg=COLOR,font= ("Comic Sans MS",13))
    texto_bienvenida.place(x=0, y=50)
    texto_para_cerrar= Label(miFrame, text="Para continuar presione continuar, de lo contrario cierre la ventana.",bg=COLOR,font= ("Comic Sans MS",13))
    texto_para_cerrar.place(x=0, y=80)
    botonEnviar = Button(ventana,text="Continuar", command=ventana2)
    botonEnviar.place (x=250, y=125)
    texto= Label(miFrame, text="Construido por : Leandro Sebastian Ramos",bg=COLOR,font= ("Comic Sans MS",13))
    texto.place(x=20, y=170)
    nombre2= Label(miFrame, text="Juan Martin Diaz",bg=COLOR,font= ("Comic Sans MS",13))
    nombre2.place(x=150, y=195)
    nombre3= Label(miFrame, text="Ruth Giselle Duarte Orue",bg=COLOR,font= ("Comic Sans MS",13))
    nombre3.place(x=150, y=225)
    nombre4= Label(miFrame, text="Iñaki Vydra",bg=COLOR,font= ("Comic Sans MS",13))
    nombre4.place(x=150, y=255)


def reiniciar_ventana2(texto1, texto2, texto3):
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
    
    raiz_ventana2 = Toplevel()
    raiz_ventana2.title("Opciones de Cifrado")
    raiz_ventana2.geometry("790x560")
    raiz_ventana2.resizable(0, 0)
    raiz_ventana2.config(bg=COLOR)
    raiz_ventana2.iconbitmap("espadachines.ico")


    frame_mensaje = Frame(raiz_ventana2, bg=COLOR,relief=SUNKEN,bd=10)
    frame_mensaje.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
     

    texto_mensaje = Label(frame_mensaje, text="Mensaje:   ",bg=COLOR)
    texto_mensaje.grid(row=0, column=0, padx=5, pady=5)


    entrada_mensaje = Text(frame_mensaje,width=33, height=12)
    entrada_mensaje.grid(row=1, column=1, padx=5, pady=5)
    

    scroll=Scrollbar(frame_mensaje,command=entrada_mensaje.yview)
    scroll.grid(row=1, column=2, padx=5, pady=5,sticky="nsew")
    entrada_mensaje.config(yscrollcommand=scroll.set)
    
    frame_modos = Frame(raiz_ventana2, bg=COLOR,relief=SUNKEN,bd=10)
    frame_modos.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")


    texto_modo = Label(frame_modos, text="Elige el tipo de cifrado:",bg=COLOR)
    texto_modo.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        

    boton_cifrar = Button(frame_modos,text="Cifrar", command= lambda: verificar_cifrado(variable_caja_cesar, entrada_mensaje.get("1.0", "end-1c"), entrada_clave.get(), resultado))
    boton_cifrar.grid(row=10, column=4, padx=5, pady=5)

    boton_descifrar = Button(frame_modos,text="Descifrar", command= lambda: verificar_cifrado(variable_caja_cesar, entrada_mensaje.get("1.0", "end-1c"), entrada_clave.get(), resultado, -1))
    boton_descifrar.grid(row=10, column=5, padx=5, pady=5)

    boton_reiniciar = Button(frame_modos, text="Cifrar otro mensaje", command=lambda: reiniciar_ventana2(entrada_mensaje,resultado,entrada_clave))
    boton_reiniciar.grid(row=16, column=0,padx=5, pady=5)


    variable_caja_cesar = IntVar()
    caja_cesar = Checkbutton(frame_modos,text="Cesar", variable=variable_caja_cesar, bg=COLOR,command=lambda: caja_atbash.deselect())
    caja_cesar.grid(row=4, column=0, padx=5, pady=5, sticky='w')
    caja_cesar.select()


    caja_atbash = Checkbutton(frame_modos,text="Atbash",bg=COLOR,command=lambda: caja_cesar.deselect())
    caja_atbash.grid(row=4, column=3, padx=5, pady=5, sticky='w')


    texto_clave = Label(frame_modos, text="Clave del cifrado Cesar:",bg=COLOR)
    texto_clave.grid(row=8, column=0, padx=5, pady=5)
    entrada_clave=Entry(frame_modos)
    entrada_clave.grid(row=10, column=0, padx=5, pady=5)


    frame_resultado = Frame(raiz_ventana2, bg=COLOR,relief=SUNKEN,bd=10)
    frame_resultado.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")


    texto_mensaje = Label(frame_resultado, text="Resultado:",bg=COLOR)
    texto_mensaje.grid(row=0, column=0, padx=5, pady=5)

    resultado = Text(frame_resultado,width=73, height=12, state=DISABLED)
    resultado.grid(row=2, column=1, padx=5, pady=5)

    scroll=Scrollbar(frame_resultado,command=resultado.yview)
    scroll.grid(row=2, column=2, padx=5, pady=5,sticky="nsew")
    resultado.config(yscrollcommand=scroll.set)

    raiz_ventana2.mainloop()

def verificar_cifrado(caja_cesar, entrada, clave, salida, descifrar=1):
    if caja_cesar.get()==1:
        if validar_clave(clave):
            salida.config(state=NORMAL)
            salida.delete(1.0, END)
            salida.insert(END, cifrado_cesar(entrada, descifrar*int(clave)))
            salida.config(state=DISABLED)
        else:
            messagebox.showwarning("Clave Inválida", "La clave debe ser un número entero.")
    else:
        salida.config(state=NORMAL)
        salida.delete(1.0, END)
        salida.insert(END, cifrado_atbash(entrada))
        salida.config(state=DISABLED)


def validar_clave(clave):
    valida = False
    if clave.isnumeric() or (clave[0]=='-' and clave[1:].isnumeric()):
        valida = True
    return valida


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
    
