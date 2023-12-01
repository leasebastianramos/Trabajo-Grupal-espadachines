from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

COLOR = "#482b6b"   
FUENTE=("Calibri",14) 
COLOR_FUENTE="white"
COLOR_BOTONES="#8f89af"



#ventana presentación
def ventana1_programa():
    """
    Esta funcion se encarga de crear la primera ventana.
    Responsable=Sebastian
    """
    ventana= Tk()
    ventana.title("TP Grupal Parte 2 - Grupo: ESPADACHINES ")
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
    Esta funcion muestra los mensajes de la primera ventana que ve el usuario y tiene el boton para después de apretarlo
    lo desplace a la segunda ventana.
    Responsable=Sebastian
    """
    texto_bienvenida= Label(miFrame, text="Bienvenido a la aplicación de mensajes secretos del grupo Espadachines.",foreground= COLOR_FUENTE,bg=COLOR,font= (FUENTE))
    texto_bienvenida.place(x=25, y=50)
    texto_para_cerrar= Label(miFrame, text="Para continuar presione continuar, de lo contrario cierre la ventana.",foreground= COLOR_FUENTE,bg=COLOR,font= (FUENTE))
    texto_para_cerrar.place(x=35, y=80)
    botonEnviar = Button(ventana,text="Continuar",font= FUENTE, relief=RAISED, bd=5, command=lambda:abrir_ventana2(ventana))
    botonEnviar.place (x=250, y=125)
    def pasa_botonEnviar(_):
        botonEnviar["bg"] = "#FFFFFF"
    def sale_botonEnviar(_):
        botonEnviar["bg"] = "SystemButtonFace"
    botonEnviar.bind("<Enter>", pasa_botonEnviar)
    botonEnviar.bind("<Leave>", sale_botonEnviar)

    texto= Label(miFrame, text="Construido por : Leandro Sebastian Ramos",foreground= COLOR_FUENTE,bg=COLOR,font= (FUENTE))
    texto.place(x=20, y=200)
    nombre2= Label(miFrame, text="Juan Martin Diaz",foreground= COLOR_FUENTE,bg=COLOR,font= (FUENTE))
    nombre2.place(x=150, y=230)
    nombre3= Label(miFrame, text="Ruth Giselle Duarte Orue",foreground= COLOR_FUENTE,bg=COLOR,font= (FUENTE))
    nombre3.place(x=150, y=260)
    nombre4= Label(miFrame, text="Iñaki Vydra",foreground= COLOR_FUENTE,bg=COLOR,font= (FUENTE))
    nombre4.place(x=150, y=290)
def abrir_ventana2(ventana):
    """
    Esta funcion hace que se cierre la primera ventana luego de apretar continuar.
    Responsable= Sebastian
    """
    ventana.destroy()
    ventana_inicio_sesion()


#ventanas de la parte 2 obj 1

#ventana iniciar sesión
def ventana_inicio_sesion():
    """Esta funcion se encarga de crear la ventana para el inicio de sesión del usuario
    Responsable= Sebastian"""
    
    raiz_iniciar_sesion=Tk()
    raiz_iniciar_sesion.title("Iniciar sesión ")
    raiz_iniciar_sesion.iconbitmap("espadachines.ico")  
    raiz_iniciar_sesion.resizable(0,0)
    frame_iniciar_sesion=Frame(raiz_iniciar_sesion,width=350,height=450)
    frame_iniciar_sesion.pack()
    frame_iniciar_sesion.config(bg=COLOR,bd=8,relief= RIDGE)


    Label(frame_iniciar_sesion, text="Iniciar sesión",font= (FUENTE[0],22),foreground= COLOR_FUENTE,bg=COLOR).place(x=85,y=20)
    
    Button(frame_iniciar_sesion,text="¿No tenés cuenta? Registrate ",font= (FUENTE[0],12,UNDERLINE),foreground= COLOR_FUENTE,background=COLOR,bd=0,command= lambda:registrar_usuario(ft_usuario,ft_contraeña)).place(x=65,y=60)


    #Esto es lo que ve el usuario en el entry si no ingresa nada
    text_usuario_por_defecto=StringVar(value="Nombre de usuario")
    text_usuario_por_defecto_top=Label(frame_iniciar_sesion,font= (FUENTE[0],12),textvariable=text_usuario_por_defecto,background=COLOR,foreground=COLOR)
    text_usuario_por_defecto_top.place(x=80,y=100)

    #acá quedarían los datos que ponga en usuario
    variable_usuario=StringVar()
    entry_usuario=Entry(frame_iniciar_sesion, relief=SUNKEN,font=(FUENTE[0],12), bd=2,width=20,textvariable=text_usuario_por_defecto)  
    entry_usuario.place(x=80,y=120)

    #estos son elementos estéticos
    ft_usuario=PhotoImage(file="usuario.png")
    Label(frame_iniciar_sesion,image=ft_usuario,bg=COLOR).place(x=50,y=120)

    entry_usuario.bind("<FocusIn>",lambda x : entry_focus_in(entry_usuario,text_usuario_por_defecto,variable_usuario,text_usuario_por_defecto_top,advertencia)) 
    entry_usuario.bind("<FocusOut>",lambda x : entry_focus_out(entry_usuario,text_usuario_por_defecto,text_usuario_por_defecto_top))


    #Esto es lo que ve el usuario en el entry si no ingresa nada
    text_contraseña_por_defecto=StringVar(value="Contraseña") 
    text_contraseña_por_defecto_top=Label(frame_iniciar_sesion,font= (FUENTE[0],12),textvariable=text_contraseña_por_defecto,background=COLOR,foreground=COLOR)
    text_contraseña_por_defecto_top.place(x=80,y=160)

    #acá quedarían los datos que ponga en contraseña
    variable_contraseña=StringVar()
    entry_contraseña=Entry(frame_iniciar_sesion, relief=SUNKEN,font=(FUENTE[0],12), bd=2,width=20,textvariable=text_contraseña_por_defecto)
    entry_contraseña.place(x=80,y=180)
    
    #estos son elementos estéticos  
    ft_contraeña=PhotoImage(file="candado.png")
    Label(frame_iniciar_sesion,image=ft_contraeña,bg=COLOR).place(x=50,y=180)
    entry_contraseña.bind("<FocusIn>",lambda x : entry_focus_in(entry_contraseña,text_contraseña_por_defecto,variable_contraseña,text_contraseña_por_defecto_top,advertencia,control.get())) 
    entry_contraseña.bind("<FocusOut>",lambda x : entry_focus_out(entry_contraseña,text_contraseña_por_defecto,text_contraseña_por_defecto_top))

    
    #Para mostrar/ocultar la contraseña ingresada
    Label(text="Mostrar",foreground=COLOR_FUENTE,bg=COLOR).place(x=115,y=225)

    control=IntVar()
    mostrar=Checkbutton(frame_iniciar_sesion,variable=control,background=COLOR,command=lambda:mostrar_contraseña_confirmacion(control,entry_contraseña,text_contraseña_por_defecto.get())) 
    mostrar.place(x=80,y=215)

    #aca se le avisa al usuario si hubo algun problema al iniciar
    advertencia=Text(frame_iniciar_sesion,font=(FUENTE[0],10),background=COLOR,foreground=COLOR_FUENTE,width=25, height=2,bd=0,state=DISABLED)   
    advertencia.place(x=80,y=250)


    Button(frame_iniciar_sesion,text="¿Olvidaste tu contraseña?",font= (FUENTE[0],10,UNDERLINE),background=COLOR,foreground= COLOR_FUENTE,bd=0, command= lambda:abrir_recuperar(entry_usuario,advertencia,ft_usuario)).place(x=85,y=310)

    Button(frame_iniciar_sesion,text="Iniciar sesion",font=(FUENTE[0],10),anchor=CENTER,padx=40,bg=COLOR_BOTONES,foreground=COLOR_FUENTE,command= lambda:inicio_sesion(entry_usuario.get(),entry_contraseña.get(),advertencia,raiz_iniciar_sesion)).place(x=80,y=350)
    
    raiz_iniciar_sesion.mainloop()

def inicio_sesion(usuario_ingresado,contraseña_ingresada,advertencia,raiz):
    """Esta funcion revisa si lo que fue ingresado por el usuario coincide con algún perfil que esté registrado
    Responsable= Sebastian"""
    advertencia.config(state=NORMAL)
    advertencia.delete(1.0, END)

    with open ("datos_registrados.csv","r") as archivo:
        usuario,contraseña,pregunta,respuesta,intentos=leer_archivo(archivo)
        intentos=int(intentos)
        if usuario==usuario_ingresado:
            if intentos<3:
                if contraseña==contraseña_ingresada:
                    raiz.destroy()
                    cifrar_enviar_mensajes(usuario)
            else:
                advertencia.insert(END,"El usuario está bloqueado")

        while usuario!=usuario_ingresado and usuario:
            usuario,contraseña,pregunta,respuesta,intentos=leer_archivo(archivo)
            intentos=int(intentos)
            if usuario==usuario_ingresado:
                if intentos<3:
                    if contraseña==contraseña_ingresada:
                        raiz.destroy()
                        cifrar_enviar_mensajes(usuario)
                else:
                    advertencia.insert(END,"El usuario está bloqueado")

        if usuario=="" or contraseña!=contraseña_ingresada and intentos<3:
            
            advertencia.insert(END,"El usuario o la contraseña\nson inválidos")
        advertencia.config(state=DISABLED)

#ventana recuperar contraseña
def abrir_recuperar(usuario_ingresado,advertencia_usuario,ft_usuario):
    """La función  se encarga de la recuperación de contraseña para un usuario ingresado, con un manejo de intentos y bloqueo de usuario
    Responsable= Sebastian"""
    advertencia_usuario.config(state=NORMAL)
    advertencia_usuario.delete(1.0, END)
    
    with open ("datos_registrados.csv","r") as archivo:
        usuario_registrado,contraseña,pregunta,respuesta,intentos=leer_archivo(archivo)
        intentos=int(intentos)
        if usuario_registrado==usuario_ingresado.get() and usuario_ingresado.get()!="":
            if intentos<3:
                recuperar_contraseña(ft_usuario,usuario_ingresado.get(),pregunta,respuesta,contraseña,intentos)
            else:
                advertencia_usuario.insert(END,"El usuario está bloqueado")

        while usuario_registrado!=usuario_ingresado.get() and usuario_registrado:

            usuario_registrado,contraseña,pregunta,respuesta,intentos=leer_archivo(archivo)
            intentos=int(intentos)
            if usuario_registrado==usuario_ingresado.get() and usuario_ingresado.get()!="":
                if intentos<3:
                    recuperar_contraseña(ft_usuario,usuario_ingresado.get(),pregunta,respuesta,contraseña,intentos)
                else:
                    advertencia_usuario.insert(END,"El usuario está bloqueado")

        if usuario_registrado=="":
            advertencia_usuario.insert(END,"Ingrese un usuario registrado")

    advertencia_usuario.config(state=DISABLED)
def recuperar_contraseña(ft_usuario,usuario,pregunta,respuesta,contraseña,intentos):
    """Esta funcion crea una ventana para poder interactuar con el usuario y asi preguntarle para poder recuperar su contraseña
    Responsable= Sebastian"""
    raiz_recuperar_contraseña= Toplevel()

    #Para congelar la otra ventana hasta que se cierre
    raiz_recuperar_contraseña.grab_set()
    raiz_recuperar_contraseña.focus_set()

    raiz_recuperar_contraseña.title("Recuperar contraseña")
    raiz_recuperar_contraseña.iconbitmap("espadachines.ico")
    raiz_recuperar_contraseña.resizable(0,0)

    frame_recuperar_contraseña=Frame(raiz_recuperar_contraseña,width=350, height=450)
    frame_recuperar_contraseña.pack()
    frame_recuperar_contraseña.config(bg=COLOR,bd=8,relief= RIDGE)

    Label(frame_recuperar_contraseña, text="Recuperar contraseña",font= (FUENTE[0],20),foreground= COLOR_FUENTE,bg=COLOR).place(x=50,y=20)
    
    Label(frame_recuperar_contraseña,font= (FUENTE[0],12),text="Nombre de usuario",background=COLOR,foreground=COLOR_FUENTE).place(x=80,y=100)
    Label(frame_recuperar_contraseña,image=ft_usuario,bg=COLOR).place(x=50,y=120)
    text_usuario=StringVar(value=usuario)
    entry_usuario=Entry(frame_recuperar_contraseña, relief=SUNKEN,font=(FUENTE[0],12), bd=2,width=20,textvariable=text_usuario,state=DISABLED)
    entry_usuario.place(x=80,y=120)

    Label(frame_recuperar_contraseña,font=(FUENTE[0],12),background=COLOR,foreground=COLOR_FUENTE,width=20,text="Pregunta de seguridad:").place(x=70,y=180)
    text_pregunta=StringVar(value=pregunta)
    pregunta_de_seguridad=Label(frame_recuperar_contraseña,font= (FUENTE[0],12),textvariable=text_pregunta,background=COLOR,foreground=COLOR_FUENTE)
    pregunta_de_seguridad.place(x=75,y=210)


    entry_pregunta_de_seguridad=Entry(frame_recuperar_contraseña, relief=SUNKEN,font=(FUENTE[0],12), bd=2,width=20)
    entry_pregunta_de_seguridad.place(x=80,y=240)
    entry_pregunta_de_seguridad.bind("<Return>",lambda x: recuperar(entry_pregunta_de_seguridad.get(),respuesta,contraseña,num_intentos,raiz_recuperar_contraseña,usuario))

    num_intentos=IntVar(value=intentos)

    Button(frame_recuperar_contraseña,text="Recuperar",font=(FUENTE[0],10),anchor=CENTER,bg=COLOR_BOTONES,foreground="white",padx=20,command=lambda:recuperar(entry_pregunta_de_seguridad.get(),respuesta,contraseña,num_intentos,raiz_recuperar_contraseña,usuario)).place(x=60,y=350)

    Button(frame_recuperar_contraseña,text="Cancelar",font=(FUENTE[0],10),anchor=CENTER,bg=COLOR_BOTONES,foreground="white",padx=20,command=lambda:cancelar_ventana(raiz_recuperar_contraseña)).place(x=180,y=350)

def recuperar(respuesta_ingresada,respuesta,contraseña,num_intentos,ventana_recuperar,nombre_usuario):
    """la función se encarga de la recuperación de contraseña, verificando la respuesta ingresada y tomando acciones en consecuencia,
       ya sea mostrando la contraseña recuperada en caso de éxito o gestionando los intentos y bloqueando al usuario si se supera el límite de intentos permitidos.
       Responsable= Sebastian
    """
    if respuesta_ingresada!="":
        if respuesta_ingresada==respuesta:
            ventana_recuperar.destroy()
            num_intentos.set(0)
            actualizar_archivo(num_intentos.get(),nombre_usuario)
            messagebox.showinfo("Recuperar contraseña",f"Tu contraseña es {contraseña}")
        else:
            num_intentos.set(num_intentos.get()+1)
            actualizar_archivo(num_intentos.get(),nombre_usuario)
            if num_intentos.get()>2:
                ventana_recuperar.destroy()
                messagebox.showwarning("Respuesta incorrecta",f"Se llegó al límite de 3 intentos\nEl usuario ha sido bloqueado")
            else:
                messagebox.showwarning("Respuesta incorrecta",f"Tiene un límite de 3 intentos\nIntentos de recuperar contraseña:{num_intentos.get()}")
def actualizar_archivo(intentos_actualizados,usuario):
    """ Esta funcion se encarga de  actualizar el número de intentos para un usuario específico. Crea un archivo temporal para almacenar las actualizaciones
        y luego sobrescribe el archivo original con las modificaciones. Finalmente, limpia el archivo temporal
        Responsable= Sebastian
    """
    archivo_actualizado=open("borrador_datos.csv","a")
    with open("datos_registrados.csv","r") as datos_registrados:

        for linea in datos_registrados:
            usuario_registrado, contraseña_registrada, pregunta, respuesta, intentos_registrados = linea.rstrip("\n").split(",")
            if usuario_registrado==usuario:
                intentos_registrados=intentos_actualizados

            linea = "{},{},{},{},{}\n".format(usuario_registrado,contraseña_registrada,pregunta,respuesta,intentos_registrados)
            archivo_actualizado.write(linea)

    archivo_actualizado.close()

    archivo_actualizado=open("borrador_datos.csv","r")
    with open("datos_registrados.csv","w") as datos_registrados:        
        for linea in archivo_actualizado:
            datos_registrados.writelines(linea)
    archivo_actualizado.close()

    with open("borrador_datos.csv","w") as datos_para_borrar:        
        datos_para_borrar.write("")

#Ventana registrar usuario
def registrar_usuario(ft_usuario,ft_contraeña):
    """Esta funcion se encarga de crear la ventana para el registro del ususario
    Responsable= Iñaki"""

    raiz_registrar_usuario= Toplevel()
    
    raiz_registrar_usuario.grab_set()
    raiz_registrar_usuario.focus_set()

    raiz_registrar_usuario.title("Registrar usuario")
    raiz_registrar_usuario.iconbitmap("espadachines.ico")
    raiz_registrar_usuario.resizable(0,0)

    frame_registrar_usuario=Frame(raiz_registrar_usuario,width=575, height=450)
    frame_registrar_usuario.pack()
    frame_registrar_usuario.config(bg=COLOR,bd=8,relief= RIDGE)

    Label(frame_registrar_usuario, text="Registrar usuario",foreground= COLOR_FUENTE,font= (FUENTE[0],22),bg=COLOR).place(x=160,y=20)
    
    #acá le muestro al usuario información de los requerimientos de el usuario y la contraseña
    info=Text(frame_registrar_usuario,font= (FUENTE[0],10),width=30, height=8, bd=0,background=COLOR,foreground= COLOR_FUENTE,state=DISABLED)
    info.place(x=310,y=180)

    #Esto es lo que ve el usuario en el entry si no ingresa nada
    text_usuario_por_defecto=StringVar(value="Nombre de usuario")
    text_usuario_por_defecto_top=Label(frame_registrar_usuario,font= (FUENTE[0],12),textvariable=text_usuario_por_defecto,background=COLOR,foreground=COLOR)
    text_usuario_por_defecto_top.place(x=60,y=70)

    #acá quedan los datos que ingrese en usuario
    variable_usuario=StringVar()
    entry_usuario=Entry(frame_registrar_usuario, relief=SUNKEN,font=(FUENTE[0],12), bd=2,width=20,textvariable=text_usuario_por_defecto)  
    entry_usuario.place(x=60,y=90)

    #son eventos para mostrar la info de los requerimientos del usuario
    entry_usuario.bind("<Enter>", lambda x:mostrar_info(info,text_usuario_por_defecto) )
    entry_usuario.bind("<Leave>",lambda x:ocultar_info(info))

    #estos son elementos esteticos  
    Label(frame_registrar_usuario,image=ft_usuario,bg=COLOR).place(x=30,y=90)
    entry_usuario.bind("<FocusIn>",lambda x : entry_focus_in(entry_usuario,text_usuario_por_defecto,variable_usuario,text_usuario_por_defecto_top,advertencia_usuario)) 
    entry_usuario.bind("<FocusOut>",lambda x : entry_focus_out(entry_usuario,text_usuario_por_defecto,text_usuario_por_defecto_top))

    #acá le muestro al usuario si no cumplió con algún requerimiento del usuario
    advertencia_usuario=Text(frame_registrar_usuario,font=(FUENTE[0],10),background=COLOR,foreground=COLOR_FUENTE,width=20, height=2,bd=0,state=DISABLED)   
    advertencia_usuario.place(x=60,y=120)

    #si el usuario da ENTER le valido el usuario

    bool_usuario_validado=BooleanVar(value=False)

    entry_usuario.bind("<Return>",lambda x:procesar_usuario_ingresado(entry_usuario,advertencia_usuario,bool_usuario_validado))


    #Esto es lo que ve el usuario en el entry si no ingresa nada
    text_contraseña_por_defecto=StringVar(value="Contraseña") 
    text_contraseña_por_defecto_top=Label(frame_registrar_usuario,font= (FUENTE[0],12),textvariable=text_contraseña_por_defecto,background=COLOR,foreground=COLOR)
    text_contraseña_por_defecto_top.place(x=60,y=160)

    #acá quedan los datos que ingrese en usuario
    variable_contraseña=StringVar()
    entry_contraseña=Entry(frame_registrar_usuario, relief=SUNKEN,font=(FUENTE[0],12), bd=2,width=20,textvariable=text_contraseña_por_defecto)
    entry_contraseña.place(x=60,y=180)

    #son eventos para mostrar la info de los requerimientos de la contraseña
    entry_contraseña.bind("<Enter>", lambda x:mostrar_info(info,text_contraseña_por_defecto) )
    entry_contraseña.bind("<Leave>",lambda x:ocultar_info(info))

    #estos son elementos estéticos  
    Label(frame_registrar_usuario,image=ft_contraeña,bg=COLOR).place(x=30,y=180)
    entry_contraseña.bind("<FocusIn>",lambda x : entry_focus_in(entry_contraseña,text_contraseña_por_defecto,variable_contraseña,text_contraseña_por_defecto_top,advertencia_contraseña,control.get())) 
    entry_contraseña.bind("<FocusOut>",lambda x : entry_focus_out(entry_contraseña,text_contraseña_por_defecto,text_contraseña_por_defecto_top))

    #acá le muestro al usuario si no cumplió con algún requerimiento de la contraseña
    advertencia_contraseña=Text(frame_registrar_usuario,font=(FUENTE[0],10),foreground=COLOR_FUENTE,background=COLOR,width=20, height=2,bd=0,state=DISABLED)   
    advertencia_contraseña.place(x=60,y=210)

    bool_contraseña_validada=BooleanVar(value=False)

    entry_contraseña.bind("<Return>",lambda x:procesar_contraseña_ingresada(entry_contraseña,advertencia_contraseña,bool_contraseña_validada))


    #Para mostrar/ocultar lo que el usuario ingrese en contraseña y confirmar 
    control=IntVar()
    Label(frame_registrar_usuario,text="Mostrar",foreground=COLOR_FUENTE,bg=COLOR).place(x=255,y=182)
    mostrar=Checkbutton(frame_registrar_usuario,variable=control,background=COLOR,command=lambda:mostrar_contraseña_confirmacion(control,entry_contraseña,text_contraseña_por_defecto.get(),confirmar_contraseña,texto_confirmar_pordecto.get())) 
    mostrar.place(x=230,y=180)

    #Esto es lo que ve el usuario en el entry si no ingresa nada   
    texto_confirmar_pordecto=StringVar(value="Confirmar")
    texto_confirmar_pordecto_top=Label(frame_registrar_usuario,font= (FUENTE[0],12),textvariable=texto_confirmar_pordecto,background=COLOR,foreground=COLOR)
    texto_confirmar_pordecto_top.place(x=60,y=250)

    #acá quedan los datos que ingrese en usuario
    variable_r_confirmar=StringVar()
    confirmar_contraseña=Entry(frame_registrar_usuario, relief=SUNKEN,font=(FUENTE[0],12), bd=2,width=20,textvariable=texto_confirmar_pordecto) 
    confirmar_contraseña.place(x=60,y=270)

    #estos son elementos estéticos  
    confirmar_contraseña.bind("<FocusIn>",lambda x : entry_focus_in(confirmar_contraseña,texto_confirmar_pordecto,variable_r_confirmar,texto_confirmar_pordecto_top,advertencia_confirmar,control.get())) 
    confirmar_contraseña.bind("<FocusOut>",lambda x : entry_focus_out(confirmar_contraseña,texto_confirmar_pordecto,texto_confirmar_pordecto_top))

    #acá le muestro si no coinciden la contraseña y el confirmar o si no ingresa nada
    advertencia_confirmar=Text(frame_registrar_usuario,font=(FUENTE[0],10),background=COLOR,foreground=COLOR_FUENTE,width=20,height=1,bd=0,state=DISABLED)
    advertencia_confirmar.place(x=60,y=300)

    bool_confirmar_validada=BooleanVar(value=False)

    confirmar_contraseña.bind("<Return>",lambda x:procesar_confirmar_ingresado(confirmar_contraseña,advertencia_confirmar,entry_contraseña,bool_confirmar_validada))


    #estas son las opciones del menu desplegable
    pregunta=StringVar()
    pregunta.set("Elija una opción:")
    list_preguntas=["Apellido de su abuela materna"
                    ,"Nombre de tu mascota"
                    ,"Nombre de tu mejor amigo/a"
                    ,"Cantante preferido"
                    ,"Ciudad preferida"
                    ,"Nombre de tu primer novio/a"
                    ,"Cual es tu deporte favorito"
                    ,"Fecha del cumple de tu mascota"
                    ,"Pelicula o libro favorito"
                    ,"Comida favorita"]
    
    recuperar_contraseña=OptionMenu(frame_registrar_usuario,pregunta,*list_preguntas,command=lambda x:entry_recuperar.config(state=NORMAL))
    recuperar_contraseña.config(width=27)
    recuperar_contraseña.place(x=310,y=90)
    
    #acá queda la respuesta del usuario a la pregunta
    entry_recuperar=Entry(frame_registrar_usuario, relief=SUNKEN,font=(FUENTE[0],12), bd=2,width=25,state=DISABLED)
    entry_recuperar.place(x=310,y=140)
    

    #este boton procesa los datos que ingreso el usuario
    
    Button(frame_registrar_usuario,text="Registrar",font=(FUENTE[0],10),anchor=CENTER,bg=COLOR_BOTONES,foreground="white",padx=55,command= lambda:verificar_datos(entry_usuario,bool_usuario_validado,entry_contraseña,bool_contraseña_validada,confirmar_contraseña,bool_confirmar_validada,advertencia_usuario,advertencia_contraseña,advertencia_confirmar,pregunta,entry_recuperar,info,raiz_registrar_usuario)).place(x=80,y=350)

    Button(frame_registrar_usuario,text="Cancelar",font=(FUENTE[0],10),anchor=CENTER,bg=COLOR_BOTONES,foreground="white",padx=55,command=lambda:cancelar_ventana(raiz_registrar_usuario)).place(x=290,y=350)

def mostrar_info(text,text_por_defecto):
    """esta funcion muestra informacion para crear el usuario y la contraseña
    Responsable= Iñaki"""
    if text_por_defecto.get()=="Nombre de usuario":
        text.config(state=NORMAL,foreground="White")
        text.delete(1.0,END)
        text.insert(END,"Para crear el usuario:\n*debe tener entre (5-15) caracteres \n*solo se permite letras(a-z),numeros\n(0-9) o “_” “-” “.” ")
        text.config(state=DISABLED)
    if text_por_defecto.get()=="Contraseña":
        text.config(state=NORMAL,foreground="White")
        text.delete(1.0,END)
        text.insert(END,"La contraseña debe tener:\n*entre (4-8) caracteres\n*una mayuscula\n*una minuscula \n*un numero\n*algunos de estos caracteres \n“_” “-” “#” “*”")

def ocultar_info(text):
    """esta funcion se encarga de ocultar la informacion para el registro del usuario
    Responsable= Iñaki"""
    text.config(state=NORMAL)
    text.delete(1.0, END)
    text.config(state=DISABLED)


def verificar_datos(usuario_ingresado,usuario_aprobado,contraseña_ingresada,contraseña_aprobada,confirmar,confirmar_aprobado,advertencia_usuario,advertencia_contraseña,advertencia_confirmar,pregunta_seguridad,entry_recuperar,advertencia_pregunta_seguridad,raiz_registrar_usuario): 
    """esta funcion comprueba si ya aprobre los datos con el evento de ENTER,chequeasi eligio una pregunta de suguridad y veo si respondio,
       y si cumplen todas las condiciones guardo los datos.
       Responsable= Iñaki
    """
    #veo si ya aprobre los datos con el evento de ENTER
    if not usuario_aprobado.get():
        usuario_aprobado=procesar_usuario_ingresado(usuario_ingresado,advertencia_usuario,usuario_aprobado)
    if not contraseña_aprobada.get():
        contraseña_aprobada=procesar_contraseña_ingresada(contraseña_ingresada,advertencia_contraseña,contraseña_aprobada)
    if not confirmar_aprobado.get():
        confirmar_aprobado=procesar_confirmar_ingresado(confirmar,advertencia_confirmar,contraseña_ingresada,confirmar_aprobado)
    
    #chequeo si eligio una pregunta de suguridad y veo si respondio
    advertencia_pregunta_seguridad.config(state=NORMAL,foreground=COLOR_FUENTE)
    advertencia_pregunta_seguridad.delete(1.0, END)
    if pregunta_seguridad.get()=="Elija una opción:":
        advertencia_pregunta_seguridad.insert(END,"No elijio una opción")
    if pregunta_seguridad.get()!="Elija una opción:" and entry_recuperar.get()=="":
        advertencia_pregunta_seguridad.insert(END,"Respuesta invalida")
    advertencia_pregunta_seguridad.config(state=DISABLED)

    #si cumplen todas las condiciones guardo los datos
    if contraseña_aprobada and confirmar_aprobado and usuario_aprobado and pregunta_seguridad!="Pregunta de seguridad" and entry_recuperar.get()!="": 
            with open("datos_registrados.csv","a") as archivo:
                linea = "{},{},{},{},0\n".format(usuario_ingresado.get(),contraseña_ingresada.get(),pregunta_seguridad.get(),entry_recuperar.get())
                archivo.write(linea)

            raiz_registrar_usuario.destroy()
            messagebox.showinfo("Registrar usuario","Usuario registrado exitosamente")      

def procesar_usuario_ingresado(usuario_ingresado,advertencia_usuario,usuario_aprobado):
    """ esta funcion valida y procesa el nombre de usuario ingresado, mostrando mensajes de advertencia según sea necesario y
      retorna el estado de aprobación del usuario.
      Responsable= Iñaki
    """
    
    usuario_validado=validar_usuario(usuario_ingresado.get()) #usuario_validado es TRUE o una devolucion para el usuario

    advertencia_usuario.config(state=NORMAL)
    advertencia_usuario.delete(1.0, END)

    usuario_aprobado.set(False)

    list_usuarios=usuario_registrados()

    if usuario_ingresado.get()!="Nombre de usuario":
        if usuario_validado!=True:   
            usuario_ingresado.config(foreground="Black")
            advertencia_usuario.insert(END,usuario_validado) #Si el usuario no es correcto le muestro la devolucion
        else:
            #me fijo si el usuario ya estaba registrado
            if usuario_ingresado.get() in list_usuarios:
                    advertencia_usuario.insert(END,"Usuario ya ingresado\nPruebe con otro")
                    advertencia_usuario.config(state=DISABLED)
            else:
                usuario_aprobado.set(True)
                usuario_ingresado.config(foreground="green")
    else:
        usuario_ingresado.config(foreground="Black")
        advertencia_usuario.insert(END,"Ingrese un nombre de \nusuario")

    advertencia_usuario.config(state=DISABLED)

    return usuario_aprobado.get()

def procesar_contraseña_ingresada(contraseña_ingresada,advertencia_contraseña,contraseña_aprobada):
    """esta funcion valida y procesa la contraseña ingresada
    Responsable= Iñaki"""
    
    contraseña_validada=validar_contraseña(contraseña_ingresada.get())
    contraseña_aprobada.set(False)

    advertencia_contraseña.config(state=NORMAL)
    advertencia_contraseña.delete(1.0, END)
    if contraseña_ingresada.get()!="Contraseña":
        if contraseña_validada!=True:
            contraseña_ingresada.config(foreground="Black")
            advertencia_contraseña.insert(END,contraseña_validada)
        else:
            contraseña_aprobada.set(True)
            contraseña_ingresada.config(foreground="green")
    else:
        contraseña_ingresada.config(foreground="Black")
        advertencia_contraseña.insert(END,"Ingrese una contraseña")
    advertencia_contraseña.config(state=DISABLED)

    return contraseña_aprobada.get()

def procesar_confirmar_ingresado(confirmar,advertencia_confirmar,contraseña_ingresada,confirmar_aprobado):
    """ esta funcion procesa la confirmación de contraseña ingresada, mostrando mensajes de advertencia según sea necesario y
        retornando el estado de aprobación de la confirmación.
        Responsable= Iñaki
    """
    confirmar_aprobado.set(False)

    advertencia_confirmar.config(state=NORMAL)
    advertencia_confirmar.delete(1.0, END)
    if contraseña_ingresada.get()!="Contraseña":
        if contraseña_ingresada.get()!=confirmar.get():
            confirmar.config(foreground="Black")
            advertencia_confirmar.insert(END,"No coinciden")
        else:
            confirmar_aprobado.set(True)
            confirmar.config(foreground="green")
    advertencia_confirmar.config(state=DISABLED)

    return confirmar_aprobado.get()

def validar_usuario(usuario):
    """esta funcion valida la variable usuario que debe ser un str, devuelve una advertencia para mostrar al usuario o True en caso de estar validada
    Responsable= Iñaki
    
    >>> validar_usuario("Lucas97*###")
    'Solo se permiten letras(a-z),numeros(0-9) y “_” “-” “.” '
    >>> validar_usuario("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    'Se excedio el limite de caracteres(15)'
    >>> validar_usuario("Iña")
    'Usa como minimo 5 caracteres'
    >>> validar_usuario("Iñaki12345")
    True
    >>> validar_usuario("Iñaki")
    True
    """
    caracteres_validos=["_","-","."]
    if 5<=len(usuario)<=15:
        i=0
        respuesta=True

        while respuesta==True and i<len(usuario):  #le puse respuesta==True por que quiero que pare cuando respuesta es un texto 
            if not usuario[i].isalnum() and not usuario[i] in caracteres_validos:
                respuesta="Usa letras(a-z),numeros\n(0-9) o “_” “-” “.” " 

            else:
                i+=1
    else:
        if 15<len(usuario):
            respuesta="Se excedio el limite de\ncaracteres(15)"   
        else:
            respuesta="Usa como minimo 5\n caracteres"

    return respuesta

def validar_contraseña(contraseña):
    """esta funcioin valida la variable contraseña que debe ser un str, devuelve una advertencia para mostrar al usuario o True en caso de estar validada
    Responsable= Iñaki
    
    >>> validar_contraseña("a1")
    'Usa como minimo 4 caracteres'
    >>> validar_contraseña("aaaaaaaaaaaaaaa")
    'Se excedio el limite de caracteres(8)'
    >>> validar_contraseña("aaaa")
    'No puede haber caracteres repetidos adyacentes'
    >>> validar_contraseña("abcd")
    'Debe contener por lo menos una mayuscula'
    >>> validar_contraseña("ABCD")
    'Debe contener por lo menos una minuscula'
    >>> validar_contraseña("Abcd")
    'Debe contener por lo menos un numero'
    >>> validar_contraseña("Abcd91")
    'Debe contener por lo menor uno de estos caracteres “_” “-” “#” “*”'
    >>> validar_contraseña("Abcd91#")
    True
    >>> validar_contraseña("Alg#rit7")
    True
    >>> validar_contraseña("Abcd_#99")
    'No puede haber caracteres repetidos adyacentes'
    """
    if 4<=len(contraseña)<=8:

        Caracteres_solicitados=["_","-",".","#","*"]

        mayusculas=False
        minusculas=False
        num=False
        caracteres=False

        respuesta=True
        i=0

        while respuesta==True and i<len(contraseña):

            if  i <len(contraseña)-1 and contraseña[i]==contraseña[i+1]:
                respuesta="No uses caracteres\nrepetidos adyacentes"

            elif contraseña[i] in Caracteres_solicitados:
                caracteres=True
            elif contraseña[i].isalpha():   
                if contraseña[i].islower():
                    minusculas=True
                else:
                    mayusculas=True
            elif contraseña[i].isnumeric():
                num=True
            else:
                respuesta="Alguno de los caracteres\nno fue reconocido"
            i+=1
        if respuesta==True and not ( mayusculas and minusculas and num and caracteres):
            respuesta=procesar_respuesta(mayusculas,minusculas,num,caracteres)
    else:
        if len(contraseña)<4:
            respuesta="Usa como minimo\n4 caracteres"
        else:
            respuesta="Se excedio el limite de\n caracteres(8)" 
    return respuesta

def procesar_respuesta(mayusculas,minusculas,num,caracteres):
    """esta funcion no te da una devolucion super larga con todo lo que te equivocaste, si te equivocaste en varios campos te da una devolucion parcial 
    Responsable= Iñaki"""    

    if not mayusculas:
        devolucion="Debe contener una\n mayuscula"
    elif not minusculas:
        devolucion="Debe contener una\n minuscula"
    elif not num:
        devolucion="Debe contener un numero"
    elif not caracteres:
        devolucion="Debe contener estos\ncaracteres “_” “-” “#” “*”"
        
    return devolucion

#funciones que se usan en varias ventanas (obj1 parte 2)
def mostrar_contraseña_confirmacion(control,contraseña,text_contraseña_por_defecto,confirmar=99,Texto_pordecto_confirmar=99):
    """Esta funcion muestra o oculta el contenido de los entrys de contraseña o el de confirmacion
    Responsable= Iñaki"""

    if contraseña.get()!=text_contraseña_por_defecto:

        if control.get()==0:
            contraseña.config(show="*")
        else: 
            contraseña.config(show="")
    
    if confirmar!=99 and text_contraseña_por_defecto!=99:
        if  confirmar.get()!=Texto_pordecto_confirmar:
            if control.get()==0:
                confirmar.config(show="*")
            else: 
                confirmar.config(show="")

def entry_focus_in(entry,text_pordefecto,variable_para_usar,text_pordefecto_top,advertencia,control_contraseña=99):
    """Esta funcion es para borrar los textos por defecto de los entry y los muestra arriva del entry
    Responsable= Iñaki"""

    advertencia.config(state=NORMAL)
    advertencia.delete(1.0,END)
    advertencia.config(state=DISABLED)

    if entry.get()==text_pordefecto.get():
        entry.config(textvariable=variable_para_usar)
        text_pordefecto_top.config(foreground="white")

    if control_contraseña==0:
        entry.config(show="*")

def entry_focus_out(entry,text_pordefecto,text_pordefecto_top):
    """Esta funcion es para volver a poner los textos por defecto en los entry, si el usuario dejo vacio el espacio"""
    if entry.get()=="":
        entry.config(textvariable=text_pordefecto,show="")
        text_pordefecto_top.config(foreground=COLOR)

def leer_archivo(archivo):
    """ esta funcion lee una línea del archivo y devulve sus elementos como una tupla.Si no hay más líneas en el archivo, devuelve una tupla vacía con valores predeterminados.
    Responsable= Iñaki"""
    linea = archivo.readline()
    if linea:
        devolver = linea.rstrip("\n").split(",")
    else:
        devolver = "","","","",0
    return devolver

def cancelar_ventana(raiz_ventana):
    """esta funcion muestra un cuadro de diálogo de confirmación preguntando al usuario si está seguro de que desea cancelar. Si la respuesta es afirmativa, la función destrye la raíz de la ventana 
    Responsable= Iñaki"""
    respuesta=messagebox.askyesno("TP Grupal - Grupo: ESPADACHINES ","¨¿Esta seguro que desea cancelar?")
    if respuesta:
        raiz_ventana.destroy()


#Cifrado/descifrado y envio de mensajes parte 1 objetivo 3 
def cifrar_enviar_mensajes(usuario_actual):
    """
    Funcion que crea la segunda ventana luego de apretar continuar.
    Responsable= Juan Martín
    """
    raiz_ventana = Tk()
    raiz_ventana.title("Cifrado y envio de mensajes-usuario: {}".format(usuario_actual))
    raiz_ventana.resizable(0, 0)
    raiz_ventana.config(bg=COLOR)
    raiz_ventana.iconbitmap("espadachines.ico")
    
    #frame donde se ingresa el mensaje
    frame_mensaje = Frame(raiz_ventana, bg=COLOR,bd=8,relief= RIDGE)
    frame_mensaje.grid(row=0, column=0, sticky="nsew")
    texto_mensaje = Label(frame_mensaje, text="Mensaje",foreground= COLOR_FUENTE,bg=COLOR,font= FUENTE)
    texto_mensaje.grid(row=0, column=0, padx=5, pady=5,sticky='w')
    entrada_mensaje = Text(frame_mensaje,width=33, height=12, relief=SUNKEN, bd=2)
    entrada_mensaje.grid(row=1, column=1, padx=5, pady=5)
    scroll=Scrollbar(frame_mensaje,command=entrada_mensaje.yview)
    scroll.grid(row=1, column=2, padx=5, pady=5,sticky="nsew")
    entrada_mensaje.config(yscrollcommand=scroll.set)

    boton_abrir = Button(frame_mensaje, text="Abrir Archivo '.txt'",font=(FUENTE[0],10),anchor=CENTER,padx=40,bg=COLOR_BOTONES,foreground=COLOR_FUENTE, command=lambda:abrir_archivo(entrada_mensaje))
    boton_abrir.grid(row=0, column=1)
    
 
    #Frame donde el usuario tiene opciones de personalizacion del programa
    frame_modos = Frame(raiz_ventana, bg=COLOR,bd=8,relief= RIDGE)
    frame_modos.grid(row=0, column=1, sticky="nsew")
    texto_modo = Label(frame_modos, text="Tipo de cifrado",foreground= COLOR_FUENTE,bg=COLOR,font= FUENTE)
    texto_modo.grid(row=0, column=0, columnspan=2, padx=5, pady=5)  
    

    variable_radiobuttons = IntVar()
    variable_radiobuttons.set(-1)

    caja_cesar = Radiobutton(frame_modos,text="Cesar",font= FUENTE, variable=variable_radiobuttons,selectcolor=COLOR,foreground=COLOR_FUENTE, value=1,activebackground=COLOR,activeforeground=COLOR_FUENTE, bg=COLOR,command=lambda:activar_desactivar_entry(entrada_clave,texto_clave,variable_radiobuttons))
    caja_cesar.grid(row=4, column=1)

    caja_atbash = Radiobutton(frame_modos,text="Atbash",font= FUENTE, variable=variable_radiobuttons,selectcolor=COLOR,foreground=COLOR_FUENTE, value=2,activebackground=COLOR,activeforeground=COLOR_FUENTE, bg=COLOR,command=lambda:activar_desactivar_entry(entrada_clave,texto_clave,variable_radiobuttons))
    caja_atbash.grid(row=4, column=0)

    texto_clave = Label(frame_modos, text="Clave: ",foreground= COLOR_FUENTE,font= FUENTE,bg=COLOR,state=DISABLED)
    texto_clave.grid(row=4, column=2, padx=5, pady=5)

    entrada_clave=Entry(frame_modos, relief=SUNKEN, bd=2,state=DISABLED)
    entrada_clave.grid(row=4, column=3, padx=5, pady=5)

    Label(frame_modos,text="Procesar mensaje",font= FUENTE,foreground= COLOR_FUENTE,bg=COLOR).grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    boton_cifrar = Button(frame_modos,text="Cifrar",font=(FUENTE[0],10),anchor=CENTER,padx=30,bg=COLOR_BOTONES,foreground=COLOR_FUENTE, command= lambda: verificar_cifrado(variable_radiobuttons.get(), entrada_mensaje, entrada_clave.get()))
    boton_cifrar.grid(row=6, column=0, padx=5, pady=5)
   

    boton_descifrar = Button(frame_modos,text="Descifrar",font=(FUENTE[0],10),anchor=CENTER,padx=30,bg=COLOR_BOTONES,foreground=COLOR_FUENTE, command= lambda: verificar_cifrado(variable_radiobuttons.get(), entrada_mensaje, entrada_clave.get(),-1))
    boton_descifrar.grid(row=6, column=1, padx=5, pady=5)
  
    Label(frame_modos, text="Enviar mensajes",font= (FUENTE[0],14),foreground= COLOR_FUENTE,bg=COLOR).grid(row=5, column=2, columnspan=2,padx=5, pady=5)

    opcion_elegida=StringVar()
    opcion_elegida.set("No enviar")
    Opciones=["Enviar a todos los usuario"
                    ,"Enviar a un usuario"
                    ,"No enviar"]

    opciones_envio=OptionMenu(frame_modos,opcion_elegida,*Opciones,command=lambda x:destapar_entry_preguntas(entry_usuario_enviar,opcion_elegida))
    opciones_envio.config(width=27)
    opciones_envio.grid(row=6, column=2, columnspan=2,padx=5, pady=5)
    
    entry_usuario_enviar=Entry(frame_modos, relief=SUNKEN,font=(FUENTE[0],12), bd=2,width=25,state=DISABLED)
    entry_usuario_enviar.grid(row=7, column=2, columnspan=2,padx=5, pady=5)

    boton_enviar=Button(frame_modos,text="Enviar",font=(FUENTE[0],10),anchor=CENTER,padx=40,bg=COLOR_BOTONES,foreground=COLOR_FUENTE,command=lambda:enviar_mensaje(opcion_elegida.get(),entry_usuario_enviar.get(),usuario_actual,variable_radiobuttons.get(),entrada_clave.get(),entrada_mensaje.get("1.0", "end-1c")))
    boton_enviar.grid(row=8, column=2, columnspan=2,padx=5, pady=5)

    boton_reiniciar = Button(frame_modos, text="Limpiar entadas",font=(FUENTE[0],10),anchor=CENTER,padx=20,bg=COLOR_BOTONES,foreground=COLOR_FUENTE, command=lambda: limpiar_entradas(entrada_mensaje,entrada_clave,variable_radiobuttons,entry_usuario_enviar,opcion_elegida))
    boton_reiniciar.grid(row=8, column=0,columnspan=2,padx=5, pady=5)


    #frame donde se ven los mensajes recibidos

    frame_mensajes_recibidos = Frame(raiz_ventana, bg=COLOR,bd=8,relief= RIDGE)
    frame_mensajes_recibidos.grid(row=1, column=0,columnspan=2,sticky="nsew")
    texto_mensaje = Label(frame_mensajes_recibidos, text="Mensajes recibidos  ",foreground= COLOR_FUENTE,bg=COLOR,font= FUENTE)
    texto_mensaje.grid(row=0, column=0,columnspan=2, padx=5, pady=5, sticky='w')
    
    pantalla_mensajes_recibidos = Text(frame_mensajes_recibidos,width=105, height=12, relief=SUNKEN, bd=2, state=DISABLED)
    pantalla_mensajes_recibidos.grid(row=2, column=1,columnspan=10,padx=5, pady=5)
    scroll=Scrollbar(frame_mensajes_recibidos,command=pantalla_mensajes_recibidos.yview)
    scroll.grid(row=2, column=11, padx=5, pady=5,sticky="nsew")
    pantalla_mensajes_recibidos.config(yscrollcommand=scroll.set)

    total_mensajes=IntVar(value=0)

    Label(frame_mensajes_recibidos, textvariable=total_mensajes,foreground= COLOR_FUENTE,font= FUENTE,bg=COLOR).grid(row=3, column=0,columnspan=2, padx=5, pady=5, sticky='w')

    mensajes_recibidos(usuario_actual,pantalla_mensajes_recibidos,total_mensajes)
    actualizar = Button(frame_mensajes_recibidos, text='Actualizar',font=(FUENTE[0],10),anchor=CENTER,padx=40,bg=COLOR_BOTONES,foreground=COLOR_FUENTE, command=lambda:mensajes_recibidos(usuario_actual,pantalla_mensajes_recibidos,total_mensajes))
    actualizar.grid(row=3, column=9)

    boton_salir = Button(frame_mensajes_recibidos, text='Cerrar sesion',font=(FUENTE[0],10),anchor=CENTER,padx=40,bg=COLOR_BOTONES,foreground=COLOR_FUENTE, command=lambda:cerrar_sesion(raiz_ventana))
    boton_salir.grid(row=3, column=10)
    

    raiz_ventana.mainloop()

#funciones cifrar_enviar_mensajes
def abrir_archivo(entrada_mensaje):
    """
    Esta funcion te permite abrir un archivo de texto para usar en el cifrado y la imprime en el texto de entrada
    Responsable= Juan Martín
    """
    archivo = filedialog.askopenfile(initialdir="/", title="Seleccionar un archivo de texto", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    if archivo:
        contenido = archivo.read()
        entrada_mensaje.delete(1.0, END)
        entrada_mensaje.insert(END, contenido)
#procesar mensaje
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

def activar_desactivar_entry(entry,label,variable_radiobuttons):
    """esta función configura el estado (activado o desactivado) del widget Entry y la etiqueta según
      el valor de variable_radiobuttons. Si el valor es 2, se desactivan ambos; de lo contrario, se activan para permitir la edición.
      Responsable= Juan Martín
    """
    if variable_radiobuttons.get()==2:
        entry.config(state=DISABLED)
        label.config(state=DISABLED)
    else:
        entry.config(state=NORMAL)
        label.config(state=NORMAL)

def destapar_entry_preguntas(entry,pregunta):
    """esta función configura el widget Entry de acuerdo al valor seleccionado en el StringVar pregunta.
    Si pregunta tiene ciertos valores, se borra el contenido del Entry y se desactiva; de lo contrario, se activa para permitir la edición.
    Responsable= Juan Martín"""
    if pregunta.get()=="Enviar a todos los usuario" or pregunta.get()=="No enviar":
        entry.delete(0,END)
        entry.config(state=DISABLED)
    else:
        entry.config(state=NORMAL)

def verificar_cifrado(variable_radiobuttons, entrada_mensaje, clave,descifrar=1):
    """
    Esta funcion imprime el mensaje segun las opciones de cifrado elegido, en caso de no elgir uno o ingresar una clave inválida, muestra un mensaje de advertencia.
    Responsable= Juan Martín
    """
    mensaje=entrada_mensaje.get("1.0", "end-1c")

    if variable_radiobuttons==1:
        if validar_clave(clave):
            cifrado=cifrado_cesar(mensaje, descifrar*int(clave))
            entrada_mensaje.delete(1.0,END)
            entrada_mensaje.insert(END,cifrado)

        else:
            if len(clave)==0:
                messagebox.showwarning("Clave Inválida", "Debe ingresar una clave para el cifrado César.")
            else:
                messagebox.showwarning("Clave Inválida", "La clave debe ser un número entero.")
    elif variable_radiobuttons==2:
        cifrado=cifrado_atbash(mensaje)
        entrada_mensaje.delete(1.0,END)
        entrada_mensaje.insert(END,cifrado)

    else:
        messagebox.showwarning("Seleccione Opción", "Debe seleccionar una de las opciones para realizar el cifrado.")

#Enviar mensaje
def enviar_mensaje(opcion_elegida,destinatario,remitente,v_radiobutton,clave_cesar,mensaje):
    """ esta función maneja la lógica de enviar mensajes, ya sea a todos los usuarios o a un usuario específico, y dependiendo de la opción de cifrado seleccionada.
        Utiliza funciones como enviar_cesar y enviar_atbash, y muestra mensajes de advertencia o de confirmación según sea necesario
        Responsable= Juan Martín"""
    list_usuarios=usuario_registrados()  
    if opcion_elegida!="No enviar" and mensaje!="":
        if opcion_elegida=="Enviar a todos los usuario":
            respuesta=messagebox.askyesno("Grupo: ESPADACHINES ","¨¿Seguro que desea enviar\n   el mensaje a todos?")
            if respuesta:
                destinatario="Todos"
                if v_radiobutton==1:
                    enviar_cesar(clave_cesar,mensaje,destinatario,remitente)

                elif v_radiobutton==2:
                    enviar_atbash(mensaje,destinatario,remitente)
                else:
                    messagebox.showwarning("Seleccione Opción", "Debe seleccionar una de las opciones para realizar el cifrado de seguridad.")

        else:
            if  destinatario not in list_usuarios:
                messagebox.showwarning("Usuario invalido", "Destinatario Inexistente.")
            else:
                respuesta=messagebox.askyesno("Grupo: ESPADACHINES ","¨¿Seguro que desea enviar\n   el mensaje a {}?".format(destinatario))
                if respuesta:
                    if v_radiobutton==1:
                        enviar_cesar(clave_cesar,mensaje,destinatario,remitente)

                    elif v_radiobutton==2:
                        enviar_atbash(mensaje,destinatario,remitente)
                    else:
                        messagebox.showwarning("Seleccione Opción", "Debe seleccionar una de las opciones para realizar el cifrado de seguridad.")

def enviar_cesar(clave_cesar,mensaje,destinatario,remitente):
    """esta función cifra un mensaje usando el cifrado César si la clave proporcionada es válida, lo prepara para ser guardado en un archivo CSV y utiliza la función guardar_mensaje
       para almacenar el mensaje cifrado en el archivo. Finalmente, muestra mensajes informativos o de advertencia según sea necesario. 
       Responsable= Juan Martín"""
    if validar_clave(clave_cesar):
        cifrado="C"+clave_cesar
        mensaje_cifrado=cifrado_cesar(mensaje,int(clave_cesar))

        mensaje_cifrado_sin_saltos=mensaje_cifrado.replace("\n","///////")
        mensaje_cifrado_sin_comas=mensaje_cifrado_sin_saltos.replace(",","$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

        guardar_mensaje(destinatario,remitente,cifrado,mensaje_cifrado_sin_comas)
        messagebox.showinfo("Grupo: ESPADACHINES","Mensaje enviado.")
    else:
        messagebox.showwarning("Seleccione Opción", "Debe ingresar una clave válida si desea usar cesar como cifrado de seguridad.")

def enviar_atbash(mensaje,destinatario,remitente):
    """esta función cifra un mensaje usando el cifrado Atbash, lo prepara para ser guardado en un archivo CSV,
    y luego utiliza la función guardar_mensaje para almacenar el mensaje cifrado en el archivo. Finalmente, muestra un mensaje informativo.
    Responsable= Juan Martín"""
    cifrado="A"
    mensaje_cifrado=cifrado_atbash(mensaje)

    mensaje_cifrado_sin_saltos=mensaje_cifrado.replace("\n","///////")
    mensaje_cifrado_sin_comas=mensaje_cifrado_sin_saltos.replace(",","$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

    guardar_mensaje(destinatario,remitente,cifrado,mensaje_cifrado_sin_comas)

    messagebox.showinfo("Grupo: ESPADACHINES","Mensaje enviado.")

def usuario_registrados():
    """esta función intenta abrir el archivo "datos_registrados.csv", lee los usuarios del archivo y retorna una lista con los nombres de usuario registrados
    Responsable= Juan Martín"""
    USUARIO=0
    lista_usuarios=[]

    try:
        archivo=open("datos_registrados.csv","r")
    except:
        archivo=open("datos_registrados.csv","a+")
       
    
    datos=leer_archivo(archivo)
    if datos[USUARIO]!="":
        lista_usuarios.append(datos[USUARIO])
    while datos[USUARIO]:
        datos=leer_archivo(archivo)
        if datos[USUARIO]!="":
            lista_usuarios.append(datos[USUARIO])
    archivo.close()

    return lista_usuarios

def guardar_mensaje(destinatario,remitente,cifrado,mensaje_cifrado):
    """esta función agrega un nuevo mensaje al archivo "mensajes.csv" con la información proporcionada, incluyendo el destinatario, el remitente, el método de cifrado y el mensaje cifrado
    Responsable= Juan Martín"""
    with open("mensajes.csv","a") as archivo:
        linea = "{},{},{},{}\n".format(destinatario,remitente,cifrado,mensaje_cifrado)
        archivo.write(linea)
def limpiar_entradas(mensaje, clave,radiobutton_v,usuario_enviar,pregunta):
    """
    Esta funcion borra los campos llenados por el ususario
    Responsable= Juan Martín
    """
    cadena_vacia = ''
    mensaje.delete(1.0, END)
    mensaje.insert(END, cadena_vacia)
    
    clave.config(state=NORMAL)
    clave.delete(0, END)
    clave.insert(0, cadena_vacia)
    
    if radiobutton_v.get()==2:
        clave.config(state=DISABLED)

    pregunta.set("No enviar")
    
    usuario_enviar.config(state=NORMAL)
    usuario_enviar.delete(0, END)
    usuario_enviar.config(state=DISABLED)
#Mostrar mensajes

def mensajes_recibidos(usuario_actual,pantalla_mensajes_recibidos,mostrar_total_mensajes):
    """ esta función procesa mensajes almacenados en un archivo, descifra los mensajes cifrados y muestra los mensajes en la pantalla de mensajes, diferenciando entre mensajes para todos y mensajes para un usuario específico.
    Responsable= Juan Martín"""
    DESTINATARIO=0
    REMITENTE=1
    CIFRADO=2
    MENSAJE_CIFRADO=3
    mensajes_para_todos=[]
    mensajes_para_usuario=[]

    with open ("mensajes.csv","r") as archivo_mensajes:
         for linea in archivo_mensajes:
            linea=linea.rstrip("\n").split(",")

            if linea[DESTINATARIO]==usuario_actual:
                mensaje_con_saltos=linea[MENSAJE_CIFRADO].replace("///////","\n"+"\t")
                mensaje_para_descifrar=mensaje_con_saltos.replace("$$$$$$$$$$$$$$$$$$$$$$$$$$$$",",")

                if linea[CIFRADO][0]=="A":
                    mensaje_descifrado=cifrado_atbash(mensaje_para_descifrar)
                else:
                    mensaje_descifrado=cifrado_cesar(mensaje_para_descifrar,-1*int(linea[CIFRADO][1:]))

                mensajes_para_usuario.append((linea[REMITENTE],mensaje_descifrado))

            elif linea[DESTINATARIO]=="Todos":
                mensaje_con_saltos=linea[MENSAJE_CIFRADO].replace("///////","\n"+"\t")
                mensaje_para_descifrar=mensaje_con_saltos.replace("$$$$$$$$$$$$$$$$$$$$$$$$$$$$",",")
                if linea[CIFRADO][0]=="A":
                    mensaje_descifrado=cifrado_atbash(mensaje_para_descifrar)
                else:
                    mensaje_descifrado=cifrado_cesar(mensaje_para_descifrar,-1*int(linea[CIFRADO][1:]))

                mensajes_para_todos.append((linea[REMITENTE],mensaje_descifrado))

    mostrar_mensajes_recibidos(mensajes_para_todos,mensajes_para_usuario,mostrar_total_mensajes,pantalla_mensajes_recibidos)

def mostrar_mensajes_recibidos(mensajes_para_todos,mensajes_para_usuario,mostrar_total_mensajes,pantalla_mensajes_recibidos):
    """esta función actualiza una pantalla de mensajes con mensajes para todos y mensajes para un usuario específico, mostrando los encabezados apropiados y utilizando separadores para mejorar la legibilidad.
    Responsable= Juan Martín"""
    total_de_mensajes=len(mensajes_para_todos)+len(mensajes_para_usuario)
    mostrar_total_mensajes.set("Total de mensajes: {}".format(total_de_mensajes))

    pantalla_mensajes_recibidos.config(state=NORMAL)
    pantalla_mensajes_recibidos.delete(1.0, END)

    mensajes_para_todos.reverse()
    mensajes_para_usuario.reverse()
    separador=("\n"+"="*105+"\n")
    separador2=("\n"+"-"*105+"\n")
    
    pantalla_mensajes_recibidos.insert(END,"\tMensajes para todos")
    pantalla_mensajes_recibidos.insert(END,separador)

    for mensaje in mensajes_para_todos:
        formato="#{}:\n\t{}".format(mensaje[0],mensaje[1])

        pantalla_mensajes_recibidos.insert(END,formato)
        pantalla_mensajes_recibidos.insert(END,separador2)

    pantalla_mensajes_recibidos.insert(END,"\n"+"\tMensajes particulares")
    pantalla_mensajes_recibidos.insert(END,separador)

    for mensaje in mensajes_para_usuario:
        formato="{}:\n\t{}".format(mensaje[0],mensaje[1])

        pantalla_mensajes_recibidos.insert(END,formato)
        pantalla_mensajes_recibidos.insert(END,separador2)
    
    pantalla_mensajes_recibidos.config(state=DISABLED)

def cerrar_sesion(raiz):
    """esta funcion permite el cierre de sesión
    Responsable= Juan Martín"""
    respuesta=messagebox.askyesno("Grupo: ESPADACHINES ","¨¿Seguro que desea cerrar sesión?")
    if respuesta:
        raiz.destroy()
        ventana_inicio_sesion()

#funciones de cifrado
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
    Responsable= Juan Martín
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


#main del programa
def main():
    ventana1_programa()

main()
