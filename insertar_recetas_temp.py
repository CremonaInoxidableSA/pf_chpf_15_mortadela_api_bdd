from sqlalchemy import text
from sqlalchemy.orm import Session
from config.db import engine

# Agregar columna Armador si no existe
with Session(engine) as session:
    try:
        session.execute(text("ALTER TABLE equipo ADD COLUMN Armador VARCHAR(255);"))
        session.commit()
    except Exception:
        session.rollback()  # Si ya existe, ignorar

    # Insertar 3 recetas
    session.execute(text("""
        INSERT INTO recetas (id_receta, codigo_producto, peso_producto, tipo_corte, alto_producto, largo_producto, ancho_producto, productos_fila, productos_columna) VALUES
        (1, 'Mortadela Larga', 500, 1, 10, 20, 5, 2, 3),
        (2, 'Mortadela Mediana', 600, 2, 12, 22, 6, 3, 4),
        (3, 'Mortadela Corta', 700, 3, 14, 24, 7, 4, 5);
    """))

    session.execute(text("""
        INSERT INTO torres (id_torre, nombre_torre, niveles_torre, filas_torre, id_receta, correccion_busqueda, correccion_guardado) VALUES
        (1, 'Torre PF1', 3, 2, 1, 10, 1),
        (2, 'Torre PF2', 4, 3, 2, 12, 2),
        (3, 'Torre PF3', 2, 1, 2, 8, 1),
        (4, 'Torre PF4', 5, 4, 3, 14, 3),
        (5, 'Torre PF5', 3, 2, 3, 10, 1);
    """))

    session.execute(text("""
        INSERT INTO equipo (id_equipo, nombre_equipo) VALUES
        (1, 'Armador');
    """))

    session.execute(text("""
        INSERT INTO correccionesniveles (id_correccion, valor, nivel, tipo, id_torre) VALUES
        (1, 1, 1, "ChG", 1),
        (2, 1, 2, "ChG", 1),
        (3, 1, 3, "ChG", 1),
        (4, 3, 4, "ChG", 1),
        (5, 3, 5, "ChG", 1),
        (6, 1, 6, "ChG", 1),
        (7, 1, 7, "ChG", 1),
        (8, 1, 8, "ChG", 1),
        (9, 1, 9, "ChG", 1),
        (10, 1, 10, "ChG", 1),
        (11, 1, 11, "ChG", 1),
        (12, 1, 12, "ChG", 1),
        (13, 1, 1, "ChB", 1),
        (14, 1, 2, "ChB", 1),
        (15, 1, 3, "ChB", 1),
        (16, 3, 4, "ChB", 1),
        (17, 3, 5, "ChB", 1),
        (18, 1, 6, "ChB", 1),
        (19, 1, 7, "ChB", 1),
        (20, 1, 8, "ChB", 1),
        (21, 1, 9, "ChB", 1),
        (22, 1, 10, "ChB", 1),
        (23, 1, 11, "ChB", 1),
        (24, 1, 12, "ChB", 1)
    """))
    
    session.commit()
print("Datos insertados correctamente en recetas, torres, correcciones y equipo.")
