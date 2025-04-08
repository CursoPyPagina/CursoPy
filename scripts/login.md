## Código completo del login

---

```python
def login():
    """ Esta funcion es la encargada de crear la ventana de login
    para los administradores del gimnasio.
    """

    import tkinter as tk
    from tkinter import messagebox
    from tkinter import ttk
    import pandas as pd
    import sqlite3 as sql
    
    from menu_app import app_principal

    # Instanciar/inicializacion nuestra ventana
    login = tk.Tk()

    # configurar un tamaño
    #             largo x Ancho
    login.geometry('400x200')

    # configurar un titulo
    login.title('Login 🥸')

    # configurar tu funcion de estilos
    estilo = ttk.Style()
    estilo.theme_use("clam")

    # seccion de espacios en blanco para un espacio de identacion
    etiqueta_espacio_blanco_1 = ttk.Label(login, text='                      ')
    etiqueta_espacio_blanco_1.grid(row=1, column=0)

    # Saltos de linea
    etiqueta_espacio_blanco_2 = ttk.Label(login, text='                      ')
    etiqueta_espacio_blanco_2.grid(row=2, column=1)

    etiqueta_espacio_blanco_3 = ttk.Label(login, text='                      ')
    etiqueta_espacio_blanco_3.grid(row=3, column=1)

    # agregar un texto ttk.Label(ventana, texto)
    etiqueta_titulo_login = ttk.Label(login, 
                                    text='Mi primera aplicación web',
                                    font=('Arial', 16))

    # localizacion de nuestra etiqueta
    etiqueta_titulo_login.grid(row=1, column=1, sticky='NSWE')

    etiqueta_password = ttk.Label(login, text='Password', font=('Arial', 12))
    etiqueta_password.grid(row=4, column=0, sticky='NSWE')

    # Procedemos a colocar una caja de texto
    caja_etiqueta_password = ttk.Entry(login, show='*')
    # padx: margen horizontal (para no tener todo pegado)
    caja_etiqueta_password.grid(row=4, column=1, sticky='WE', padx='10')


    ##########################################################################
    ##########################################################################
    # los botones van asociados con comandos: funcion
    # Definicion de un boton: ttk.Button(ventana, texto, comando)
    def ingresar():
        """ Comando asociado a boton_entrar_login.
        * Nos conectaremos a la bbdd para traernos los passwords
        registrados.
        """
        # Parte 1: traernos la lista con los passwords
        con = sql.connect("bbdd_gym.db")
        df = pd.read_sql_query("SELECT * FROM admins", con)
        con.close()
        passwords_lista = list(df['password'])
        # Parte 2: traernos ese password de la caja caja_etiqueta_password
        # dada una caja de texto, puedes extraer la informacion de ahi
        # con el metodo get()
        password_user = caja_etiqueta_password.get()
        # Parte 3: validar que el password sea correcto
        if password_user in passwords_lista:
            # en caso de que el password este en la lista permita
            # daremos acceso
            # ------------------booleano--------------------
            # yes ---> True
            # no  ---> False
            acceso = messagebox.askyesno(message='¿Deseas continuar?')

            if acceso:
                # si el administrador le da que si, entonces abriremos la 
                # app del gym (continuacion)
                app_principal()
                
                # cuando ya hayamos ingresado eliminamos el password para que no se vea en la pantalla
                caja_etiqueta_password.delete(0, tk.END)
            else:
                # si le da en No el admin, entonces cerraremos la aplicacion
                login.destroy()
        else:
            # caso contrario, no daremos acceso
            messagebox.showerror('Contraseña incorrecta, intente de nuevo')
            
    boton_entrar_login = ttk.Button(login, text='Ingresar', command=ingresar)
    boton_entrar_login.grid(row=5, column=1)

    boton_entrar_limpiar = ttk.Button(login, text='Limpiar', 
                                    command=lambda: caja_etiqueta_password.delete(0, tk.END))
    boton_entrar_limpiar.grid(row=6, column=1)

    # Ejecutamos en bucle la interfaz
    login.mainloop()
```
