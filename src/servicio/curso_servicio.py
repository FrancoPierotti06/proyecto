from modelo.curso import Curso


class CursoServicio:
    
    @staticmethod
    def crear_curso(nombre,descripcion, fecha_inicio,fecha_inicio_fin,horas ):
        curso = Curso.create(nombre=nombre, descripcion=descripcion, fecha_inicio=fecha_inicio,fecha_inicio_fin=fecha_inicio_fin,horas=horas)
        return curso
    
    @staticmethod
    def mostrar_cursos():
        return list(Curso.select())
    