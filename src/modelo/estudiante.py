from peewee import Model, AutoField, CharField,DateField, ForeignKeyField, Model
from basedato.db import db

from modelo.curso import Curso

class Estudiante(Model):
     id = AutoField
     nombre = CharField(unique=True)
     DNI = CharField()
     Correo_Electronico = CharField()
     número_de_telefono = CharField()
     fecha_de_nacimiento = CharField(unique= True)
     curso_id = ForeignKeyField(Curso)

     class Meta:
        database = db
        table_name = "Estudiante"

    
