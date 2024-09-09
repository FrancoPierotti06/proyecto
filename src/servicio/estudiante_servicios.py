from modelo.estudiante import Estudiante
from modelo.curso import Curso

class estudianteServicios():

    @staticmethod
    def crear_estudiante(nombre,DNI,telefono, correo_electronico,fecha_de_nacimiento,curso_id):
        curso = Curso.get(Curso.id == curso_id)
        estudiante= Estudiante.create(nombre=nombre, DNI=DNI, número_de_telefono=telefono, correo_electronico=correo_electronico, fecha_de_nacimiento=fecha_de_nacimiento,curso_id=curso)
        return estudiante
    
    @staticmethod
    def eliminar_estudiante(id):
        estudiante = Estudiante.get(Estudiante.id == id)
        estudiante.delete_instance()
        return estudiante
    @staticmethod
    def mostrar_estudiante():
        return list(Estudiante.select())
