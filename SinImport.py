import pickle
import os
class ESTUDIANTE:
    def __init__(self):
        self.id_estudiante = 0,
        self.email = "",
        self.nombre = "",
        self.sexo = '',
        self.contrasenia = "",
        self.estado = False,
        self.hobbies = "",
        self.materia_favorita = "",
        self.deporte_favorito = "",
        self.materia_fuerta = "",
        self.materia_debil = "",
        self.biografia = "",
        self.pais = "",
        self.ciudad = "",
        self.fecha_nacimiento = ""
rutaEstudiante = "./ESTUDIANTES.DAT"
if (os.path.exists(rutaEstudiante) == False):
        regEstudiantes = open(rutaEstudiante, "w+b")
elif(os.path.exists(rutaEstudiante) == True):
        regEstudiantes = open(rutaEstudiante, "r+b")

def formatearEstudiante(estudiante):
    estudiante.email = estudiante.email.ljust(32, ' ')
    estudiante.contrasenia =  estudiante.contrasenia.ljust(32, ' ')
    estudiante.nombre = estudiante.nombre.ljust(32, ' ')
    estudiante.fecha_nacimiento = estudiante.fecha_nacimiento.ljust(10, ' ')
    estudiante.biografia = estudiante.biografia.ljust(255, ' ')
    estudiante.hobbies = estudiante.hobbies.ljust(255, ' ')
    estudiante.sexo = estudiante.sexo.ljust(1, ' ')
    estudiante.ciudad = estudiante.ciudad.ljust(32, ' ')
    estudiante.pais = estudiante.pais.ljust(32, ' ')




estudiante1 = ESTUDIANTE()
estudiante1.email = "estudiante1@ayed.com"
estudiante1.contrasenia = "111222"
estudiante1.nombre = "Juan Peréz"
estudiante1.fecha_nacimiento = "2001-10-01"
estudiante1.biografia = "Juan Peréz es un estudiante de informática apasionado por la programación. Le encanta aprender nuevos lenguajes y tecnologías."
estudiante1.hobbies = "Lectura - Senderismo - Juegos de mesa"
estudiante1.sexo = "M"
estudiante1.ciudad = "Rosario"
estudiante1.pais = "Argentina"
estudiante1.estado = True

formatearEstudiante(estudiante1)

pickle.dump(estudiante1, regEstudiantes)
regEstudiantes.flush()

estudiante2 = ESTUDIANTE()
estudiante2.email = "estudiante2@ayed.com"
estudiante2.contrasenia = "333444"
estudiante2.nombre = "María García"
estudiante2.fecha_nacimiento = "1998-04-11"
estudiante2.biografia = "María García es una estudiante de arte con una pasión por la pintura y el dibujo desde una edad temprana. Actualmente está explorando nuevas formas de expresión artística."
estudiante2.hobbies = "Pintura al óleo - Dibujo de retratos - Lectura de novelas históricas"
estudiante2.pais = "España"
estudiante2.sexo = "m"
estudiante2.ciudad = "Madrid"
estudiante2.estado = True

formatearEstudiante(estudiante2)

pickle.dump(estudiante2, regEstudiantes)
regEstudiantes.flush()

regEstudiantes.seek(0,0)

t = os.path.getsize(rutaEstudiante)
print(t)
if(t != 0):
    while(regEstudiantes.tell() < os.path.getsize(rutaEstudiante)):
        E = pickle.load(regEstudiantes)
        print(E.email)
        print(E.contrasenia)
        print(E.nombre)
        print(E.pais)