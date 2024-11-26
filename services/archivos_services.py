# Personalizados
from utils.sqlite_utils import read_sql_query, formatear_archivos
from queries.archivos_queries import query_read_archivos, query_read_archivo, query_create_archivo, query_update_archivo, query_delete_archivo

# Obtener archivos
def read_archivos():
    try:
        # lambda (función) es llamada como callback en read_sql_query. Es decir, que le pasamos a read_sql_query una función como argumento, que se ejecuta dentro de la función en la que se llama.
        # Para comprender mejor el funcionamiento, ve al archivo sqlite_utils.py
        res = read_sql_query(lambda cur: cur.execute(query_read_archivos).fetchall()) # "cur" lo recibe en la función read_sql_query.
        # "cur.execute(query)" -> ejecuta la consulta | ".fetchall()" -> Devuelve todos los registros

        # Retorna: List(dict)
        return formatear_archivos(res, multiple=True)
    except Exception as err:
        return {
            "message": "Ha ocurrido un error.",
            "error": f"Unexpected {err=}, {type(err)=}"
        }

# Obtener un archivo
def read_archivo(id):
    try:
        # (id,) -> Pasa el parametro como tupla. Ya que sqlite3 requiere una secuencia
        res = read_sql_query(lambda cur: cur.execute(query_read_archivo, (id,)).fetchone())
        return formatear_archivos(res) # type(res): Tuple
    except Exception as err:
        return {
            "message": "Ha ocurrido un error.",
            "error": f"Unexpected {err=}, {type(err)=}"
        }

# Agregar archivo
def create_archivo(archivo):
    try:
        read_sql_query(lambda cur: cur.execute(query_create_archivo, archivo), commit=True)
        
        # Retorar archivo agregado
        archivo_creado = filter(lambda item: item["nombre"] == archivo[0], read_archivos()) # Obtenemos el archivo desde read_archivos porque no contamos con su id, pero si con su nombre
        return list(archivo_creado)[0] # Convertimos el filter Object en lista y obtenemos el primer elemento
    except Exception as err:
        return {
            "message": "Ha ocurrido un error.",
            "error": f"Unexpected {err=}, {type(err)=}"
        }

# Modificar archivo
def update_archivo(id, archivo):
    try:
        read_sql_query(lambda cur: cur.execute(query_update_archivo, (*archivo, id)), commit=True)
        return read_archivo(id) # TypeError: "NoneType" object is not subscriptable
    except Exception as err:
        return {
            "message": "Ha ocurrido un error.",
            "error": f"Unexpected {err=}, {type(err)=}"
        }

# Eliminar archivo
def delete_archivo(id):
    try:
        read_sql_query(lambda cur: cur.execute(query_delete_archivo, (id,)), commit=True)
        return None
    except Exception as err:
        return {
            "message": "Ha ocurrido un error.",
            "error": f"Unexpected {err=}, {type(err)=}"
        }
