import json
import falcon
import waitress as waitress
from falcon import App
from tienda_Mascotas.Dominio.mascota import Mascota
from tienda_Mascotas.Infraestructura.persistenciaMascota import PersistenciaMascota


class mascota():

    def on_get(self, req, resp):
        db = PersistenciaMascota()
        mascotas = db.consultar_tabla_mascota()
        template = """<!-- #######  YAY, I AM THE SOURCE EDITOR! #########-->
                    <h1 style="color: #5e9ca0;">La tienda del CAMI</h1>
                    <h2 style="color: #2e6c80;">Mascotas:</h2>
                    <h2 style="color: #2e6c80;">Cleaning options:</h2>
                    <table class="editorDemoTable" style="height: 362px;">
                    <thead>
                    <tr style="height: 18px;">
                    <td style="height: 18px; width: 263.172px;">Codigo Mascota</td>
                    <td style="height: 18px; width: 263.172px;">Nombre</td>
                    <td style="height: 18px; width: 348.625px;">Tipo Mascota</td>
                    <td style="height: 18px; width: 55.2031px;">Raza</td>
                    </tr>
                    </thead>
                    <tbody>
                """
        for mascota in mascotas:
            mascota_template = f"""<tr style="height: 22px;">
                                <td style="height: 22px; width: 263.172px;">{mascota.codigoMascota}</td>
                                <td style="height: 22px; width: 263.172px;">{mascota.nombre}</td>
                                <td style="height: 22px; width: 348.625px;">{mascota.tipoMascota}</td>
                                <td style="height: 22px; width: 55.2031px;">{mascota.raza}</td>
                                </tr>
                                """
            template += mascota_template
        template += """</tbody>
        </table>"""
        resp.body = template
        resp.content_type = 'text/html'
        resp.status = falcon.HTTP_OK

    def on_post(self, req, resp):
        mascota = Mascota(**req.media)
        mascota.guardar(mascota)
        resp.status = falcon.HTTP_CREATED

    def on_put(self, req, resp, codigoMascota):
        mascota_repositorio = PersistenciaMascota()
        mascota = mascota_repositorio.cargar_mascota(codigoMascota)
        mascota.update(req.media)
        mascota.codigoMascota = codigoMascota
        mascota.guardar_actualizar()
        resp.body = mascota.__dict__

    def on_delete(self, req, resp, codigoMascota):
        mascota_repositorio = PersistenciaMascota()
        mascota = mascota_repositorio.cargar_mascota(codigoMascota)
        mascota.eliminar(mascota.codigoMascota)
        resp.body = codigoMascota
        resp.status = falcon.HTTP_OK


def iniciar(api) -> App:
    # run:app -b 0.0.0.0:2020 --workers 1 -t 240
    api.add_route("/mascota/", mascota())
    api.add_route("/mascota_guardar/", mascota())
    api.add_route("/mascota_actualizar/{codigoMascota}", mascota())
    api.add_route("/mascota_eliminar/{codigoMascota}", mascota())
    return api

