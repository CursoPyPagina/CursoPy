-- Hola mundo en PostgreSQL
SELECT 'Hola Mundo' AS Bienvenido;

-- CONSULTAS AVANZADAS -------------------------------------
-- Creamos la tabla
CREATE TABLE tabla1(
    Id_empleado SERIAL, 
    Nombre VARCHAR, 
    Direccion VARCHAR,
    Trabajo VARCHAR, 
    Ciudad VARCHAR, 
    Compañia VARCHAR, 
    CURP VARCHAR, 
    FechaNacimiento VARCHAR, 
    Sueldo REAL,
    Email VARCHAR, 
    Edad INT, 
    Sexo VARCHAR, 
    Region VARCHAR
);

-- LIMIT: obtener los primeros 10 registros
SELECT * FROM tabla1 LIMIT 10;

SELECT COUNT(*) FROM tabla1;

-- A partir del registro 100, retornamos 5 registros
SELECT * FROM tabla1 LIMIT 5 OFFSET 100;

-- ORDER BY
SELECT * FROM tabla1
-- ordenamos de manera descentente
ORDER BY sueldo DESC
-- obtenemos  5 registros a partir del registro 100
LIMIT 5 OFFSET 100;

-- WHERE (donde)
-- Obtenemos las mujeres que más ganan
SELECT nombre, edad, sueldo, sexo FROM tabla1
-- donde el sexo sea igual a 'F'
WHERE sexo = 'F'
ORDER BY sueldo DESC
LIMIT 5;

-- LIKE: parecido a
-- Obtener la información donde el nombre
-- comience con Luis
-- % significa "lo que sea"
SELECT nombre, edad, sueldo, sexo FROM tabla1
WHERE nombre LIKE 'Luis%';

-- Obtener la información donde la persona
-- tenga un apellido Camarillo
-- % significa "lo que sea"
SELECT nombre, edad, sueldo, sexo FROM tabla1
WHERE nombre LIKE '%Camarillo';

-- BETWEEN (entre)
-- Obtener información sobre las personas que
-- ganan entre 10000 y 15000
SELECT nombre, edad, sueldo, sexo FROM tabla1
WHERE sueldo BETWEEN 10000 AND 15000;

-- Obtener información sobre las personas que
-- NO ganan entre 10000 y 15000
SELECT nombre, edad, sueldo, sexo FROM tabla1
WHERE sueldo NOT BETWEEN 10000 AND 15000;

-- Jerarquía en las sentencias
--1. FROM
--2. ON
--3. OUTER
--4. WHERE
--5. GROUP BY
--6. CUBE | ROLLUP
--7. HAVING
--8. SELECT
--9. DISTINCT
--10 ORDER BY
--11. TOP

-- GROUP BY: agrupa una columna por sus categorías
-- y obtiene información de otra columna mediante
-- una función de agregación
-- Obtener el salario promedio por sexo
SELECT sexo, ROUND(AVG(sueldo)) FROM tabla1
GROUP BY sexo;

-- Obtener el salario promedio por region por sexo
SELECT region, sexo, ROUND(AVG(sueldo)) FROM tabla1
GROUP BY region, sexo
ORDER BY region;

-- WHERE-->condición para consultas normales
-- HAVING-->condición para consultas con agrupaciones (group by)
-- Promedio de sueldo mayor a 25000 por region por sexo
SELECT region, sexo, ROUND(AVG(sueldo)) FROM tabla1
GROUP BY region, sexo
HAVING avg(SUELDO) > 25000;

-- Promedio de sueldo por region para M
SELECT region, sexo, ROUND(AVG(sueldo)) FROM tabla1
GROUP BY region, sexo
HAVING sexo = 'M'
ORDER BY AVG(sueldo) DESC;

-- Operadores lógicos
-- Promedio de sueldo por region para M o F
-- para la región sur
SELECT region, sexo, ROUND(AVG(sueldo)) FROM tabla1
GROUP BY region, sexo
-- colocamos paréntesis para agrupar condiciones
HAVING ((sexo = 'M') OR (sexo = 'F')) AND (region = 'Sur')
ORDER BY AVG(sueldo) DESC;

