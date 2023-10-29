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
    botonEnviar = Button(ventana,text="continuar")
    botonEnviar.place (x=200, y=150)
    texto= Label(miFrame, text="Construido por : Leandro Sebastian Ramos")
    texto.place(x=20, y=400)
    nombre2= Label(miFrame, text="Juan Martin Diaz")
    nombre2.place(x=110, y=420)
    nombre3= Label(miFrame, text="Ruth Giselle Duarte Orue")
    nombre3.place(x=110, y=440)
    nombre4= Label(miFrame, text="Iñaki Vydra")
    nombre4.place(x=110, y=460)
    
def main():
    ventana1_programa()

main()
    
