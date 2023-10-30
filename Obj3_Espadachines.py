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

def main():
    ventana1_programa()

if __name__=='__main__':
    main()
    
