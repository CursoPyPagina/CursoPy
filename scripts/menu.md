## Código completo del menú

---

```python
def app_principal():
    """Función que crea la interfaz gráfica principal de la app."""
    
    import tkinter as tk
    from tkinter import messagebox
    from tkinter import ttk
    import pandas as pd
    import sqlite3 as sql
    
    from tools_menu_app import dar_alta
    
    # Como esta ventana se abre a partir de otra ventana, entonces
    # configuramoas con toplevel para que sea una ventana secundaria
    ventana = tk.Toplevel()
    # colocamos un titulo
    ventana.title('App')
    # tamaña en pixeles que queremos sobre 
    # nuestra ventana
    ventana.geometry('500x400')
    # sombreado
    estilo = ttk.Style()
    estilo.theme_use("clam")

    # creamos "virtualmente" nuestro menu
    menu_config = tk.Menu(ventana)
    # asociacion
    #              menu = asociamos ese menu virtual
    ventana.config(menu = menu_config)

    # Anclamos el menu
    menu = tk.Menu(menu_config)

    # Agregamos las opciones del menu (Son acciones, van asociadas a funciones)
    menu.add_command(label = 'Ingreso')
    menu.add_command(label = 'Dar de alta', command=dar_alta)

    # Linea horizontal separadora
    menu.add_separator()

    # La funcion destroy() nos permite cerrar la ventana
    menu.add_command(label = 'Salir', command=ventana.destroy)

    # add_cascade() -> nos permite agregar las opciones del menu
    # sin este codigo no veriamos las opciones del menu
    menu_config.add_cascade(label='Menú 👁️', menu = menu)
```