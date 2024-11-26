from utils.sqlite_utils import read_sql_query, formatear_imagenes
from queries.imagenes_queries import query_read_imagenes, query_read_imagen, query_create_imagen, query_update_imagen, query_delete_imagen

# Path de la base de datos de imagenes
db = "./db/imagenes.db"

def read_imagenes():
    try:
        res = read_sql_query(lambda cur: cur.execute(query_read_imagenes).fetchall(), url_db=db)

        return formatear_imagenes(res, multiple=True)
    except Exception as err:
        return {
            "message": "Ha ocurrido un error.",
            "error": f"Unexpected {err=}, {type(err)=}"
        }

def read_imagen(id):
    try:
        res = read_sql_query(lambda cur: cur.execute(query_read_imagen, (id,)).fetchone(), url_db=db)

        return formatear_imagenes(res)
    except Exception as err:
        return {
            "message": "Ha ocurrido un error.",
            "error": f"Unexpected {err=}, {type(err)=}"
        }

def create_imagen(imagen):
    try:
        read_sql_query(lambda cur: cur.execute(query_create_imagen, imagen), commit=True, url_db=db)
        
        imagen_creada = filter(lambda item: item["nombre"] == imagen[0], read_imagenes())
        return list(imagen_creada)[0]
    except Exception as err:
        return {
            "message": "Ha ocurrido un error.",
            "error": f"Unexpected {err=}, {type(err)=}"
        }

def update_imagen(id, imagen):
    try:
        read_sql_query(lambda cur: cur.execute(query_update_imagen, (*imagen, id)), commit=True, url_db=db)
        return read_imagen(id)
    except Exception as err:
        return {
            "message": "Ha ocurrido un error.",
            "error": f"Unexpected {err=}, {type(err)=}"
        }

def delete_imagen(id):
    try:
        read_sql_query(lambda cur: cur.execute(query_delete_imagen, (id,)), commit=True, url_db=db)
        return None
    except Exception as err:
        return {
            "message": "Ha ocurrido un error.",
            "error": f"Unexpected {err=}, {type(err)=}"
        }