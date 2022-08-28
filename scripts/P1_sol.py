# TU NOMBRE:

# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------
# EJERCICIO 1
# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------
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


# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------
# EJERCICIO 2
# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------

# Configuracion de la ventana principal
# Crea un objeto ventana denominado _ventana_
ventana = tk.Tk()
# Asignale un titulo
ventana.title('Cálculo Diferencial')
# Configura un tamanio de 500 px por 300 px
ventana.geometry('500x300')

# Creamos un menu principal en la ventana antes creada
menu_principal = tk.Menu(ventana)
# Agregamos dicho menu a la ventana principal
ventana.config(menu = menu_principal)

# Creamos un submenu de opciones para el
# menu principal
submenu = tk.Menu(menu_principal, tearoff=False)


# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------
# EJERCICIO 3
# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------

# Completa segun se te indique:

# Configuramos una nueva ventana correspondiente a 
# la opcion de calculadora graficadora
# Completa segun se te indique:
def c_graficar():
    # Creamos una nueva ventana y la denominamos vc_graficar
    vc_graficar = tk.Toplevel()
    # Configura el tamanio de esta nueva ventana en
    # 500px por 200px
    vc_graficar.geometry('500x200')
    # ------------------------------------------------------
    
    # Ahora agregaremos una etiqueta de texto a esta 
    # nueva ventana:
    #                         ventana donde| texto que
    #                         colocaremos  | se mostrara
    #                         la etiqueta  |
    etiqueta_fun = ttk.Label(vc_graficar, text='Ingrese la función: ')
    # Posicion de la etiqueta
    etiqueta_fun.place(x = 20, y = 20)
    # ------------------------------------------------------
    
    # Caja de texto para que el usuario ingrese la funcion.
    # La caja de texto se mostrara en esta nueva ventana
    caja_fun = ttk.Entry(vc_graficar)
    # Posicion de la caja de texto
    caja_fun.place(x = 120, y = 20, width = 80)
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

# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------
# EJERCICIO 4
# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------

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
        plt.ylim(-3,3)
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
            plt.ylim(-3,3)
            
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
        plt.plot(x, y)
        # Mostramos
        plt.title(f'f(x)={fun_str1}')
        plt.show()

# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------
# EJERCICIO 5
# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------


    # Botones:
    # --------------------------------------------------------------------------
    # BOTON PARA GRAFICAR
    #                          ventana donde| texto a mostrar| funcion o accion a 
    #                         lo colocaremos|                | asociar al boton
    boton_graficar = ttk.Button(vc_graficar, text='Graficar', command = graficar)
    # Posicion de este boton
    boton_graficar.place(x=20, y=60)
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # BOTON PARA GRAFICAR FUNCIONES RACIONALES
    boton_graficar_rac = ttk.Button(vc_graficar, text='Graficar fun racional', 
                                    command = graficar_rac)
    # Posicion de este boton
    boton_graficar_rac.place(x=330, y=60)
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # BOTON PARA GRAFICAR FUNCIONES TRIGONOMETRICAS
    boton_graficar_trigo = ttk.Button(vc_graficar, text='Graficar Trigonometric', 
                                      command = graficar_trigo)
    # Posicion de este boton
    boton_graficar_trigo.place(x=100, y=60)
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # BOTON PARA GRAFICAR FUNCIONES EXPONENCIALES Y LOGARITMICAS
    boton_graficar_exp_log = ttk.Button(vc_graficar, text='Graficar Exp/ log', 
                                        command = graficar_exp_log)
    # Posicion de este boton
    boton_graficar_exp_log.place(x=230, y=60)
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # CONFIGURACION DE UN BOTON PARA SALIR DE LA VENTANA DE GRAFICACION
    
    # Para sallir de una ventana o cerrarla escribimos: 
    # <nombre de la ventana>.destroy
    boton_graf_salir = ttk.Button(vc_graficar, text='Regresar', 
                                  # accion que hara nuestro boton
                                  command = vc_graficar.destroy)
    # Posicion de este boton
    boton_graf_salir.place(x=20, y=100)

# ---------------------------------------------------------

# Ignora lo que se te pide aqui. Este espacio lo ocuparas hasta
# el ejercicio 10
# NOMBRE CLAVE: BOB PANTALONES CUADRADOS

