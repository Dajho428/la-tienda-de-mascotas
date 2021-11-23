import falcon
import waitress
from falcon import App

from tienda_Mascotas.Dominio.cliente import Cliente
from tienda_Mascotas.Infraestructura.persistenciaCliente import PersistenciaCliente


class cliente():

    def on_get(self, req, resp):
        db = PersistenciaCliente()
        clientes = db.consultar_tabla_cliente()
        template = """<!-- #######  YAY, I AM THE SOURCE EDITOR! #########-->
                    <h1 style="color: #5e9ca0;">La tienda del CAMI</h1>
                    <h2 style="color: #2e6c80;">Clientes:</h2>
                    <h2 style="color: #2e6c80;">Cleaning options:</h2>
                    <table class="editorDemoTable" style="height: 362px;">
                    <thead>
                    <tr style="height: 18px;">
                    <td style="height: 18px; width: 263.172px;">Codigo Cliente</td>
                    <td style="height: 18px; width: 263.172px;">Nombre</td>
                    <td style="height: 18px; width: 348.625px;">Cedula</td>
                    </tr>
                    </thead>
                    <tbody>
                """
        for cliente in clientes:
            cliente_template = f"""<tr style="height: 22px;">
                                <td style="height: 22px; width: 263.172px;">{cliente.codigoCliente}</td>
                                <td style="height: 22px; width: 263.172px;">{cliente.nombre}</td>
                                <td style="height: 22px; width: 348.625px;">{cliente.cedula}</td>                                
                                </tr>
                                """
            template += cliente_template
        template += """</tbody>
        </table>"""
        resp.body = template
        resp.content_type = 'text/html'
        resp.status = falcon.HTTP_OK

    def on_post(self, req, resp):
        cliente = Cliente(**req.media)
        cliente.guardar(cliente)
        resp.status = falcon.HTTP_CREATED

    def on_put(self, req, resp, codigoCliente):
        cliente_repositorio = PersistenciaCliente()
        cliente = cliente_repositorio.cargar_cliente(codigoCliente)
        cliente.update(req.media)
        cliente.codigoCliente = codigoCliente
        cliente.guardar_actualizar()
        resp.body = cliente.__dict__

    def on_delete(self, req, resp, codigoCliente):
        cliente_repositorio = PersistenciaCliente()
        cliente = cliente_repositorio.cargar_cliente(codigoCliente)
        cliente.eliminar(cliente.codigoCliente)
        resp.body = codigoCliente
        resp.status = falcon.HTTP_OK


def iniciar(api) -> App:
    # run:app -b 0.0.0.0:2020 --workers 1 -t 240
    api.add_route("/cliente/", cliente())
    api.add_route("/cliente_guardar/", cliente())
    api.add_route("/cliente_actualizar/{codigoCliente}", cliente())
    api.add_route("/cliente_eliminar/{codigoCliente}/", cliente())
    return api