-- En vez de escribir (sexo = 'M') OR (sexo = 'F')
-- podemos escribir: sexo IN ('M', 'F')
SELECT region, sexo, ROUND(AVG(sueldo)) FROM tabla1
GROUP BY region, sexo
HAVING (sexo IN ('M', 'F')) AND (region = 'Sur')
ORDER BY AVG(sueldo) DESC;

-- SUBCONSULTAS -----------------------------------------
-- La siguiente consulta, al fin de cuentas, es una tabla
SELECT region, sexo, ROUND(AVG(sueldo)) as sueldo_promedio 
FROM tabla1
GROUP BY region, sexo;

-- Podemos hacer un select, pero en vez de poner el 
-- nombre de una tabla, colocamos una consulta
-- y además le damos un alias a dicha tabla (consulta)
SELECT * FROM
	(SELECT region, sexo, ROUND(AVG(sueldo) AS sueldo_promedio) 
	 FROM tabla1
	 GROUP BY region, sexo) AS tabla_aux;
	 
-- Suma del sueldo promedio por sexo por región
SELECT region, SUM(sueldo_promedio) FROM
	(SELECT region, sexo, ROUND(AVG(sueldo)) AS sueldo_promedio 
	 FROM tabla1
	 GROUP BY region, sexo) AS tabla_aux
GROUP BY region;

-- Otro ejemplo pero usando where
-- Obtener registros donde el sueldo esté
-- entre el mínimo del sueldo y el máximo
SELECT nombre, edad, sueldo, sexo FROM tabla1
WHERE sueldo 
BETWEEN 
	(SELECT MIN(sueldo)
	 FROM tabla1)
AND
	(SELECT MAX(sueldo)
	 FROM tabla1)

-- JOINS ---------------------------------------------------
-- Creamos otras dos tablas
CREATE TABLE tabla2(
	Id_empleado SERIAL, 
	agno_ingreso VARCHAR,
    antiguedad INT,
    categoria VARCHAR,
    caja_ahorro REAL
);

CREATE TABLE tabla3(
	Id_empleado SERIAL, 
	telefono VARCHAR,
    banco VARCHAR,
    num_tarjeta VARCHAR
);

--- UNION e INTERSECT (conjuntista)
SELECT * FROM tabla2 LIMIT 5;
SELECT * FROM tabla3 LIMIT 5;
SELECT COUNT(*) FROM tabla3;

-- La clave de las uniones será la columna id_empleados que une las tablas
-- UNION mantiene solo los registros únicos
-- UNION ALL mantiene todos los registros
-- Mismo número de columnas con el mismo tipo de datos
-- Nos sirve para unir información de una misma tabla o de tablas parecidas
-- Obtenemos los empleados de la region Sur y Norte en una misma tabla
SELECT nombre, region
FROM tabla1
WHERE region = 'Sur'
UNION
SELECT nombre, region
FROM tabla1
WHERE region = 'Norte'
LIMIT 5;

-- En automático se detecta la columna que une las tablas
-- Al mostrar columnas de varias tablas, en el caso de que exista 
-- la misma columna en varias tablas dará error. 
-- siempre se aconseja utilizar alias de tablas para evitar este problema.
-- Solo registros compatibles, por ejemplo, si en una tabla no tenemos un
-- id, entonces ese registros no se considerará en la unión.
SELECT *
FROM tabla1 NATURAL JOIN tabla2;

-- INNER JOIN
-- requerimos especificar la columna de union
SELECT *
FROM tabla1 INNER JOIN tabla2
ON tabla1.Id_empleado = tabla2.Id_empleado;

-- uso de alias
SELECT *
FROM 
tabla1 t1 INNER JOIN tabla2 t2
ON t1.Id_empleado = t2.Id_empleado;

-- LEFT JOIN le da prioridad a los registros de la primer tabla de la
-- union

-- RIGHT JOIN le da prioridad a los registros de la segunda tabla de la
-- union