# Ventana correspondiente al calculo de limites
# Ventana limites
def c_limites():
    # Ventana nueva
    vc_limites = tk.Toplevel()
    vc_limites.geometry('500x200')
    # Configuracion de las filas. Establecemos una 
    # proporcion de 1:2 respecto a la fila 0 y 1 
    # el resto de las filas, entorno al espacio
    # total de dicha ventana.
    # (Sugerencia)
    vc_limites.rowconfigure(0, weight=1)
    vc_limites.rowconfigure(1, weight=1)
    vc_limites.rowconfigure(2, weight=2)
    vc_limites.rowconfigure(3, weight=2)
    # Configuramos las columnas Establecemos una 
    # proporcion de 1:2 respecto a la columna 0 y 
    # columnas 1, entorno al espacio
    # total de dicha ventana
    vc_limites.columnconfigure(0, weight=1)
    vc_limites.columnconfigure(1, weight=2)
    
    # Texto
    etiqueta_fun = ttk.Label(vc_limites, text='Ingrese la función:')
    etiqueta_fun.grid(row=0, column=0, sticky='NSWE')
    etiqueta_fun_x = ttk.Label(vc_limites, text='Hacía qué valor\ntiende x:')
    etiqueta_fun_x.grid(row=1, column=0, sticky='NSWE')

    # Caja para que el usuario ingrese la funcion
    caja_fun = ttk.Entry(vc_limites)
    caja_fun.grid(row=0, column=1, sticky='NSWE')
    caja_x = ttk.Entry(vc_limites)
    caja_x.grid(row=1, column=1, sticky='NSWE')
    
    # Acciones asociadas a los botones que definiremos abajo.
    # Limpiar celdas de las cajas
    def clear_text():
        caja_fun.delete(0, tk.END)
        caja_x.delete(0, tk.END)
            
    # Funcion para calcular el limite
    def calcular_lim():
        x = sp.symbols('x')
        # funcion
        y = caja_fun.get()
        # Valor del limite
        limite = sp.limit(y,x, eval(caja_x.get()))
        # Etiqueta para mostrar el resultado
        etiqueta_resul_lim = ttk.Label(vc_limites, 
            text = f'El límite de f(x)={caja_fun.get()} cuando x tiende a {caja_x.get()} es {limite}')
        etiqueta_resul_lim.grid(row=3, column=0, columnspan=2, sticky='NSWE')
        
    # Botones
    # Boton para calcular el limite de una funcion
    boton_calc = ttk.Button(vc_limites, text='Calcular', command = calcular_lim)
    boton_calc.grid(row=2, column=0, sticky='NSWE')
    # Boton para limpiar la caja de texto
    boton_calc_nuevo = ttk.Button(vc_limites, text='Nuevo', command = clear_text)
    boton_calc_nuevo.grid(row=2, column=1, sticky='NSWE')
    # Boton para salir de la venta vc_limites
    boton_calc_salir = ttk.Button(vc_limites, text='Regresar', command = vc_limites.destroy)
    boton_calc_salir.grid(row=4, column=0, columnspan=2, sticky='NSWE')

# ---------------------------------------------------------


# ---------------------------------------------------------

# Ignora lo que se te pide aqui. Este espacio lo ocuparas hasta
# el ejercicio 11
# NOMBRE CLAVE: KND los chicos del barrio

# Ventana correspondiente al calculo de derivadas
def c_derivadas():
    # Creamos una ventana nueva
    vc_derivadas = tk.Toplevel()
    # Titulo de la ventana
    vc_derivadas.title('Derivadas')
    # Tamanio
    vc_derivadas.geometry('500x200')
    # Configuracion de las filas. Establecemos una 
    # proporcion de 1:2 respecto a la fila 0 y 
    # el resto de las filas, entorno al espacio
    # total de dicha ventana
    vc_derivadas.rowconfigure(0, weight=1)
    vc_derivadas.rowconfigure(1, weight=1)
    vc_derivadas.rowconfigure(2, weight=4)
    vc_derivadas.rowconfigure(3, weight=4)
    
    # Configuramos las columnas Establecemos una 
    # proporcion de 1:3 respecto a la columna 0 y 
    # columnas 1, entorno al espacio
    # total de dicha ventana
    vc_derivadas.columnconfigure(0, weight=1)
    vc_derivadas.columnconfigure(1, weight=2)

    # Texto
    etiqueta_fun = ttk.Label(vc_derivadas, text='Ingrese la función:')
    etiqueta_fun.grid(row=0, column=0, sticky='NSWE')
    etiqueta_fun_ord = ttk.Label(vc_derivadas, text='Orden de \nderivación:')
    etiqueta_fun_ord.grid(row=1, column=0, sticky='NSWE')

    # Caja para que el usuario ingrese la funcion
    caja_fun = ttk.Entry(vc_derivadas)
    caja_fun.grid(row=0, column=1, sticky='NSWE')
    caja_ord = ttk.Entry(vc_derivadas)
    caja_ord.grid(row=1, column=1, sticky='NSWE')
    # Limpiar celdas de las cajas
    def clear_text():
        caja_fun.delete(0, tk.END)
        caja_ord.delete(0, tk.END)

    # Funcion para calcular la derivada
    def calcular_der():
        x = sp.symbols('x')
        # funcion
        x = sp.symbols('x')
        y = caja_fun.get()
        # derivada
        derivada = sp.diff(y,x,eval(caja_ord.get()))
        # Etiqueta
        etiqueta_resul_der = ttk.Label(vc_derivadas, 
            text = f'La derivada de f(x)={caja_fun.get()} de orden {caja_ord.get()} es {derivada}')
        etiqueta_resul_der.grid(row=3, column=0, sticky='NSWE', columnspan=2)

    # Botones
    boton_calc = ttk.Button(vc_derivadas, text='Calcular', command = calcular_der)
    boton_calc.grid(row=2, column=0, sticky='NSWE')
    boton_calc_nuevo = ttk.Button(vc_derivadas, text='Nuevo', command = clear_text)
    boton_calc_nuevo.grid(row=2, column=1, sticky='NSWE')
    boton_calc_salir = ttk.Button(vc_derivadas, text='Regresar', command = vc_derivadas.destroy)
    boton_calc_salir.grid(row=4, column=0, sticky='NSWE', columnspan=2)

