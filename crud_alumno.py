import conexion

db = conexion.conexion()

class crud_alumno:
    def consultar_alumno(self):
        sql = "SELECT * FROM alumnos"
        return db.consultar(sql)

    def administrar_alumnos(self, contenido):
        try:
            if contenido["accion"]=="nuevo":
                sql = "INSERT INTO alumnos (codigo, nombre, telefono) VALUES (%s, %s, %s)"
                val = (contenido["codigo"], contenido["nombre"], contenido["telefono"])

            elif contenido["accion"]=="modificar":
                sql = "UPDATE alumnos SET codigo=%s, nombre=%s, telefono=%s WHERE idAlumno=%s"
                val = (contenido["codigo"], contenido["nombre"], contenido["telefono"], contenido["idAlumno"])

            elif contenido["accion"]=="eliminar":
                sql = "DELETE FROM alumnos WHERE idAlumno=%s"
                val = (contenido["idAlumno"],)

            return db.ejecutar_consulta(sql, val)
        except Exception as e:
            return str(e)