from modelo.curso import Curso
from modelo.estudiante import Estudiante
from controlador.curso_controlador import Cursocontrolador
from controlador.estudiante_controlador import Estudiantecontrolador
from basedato.db import db


def main():
    db.connect()
    #db.create_tables([Curso, Estudiante])
    estudiantes = Estudiantecontrolador.mostrar()

    for estudiante in estudiantes:
        print(f"{estudiante.id} {estudiante.nombre} {estudiante.dni}")

    #Cursocontrolador.crear("Programcion III", "hola", "12/01/2024", "12/08/2023", "12:00")
    cursos = Cursocontrolador.mostrar()

    for curso in cursos:
        print(f"{curso.id} {curso.nombre} {curso.descripcion}")

    #Estudiantecontrolador.crear("Victor","47.588.511","2901513850", "francopierotti06@gmail.com","2023-09-23",3)
    Estudiantecontrolador.eliminar(5)


if __name__ ==  "__main__":
    main()

