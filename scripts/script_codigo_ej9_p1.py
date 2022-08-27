# Realiza la importacion de las librerias tkinter
# (asi como del modulo ttk), matplotlib.pyplot,
# numpy y sympy:
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# Configura el estilo de graficacion ggplot
plt.style.use('ggplot')
# Configuracion de la ventana principal
# Crea un objeto ventana
ventana = tk.Tk()
# Asignale un titulo
ventana.title('Cálculo Diferencial')
# Configura un tamanio de 500 px por 300 px
ventana.geometry('500x300')



# Creamos un menu principal en la ventana antes creada
menu_principal = tk.Menu(ventana)
# Agregamos dicho menu a la ventana principal
ventana.config(menu=menu_principal)

# Creamos un submenu de opciones para el
# menu principal
submenu = tk.Menu(menu_principal, tearoff=False)

# Completa segun se te indique:
# Configuramos una nueva ventana correspondiente a
# la opcion de calculadora graficadora
def c_graficar():
    # Creamos una nueva ventana y la denominamos vc_graficar
    vc_graficar = tk.Toplevel()
    # Configura el tamanio de esta nueva ventana en
    # 500px por 200px
    vc_graficar.geometry('500x200')
    # Configuracion de las filas. Establecemos una 
    # proporcion de 1:2 respecto a la fila 0 y 
    # el resto de las filas, entorno al espacio
    # total de dicha ventana
    vc_graficar.rowconfigure(0, weight=1)
    vc_graficar.rowconfigure(1, weight=2)
    vc_graficar.rowconfigure(2, weight=2)
    vc_graficar.rowconfigure(3, weight=2)
    
    # Configuramos las columnas Establecemos una 
    # proporcion de 1:3 respecto a la columna 0 y 
    # columnas 1, entorno al espacio
    # total de dicha ventana
    vc_graficar.columnconfigure(0, weight=1)
    vc_graficar.columnconfigure(1, weight=3)
    

    
    
    # Con lo anterior hemos configurado una relacion de proporcion 1:5 entre el renglon 0 y el renglon 1
    # ------------------------------------------------------

    # Ahora agregaremos una etiqueta de texto a esta
    # nueva ventana:
    #                         ventana donde| texto que
    #                         colocaremos  | se mostrara
    #                         la etiqueta  |
    etiqueta_fun = ttk.Label(vc_graficar, text='Ingrese la función: ')
    # Posicion de la etiqueta
    etiqueta_fun.grid(row=0, column=0, sticky='NSWE')
    # ------------------------------------------------------

    # Caja de texto para que el usuario ingrese la funcion.
    # La caja de texto se mostrara en esta nueva ventana
    caja_fun = ttk.Entry(vc_graficar, width=15)
    # Posicion de la caja de texto
    #                                                           pequenio margen
    #                                                           a la caja de texto
    caja_fun.grid(row=0, column=1, sticky='NSWE', columnspan=2, padx=5, pady=5)

    # ------------------------------------------------------

    # Ahora definiremos las funciones que realizaran
    # las acciones de nuestros botones.
    # Accion del boton _graficar_
    def graficar():
        # Rango fijo de graficacion
        x = np.arange(-3, 3, 0.1)
        # Obtendremos la funcion que el usuario ingreso
        # en la caja de texto caja_fun, para lo cual
        # utilizaremos el metodo get() como sigue
        #          Recuperamos la funcion
        #          que el usuario ingreso
        fun_str = caja_fun.get()
        # El siguiente codigo nos permite realizar
        # evaluaciones numericas sobre variables de tipo
        # string. Recordemos que la funcion que ingreso el
        # usuario es una cadena de texto.
        y = eval(fun_str)
        # Graficamos la funcion
        plt.plot(x, y)
        # Agregamos un titulo al grafico
        plt.title(f'f(x)={fun_str}')
        # Mostramos el grafico creado
        plt.show()
