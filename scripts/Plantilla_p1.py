
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
# .
# .
# .

# Configura el estilo de graficacion ggplot
# .
# .
# .


# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------
# EJERCICIO 2
# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------

# Configuracion de la ventana principal
# Crea un objeto ventana denominado _ventana_
# .

# Asignale un titulo
# .

# Configura un tamanio de 500 px por 300 px
# .


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
def c_graficar():
    # Creamos una nueva ventana y la denominamos vc_graficar
    # auxiliandonos del metodo Toplevel()
    vc_graficar = tk.Toplevel()
    # Configura el tamanio de esta nueva ventana en
    # 500px por 200px
    vc_graficar._ _ _ 
    # ------------------------------------------------------
    
    # Ahora agregaremos una etiqueta de texto a esta 
    # nueva ventana:
    #                         ventana donde| texto que
    #                         colocaremos  | se mostrara
    #                         la etiqueta  |
    etiqueta_fun = ttk._ _ _ (vc_graficar, text='Ingrese la función: ')
    # Posicion de la etiqueta
    etiqueta_fun.place(x = 20, y = 20)
    # ------------------------------------------------------
    
    # Caja de texto para que el usuario ingrese la funcion.
    # La caja de texto se mostrara en esta nueva ventana
    caja_fun = ttk._ _ _ (vc_graficar)
    # Posicion de la caja de texto y capacidad de caracteres
    caja_fun.place(x = 120, y = 20, width = 80)
    # ------------------------------------------------------
    
    # Ahora definiremos las funciones que realizaran
    # las acciones de nuestros botones.
    # Accion del boton  graficar.
    # (Para graficar funciones polinomiales)
    def graficar():
        # Rango fijo de graficacion
        x = np.arange(-3, 3, 0.1)
        # Obtendremos la funcion que el usuario ingreso
        # en la caja de texto caja_fun, para lo cual
        # utilizaremos el metodo get() como sigue
        #          Recuperamos la cadena de texto
        #          que el usuario ingreso.
        #          Dicha cadena de texto corresponde
        #          a la funcion a graficar
        fun_str = caja_fun.get()
        # El siguiente codigo nos permite realizar
        # evaluaciones numericas sobre variables de tipo
        # string. Recordemos que la funcion que ingreso el 
        # usuario es una cadena de texto.
        y = eval(fun_str)
        # Graficamos la funcion
        plt._ _ _(x, y)
        # Agregamos un titulo al grafico
        plt._ _ _(f'f(x)={fun_str}')
        # Mostramos el grafico creado
        plt._ _ _ ()

# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------
# EJERCICIO 4
# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------

# Accion del boton graficar_rac
    # para graficar funciones racionales
    def graficar_rac():
        # Rango fijo
        x = np.arange(-3, 3, 0.1, dtype=float)
        # funcion (la obtenemos de la caja_fun)
        fun_str = caja_fun.get()
        # Comando para poder evaluar numericamente
        # cadenas de texto
        y = eval(fun_str)
        # Establecemos un limite de rango de graficacion
        # del eje y. Esto es preciso para las funciones
        # racionales
        plt.ylim(-3,3)
        # graficamos la funcion
        plt._ _ _(x, y)
        # Creamos un titulo y mostramos el grafico
        plt._ _ _ (f'f(x)={fun_str}')
        plt._ _ _ ()

    # Accion del boton graficar_trigo
    # para graficar funciones trigonometricas. Para esto
    # nos auxiliaremos de la libreria numpy
    def graficar_trigo():
        # Rango fijo. En este caso los rangos de graficacion
        # seran en terminos del numero pi
        x = np.arange(-2 * np.pi, 2 * np.pi, 0.1, dtype=float)
        # funcion (la obtenemos de la caja_fun)
        fun_str1 = caja_fun.get()
        # Para el caso en que la funcion a graficar sea 
        # la funcion tangente estableceremos un 
        # limite de rango de graficacion del eje y.
        # (Las primeras tres letras de la cadena que ingreso
        # el usuario deben ser exactamente 'tan' para este caso)
        if fun_str1[:3] == 'tan':
            plt.ylim(-3,3)
            
        # Para trabajar con funciones trigonometricas nos 
        # auxiliaremos de la libreria numpy.
        # Por ejemplo:
        #       Lo que ingreso|
        #       el usuario:   | resultado
        # 'np' + 'sin(x)'     | np.sin(x)
        # 'np' + 'cos(x)'     | np.cos(x)
        # 'np' + 'tan(x)'     | np.tan(x)
        fun_str2 = 'np.' + fun_str1
        # Comando para poder evaluar numericamente
        # cadenas de texto
        y = eval(fun_str2)
        # graficamos
        plt._ _ _ (x, y)
        # Creamos un titulo y mostramos el grafico
        plt._ _ _ (f'f(x)={fun_str1}')
        plt._ _ _ ()

    # Accion del boton  graficar_exp_log 
    # para graficar funciones exponenciales y logaritmicas
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
        plt._ _ _(x, y)
        # Mostramos
        plt._ _ _ (f'f(x)={fun_str1}')
        plt._ _ _ ()

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
    boton_graficar = ttk._ _ _ (vc_graficar, text='Graficar', command = _ _ _ )
    # Posicion de este boton
    boton_graficar.place(x=20, y=60)
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # BOTON PARA GRAFICAR FUNCIONES RACIONALES
    boton_graficar_rac = ttk._ _ _ (vc_graficar, text='Graficar fun racional', 
                                    command = _ _ _ )
    # Posicion de este boton
    boton_graficar_rac.place(x=330, y=60)
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # BOTON PARA GRAFICAR FUNCIONES TRIGONOMETRICAS
    boton_graficar_trigo = ttk._ _ _ (vc_graficar, text='Graficar Trigonometric', 
                                      command = _ _ _ )
    # Posicion de este boton
    boton_graficar_trigo.place(x=100, y=60)
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # BOTON PARA GRAFICAR FUNCIONES EXPONENCIALES Y LOGARITMICAS
    boton_graficar_exp_log = ttk._ _ _ (vc_graficar, text='Graficar Exp/ log', 
                                        command = _ _ _ )
    # Posicion de este boton
    boton_graficar_exp_log.place(x=230, y=60)
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # CONFIGURACION DE UN BOTON PARA SALIR DE LA VENTANA DE GRAFICACION
    
    # Para salir de una ventana o cerrarla escribimos: 
    # <nombre de la ventana>.destroy
    # En este caso este boton nos hara salir de la ventana
    # vc_graficar.destroy y nos regresara a la ventana principal
    boton_graf_salir = ttk._ _ _ (vc_graficar, text='Regresar', 
                                  # accion que hara nuestro boton
                                  command = vc_graficar.destroy)
    # Posicion de este boton
    boton_graf_salir.place(x=20, y=100)

