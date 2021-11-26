import conexion

db = conexion.conexion()

class crud_materia:
    def consultar_materias(self):
        sql = """
            select materia.idMateria, materia.codigo, materia.nombre, materia.uv,
                materia.idPrerequisito, prerequisito.nombre AS prerequisito
            from materia
                left join materia prerequisito on (prerequisito.idMateria=materia.idPrerequisito)
        """
        return db.consultar(sql)
    
    def consultar_prerequisito(self):
        sql = """
            select materia.idMateria, materia.codigo, materia.nombre, materia.uv
            from materia
        """
        return db.consultar(sql)

    def administrar_materia(self, contenido):
        try:
            if contenido["accion"]=="nuevo":
                sql = "INSERT INTO materia (codigo, nombre, uv, idPrerequisito) VALUES (%s, %s, %s, %s)"
                val = (contenido["codigo"], contenido["nombre"], contenido["uv"], contenido["idPrerequisito"])

            elif contenido["accion"]=="modificar":
                sql = "UPDATE materia SET codigo=%s, nombre=%s, uv=%s, idPrerequisito=%s WHERE idMateria=%s"
                val = (contenido["codigo"], contenido["nombre"], contenido["uv"], contenido["idPrerequisito"], contenido["idMateria"])

            elif contenido["accion"]=="eliminar":
                sql = "DELETE FROM materia WHERE idMateria=%s"
                val = (contenido["idMateria"],)

            return db.ejecutar_consulta(sql, val)
        except Exception as e:
            return str(e)