import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

#Configuracion del estilo de graficacion
plt.style.use('ggplot')



# Configuracion de la ventana
ventana = tk.Tk()
ventana.title('Cálculo Diferencial')
ventana.geometry('500x300')


# Creamos una barra de menus en la ventana
barra_menus = tk.Menu(ventana)
ventana.config(menu = barra_menus)

# Creamos un menu y lo anclamos
menu = tk.Menu(barra_menus, tearoff=False)

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

# funciones para abrir nuevas ventanas: graficar, limites y derivadas

# Ventana graficar
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
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ---------------------------------------------------------------------- 



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
    
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

# Opciones del menu
menu.add_command(label = 'Graficador', command = c_graficar)
menu.add_command(label = 'Limites', command = c_limites)
menu.add_command(label = 'Derivadas', command = c_derivadas)

# linea separadora
menu.add_separator()
menu.add_command(label = 'Salir', command=ventana.destroy)
barra_menus.add_cascade(label='Menú', menu = menu)

# Texto
etiqueta1 = ttk.Label(ventana, text="¡Bienvenido!", font=('Helvetica', 16))
etiqueta1.place(x=50, y=20)
etiqueta2 = ttk.Label(ventana, 
                      text="Este es un programa para graficar\ny calcular límites y derivadas.\nExplora las opciones del menú", 
                      font=('Helvetica', 12))
etiqueta2.place(x=50, y=60)
ventana.mainloop()