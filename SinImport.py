#region creacion y formateo
import pickle
import os
class ESTUDIANTE:
    def __init__(self):
        self.email = "",
        self.nombre = "",
        self.sexo = "",
        self.contrasenia = "",
        #self.hobbies = "",
        #self.biografia = "",
        self.pais = "",
        self.ciudad = "",
        self.fecha_nacimiento = ""
        self.materia_favorita = "",
        self.deporte_favorito = "",
        self.materia_fuerte = "",
        self.materia_debil = "",

rutaEstudiante = "./ESTUDIANTES.DAT"
if (os.path.exists(rutaEstudiante) == False):
        regEstudiantes = open(rutaEstudiante, "w+b")
elif(os.path.exists(rutaEstudiante) == True):
        regEstudiantes = open(rutaEstudiante, "r+b")

def formatearEstudiante(estudiante):
    estudiante.email = estudiante.email.ljust(32, ' ')
    estudiante.nombre = estudiante.nombre.ljust(32, ' ')
    estudiante.sexo = estudiante.sexo.ljust(10, ' ')
    estudiante.contrasenia =  estudiante.contrasenia.ljust(32, ' ')
    #estudiante.hobbies = estudiante.hobbies.ljust(512, ' ')
    #estudiante.biografia = estudiante.biografia.ljust(512, ' ')
    estudiante.pais = estudiante.pais.ljust(32, ' ')
    estudiante.ciudad = estudiante.ciudad.ljust(32, ' ')
    estudiante.fecha_nacimiento = estudiante.fecha_nacimiento.ljust(10, ' ')
    estudiante.materia_favorita = estudiante.materia_favorita.ljust(50, ' ')
    estudiante.deporte_favorito = estudiante.deporte_favorito.ljust(50, ' ')
    estudiante.materia_fuerte = estudiante.materia_fuerte.ljust(50, ' ')
    estudiante.materia_debil = estudiante.materia_debil.ljust(50, ' ')

estudiante1 = ESTUDIANTE()
estudiante1.email = "estudiante1@ayed.com"
estudiante1.nombre = "Juan Peréz"
estudiante1.sexo = "M"
estudiante1.contrasenia = "111222"
#estudiante1.hobbies = "Lectura - Senderismo - Juegos de mesa"
#estudiante1.biografia = "Juan Peréz es un estudiante de informática apasionado por la programación. Le encanta aprender nuevos lenguajes y tecnologías."
estudiante1.pais = "Argentina"
estudiante1.ciudad = "Rosario"
estudiante1.fecha_nacimiento = "2001-10-01"
estudiante1.materia_favorita = ""
estudiante1.deporte_favorito = ""
estudiante1.materia_fuerte = ""
estudiante1.materia_debil = ""

formatearEstudiante(estudiante1)
pickle.dump(estudiante1, regEstudiantes)
regEstudiantes.flush()

estudiante2 = ESTUDIANTE()
estudiante2.email = "@ayed.com"
estudiante2.nombre = " García"
estudiante2.sexo = "m"
estudiante2.contrasenia = ""
#estudiante2.hobbies = "Pintura al óleo - Dibujo de retratos - Lectura de novelas históricas"
#estudiante2.biografia = "María García es una estudiante de arte con una pasión por la pintura y el dibujo desde una edad temprana. Actualmente está explorando nuevas formas de expresión artística."
estudiante2.pais = ""
estudiante2.ciudad = ""
estudiante2.fecha_nacimiento = "-04-11"
estudiante2.materia_favorita = ""
estudiante2.deporte_favorito = ""
estudiante2.materia_fuerte = ""
estudiante2.materia_debil = ""

formatearEstudiante(estudiante2)
pickle.dump(estudiante2, regEstudiantes)
regEstudiantes.flush()

estudiante3 = ESTUDIANTE()
estudiante3.email = "estudiante3"
estudiante3.nombre = "Carlos Martínez"
estudiante3.sexo = "f"
estudiante3.contrasenia = "123"
#estudiante3.hobbies = "Correr - Tocar la guitarra - Cocinar platos internacionales"
#estudiante3.biografia = "Carlos Martínez es un estudiante de medicina enfocado en la investigación de enfermedades infecciosas. Su objetivo es contribuir al desarrollo de tratamientos más efectivos y accesibles."
estudiante3.pais = "Bolivia"
estudiante3.ciudad = "La Paz" 
estudiante3.fecha_nacimiento = "2005-06-30"
estudiante3.materia_favorita = ""
estudiante3.deporte_favorito = ""
estudiante3.materia_fuerte = ""
estudiante3.materia_debil = ""

formatearEstudiante(estudiante3)
pickle.dump(estudiante3, regEstudiantes)
regEstudiantes.flush()
regEstudiantes.seek(0,0)
#endregion

t = os.path.getsize(rutaEstudiante)
pickle.load(regEstudiantes)
tamEst = regEstudiantes.tell()
canEst = t / tamEst
regEstudiantes.seek(0, 0)

print(t)
print(tamEst)
print(canEst)

if(t != 0):
    regEstudiantes.seek(0,0)
    while(regEstudiantes.tell() < os.path.getsize(rutaEstudiante)):
        E = pickle.load(regEstudiantes)
        if E.nombre == ("Juan Peréz").ljust(32, ' '):
            E.nombre = "Conchita Barreda"
            regEstudiantes.seek(1*tamEst,0)
            formatearEstudiante(E)
            pickle.dump(E, regEstudiantes)
        print(E.nombre)
