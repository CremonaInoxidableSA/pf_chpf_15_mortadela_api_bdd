import os

from sqlalchemy import text

from config import db


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SQL_DIR = os.path.join(BASE_DIR, "sql")


def cargar_archivo_sql(file_path: str, obligatorio: bool = True) -> bool:
    """Ejecuta un archivo SQL sobre la conexion principal de la API."""
    if not os.path.exists(file_path):
        mensaje = f"El archivo SQL no existe: {file_path}"
        if obligatorio:
            raise FileNotFoundError(mensaje)
        print(f"Aviso: {mensaje}")
        return False

    with open(file_path, "r", encoding="utf-8") as file:
        sql_script = file.read().strip()

    if not sql_script:
        print(f"Aviso: archivo SQL vacio: {file_path}")
        return False

    with db.engine.connect() as conn:
        conn.execute(text(sql_script))
        conn.commit()

    print(f"SQL ejecutado: {file_path}")
    return True


def tabla_tiene_registros(tabla: str) -> bool:
    with db.engine.connect() as conn:
        resultado = conn.execute(text(f"SELECT COUNT(*) AS total FROM {tabla}"))
        fila = resultado.fetchone()
        total = int(fila[0]) if fila else 0
        return total > 0


def cargar_datos_iniciales() -> None:
    """Carga estructura adicional e inserts iniciales en orden."""
    # Cargar solo cuando las tablas base estan vacias para evitar recargas.
    if tabla_tiene_registros("recetas"):
        print("Carga inicial omitida: la tabla recetas ya tiene datos.")
        return

    archivos = [
        os.path.join(SQL_DIR, "insert_recetas.sql"),
        os.path.join(SQL_DIR, "insert_torres.sql"),
        os.path.join(SQL_DIR, "insert_equipo.sql"),
        os.path.join(SQL_DIR, "insert_correccionesniveles.sql"),
    ]

    for ruta in archivos:
        cargar_archivo_sql(ruta, obligatorio=True)
