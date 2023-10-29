from tkinter import *
def ventana1_programa():
    ventana= Tk()
    ventana.title("TP Grupal Parte 1 - Grupo: ESPADACHINES ")
    ventana.resizable(0,0)
    ventana.iconbitmap("espadachines.ico")
    miFrame=Frame(ventana, width=500, height=500)
    miFrame.pack()
    texto1era_ventana(miFrame,ventana)
    ventana.mainloop()
    

def texto1era_ventana(miFrame,ventana):
    texto_bienvenida= Label(miFrame, text="Bienvenido a la aplicación de mensajes secretos del grupo Espadachines.")
    texto_bienvenida.place(x=20, y=50)
    texto_para_cerrar= Label(miFrame, text="Para continuar presione continuar, de lo contrario cierre la ventana.")
    texto_para_cerrar.place(x=20, y=80)
    botonEnviar = Button(ventana,text="continuar", command=cifrados)
    botonEnviar.place (x=200, y=150)
    texto= Label(miFrame, text="Construido por : Leandro Sebastian Ramos")
    texto.place(x=20, y=400)
    nombre2= Label(miFrame, text="Juan Martin Diaz")
    nombre2.place(x=110, y=420)
    nombre3= Label(miFrame, text="Ruth Giselle Duarte Orue")
    nombre3.place(x=110, y=440)
    nombre4= Label(miFrame, text="Iñaki Vydra")
    nombre4.place(x=110, y=460)

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
    
