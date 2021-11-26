import conexion

db = conexion.conexion()

class crud_docente:
    def consultar_docente(self):
        sql = """
            select docentes.idDocente, docentes.codigo, docentes.nombre, docentes.telefono,
                docentes.idEscalafon, escalafon.escalafon
            from docentes
                inner join escalafon on (escalafon.idEscalafon=docentes.idEscalafon)
        """
        return db.consultar(sql)

    def administrar_docentes(self, contenido):
        try:
            if contenido["accion"]=="nuevo":
                sql = "INSERT INTO docentes (codigo, nombre, telefono, idEscalafon) VALUES (%s, %s, %s, %s)"
                val = (contenido["codigo"], contenido["nombre"], contenido["telefono"], contenido["idEscalafon"])

            elif contenido["accion"]=="modificar":
                sql = "UPDATE docentes SET codigo=%s, nombre=%s, telefono=%s, idEscalafon=%s WHERE idDocente=%s"
                val = (contenido["codigo"], contenido["nombre"], contenido["telefono"], contenido["idEscalafon"], contenido["idDocente"])

            elif contenido["accion"]=="eliminar":
                sql = "DELETE FROM docentes WHERE idDocente=%s"
                val = (contenido["idDocente"],)

            return db.ejecutar_consulta(sql, val)
        except Exception as e:
            return str(e)