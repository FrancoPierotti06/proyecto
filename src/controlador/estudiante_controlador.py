from servicio.estudiante_servicios import estudianteServicios


class Estudiantecontrolador():

    def crear(nombre,DNI,telefono, correo_electronico,fecha_de_nacimiento,curso_id):
         return estudianteServicios.crear_estudiante(nombre,DNI,telefono,correo_electronico,fecha_de_nacimiento,curso_id)
    
    def eliminar(id):
         return estudianteServicios.eliminar_estudiante(id)
    
    def mostrar():
         return estudianteServicios.mostrar_estudiante()