# Accion del boton graficar_rac

    def graficar_rac():
        # Rango fijo
        x = np.arange(-3, 3, 0.1, dtype=float)
        # funcion (la obtenemos de la caja_fun)
        fun_str = caja_fun.get()
        # Comando para poder evaluar numericamente
        # cadenas de texto
        y = eval(fun_str)
        # Establecemos un limite de rango de graficacion
        # del eje y
        plt.ylim(-3, 3)
        # graficamos la funcion
        plt.plot(x, y)
        # Creamos un titulo y mostramos el grafico
        plt.title(f'f(x)={fun_str}')
        plt.show()

    # Accion del boton graficar_trigo
    def graficar_trigo():
        # Rango fijo. En este caso los rangos de graficacion
        # seran en terminos del numero pi
        x = np.arange(-2 * np.pi, 2 * np.pi, 0.1, dtype=float)
        # funcion (la obtenemos de la caja_fun)
        fun_str1 = caja_fun.get()
        # Para el caso en que la funcion a graficar sea
        # la funcion tangente cambiaremos el
        # limite de rango de graficacion del eje y
        if fun_str1[:3] == 'tan':
            plt.ylim(-3, 3)

        # Para trabajar con funciones trigonometricas nos
        # auxiliaremos de la libreria numpy
        fun_str2 = 'np.' + fun_str1
        # Comando para poder evaluar numericamente
        # cadenas de texto
        y = eval(fun_str2)
        # graficamos
        plt.plot(x, y)
        # Creamos un titulo y mostramos el grafico
        plt.title(f'f(x)={fun_str1}')
        plt.show()

    # Accion del boton  graficar_exp_log
    def graficar_exp_log():
        # Rango fijo
        x = np.arange(-3, 3, 0.1, dtype=float)
        # funcion (la obtenemos de la caja_fun)
        fun_str1 = caja_fun.get()
        # Para trabajar con funciones exponenciales y
        # logaritmicas nos auxiliaremos de la libreria numpy
        fun_str2 = 'np.' + fun_str1
        # Comando para poder evaluar numericamente
        # cadenas de texto
        y = eval(fun_str2)
        # Graficamos
        plt.ylim(-3, 3)
        plt.plot(x, y)
        # Mostramos
        plt.title(f'f(x)={fun_str1}')
        plt.show()
    # Botones:

    # --------------------------------------------------------------------------
    # BOTON PARA GRAFICAR
    #                          ventana donde| texto a mostrar| funcion o accion a
    #                         lo colocaremos|                | asociar al boton
    boton_graficar = ttk.Button(vc_graficar, text='Graficar', command=graficar)
    # Posicion de este boton
    boton_graficar.grid(row=1, column=0, sticky='NSWE')
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # BOTON PARA GRAFICAR FUNCIONES RACIONALES
    boton_graficar_rac = ttk.Button(vc_graficar,
                                    text='Graficar fun racional',
                                    command=graficar_rac)
    # Posicion de este boton
    boton_graficar_rac.grid(row=1, column=1, sticky='NSWE')
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # BOTON PARA GRAFICAR FUNCIONES TRIGONOMETRICAS
    boton_graficar_trigo = ttk.Button(vc_graficar,
                                      text='Graficar Trigonometric',
                                      command=graficar_trigo)
    # Posicion de este boton
    boton_graficar_trigo.grid(row=1, column=2, sticky='NSWE')
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # BOTON PARA GRAFICAR FUNCIONES EXPONENCIALES Y LOGARITMICAS
    boton_graficar_exp_log = ttk.Button(vc_graficar,
                                        text='Graficar Exp/ log',
                                        command=graficar_exp_log)
    # Posicion de este boton
    boton_graficar_exp_log.grid(row=2, column=0, sticky='NSWE')
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # CONFIGURACION DE UN BOTON PARA SALIR DE LA VENTANA DE GRAFICACION

    # Para sallir de una ventana o cerrarla escribimos:
    # <nombre de la ventana>.destroy
    boton_graf_salir = ttk.Button(
        vc_graficar,
        text='Regresar',
        # accion que hara nuestro boton
        command=vc_graficar.destroy)
    # Posicion de este boton
    boton_graf_salir.grid(row=2, column=1, sticky='NSWE')


# Opciones del menu:

# Agregamos una opcion a nuestra submenu. Esta opcion
# abrira la ventana nueva que creamos con la interfaz
# para graficar funciones.
#                   nombre de la opcion| accion que hara esta opcion
#                   agregada a nuestro | en este caso la accion sera
#                   submenu            | ejecutar la funcion c_graficar
#                                      | que crea la ventana con la
#                                      | interfaz para graficar
submenu.add_command(label='Graficador', command=c_graficar)

# Mostramos una linea separadora
submenu.add_separator()

# Agregamos la opcion para salir de nuestro programa
#                                    cerraremos la ventana principal
submenu.add_command(label='Salir', command=ventana.destroy)

# Agregamos el submenu al menu principal
#                    nombre del menu | submenu a
#                    principal       | agregar
menu_principal.add_cascade(label='Menú', menu=submenu)

# Mas etiquetas
#                                                    especificamos la tipografia
#                                                    y el tamaño de la letra
etiqueta1 = ttk.Label(ventana, text="¡Bienvenido!", font=('Helvetica', 16))
# posicion de la etiqueta
etiqueta1.place(x=50, y=20)

# -------------------------------------------------------------------------------
etiqueta2 = ttk.Label(
    ventana,
    text="Este es un programa para graficar\ny calcular límites y derivadas",
    font=('Helvetica', 12))
# posicion de la etiqueta
etiqueta2.place(x=50, y=60)

# Mostramos la ventana principal creada
ventana.mainloop()