-- Esto es un comentario
-- Ver el contenido de la tabla1 mediante una consulta:
SELECT * FROM tabla1;


--- Procederemos a crear las tablas del diseño que vimos en el pizarrón
-- Crear las demás tablas
CREATE TABLE productos(
	id_productos SERIAL,
	nombre VARCHAR,
	proveedor VARCHAR,
	precio REAL,
	codigo INT
)
-- MySQL, SQLServer, Oracle, Sqlite3: sistema gestor de base de datos
-- PostgreSQL: sistema gestor de base de datos que utiliza SQL
-- pgAdmin: interfaz gráfica (Usuario)

-- no se puede cambiar de cadena de texto a numerico de manera directa:
-- ALTER TABLE productos ALTER COLUMN proveedor SET DATA TYPE int;
-- En su lugar escribiremos:
ALTER TABLE productos ALTER COLUMN proveedor TYPE INT USING proveedor::INTEGER;

-- Continuamos con la creación de la base de datos
CREATE TABLE proveedores(
	id_proveedores SERIAL,
	nombre_proveedor VARCHAR,
	direccion VARCHAR,
	telefono VARCHAR
);

CREATE TABLE almacen(
	id_producto_almacen SERIAL,
	nombre_producto VARCHAR,
	cantidad_almacen INT,
	proveedor INT
);

-------------------------------------------------------------------------------------------------------------------

-- Después de definir las tablas, pasamos a definir las llaves
-- Llaves primarias y las llaves foraneas:
-- PK                 Para nombrar una llave primaria
ALTER TABLE productos ADD CONSTRAINT pk_productos_id_productos 
	PRIMARY KEY (id_productos);
ALTER TABLE proveedores ADD CONSTRAINT pk_proveedores_id_proveedores 
	PRIMARY KEY (id_proveedores);
ALTER TABLE almacen ADD CONSTRAINT pk_almacen_id_producto_almacen
	PRIMARY KEY (id_producto_almacen);

-- Definir las llaves foraneas        
ALTER TABLE productos ADD CONSTRAINT fk_productos_proveedor_id_proveedores
	FOREIGN KEY (proveedor) REFERENCES proveedores(id_proveedores);
	
ALTER TABLE productos ADD CONSTRAINT fk_productos_codigo_id_producto_almacen
	FOREIGN KEY (codigo) REFERENCES almacen(id_producto_almacen);
	
ALTER TABLE almacen ADD CONSTRAINT fk_almacen_proveedor_id_proveedores
	FOREIGN KEY (proveedor) REFERENCES proveedores(id_proveedores);
	
-- eliminar llave foranea:
-- ALTER TABLE productos DROP CONSTRAINT fk_productos_codigo_id_producto_almacen;

-------------------------------------------------------------------------------------------------------------------

-- Procedemos a realizar la inserción de los datos
INSERT INTO proveedores(nombre_proveedor, direccion,telefono) VALUES ('Bimbo', 'Calle x', '55-12-34-56-78');
INSERT INTO proveedores(nombre_proveedor, direccion,telefono) VALUES ('Coca-Cola', 'Calle y', '56-12-34-56-78');
INSERT INTO productos(nombre, proveedor, precio, codigo) VALUES ('Coca-cola', 2, 9.99, 3);
INSERT INTO almacen(nombre_producto, cantidad_almacen, proveedor) VALUES ('Pan Bimbo blanco', 20, 1);
INSERT INTO almacen(nombre_producto, cantidad_almacen, proveedor) VALUES ('Pan Bimbo blanco integral', 30, 1);
INSERT INTO almacen(nombre_producto, cantidad_almacen, proveedor) VALUES ('Coca-cola 600', 300, 2);
INSERT INTO productos(nombre, proveedor, precio, codigo) VALUES ('Coca-cola', 2, 9.99, 2);

-- Veamos los cambios en las tablas con las siguientes consultas
SELECT * FROM proveedores;
SELECT * FROM productos;
SELECT * FROM almacen;

-- Si quisieramos eliminar una tabla:
-- DROP TABLE almacen;

-- Podemos cambiar el nombre de una columna de una tabla
-- ALTER TABLE almacen RENAME COLUMN nombre_actual TO nuevo_nombre;

-------------------------------------------------------------------------------------------------------------------

-- Consultas --
-- *: ver todas columnas
SELECT telefono, nombre_proveedor FROM proveedores;
SELECT * FROM almacen;

-- Count()
-- El total de registros de una tabla
SELECT COUNT(telefono) from proveedores;
-- Promedio
SELECT AVG(cantidad_almacen) FROM almacen;
SELECT MAX(cantidad_almacen) FROM almacen;

-- LIMIT
SELECT * FROM almacen LIMIT 3;
--

-- WHERE
-- Ver en almacen todos los productos de bimbo (1)
SELECT * FROM almacen WHERE proveedor = 1;

-- Obtener el numero de distitnos productos de bimbo en el almacen
SELECT COUNT(*) FROM almacen WHERE proveedor = 1;

-- Columna sexo: H y M
-- SELECT * FROM nombre_tabla WHERE sexo = 'H';
-- SELECT COUNT(*) FROM nombre_tabla WHERE sexo = 'H';
	