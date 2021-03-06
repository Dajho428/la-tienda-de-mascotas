import falcon
from falcon import App
from jsonpickle import json

from tienda_Mascotas.Dominio.accesorio import Accesorio
from tienda_Mascotas.Infraestructura.persistencia_accesorio import Persistencia_accesorio

class Obtener_accesorio():
    def on_get(self,req,resp,codigoAccesorio):
        db=Persistencia_accesorio()
        accesorios=db.consultar_tabla_accesorio()
        for accesorio in accesorios:
            if accesorio.codigoAccesorio==codigoAccesorio:
                resp.body=json.dumps(accesorio.__dict__)
                resp.status=200
                break

class Obtener_accesorios():
    def on_get(self,req,resp):
        db=Persistencia_accesorio()
        accesorios=db.consultar_tabla_accesorio()
        resultado=[]
        for accesorio in accesorios:
            resultado.append(accesorio.__dict__)
        resp.body=json.dumps(resultado)
        resp.status=200





class Api_accesorio():
    def on_get(self, req, resp):
        db = Persistencia_accesorio()
        accesorios = db.consultar_tabla_accesorio()
        template = """<!-- #######  YAY, I AM THE SOURCE EDITOR! #########-->
                    <h1 style="color: #5e9ca0;">La tienda del CAMI</h1>
                    <h2 style="color: #2e6c80;">Accesorios:</h2>
                    <h2 style="color: #2e6c80;">Cleaning options:</h2>
                    <table class="editorDemoTable" style="height: 362px;">
                    <thead>
                    <tr style="height: 18px;">
                    <td style="height: 18px; width: 263.172px;">Codigo Accesorio</td>
                    <td style="height: 18px; width: 263.172px;">Nombre Accesorio</td>
                    <td style="height: 18px; width: 348.625px;">Descripcion</td>
                    <td style="height: 18px; width: 263.172px;">Cantidad</td>
                    <td style="height: 18px; width: 348.625px;">Precio</td>
                    
                    </tr>
                    </thead>
                    <tbody>
                """
        for accesorio in accesorios:
            accesorio_template = f"""<tr style="height: 22px;">
                                <td style="height: 22px; width: 263.172px;">{accesorio.codigoAccesorio}</td>
                                <td style="height: 22px; width: 263.172px;">{accesorio.nombreAccesorio}</td>
                                <td style="height: 22px; width: 348.625px;">{accesorio.descripcionAccesorio}</td> 
                                 <td style="height: 22px; width: 348.625px;">{accesorio.cantidad}</td> 
                                 <td style="height: 22px; width: 348.625px;">{accesorio.precio}</td>                               
                                </tr>
                                """
            template += accesorio_template
        template += """</tbody>
        </table>"""
        resp.body = template
        resp.content_type = 'text/html'
        resp.status = falcon.HTTP_OK

    def on_post(self, req, resp):
        accesorio = Accesorio(**req.media)
        accesorio.guardar(accesorio)
        resp.status = falcon.HTTP_CREATED

    def on_put(self, req, resp, codigoAccesorio):
        accesorio_repositorio = Persistencia_accesorio()
        accesorio = accesorio_repositorio.cargar_accesorio(codigoAccesorio)
        accesorio.update(req.media)
        accesorio.codigoAccesorio = codigoAccesorio
        accesorio.guardar_actualizar()
        resp.body = accesorio.__dict__

    def on_delete(self, req, resp, codigoAccesorio):
        accesorio_repositorio = Persistencia_accesorio()
        accesorio = accesorio_repositorio.cargar_accesorio(codigoAccesorio)
        accesorio.eliminar(accesorio.codigoAccesorio)
        resp.body = codigoAccesorio
        resp.status = falcon.HTTP_OK


def iniciar(api) -> App:

    api.add_route("/accesorio/", Api_accesorio())
    api.add_route("/accesorio_guardar/", Api_accesorio())
    api.add_route("/accesorio_actualizar/{codigoAccesorio}", Api_accesorio())
    api.add_route("/accesorio_eliminar/{codigoAccesorio}", Api_accesorio())
    api.add_route("/obtener-accesorio/{codigoAccesorio}", Obtener_accesorio())
    api.add_route("/obtener-accesorio/", Obtener_accesorios())
    return api


