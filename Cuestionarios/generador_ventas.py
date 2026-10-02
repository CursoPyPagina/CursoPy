import pandas as pd
import datetime as dt
import random as r
import sqlite3 as sql

##################################
# Funcion para generar y alimentar
# la vase un dia de ventas
##################################
def generar_df_info(fechaVenta, ifExists):
  listaInsumosProductos = [
      "Cuaderno profesional", "Cuaderno doble raya", "Lápiz del número 2", "Pluma azul",
      "Pluma negra", "Pluma roja", "Marcador permanente", "Marcador para pizarrón",
      "Resaltador amarillo", "Resaltador verde", "Resaltador rosa", "Goma de borrar",
      "Sacapuntas", "Tijeras escolares", "Tijeras de oficina", "Regla de 30 cm",
      "Compás metálico", "Juego de geometría", "Pegamento en barra", "Pegamento líquido",
      "Cinta adhesiva", "Corrector líquido", "Corrector en cinta", "Carpeta tamaño carta",
      "Carpeta tamaño oficio", "Separadores de plástico", "Hojas blancas tamaño carta",
      "Hojas recicladas", "Hojas cuadriculadas", "Post-it", "Bloc de notas",
      "Engrapadora", "Caja de grapas", "Clips metálicos", "Broches tipo baco",
      "Folder manila", "Folder plástico con broche", "Archivador", "Tóner para impresora",
      "Cartuchos de tinta", "Calculadora científica", "Calculadora básica", "Memoria USB",
      "Mouse inalámbrico", "Teclado", "Agenda anual", "Calendario de escritorio",
      "Papel fotográfico", "Papel bond", "Cinta doble cara", "Pega diamantina"
  ]

  listaInsumosCajeros = [
      "Juan Carlos Ramírez López", "Miguel Ángel Torres Hernández", "José Luis González Cruz",
      "Carlos Alberto Mendoza Pérez", "Luis Fernando Ortega Díaz",
      "María Fernanda Castillo Reyes", "Ana Sofía Morales García", "Valeria Jiménez Flores",
      "Diana Carolina Salazar Ruiz", "Paola Alejandra Vargas León"
  ]

  listaInsumosSucursales = [
      "Centro Histórico", "Polanco", "Santa Fe", "Coyoacán", "Cuemanco",
      "Tlalpan", "Xochimilco", "La Condesa", "Reforma", "San Ángel"
  ]

  listaInsumoV_fecha = []
  listaInsumoV_cajero = []
  listaInsumoV_producto = []
  listaInsumoV_precio = []
  listaInsumoV_cantidad = []
  listaInsumoV_total = []
  listaInsumoV_sucursal = []

  for i in range(1, r.randint(1000, 35001)):
    cajero = r.choice(listaInsumosCajeros)
    producto = r.choice(listaInsumosProductos)
    precio = round(r.randint(10, 20000) * r.random(), 2)
    cantidad = r.randint(1, 100)
    total = round(precio * cantidad, 2)
    sucursal = r.choice(listaInsumosSucursales)

    listaInsumoV_fecha.append(fechaVenta)
    listaInsumoV_cajero.append(cajero)
    listaInsumoV_producto.append(producto)
    listaInsumoV_precio.append(precio)
    listaInsumoV_cantidad.append(cantidad)
    listaInsumoV_total.append(total)
    listaInsumoV_sucursal.append(sucursal)

  dictPrevio = {
    "ColFecha": listaInsumoV_fecha,
    "ColCajero": listaInsumoV_cajero,
    "ColProducto": listaInsumoV_producto,
    "ColPrecio": listaInsumoV_precio,
    "ColCantidad": listaInsumoV_cantidad,
    "ColTotal": listaInsumoV_total,
    "ColSucursal": listaInsumoV_sucursal
  }

  # Construimos nuestro dataframe
  df_ventas = pd.DataFrame(dictPrevio)
  print(f"Dataframe generado con éxito al {fechaVenta}")

  # Alimentamos la base de datos
  conexion = sql.connect("Ventas.db")
  df_ventas.to_sql("Ventas_2025", conexion, if_exists=ifExists)
  conexion.close()
  print(f"Base de datos alimentada al {fechaVenta}")

#################################
# Funcion para realizar consultas
#################################
def consulta(query):
  conexion = sql.connect("Ventas.db")
  df_consulta = pd.read_sql_query(query, conexion)
  conexion.close()
  return df_consulta

#################################
# Funcion para generar
# una lista de fechas
#################################
def rangoFecha(fechaInicial, fechaFinal):
  rangoObjetosFecha = pd.date_range(start=fechaInicial, end=fechaFinal, freq="1d")
  rangoStrFecha = []

  for objFecha in rangoObjetosFecha:
    strFecha = dt.datetime.strftime(objFecha, "%Y-%m-%d")
    rangoStrFecha.append(strFecha)

  return rangoStrFecha

##################################
# Funcion para generar y alimentar
# ventas en un rango de fechas
##################################
def generar_df_info_rango(fechaInicial, fechaFinal):

  # 1. Creamos el rango de fechas con la funcion que ya tenemos
  rango_fechas = rangoFecha(fechaInicial, fechaFinal)

  # 2. Recorremos el rango de fechas, y para cada fecha del rango
  # ejecutaremos la funcion generar_df_info
  for fechaVenta in rango_fechas:
    # En este paso presuponeremos que ya fue inicializada la tabla
    # de SQL colocando el parametro "replace" como en efecto
    # ya lo hicimos lineas arriba.

    # Generamos la informacion del dia fechaVenta
    # y de una vez lo subimos a la base de datos
    generar_df_info(fechaVenta, "append")

    # No es necesario que demos prints informativos pues la
    # funcion generar_df_info ya lo hace por si misma

  # Una vez terminado de generarse y subirse la informacion
  # del rango de fechas, damos un print de finalizacion
  print(f"Se generó con éxito las ventas del {fechaInicial} al {fechaFinal}")