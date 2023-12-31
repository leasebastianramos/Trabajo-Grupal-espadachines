from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

COLOR = "#79c4ae"
FUENTE=("Calibri",14)

def ventana1_programa():
    """
    Esta funcion se encarga de crear la primera ventana.
    Responsable=Sebastian
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
    posicionimagen.place(x=380,y=210)
    texto1era_ventana(miFrame,ventana)
    ventana.mainloop()
    
def texto1era_ventana(miFrame,ventana):
    """
    Esta funcion muestra los mensajes de la primera ventana que ve el usuario y tiene el boton para despues de apretarlo
    lo desplaze a la segunda ventana.
    Responsable=Sebastian
    """
    texto_bienvenida= Label(miFrame, text="Bienvenido a la aplicación de mensajes secretos del grupo Espadachines.",bg=COLOR,font= (FUENTE))
    texto_bienvenida.place(x=25, y=50)
    texto_para_cerrar= Label(miFrame, text="Para continuar presione continuar, de lo contrario cierre la ventana.",bg=COLOR,font= (FUENTE))
    texto_para_cerrar.place(x=35, y=80)
    botonEnviar = Button(ventana,text="Continuar",font= FUENTE, relief=RAISED, bd=5, command=lambda:abrir_ventana2(ventana))
    botonEnviar.place (x=250, y=125)
    def pasa_botonEnviar(_):
        botonEnviar["bg"] = "#FFFFFF"
    def sale_botonEnviar(_):
        botonEnviar["bg"] = "SystemButtonFace"
    botonEnviar.bind("<Enter>", pasa_botonEnviar)
    botonEnviar.bind("<Leave>", sale_botonEnviar)
    texto= Label(miFrame, text="Construido por : Leandro Sebastian Ramos",bg=COLOR,font= (FUENTE))
    texto.place(x=20, y=200)
    nombre2= Label(miFrame, text="Juan Martin Diaz",bg=COLOR,font= (FUENTE))
    nombre2.place(x=150, y=230)
    nombre3= Label(miFrame, text="Ruth Giselle Duarte Orue",bg=COLOR,font= (FUENTE))
    nombre3.place(x=150, y=260)
    nombre4= Label(miFrame, text="Iñaki Vydra",bg=COLOR,font= (FUENTE))
    nombre4.place(x=150, y=290)

def abrir_ventana2(ventana):
    """
    Esta funcion hace que se cierre la primera ventana luego de apretar continuar.
    Responsable=Juan Martin
    """
    ventana.destroy()
    ventana2()

def reiniciar_ventana2(texto1, texto2, texto3,radiobutton_v):
    """
    Esta funcion borra los campos llenados por el ususario
    Responsable= Ruth
    """
    cadena_vacia = ''
    texto1.delete(1.0, END)
    texto1.insert(END, cadena_vacia)
    texto2.config(state=NORMAL)
    texto2.delete(1.0, END)
    texto2.insert(END, cadena_vacia)
    texto2.config(state=DISABLED)
    
    texto3.config(state=NORMAL)
    texto3.delete(0, END)
    texto3.insert(0, cadena_vacia)
    if radiobutton_v.get()==2:
        texto3.config(state=DISABLED)


def ventana2():
    """
    Funcion que crea la segunda ventana luego de apretar continuar.
    Responsable= Iñaki
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
    Responsable= Iñaki
    """
    frame_mensaje = Frame(raiz_ventana2, bg=COLOR, relief=SUNKEN, bd=10)
    frame_mensaje.grid(row=0, column=0, sticky="nsew")
    texto_mensaje = Label(frame_mensaje, text="Mensaje:",bg=COLOR,font= FUENTE)
    texto_mensaje.grid(row=0, column=0, padx=5, pady=5,sticky='w')
    entrada_mensaje = Text(frame_mensaje,width=33, height=12, relief=SUNKEN, bd=2)
    entrada_mensaje.grid(row=1, column=1, padx=5, pady=5)
    scroll=Scrollbar(frame_mensaje,command=entrada_mensaje.yview)
    scroll.grid(row=1, column=2, padx=5, pady=5,sticky="nsew")
    entrada_mensaje.config(yscrollcommand=scroll.set)
    boton_abrir = Button(frame_mensaje, text="Abrir Archivo '.txt'",font= FUENTE,relief=RAISED, bd=5, command=lambda:abrir_archivo(entrada_mensaje))
    boton_abrir.grid(row=0, column=1)
    
    frame_resultado = Frame(raiz_ventana2, bg=COLOR,relief=SUNKEN,bd=10)
    frame_resultado.grid(row=1, column=0, columnspan=2, sticky="nsew")
    texto_mensaje = Label(frame_resultado, text="Resultado:",bg=COLOR,font= FUENTE)
    texto_mensaje.grid(row=0, column=0, padx=5, pady=5, sticky='w')
    resultado = Text(frame_resultado,width=73, height=12, relief=SUNKEN, bd=2, state=DISABLED)
    resultado.grid(row=2, column=1, padx=5, pady=5)
    scroll=Scrollbar(frame_resultado,command=resultado.yview)
    scroll.grid(row=2, column=2, padx=5, pady=5,sticky="nsew")
    resultado.config(yscrollcommand=scroll.set)
    usuario_conf_ventana2(raiz_ventana2,entrada_mensaje,resultado)

def abrir_archivo(entrada_mensaje):
    """
    Esta funcion te permite abrir un archivo de texto para usar en el cifrado y la imprime en el texto de entrada
    Responsable= Iñaki
    """
    archivo = filedialog.askopenfile(initialdir="/", title="Seleccionar un archivo de texto", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    if archivo:
        contenido = archivo.read()
        entrada_mensaje.delete(1.0, END)
        entrada_mensaje.insert(END, contenido)
        
def usuario_conf_ventana2(raiz_ventana2,entrada_mensaje,resultado):
    """
    Esta funcion sirve para que el usuario pueda configurar el programa.
    Responsable= Iñaki
    """
    frame_modos = Frame(raiz_ventana2, bg=COLOR,relief=SUNKEN,bd=10)
    frame_modos.grid(row=0, column=1, sticky="nsew")
    texto_modo = Label(frame_modos, text="Elige el tipo de cifrado:",bg=COLOR,font= FUENTE)
    texto_modo.grid(row=0, column=0, columnspan=2, padx=5, pady=5)  
    
    boton_cifrar = Button(frame_modos,text="Cifrar",font= FUENTE, relief=RAISED, bd=5, command= lambda: verificar_cifrado(variable_radiobuttons, entrada_mensaje.get("1.0", "end-1c"), entrada_clave.get(), resultado))
    boton_cifrar.grid(row=6, column=0, padx=5, pady=5)

    def entra_boton(boton):
        boton.widget["bg"] = "#FFFFFF"
    def sale_boton(boton):
        boton.widget["bg"] = "SystemButtonFace"
   
    boton_cifrar.bind("<Enter>", entra_boton)
    boton_cifrar.bind("<Leave>", sale_boton)
    boton_descifrar = Button(frame_modos,text="Descifrar",font= FUENTE, relief=RAISED, bd=5, command= lambda: verificar_cifrado(variable_radiobuttons, entrada_mensaje.get("1.0", "end-1c"), entrada_clave.get(), resultado, -1))
    boton_descifrar.grid(row=6, column=1, padx=5, pady=5)
    boton_descifrar.bind("<Enter>", entra_boton)
    boton_descifrar.bind("<Leave>", sale_boton)

    variable_radiobuttons = IntVar()
    variable_radiobuttons.set(-1)
    caja_cesar = Radiobutton(frame_modos,text="Cesar",font= FUENTE, variable=variable_radiobuttons, value=1, bg=COLOR,command=lambda:evento_destapar(texto_clave,entrada_clave))
    caja_cesar.grid(row=4, column=1, padx=5, pady=5, sticky='w')
    caja_atbash = Radiobutton(frame_modos,text="Atbash",font= FUENTE, variable=variable_radiobuttons, value=2, bg=COLOR,command=lambda:evento_tapar(texto_clave,entrada_clave))
    caja_atbash.grid(row=4, column=0, padx=5, pady=5, sticky='w')
    texto_clave = Label(frame_modos, text="Clave: ",font= FUENTE,bg=COLOR,state=DISABLED)
    texto_clave.grid(row=4, column=2, padx=5, pady=5)
    entrada_clave=Entry(frame_modos, relief=SUNKEN, bd=2,state=DISABLED)
    entrada_clave.grid(row=4, column=3, padx=5, pady=5)
    opciones_finales_ventana2(frame_modos,raiz_ventana2,entrada_mensaje,entrada_clave,resultado,variable_radiobuttons)

def evento_destapar(label,entry):
        entry.config(state=NORMAL)
        label.config(state=NORMAL)
def evento_tapar(label,entry):
        entry.config(state=DISABLED)
        label.config(state=DISABLED)


def opciones_finales_ventana2(frame_modos,raiz_ventana2,entrada_mensaje,entrada_clave,resultado,variable_radiobuttons):
    """
    Esta funcion sirve para que te limpie la pantalla del programa y para cerrarlo si apretan sus respectivos botones.
    Responsable= Iñaki
    """
    frame_opciones_extra=Frame(frame_modos,bg=COLOR)
    frame_opciones_extra.place(x=0, y=190)

    boton_reiniciar = Button(frame_opciones_extra, text="Cifrar otro mensaje", relief=RAISED, bd=5, font= FUENTE, command=lambda: reiniciar_ventana2(entrada_mensaje,resultado,entrada_clave,variable_radiobuttons))
    boton_reiniciar.grid(row=16, column=0,padx=5, pady=5)
    def entra_boton(boton):
        boton.widget["bg"] = "#FFFFFF"
    def sale_boton(boton):
        boton.widget["bg"] = "SystemButtonFace"
    boton_reiniciar.bind("<Enter>", entra_boton)
    boton_reiniciar.bind("<Leave>", sale_boton)
    boton_salir = Button(frame_opciones_extra, text='Salir', relief=RAISED, bd=5, font= FUENTE, command=raiz_ventana2.destroy)
    boton_salir.grid(row=16, column=3, padx=5, pady=5)
    boton_salir.bind("<Enter>", entra_boton)
    boton_salir.bind("<Leave>", sale_boton)
    

def verificar_cifrado(variable_radiobuttons, entrada, clave, salida, descifrar=1):
    """
    Esta funcion imprime el mensaje segun las opcines de cifrado elegido, en caso de no elgir uno o ingresar una clave invalida muestra un mensaje de advertencia.
    Responsable= Sebastian
    """
    if variable_radiobuttons.get()==1:
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
    elif variable_radiobuttons.get()==2:
        salida.config(state=NORMAL)
        salida.delete(1.0, END)
        salida.insert(END, cifrado_atbash(entrada))
        salida.config(state=DISABLED)
    else:
        messagebox.showwarning("Seleccione Opción", "Debe seleccionar una de las opciones para realizar el cifrado.")

def validar_clave(clave):
    """
    Esta funcion valida que la clave que el ususario escribió sea un numero y devuelve un valor booleano.
    Responsable= Juan Martin 
    >>> validar_clave('')
    False
    >>> validar_clave('a')
    False
    >>> validar_clave('0')
    True
    >>> validar_clave('1')
    True
    >>> validar_clave('-1')
    True
    """
    try:
        int(clave)
        valida = True
    except ValueError:
        valida = False
    return valida

def cifrado_cesar(cadena, clave):
    """
    Esta función recibe una cadena de caracteres y una clave numérica entera y devuelva la cadena cifrada mediante el cifrado cesar.
    Letras con tildes, ñ y otros símbolos se mantienen igual.
    Responsable= Juan Martin
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
    Responsable= Ruth
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
    
