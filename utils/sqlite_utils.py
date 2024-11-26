import sqlite3

# Hacer una consulta
def read_sql_query(cb, commit = False, url_db = "./db/datos.db"):
    # Conexión con la base de datos
    conn = sqlite3.connect(url_db)

    # Ejecutar consulta
    cur = conn.cursor()
    # cb(cur) es la función que se pasa como argumento. Aquí la ejecutamos con el cursor como argumento, para que pueda ejecutar la consulta.
    # La consulta que ejecuta la puedes ver en crud.py
    res = cb(cur) # Callback(cursor)
    
    # Grabar cambios
    if commit:
        res = cur.lastrowid
        conn.commit()
    
    # Cerrar consulta
    conn.close()
    return res

# Formatear archivos con manejo de errores
def formatear_archivos(archivo: list, multiple=False):
    # Si es un solo archivo lo convierte en lista, sino guarda la lista de archivos
    archivos = archivo if multiple else [archivo]
    
    archivos_formateados = []
    
    # Se ejecuta la cantidad de archivos que haya | a es el archivo actual del ciclo
    for a in archivos:
        # Verifica que se hayan ingresado los cinco elementos
        try:
            if len(a) != 6:
                raise ValueError(f"Estructura incorrecta: se esperaban 6 elementos, pero se encontró {len(a)}.")

            # Agrega el archivo formateado en dict
            archivos_formateados.append({
                "id": a[0],
                "nombre": a[1],
                "descripcion": a[2],
                "src": a[3],
                "activo": a[4],
                "fecha_creacion": a[5]
            })
        except ValueError as e:
            print(f"Error al procesar el archivo {a}: {e}")
    
    return archivos_formateados

# Formatear archivos con manejo de errores
def formatear_imagenes(imagen: list, multiple=False):
    # Si es una sola imagen lo convierte en lista, sino guarda la lista de imagenes
    imagenes = imagen if multiple else [imagen]
    
    imagenes_formateadas = []
    
    # Se ejecuta la cantidad de imagenes que haya | "i" es la imagen actual del ciclo
    for i in imagenes:
        # Verifica que se hayan ingresado los cinco elementos
        try:
            if len(i) != 6:
                raise ValueError(f"Estructura incorrecta: se esperaban 6 elementos, pero se encontró {len(i)}.")
            
            # Agrega la imagen formateada en dict
            imagenes_formateadas.append({
                "id": i[0],
                "nombre": i[1],
                "alt": i[2],
                "categoria_id": i[3],
                "src": i[4],
                "fecha_creacion": i[5]
            })
        except ValueError as e:
            print(f"Error al procesar la imagen {i}: {e}")
    
    return imagenes_formateadas
