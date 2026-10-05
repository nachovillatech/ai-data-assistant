# title: Herramienta de Consulta PostgreSQL para Open WebUI
# author: Nacho (nachovillatech)
# requirements: psycopg2-binary
import os
import re
import psycopg2


class Tools:
    def __init__(self):
        pass

    def consultar_base_de_datos(self, consulta_sql: str) -> str:
        """
        Ejecuta una consulta SQL SELECT de solo lectura en la base de datos empresarial
        para obtener información en tiempo real.
        :param consulta_sql: La consulta SQL exacta a ejecutar. Debe ser una sentencia SELECT.
        :return: Los datos encontrados o el error de conexión/validación.
        """
        consulta_limpia = consulta_sql.strip().rstrip(";")

        # Validación 1: Solo permitir consultas SELECT
        if not re.match(r"^\s*SELECT\b", consulta_limpia, re.IGNORECASE):
            return "Solo se permiten consultas SELECT. Consulta rechazada."

        # Validación 2: Palabras clave prohibidas por seguridad
        palabras_prohibidas = [
            "insert",
            "update",
            "delete",
            "drop",
            "alter",
            "truncate",
            "grant",
            "revoke",
        ]
        if any(
            re.search(rf"\b{p}\b", consulta_limpia, re.IGNORECASE)
            for p in palabras_prohibidas
        ):
            return "La consulta contiene una palabra no permitida. Consulta rechazada."

        # Validación 3: Evitar saturación limitando resultados
        if not re.search(r"\bLIMIT\b", consulta_limpia, re.IGNORECASE):
            consulta_limpia += " LIMIT 200"

        conn = None
        try:
            conn = psycopg2.connect(
                host=os.getenv("DB_HOST", "YOUR_DB_IP"),
                database=os.getenv("DB_NAME", "your_database"),
                user=os.getenv("DB_USER", "your_user"),
                password=os.getenv("DB_PASSWORD", "YOUR_SECURE_PASSWORD"),
                port=os.getenv("DB_PORT", "5432"),
                connect_timeout=5,
                options="-c statement_timeout=5000",
            )
            cursor = conn.cursor()
            cursor.execute(consulta_limpia)
            columnas = [desc[0] for desc in cursor.description]
            filas = cursor.fetchall()
            cursor.close()

            if not filas:
                return "No se encontraron registros en la base de datos."

            resultado = "Resultados obtenidos:\n"
            for fila in filas:
                resultado += str(dict(zip(columnas, fila))) + "\n"
            return resultado

        except Exception as e:
            return f"Error de conexión o consulta a la base de datos: {str(e)}"
        finally:
            if conn is not None:
                conn.close()