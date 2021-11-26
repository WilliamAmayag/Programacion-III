import conexion

class crud_escalafon:
    def consultar_escalafon(self):
        sql = "SELECT * FROM escalafon"
        return db.consultar(sql)

    def administrar_escalafon(self, contenido):
        try:
            if contenido["accion"]=="nuevo":
                sql = "INSERT INTO escalafon (escalafon) VALUES (%s)"
                val = (contenido["escalafon"],)

            elif contenido["accion"]=="modificar":
                sql = "UPDATE escalafon SET escalafon=%s WHERE idEscalafon=%s"
                val = (contenido["escalafon"], contenido["idEscalafon"])

            elif contenido["accion"]=="eliminar":
                sql = "DELETE FROM escalafon WHERE idEscalafon=%s"
                val = (contenido["idEscalafon"],)

            return db.ejecutar_consulta(sql, val)
        except Exception as e:
            return str(e)