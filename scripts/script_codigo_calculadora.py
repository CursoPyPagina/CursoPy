# Importaciones necesarias
import tkinter as tk
from tkinter import ttk

# Configuracion de la ventana
ventana = tk.Tk()
ventana.title('Calculadora')
ventana.geometry('500x300')

# Configuraciones de las proporciones de las filas y columnas
# respecto al tamanio total de la ventana
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=2)
ventana.rowconfigure(2, weight=2)
ventana.rowconfigure(3, weight=2)
ventana.rowconfigure(4, weight=2)
ventana.rowconfigure(5, weight=2)
ventana.columnconfigure(0, weight=2)
ventana.columnconfigure(1, weight=2)
ventana.columnconfigure(2, weight=2)
ventana.columnconfigure(3, weight=1)

# Caja de texto
caja_fun = ttk.Entry(ventana, width=40)
#                                                          colocamos un pequenio
#                                                          margen
caja_fun.grid(row=0, column=0, sticky='NSWE', columnspan=4, padx=2, pady=2)

# BOTONES:
boton_izq = ttk.Button(ventana, text='(')
boton_izq.grid(row=1, column=0, sticky='NSWE')

boton_der = ttk.Button(ventana, text=')')
boton_der.grid(row=1, column=1, sticky='NSWE')

boton_porc = ttk.Button(ventana, text='%')
boton_porc.grid(row=1, column=2, sticky='NSWE')

boton_ac = ttk.Button(ventana, text='Ac')
boton_ac.grid(row=1, column=3, sticky='NSWE')

boton_1 = ttk.Button(ventana, text='1')
boton_1.grid(row=2, column=0, sticky='NSWE')

boton_2 = ttk.Button(ventana, text='2')
boton_2.grid(row=2, column=1, sticky='NSWE')

boton_3 = ttk.Button(ventana, text='3')
boton_3.grid(row=2, column=2, sticky='NSWE')

boton_sum = ttk.Button(ventana, text='+')
boton_sum.grid(row=2, column=3, sticky='NSWE')

boton_4 = ttk.Button(ventana, text='4')
boton_4.grid(row=3, column=0, sticky='NSWE')

boton_5 = ttk.Button(ventana, text='5')
boton_5.grid(row=3, column=1, sticky='NSWE')

boton_6 = ttk.Button(ventana, text='6')
boton_6.grid(row=3, column=2, sticky='NSWE')

boton_res = ttk.Button(ventana, text='-')
boton_res.grid(row=3, column=3, sticky='NSWE')

boton_7 = ttk.Button(ventana, text='7')
boton_7.grid(row=4, column=0, sticky='NSWE')

boton_8 = ttk.Button(ventana, text='8')
boton_8.grid(row=4, column=1, sticky='NSWE')

boton_9 = ttk.Button(ventana, text='9')
boton_9.grid(row=4, column=2, sticky='NSWE')

boton_mult = ttk.Button(ventana, text='*')
boton_mult.grid(row=4, column=3, sticky='NSWE')

boton_0 = ttk.Button(ventana, text='0')
boton_0.grid(row=5, column=0, sticky='NSWE')

boton_pt = ttk.Button(ventana, text='.')
boton_pt.grid(row=5, column=1, sticky='NSWE')

boton_igual = ttk.Button(ventana, text='=')
boton_igual.grid(row=5, column=2, sticky='NSWE')

boton_div = ttk.Button(ventana, text='÷')
boton_div.grid(row=5, column=3, sticky='NSWE')

# Accion asociada a la opcion 'Nueva ventana'
# del submenu
def nueva_ventana():
    # Creamos una nueva ventana
    new_ventana = tk.Toplevel()
    new_ventana.geometry('500x200')
    # Titulo de esta nueva ventana
    new_ventana.title('Ventana Nueva :D')

# Creamos un menu
menu_principal = tk.Menu(ventana)
# agregamos el menu a la ventana
ventana.config(menu = menu_principal)

# creamos un submenu
submenu = tk.Menu(menu_principal, tearoff = False)
# agregamos opciones al submenu
submenu.add_command(label='Nueva ventana', command = nueva_ventana)
submenu.add_command(label='Salir', command = ventana.destroy)

# Agregamos el submenu al menu
menu_principal.add_cascade(label='Menú', menu=submenu)

# Mostramos la ventana principal
ventana.mainloop()