# ---------------------------------------------------------



# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------
# EJERCICIO 6
# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------

# Opciones del menu:

# Agregamos una opcion a nuestra submenu. Esta opcion
# abrira la ventana nueva que creamos con la interfaz
# para graficar funciones.
#                   nombre de la opcion| accion que hara esta opcion
#                   agregada a nuestro | en este caso la accion sera
#                   submenu            | ejecutar la funcion c_graficar
#                                      | que crea la ventana con la 
#                                      | interfaz para graficar
submenu.add_command(label = 'Graficador', command = c_graficar)

# ---------------------------------------------------------

# Ignora lo que se te pide aqui. Este espacio lo ocuparas hasta
# la parte final del proyecto
# NOMBRE CLAVE: Bombon, Burbuja y Bellota

submenu.add_command(label = 'Limites', command = c_limites)
submenu.add_command(label = 'Derivadas', command = c_derivadas)

# ---------------------------------------------------------


# Mostramos una linea separadora
submenu.add_separator()

# Agregamos la opcion para salir de nuestro programa
#                                    cerraremos la ventana principal   
submenu.add_command(label = 'Salir', command = ventana.destroy)

# Agregamos el submenu al menu principal
#                    nombre del menu | submenu a 
#                    principal       | agregar
menu_principal.add_cascade(label='Menú', menu = submenu)

# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------
# EJERCICIO 7
# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------

# Mas etiquetas
#                                                    especificamos la tipografia
#                                                    y el tamaño de la letra
etiqueta1 = ttk.Label(ventana, text="¡Bienvenido!", font=('Helvetica', 16))
# posicion de la etiqueta
etiqueta1.place(x=50, y=20)

# -------------------------------------------------------------------------------
etiqueta2 = ttk.Label(ventana, 
                      text="Este es un programa para graficar\ny calcular límites y derivadas", 
                      font=('Helvetica', 12))
# posicion de la etiqueta
etiqueta2.place(x=50, y=60)

# Mostramos la ventana principal creada
ventana.mainloop()

# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------
# EJERCICIO 8
# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------

# Ejecuta el codigo que llevas hasta ahora y compara como se te indico

# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------
# EJERCICIO 9
# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------

# Realiza las indicaciones que se dicen respecto a este ejercicio
# EL CODIGO SOLUCION CORRESPONDIENTE A DICHO EJERCICIO LO ENCUENTRAS
# EN LA NOTEBOOK SOLUCION DEL PROYECTO 1. LO QUE PUEDES HACER ES COPIAR
# EL CODIGO QUE ESTA EN LA CELDA DE CODIGO CORRESPONDIENTE AL EJERCICIO 9
# Y PEGARLO EN LA DEFINICION DE LA FUNCION c_graficar.PUEDES CHECAR 
# EL CODIGO TOTAL SOLUCION HASTA ESTE EJERCICIO CONSULTADANDO EL SIGUIENTE ENLACE
# https://github.com/CursoPyPagina/CursoPy/blob/gh-pages/scripts/script_codigo_ej9_p1.py


# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------
# EJERCICIO 10
# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------

# Realiza lo que se te pide en este ejercicio. Copia el codigo 
# en la celda de codigo debajo de la indicacion del ejercicio 10 y
# pegalo donde escribimos: 

# NOMBRE CLAVE: BOB PANTALONES CUADRADOS

# lineas arriba. Ten cuidado con la identacion 


# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------
# EJERCICIO 11
# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------

# Realiza lo que se te pide en este ejercicio. Copia el codigo 
# en la celda de codigo debajo de la indicacion del ejercicio 11 y
# pegalo donde escribimos: 

# NOMBRE CLAVE: KND los chicos del barrio

# lineas arriba. Ten cuidado con la identacion 


# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------
# Para finalizar
# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------

# Agrega las siguientes dos lineas de codigo:

# submenu.add_command(label = 'Limites', command = c_limites)
# submenu.add_command(label = 'Derivadas', command = c_derivadas)

# sin los comentarios, donde escribimos: 

# NOMBRE CLAVE: Bombon, Burbuja y Bellota

# lineas arriba. Ten cuidado con la identacion 