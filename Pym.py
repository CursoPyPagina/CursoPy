class tools:
  ########################## Atributos de clase ################################
  # YA ES CODIGO QUE CONOCEMOS.
  abcdario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
              'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
              'U', 'V', 'W', 'X', 'Y', 'Z']
  papelerias = ['Xochimilco', 'Cuemanco', 'Coapa', 'Milpa Alta', 'CU', 'Zócalo',
                'Narvarte', 'Santa Fé', 'Polanco', 'Centro']
  lineas = ['Cuadernos', 'Libretas', 'Lápices', 'Plumones', 'Borradores', 'Sacapuntas',
            'Laptops', 'Tablets', 'Mochilas', 'Bolsas', 'Cajas', 'Pegamento', 'Tijeras',
            'Monitores', 'Teclados', 'Mouse', 'Audífonos', 'Cables', 'Cargadores', 'Baterías',
            'Pc', 'Uniformes', 'Pinturas', 'Pinceles', 'Papel', 'Cartulinas']

  ############################ Metodo de clase #################################
  def generar_info(fecha_reporte):
    """Método (privado) para simular las ventas de las diferentes papelerías"""

    ############################################################################
    # Este codigo ya lo conocemos
    import random as r
    import pandas as pd

    # Difinir listas vacias para posteriormente ir llenando
    # la informacion
    fechas = []
    sucursales = []
    productos = []
    claves_producto = []
    precios = []
    cantidades_vendidas = []
    totales_ticket = []

    # 1000 ventas en total
    # 1,2,...,1000
    # range(1000) ---> 0, .., 999
    for i in range(1000):
      # Generamos la informacion de las ventas
      # de manera granular
      sucursal = r.choice(tools.papelerias)
      producto = r.choice(tools.lineas)
      clave_producto = r.choice(tools.abcdario) + r.choice(tools.abcdario) + r.choice(tools.abcdario) + "-" + str(r.randint(1,9)) + str(r.randint(1,9)) + str(r.randint(1,9))
      precio = round(r.random() * r.randint(100,10000), 2)
      cantidad_vendida = r.randint(1, 1000)
      total_ticket = precio * cantidad_vendida

      # la info anterior, la agregamos a las listas vacias
      fechas.append(fecha_reporte)
      sucursales.append(sucursal)
      productos.append(producto)
      claves_producto.append(clave_producto)
      precios.append(precio)
      cantidades_vendidas.append(cantidad_vendida)
      totales_ticket.append(total_ticket)

    # una vez que ya repetimos el proceso las mil veces, lo que sigue 
    # es crear nuestro dataframe (tabla) de pandas.
    diccionario_ventas_df = {
        "Fecha": fechas,
        "Sucursal": sucursales,
        "Producto": productos,
        "Clave_Producto": claves_producto,
        "Precio": precios,
        "Cantidad_Vendida": cantidades_vendidas,
        "Total_Ticket": totales_ticket
    }

    df_ventas = pd.DataFrame(diccionario_ventas_df)

    # Lo unico que estamos agregando aca es que la funcion o metodo
    # nos esta regresando el dataframe con la informacion simulada
    print(f"Generación exitosa al {fecha_reporte}")
    return df_ventas
    ############################################################################

  ############################ Metodo "SQL" ####################################
  def definiciones():
    """Funcion para crear la base de datos y la tabla que ocuparemos para
    almacenar la infomacion simulada de las ventas"""

    ############################################################################
    # Este codigo tambien ya lo conocemos, es donde definimos la bbdd y la tabla
    import sqlite3 as sql

    # o te crea la base de datos o te conecta a la base de datos
    conn = sql.connect("Ventas.db")
    # Puente Python y SQL
    cursor = conn.cursor()

    query_create = """
      CREATE TABLE VENTAS_2025(
        Fecha            TEXT,
        Sucursal         TEXT,
        Producto         TEXT,
        Clave_Producto   TEXT,
        Precio           REAL,
        Cantidad_Vendida INTEGER,
        Total_Ticket     REAL
      )
    """
    cursor.execute(query_create)
    conn.commit()
    conn.close()

    # Aca podemos ver de nuevo lo util que son los prints para que nos vayan
    # informando como va nuestro proceso
    print("Base de datos creada/conectada")
    print("Tabla creada")

  def inserciones_mult(df):
      """Método para alimentar la tabla de la base de datos
      es necesario haber corrido primero el metodo
      1. definiciones() -----> Para definir la base de datos y la tabla
      2. _generar_info() ----> Para crear el dataframe con la info
      """

      # Esto codigo tambien ya es conocido por nosotros, es donde montamos
      # o (vamos guardando) los datos de python a la base de datos
      import random as r
      import pandas as pd
      import sqlite3 as sql

      conn = sql.connect("Ventas.db")
      cursor = conn.cursor()

      for i in range(1000):
          query_insert = f"""
          INSERT INTO
            VENTAS_2025
          VALUES(
            '{df.loc[i, "Fecha"]}',
            '{df.loc[i, "Sucursal"]}',
            '{df.loc[i, "Producto"]}',
            '{df.loc[i, "Clave_Producto"]}',
             {df.loc[i, "Precio"]},
             {df.loc[i, "Cantidad_Vendida"]},
             {df.loc[i, "Total_Ticket"]}
          )
          """
          cursor.execute(query_insert)
          conn.commit()

      conn.close()
      print(f"Inserción existosa")

  ######################## Metodo proceso final ################################
  # Este codigo es nuevo, pero ya lo mencionamos,es donde conjuntaremos
  # la creacion de la informacion y donde subimos los datos a SQL. Mas a
  # delante explicaremos a fondo el codigo
  def proceso(fecha_ini):
      """Metodo en el cual simulamos la informacion de las ventas y adicionalmente realizamos
      las inserciones. Se podra generar informacion de un solo dia o informacion de
      todo un rango de fechas."""

      import pandas as pd
      import time as t

      # Pantallazo inicial del tiempo
      inicio = t.time()

      # Generamos la info
      print("Comienzo del programa .....")
      df = tools.generar_info(fecha_ini)

      # Insertamos
      print("Comienzo de las inserciones ....")
      tools.inserciones_mult(df)

      # Pantallazo de tiempo de cuando termino el proceso
      fin = t.time()

      print(f'Fecha: {fecha_ini} || Tiempo de ejecución: {round((fin - inicio) / 60, 2)} minutos')

  def comprobar_fechas():
      """Método para ver cuales fechas tenemos cargadas en la tabla
      con base en una consulta SQL"""
      import sqlite3 as sql
      import pandas as pd

      conn = sql.connect("Ventas.db")

      query = """
      SELECT
        DISTINCT FECHA
      FROM
        VENTAS_2025
      """

      df = pd.read_sql_query(query, conn)
      conn.close()

      return df