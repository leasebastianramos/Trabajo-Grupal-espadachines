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


def ventana2():
    
    raiz_ventana2 = Toplevel()
    raiz_ventana2.title("Opciones de Cifrado")
    #raiz_ventana2.iconbitmap("espadachines.ico")  # NO TE OLVIDES DE  DESCOMENTAR
    raiz_ventana2.geometry("752x525")
    raiz_ventana2.resizable(0,0)
    raiz_ventana2.config(bg="LightSeaGreen")

    frame_mensaje=Frame(raiz_ventana2, width=450, height=250)
    frame_mensaje.grid(row=0,column=0,sticky="nsew")
    frame_mensaje.config(bd=10,relief=SUNKEN,bg="LightSeaGreen")

    texto_mensaje = Label(frame_mensaje, text="Mensaje:   ",bg="LightSeaGreen")
    texto_mensaje.grid(row=0, column=0, padx=5, pady=5)



    entrada_mensaje = Text(frame_mensaje,width=33, height=12)
    entrada_mensaje.grid(row=1, column=1, padx=5, pady=5)
    
    

    scroll=Scrollbar(frame_mensaje,command=entrada_mensaje.yview)
    scroll.grid(row=1, column=2, padx=5, pady=5,sticky="nsew")
    entrada_mensaje.config(yscrollcommand=scroll.set)
    

    frame_modos=Frame(raiz_ventana2, width=350, height=250)
    frame_modos.grid(row=0,column=1,sticky="nsew")
    frame_modos.config(bd=10,relief=SUNKEN,bg="LightSeaGreen")

    variable_modo=IntVar()

    texto_modo = Label(frame_modos, text="Elige el modo:",bg="LightSeaGreen").grid(row=0, column=0, padx=5, pady=5)
        

    Radiobutton(frame_modos,text="Cifrar",bg="LightSeaGreen",variable=variable_modo,value=1).grid(row=4, column=0, padx=5, pady=5)

    Radiobutton(frame_modos,text="Descifrar",bg="LightSeaGreen",variable=variable_modo,value=0).grid(row=12, column=0, padx=5, pady=5)

    
    variable_cifrado=IntVar()

    texto_cifrado = Label(frame_modos, text="Elige el cifrado:",bg="LightSeaGreen").grid(row=0, column=3, padx=5, pady=5)
        

    Radiobutton(frame_modos,text="Cesar",bg="LightSeaGreen",variable=variable_cifrado,value=1).grid(row=4, column=3, padx=5, pady=5)

    texto_clave = Label(frame_modos, text="Clave del cifrado Cesar:",bg="LightSeaGreen").grid(row=4, column=4, padx=5, pady=5)
    entrad_clave=Entry(frame_modos).grid(row=8, column=4, padx=5, pady=5)

    Radiobutton(frame_modos,text="Atbash",bg="LightSeaGreen",variable=variable_cifrado,value=0).grid(row=12, column=3, padx=5, pady=5)


    frame_resultado=Frame(raiz_ventana2,width=350, height=250)
    frame_resultado.config(bd=15,relief=SUNKEN,bg="LightSeaGreen")
    frame_resultado.grid(row=1,column=0,sticky="nsew")

    texto_mensaje = Label(frame_resultado, text="Resultado:",bg="LightSeaGreen")
    texto_mensaje.grid(row=0, column=0, padx=5, pady=5)

    Resultado = Text(frame_resultado,width=33, height=12) #ahi que  cambiar esto que  no sea  un entry que   sea una pantalla  donde  mostrar el resultado
    Resultado.grid(row=2, column=1, padx=5, pady=5)

    scroll=Scrollbar(frame_resultado,command=Resultado.yview)
    scroll.grid(row=2, column=2, padx=5, pady=5,sticky="nsew")
    Resultado.config(yscrollcommand=scroll.set)


    frame_control=Frame(raiz_ventana2, width=350, height=100)
    frame_control.config(bd=15,relief=SUNKEN,bg="LightSeaGreen")
    frame_control.grid(row=1,column=1,sticky="nsew")
    
    info_iniciar=Label(frame_control,text="Procesar el mensaje:",bg="LightSeaGreen").grid(row=0, column=0, padx=5, pady=5)
    boton_iniciar=Button(frame_control,text="Iniciar").grid(row=1, column=0, padx=5, pady=5)   #falta hacerlo funcional

    info_reiniciar=Label(frame_control,text="Limpiar las pantallas para ingresar otro mensaje:",bg="LightSeaGreen").grid(row=2, column=0, padx=5, pady=5)
    boton_reiniciar=Button(frame_control, text="Reiniciar").grid(row=3, column=0, padx=5, pady=5)#command=)


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
    
