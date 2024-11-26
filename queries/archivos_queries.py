# Consultas
query_read_archivos = '''
    SELECT id_archivo, nombre, descripcion, src, activo, fecha_creacion
    FROM Archivos
'''

query_read_archivo = '''
    SELECT id_archivo, nombre, descripcion, src, activo, fecha_creacion
    FROM Archivos
    WHERE Archivos.id_archivo = ?
'''

query_create_archivo = '''
    INSERT INTO Archivos (nombre, descripcion, src, activo, fecha_creacion)
    VALUES (?, ?, ?, ?, ?)
'''

query_update_archivo = '''
    UPDATE Archivos
    SET nombre = ?,
    descripcion = ?,
    activo = ?
    WHERE Archivos.id_archivo = ?
'''

query_delete_archivo = '''
    DELETE FROM Archivos
    WHERE Archivos.id_archivo = ?
'''