query_read_imagenes = """
    SELECT id, nombre, alt, categoria_id, src, fecha_creacion FROM Imagenes
"""

# TODO: Hacer que la consulta traiga la categoría
# SELECT Imagenes.nombre, Imagenes.alt, Imagenes.src, Categorias.nombre, Imagenes.fecha_creacion
# FROM Imagenes INNER JOIN Categorias
# ON Categorias.id = Imagenes.categoria_id

query_read_imagen = """
    SELECT id, nombre, alt, categoria_id, src, fecha_creacion FROM Imagenes
    WHERE Imagenes.id = ?
"""

query_create_imagen = '''
    INSERT INTO Imagenes (nombre, alt, categoria_id, src, fecha_creacion)
    VALUES (?, ?, ?, ?, ?)
'''

query_update_imagen = '''
    UPDATE Imagenes
    SET nombre = ?,
    alt = ?,
    categoria_id = ?
    WHERE Imagenes.id = ?
'''

query_delete_imagen = '''
    DELETE FROM Imagenes
    WHERE Imagenes.id = ?
'''
