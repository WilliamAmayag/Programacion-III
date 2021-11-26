from urllib import parse
from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import crud_alumno
import crud_docente
import crud_escalafon
import crud_materia

crud_alumno = crud_alumno.crud_alumno()
crud_docente = crud_docente.crud_docente()
crud_escalafon = crud_escalafon.crud_escalafon()
crud_materia = crud_materia.crud_materia()
class servidorBasico(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
            return SimpleHTTPRequestHandler.do_GET(self)
        
        elif self.path == '/consultar-alumno':
            resp = crud_alumno.consultar_alumno()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))
        
        elif self.path == '/consultar-docente':
            resp = crud_docente.consultar_docente()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))
        
        elif self.path == '/consultar-escalafon':
            resp = crud_escalafon.consultar_escalafon()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))
        
        elif self.path == '/consultar-materias':
            resp = crud_materia.consultar_materias()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))
        
        elif self.path == '/consultar-prerequisito':
            resp = crud_materia.consultar_prerequisito()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))
        
        else:
            return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        data = data.decode('utf-8')
        data = parse.unquote(data)
        data = json.loads(data)
        if self.path == '/alumno':
            resp = crud_alumno.administrar_alumnos(data)
        elif self.path == '/docente':
            resp = crud_docente.administrar_docentes(data)
        elif self.path == '/materia':
            resp = crud_materia.administrar_materia(data)
        elif self.path == '/escalafon':
            resp = crud_escalafon.administrar_escalafon(data)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))
          

print('Servidor iniciado en el puerto 3000')
servidor = HTTPServer(('localhost', 3000), servidorBasico)
servidor.serve_forever()