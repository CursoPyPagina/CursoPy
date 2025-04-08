## Código completo de las funciones

**Dar_alta() e ingreso()**

---

```python
def dar_alta():
    """ Función que crea la interfaz gráfica para dar de alta a un nuevo cliente.|
    """
    import tkinter as tk
    from tkinter import messagebox
    from tkinter import ttk
    import pandas as pd
    import sqlite3 as sql
    import datetime as dt
    
    
    # Creamos una nueva ventana y la denominamos vc_graficar
    # como no es una ventana principal, pondremos Toplevel()
    vc_graficar = tk.Toplevel()
    vc_graficar.geometry('500x350')
    
    # ------------------------------------------------------

    # Etiquetas
    etiqueta_title = ttk.Label(vc_graficar, text=' REGISTROS DE NUEVOS CLIENTES\n ', 
                               font=('Helvetica', 12))
    etiqueta_title.grid(row=0, column=1, sticky='NSWE')
    etiqueta_nombre = ttk.Label(vc_graficar, text='Nombre: ')
    etiqueta_nombre.grid(row=1, column=0, sticky='NSWE')
    etiqueta_edad = ttk.Label(vc_graficar, text='Edad: ')
    etiqueta_edad.grid(row=2, column=0, sticky='NSWE')
    etiqueta_sexo = ttk.Label(vc_graficar, text='Sexo: ')
    etiqueta_sexo.grid(row=3, column=0, sticky='NSWE')
    etiqueta_telefono = ttk.Label(vc_graficar, text='Telefono: ')
    etiqueta_telefono.grid(row=4, column=0, sticky='NSWE')
    etiqueta_pass = ttk.Label(vc_graficar, text='Password: ')
    etiqueta_pass.grid(row=5, column=0, sticky='NSWE')
    
    # ------------------------------------------------------

    # La caja de texto se mostrara en esta nueva ventana
    #                                    width=tamaño de caracteres
    caja_nombre = ttk.Entry(vc_graficar, width=15)
    # Posicion de la caja de texto
    #                                                pequenio margen
    #                                                a la caja de texto
    caja_nombre.grid(row=1, column=1, sticky='NSWE', padx=5, pady=5)
    caja_edad = ttk.Entry(vc_graficar, width=15)
    caja_edad.grid(row=2, column=1, sticky='NSWE', padx=5, pady=5)
    # lo que hace combobox es generar una lista desplegable con los valores que le pasamos
    # en formato de una lista
    caja_sexo = ttk.Combobox(vc_graficar,
                             values=["M", "F", "O"])
    caja_sexo.grid(row=3, column=1, sticky='NSWE', padx=5, pady=5)
    caja_telefono = ttk.Entry(vc_graficar, width=15)
    caja_telefono.grid(row=4, column=1, sticky='NSWE', padx=5, pady=5)
    caja_pass = ttk.Entry(vc_graficar, width=15)
    caja_pass.grid(row=5, column=1, sticky='NSWE', padx=5, pady=5)
    
    # ------------------------------------------------------

    # Ahora definiremos las funciones que realizaran
    # las acciones de nuestros botones.
    def subir_cliente():
        # Deplegar el while para estarle exigiendo que coloque bien la info
        while True:
            if caja_nombre.get() == '':
                messagebox.showerror("Error", "Debes ingresar un nombre")
                break
            
            elif caja_edad.get() == '':
                messagebox.showerror("Error", "Debes ingresar un dato en la edad")
                break
        
            # el usuario no ingresa info
            elif caja_sexo.get() == '':
                messagebox.showerror("Error", "Debes ingresar un valor para le etiqueta de Sexo")
                break
                    
            elif caja_telefono.get() == '':
                messagebox.showerror("Error", "Debes ingresar un número de teléfono")
                break
                
            elif caja_pass.get() == '':
                messagebox.showerror("Error", "Debes ingresar un número de pasword")
                break
            
            break
        
        while True:
            # el usuario si ingresa info
            if (caja_sexo.get() != '') and (caja_sexo.get() not in ["M", "F", "O"]):
                messagebox.showerror("Error", "Debes ingresar un valor válido")
                break
            
            elif caja_edad.get() != '':
                try:
                    int(caja_edad.get())
                    break
                except:
                    messagebox.showerror("Error", "Debes ingresar un número entero")
                    break
            
            # cierre final del bucle
            break

        # Ya que controlamos los errores:
        # dt.strftime(string, '%Y-%m-%d')
        fecha_inicio = dt.datetime.now().strftime('%Y-%m-%d')
        fecha_fin = (dt.datetime.now() + dt.timedelta(days=30)).strftime('%Y-%m-%d')
        estado = 'Activo'
        contador = 0
        
        con = sql.connect("bbdd_gym.db") 
        # info a subir 
        # OJO 👁️: no hemos definido esta tabla, lo haremos mas adelante
        query = f"""
            INSERT INTO 
                clientes_3 
            VALUES(
            '{caja_nombre.get()}', 
            {int(caja_edad.get())},
            '{caja_sexo.get()}', 
            '{caja_telefono.get()}',
            '{caja_pass.get()}', 
            '{fecha_inicio}',
            '{fecha_fin}',
            '{estado}', 
            {contador}
            )
        """

        # la insercion de arriba solo nos debe dar un posible error y eso tiene que ver con el password
        # Para ello, cuando definamos la tabla de SQL diremos que el password es una llave primaria
        # (mas adelante lo explicaremos, pero basicamente sirve para no meter duplicados a nuestra
        # base de datos).

        try:
            con.execute(query)
            messagebox.showinfo(message="Usuario insertado exitosamente", title='Mensaje')
        except:
            messagebox.showerror('Error', 'Error o Password ya existente')
        con.commit()
        con.close()
            
    def clean():
        """ Funcion para limpiar la informacion que se encuentra en las cajas de texto
        """
        caja_nombre.delete(0, tk.END)
        caja_edad.delete(0, tk.END)
        caja_sexo.delete(0, tk.END)
        caja_telefono.delete(0, tk.END)
        caja_pass.delete(0, tk.END)
         
    # Botones:
    boton_sub_cliente = ttk.Button(vc_graficar, text='Subir cliente', command=subir_cliente)
    # # Posicion de este boton
    boton_sub_cliente.grid(row=6, column=1)
    
    # Boton para limpiar
    boton_sub_clean = ttk.Button(vc_graficar, text='Limpiar', command=clean)
    boton_sub_clean.grid(row=8, column=1)
    
    # Boton para salir
    boton_sub_salir = ttk.Button(vc_graficar, text='Regresar', command=vc_graficar.destroy)
    boton_sub_salir.grid(row=9, column=1)   
```