# ---------------------------------------------------------

# Ignora lo que se te pide aqui. Este espacio lo ocuparas hasta
# el ejercicio 10
# NOMBRE CLAVE: BOB PANTALONES CUADRADOS
# .
# .
# .

# ---------------------------------------------------------


# ---------------------------------------------------------

# Ignora lo que se te pide aqui. Este espacio lo ocuparas hasta
# el ejercicio 11
# NOMBRE CLAVE: KND los chicos del barrio
# .
# .
# .

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

# Mostramos una linea separadora
submenu.add_separator()

# Agregamos la opcion para salir de nuestro programa.
#                                             cerraremos la ventana
#                                             principal   
submenu.add_command(label = 'Salir', command = ventana.destroy)

# Agregamos el submenu al menu principal
#                    nombre del menu | submenu a 
#                    principal       | agregar
menu_principal._ _ _ (label='Menú', menu = _ _ _ )


# ---------------------------------------------------------

# Ignora lo que se te pide aqui. Este espacio lo ocuparas hasta
# la parte final del proyecto
# NOMBRE CLAVE: Bombon, Burbuja y Bellota
# .
# .
# .

# ---------------------------------------------------------


# Mostramos una linea separadora
submenu.add_separator()

# Agregamos la opcion para salir de nuestro programa.
#                                             cerraremos la ventana
#                                             principal   
submenu.add_command(label = 'Salir', command = ventana.destroy)

# Agregamos el submenu al menu principal
#                    nombre del menu | submenu a 
#                    principal       | agregar
menu_principal._ _ _ (label='Menú', menu = _ _ _ )

# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------
# EJERCICIO 7
# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------

# Mas etiquetas
#                                                    especificamos la tipografia
#                                                    y el tamanio de la letra
etiqueta1 = ttk._ _ _ (ventana, text="¡Bienvenido!", font=('Helvetica', 16))
# posicion de la etiqueta
etiqueta1.place(x=50, y=20)

# -------------------------------------------------------------------------------
etiqueta2 = ttk._ _ _ (ventana, 
                      text="Este es un programa para graficar\ny calcular límites y derivadas", 
                      font=('Helvetica', 12))
# posicion de la etiqueta
etiqueta2.place(x=50, y=60)

# Mostramos la ventana principal creada
ventana._ _ _ ()


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

# menu.add_command(label = 'Limites', command = c_limites)
# menu.add_command(label = 'Derivadas', command = c_derivadas)

# sin los comentarios, donde escribimos: 

# NOMBRE CLAVE: Bombon, Burbuja y Bellota

# lineas arriba. Ten cuidado con la identacion 
