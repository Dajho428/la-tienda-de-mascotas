import falcon
import waitress
from falcon import App

from tienda_Mascotas.Dominio.venta import Venta
from tienda_Mascotas.Infraestructura.persistenciaVenta import PersistenciaVenta
from tienda_Mascotas.controlador.controladorInventario import ControladorInventario


class venta():

    def on_get(self, req, resp):
        controlInven=ControladorInventario()
        inventario= controlInven.generarInventario()
        db = PersistenciaVenta()
        ventas = db.consultar_tabla_venta(inventario)
        template = """<!-- #######  YAY, I AM THE SOURCE EDITOR! #########-->
                    <h1 style="color: #5e9ca0;">La tienda del CAMI</h1>
                    <h2 style="color: #2e6c80;">Ventas:</h2>
                    <h2 style="color: #2e6c80;">Cleaning options:</h2>
                    <table class="editorDemoTable" style="height: 362px;">
                    <thead>
                    <tr style="height: 18px;">
                    <td style="height: 18px; width: 263.172px;">Codigo Venta</td>
                    <td style="height: 18px; width: 263.172px;">Cliente</td>
                    <td style="height: 18px; width: 263.172px;">Producto</td>
                    <td style="height: 18px; width: 348.625px;">Total Venta</td>
                    </tr>
                    </thead>
                    <tbody>
                """
        for venta in ventas:
            venta_template = f"""<tr style="height: 22px;">
                                <td style="height: 22px; width: 263.172px;">{venta.codigoVenta}</td>
                                <td style="height: 22px; width: 263.172px;">{venta.codigoCliente}</td>
                                <td style="height: 22px; width: 263.172px;">{venta.nombreProducto}</td>
                                <td style="height: 22px; width: 348.625px;">{venta.precioTotal}</td>                                
                                </tr>
                                """
            template += venta_template
        template += """</tbody>
        </table>"""
        resp.body = template
        resp.content_type = 'text/html'
        resp.status = falcon.HTTP_OK

    def on_post(self, req, resp):
        venta = Venta(**req.media)
        venta.guardar(venta,venta.codigoCliente,venta.codigo)
        resp.status = falcon.HTTP_CREATED




def iniciar(api) -> App:
    # run:app -b 0.0.0.0:2020 --workers 1 -t 240
    api.add_route("/venta/", venta())
    api.add_route("/venta_guardar/", venta())

    return api


