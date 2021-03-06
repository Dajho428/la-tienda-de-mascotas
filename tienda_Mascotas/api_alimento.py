import falcon
import waitress
from falcon import App
from jsonpickle import json

from tienda_Mascotas.Dominio.alimento import Alimento
from tienda_Mascotas.Infraestructura.persistencia_alimento import Persistencia_alimento

class Obtener_alimentos():
    def on_get(self,req,resp):
        db=Persistencia_alimento()
        accesorios=db.consultar_tabla_alimento()
        resultado=[]
        for accesorio in accesorios:
            resultado.append(accesorio.__dict__)
        resp.body=json.dumps(resultado)
        resp.status=200


class Api_alimento():

    def on_get(self, req, resp):
        db = Persistencia_alimento()
        alimentos = db.consultar_tabla_alimento()
        template = """<!-- #######  YAY, I AM THE SOURCE EDITOR! #########-->
                    <h1 style="color: #5e9ca0;">La tienda del CAMI</h1>
                    <h2 style="color: #2e6c80;">Alimentos:</h2>
                    <h2 style="color: #2e6c80;">Cleaning options:</h2>
                    <table class="editorDemoTable" style="height: 362px;">
                    <thead>
                    <tr style="height: 18px;">
                    <td style="height: 18px; width: 263.172px;">Codigo Alimento</td>
                    <td style="height: 18px; width: 263.172px;">Nombre</td>
                    <td style="height: 18px; width: 348.625px;">Tipo Alimento</td>
                    </tr>
                    </thead>
                    <tbody>
                """
        for alimento in alimentos:
            alimento_template = f"""<tr style="height: 22px;">
                                <td style="height: 22px; width: 263.172px;">{alimento.codigoAlimento}</td>
                                <td style="height: 22px; width: 263.172px;">{alimento.nombreProducto}</td>
                                <td style="height: 22px; width: 348.625px;">{alimento.tipoAlimento}</td>                                
                                </tr>
                                """
            template += alimento_template
        template += """</tbody>
        </table>"""
        resp.body = template
        resp.content_type = 'text/html'
        resp.status = falcon.HTTP_OK

    def on_post(self, req, resp):
        alimento = Alimento(**req.media)
        alimento.guardar(alimento)
        resp.status = falcon.HTTP_CREATED

    def on_put(self, req, resp, codigoAlimento):
        alimento_repositorio = Persistencia_alimento()
        alimento = alimento_repositorio.cargar_alimento(codigoAlimento)
        alimento.update(req.media)
        alimento.codigoAlimento = codigoAlimento
        alimento.guardar_actualizar()
        resp.body = alimento.__dict__

    def on_delete(self, req, resp, codigoAlimento):
        alimento_repositorio = Persistencia_alimento()
        alimento = alimento_repositorio.cargar_alimento(codigoAlimento)
        alimento.eliminar(alimento.codigoAlimento)
        resp.body = codigoAlimento
        resp.status = falcon.HTTP_OK


def iniciar(api) -> App:
    # run:app -b 0.0.0.0:2020 --workers 1 -t 240
    api.add_route("/alimento/", Api_alimento())
    api.add_route("/alimento_guardar/", Api_alimento())
    api.add_route("/alimento_actualizar/{codigoAlimento}", Api_alimento())
    api.add_route("/alimento_eliminar/{codigoAlimento}", Api_alimento())
    api.add_route("/obtener-alimentos/", Obtener_alimentos())
    return api


