# Predicción de la Fecha de Modificación (ModifiedDate) usando SQL y Regresión

Este repositorio contiene la solución al ejercicio para montar una base de datos en SQL, entrenar un modelo de regresión y desplegar un servicio en la nube.

## Descripción del Proyecto

Este proyecto incluye:
1. **Montar una base de datos en Azure**: Se crea un servidor en Azure con la base de datos de prueba de SQL y se importa la tabla `SalesLT.customer`.
2. **Entrenar un modelo de regresión**: Usando la tabla `SalesLT.customer`, se entrena un modelo de regresión para predecir la fecha de modificación (`ModifiedDate`).
3. **Desplegar el servicio**: Se crea un API en la nube para exponer el modelo entrenado.

## Requisitos

- Tener una cuenta activa en Azure.
- Conocimiento básico de SQL y aprendizaje automático.
- Python (para el modelo de regresión y la API).
- Herramientas necesarias: SQL Server Management Studio (SSMS), Jupyter Notebook o IDE similar, y Azure CLI.

## Instrucciones

### 1. Montar la Base de Datos
- Configurar un servidor SQL en Azure.
- Crear una base de datos de prueba y agregar la tabla `SalesLT.customer`.
- Importar los datos necesarios desde la base de datos de prueba de SQL.

### 2. Entrenar el Modelo
- Usar el script para cargar los datos y entrenar un modelo de regresión.
- El objetivo es predecir la columna `ModifiedDate` de la tabla `SalesLT.customer`.

### 3. Desplegar el Servicio
- Crear un API para exponer el modelo entrenado.
- Desplegar el servicio en la nube (por ejemplo, utilizando Azure App Service).
