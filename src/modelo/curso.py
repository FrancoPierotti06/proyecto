from peewee import Model,AutoField,CharField
from basedato.db import db

class Curso(Model):
    id = AutoField()
    nombre = CharField(unique=True)
    descripcion = CharField()
    fecha_inicio = CharField()
    fecha_inicio_fin = CharField()
    horas = CharField()

    class Meta:
        database = db
