#region Imports
from datetime import date, datetime
from getpass import getpass
import os, platform, random
import pickle
#endregion

GENERO = ["F", "M"]
PROPS_ESTUDIANTE = ["Nombre","Nacimiento","Biografía","Hobbies","Género","Ciudad","País",]

#region formateos
def formatearEstudiante(estudiante):
    estudiante.email = estudiante.email.ljust(32, ' ')
    estudiante.nombre = estudiante.nombre.ljust(32, ' ')
    estudiante.sexo = estudiante.sexo.ljust(1, ' ')
    estudiante.contrasenia =  estudiante.contrasenia.ljust(32, ' ')
    estudiante.hobbies = estudiante.hobbies.ljust(255, ' ')
    estudiante.materia_favorita = estudiante.materia_favorita.ljust(255, ' ')
    estudiante.deporte_favorito = estudiante.deporte_favorito.ljust(255, ' ')
    estudiante.materia_fuerte = estudiante.materia_fuerte.ljust(255, ' ')
    estudiante.materia_debil = estudiante.materia_debil.ljust(255, ' ')
    estudiante.biografia = estudiante.biografia.ljust(255, ' ')
    estudiante.ciudad = estudiante.ciudad.ljust(32, ' ')
    estudiante.pais = estudiante.pais.ljust(32, ' ')
    estudiante.fecha_nacimiento = estudiante.fecha_nacimiento.ljust(10, ' ')


def formatearModerador(moderador):
    moderador.email =  moderador.email.ljust(32, ' ')
    moderador.contrasenia = moderador.contrasenia.ljust(32, ' ')

def formatearReporte(reporte):
    reporte.razon_reporte = reporte.razon_reporte.ljust(255, ' ')

#endregion

#region Declaracion de Clases
...
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
        self.materia_fuerte = "",
        self.materia_debil = "",
        self.biografia = "",
        self.pais = "",
        self.ciudad = "",
        self.fecha_nacimiento = ""

class MODERADOR:
    def __init__(self):
        self.id_moderadores = 0,
        self.email = "",
        self.contrasenia = "",
        self.estado = False

class ADMINISTRADOR:
    def __init__(self):
        self.id_admin = 0,
        self.email = "",
        self.contrasenia = ""

class LIKE:
    def __init__(self):
        self.remitente = 0,
        self.destinatario = 0

class REPORTE:
    def __init__(self):
        self.id_reportante = 0,
        self.id_reportado = 0,
        self.razon_reporte = "",
        self.estado = 0

#endregion

#region InicializarMocks
def inicializar_likes_mock(regLikes):
    for i in range(8):
        like = LIKE()
        like.remitente = random.randint(0, 7)
        like.destinatario = random.randint(0, 7)
        while like.remitente == like.destinatario:
            like.destinatario = random.randint(0, 7)
        pickle.dump(like, regLikes)
        regLikes.flush()


def inicializar_estudiantes_mock(regEstudiante):
    estudiante1 = ESTUDIANTE()
    estudiante1.id_estudiante = 0
    estudiante1.email = "estudiante1"
    estudiante1.nombre = "Juan Peréz"
    estudiante1.sexo = GENERO[1]
    estudiante1.contrasenia = "123"
    estudiante1.estado = True
    estudiante1.hobbies = "Lectura - Senderismo - Juegos de mesa"
    estudiante1.materia_favorita = ""
    estudiante1.deporte_favorito = ""
    estudiante1.materia_fuerte = ""
    estudiante1.materia_debil = ""
    estudiante1.biografia = "Juan Peréz es un estudiante de informática apasionado por la programación. Le encanta aprender nuevos lenguajes y tecnologías."
    estudiante1.pais = "Argentina"
    estudiante1.ciudad = "Rosario"
    estudiante1.fecha_nacimiento = "2001-10-01"

    formatearEstudiante(estudiante1)

    pickle.dump(estudiante1, regEstudiante)
    regEstudiante.flush()

    estudiante2 = ESTUDIANTE()
    estudiante2.id_estudiante = 1
    estudiante2.email = "estudiante2"
    estudiante2.nombre = "María García"
    estudiante2.sexo = GENERO[0]
    estudiante2.contrasenia = "123"
    estudiante2.estado = True
    estudiante2.hobbies = "Pintura al óleo - Dibujo de retratos - Lectura de novelas históricas"
    estudiante2.materia_favorita = ""
    estudiante2.deporte_favorito = ""
    estudiante2.materia_fuerte = ""
    estudiante2.materia_debil = ""
    estudiante2.biografia = "María García es una estudiante de arte con una pasión por la pintura y el dibujo desde una edad temprana. Actualmente está explorando nuevas formas de expresión artística."
    estudiante2.pais = "España"
    estudiante2.ciudad = "Madrid"
    estudiante2.fecha_nacimiento = "1998-04-11"

    formatearEstudiante(estudiante2)

    pickle.dump(estudiante2, regEstudiante)
    regEstudiante.flush()

    estudiante3 = ESTUDIANTE()
    estudiante3.id_estudiante = 2
    estudiante3.email = "estudiante3"
    estudiante3.nombre = "Carlos Martínez"
    estudiante3.sexo = GENERO[1]
    estudiante3.estado = True
    estudiante3.contrasenia = "123"
    estudiante3.hobbies = "Correr - Tocar la guitarra - Cocinar platos internacionales"
    estudiante3.materia_favorita = ""
    estudiante3.deporte_favorito = ""
    estudiante3.materia_fuerte = ""
    estudiante3.materia_debil = ""
    estudiante3.biografia = "Carlos Martínez es un estudiante de medicina enfocado en la investigación de enfermedades infecciosas. Su objetivo es contribuir al desarrollo de tratamientos más efectivos y accesibles."
    estudiante3.pais = "Bolivia"
    estudiante3.ciudad = "La Paz"
    estudiante3.fecha_nacimiento = "2005-06-30"

    formatearEstudiante(estudiante3)

    pickle.dump(estudiante3, regEstudiante)
    regEstudiante.flush()

    estudiante4 = ESTUDIANTE()
    estudiante4.id_estudiante = 3
    estudiante4.email = "estudiante4"
    estudiante4.nombre = "Ana López"
    estudiante4.sexo = GENERO[0]
    estudiante4.contrasenia = "123"
    estudiante4.estado = True
    estudiante4.hobbies = "Leer ciencia ficción - Pintar - Practicar yoga"
    estudiante4.materia_favorita = ""
    estudiante4.deporte_favorito = ""
    estudiante4.materia_fuerte = ""
    estudiante4.materia_debil = ""
    estudiante4.biografia = "Ana López es una estudiante de ingeniería informática interesada en la inteligencia artificial y la ciberseguridad. Aspira a desarrollar tecnologías innovadoras que mejoren la seguridad digital."
    estudiante4.pais = "Paraguay"
    estudiante4.ciudad = "Asunción"
    estudiante4.fecha_nacimiento = "2001-09-15"
    

def inicializar_moderadores_mock(regModerador):
    moderador = MODERADOR()
    moderador.id_moderadores = 0
    moderador.email = "moderador1"
    moderador.contrasenia = "123"
    moderador.estado = 1

    formatearModerador(moderador)
    pickle.dump(moderador, regModerador)
    regModerador.flush()

def inicializar_reportes_mock(regReportes):
    reporte1 = REPORTE()
    reporte1.estado = 0
    reporte1.id_reportante = 1
    reporte1.id_reportado = 2
    reporte1.razon_reporte = "Motivo 1"

    formatearReporte(reporte1)
    pickle.dump(reporte1, regReportes)
    regReportes.flush()

    reporte2 = REPORTE()
    reporte2.estado = 0
    reporte2.id_reportante = 2
    reporte2.id_reportado = 3
    reporte2.razon_reporte = "Motivo 2"
    formatearReporte(reporte2)
    pickle.dump(reporte2, regReportes)
    regReportes.flush()

    reporte3 = REPORTE()
    reporte3.estado = 0
    reporte3.id_reportante = 4
    reporte3.id_reportado = 2
    reporte3.razon_reporte = "Motivo 3"
    formatearReporte(reporte3)
    pickle.dump(reporte3, regReportes)
    regReportes.flush()

#endregion

#region Abrir y Cerrar Archivos
rutaCarpetaDatos = "./carpetaDatos"
rutaEstudiante = "./carpetaDatos/ESTUDIANTES.DAT"
rutaModeradores = "./carpetaDatos/MODERADORES.DAT"
rutaAdministradores = "./carpetaDatos/ADMINISTRADORES.DAT"
rutaLikes = "./carpetaDatos/LIKES.DAT"
rutaReportes = "./carpetaDatos/REPORTES.DAT"

def AbrirArchivo(rutaCarpetaDatos, rutaEstudiante, rutaModeradores, rutaAdministradores, rutaLikes, rutaReportes):
    global primeraVez
    global regEstudiantes, regModeradores, regAdministradores, regLikes, regReportes

    if not os.path.exists(rutaCarpetaDatos):
        os.makedirs(rutaCarpetaDatos)
    
    if (os.path.exists(rutaEstudiante) == False):
        regEstudiantes = open(rutaEstudiante, "w+b")
        inicializar_estudiantes_mock(regEstudiantes)
    elif(os.path.exists(rutaEstudiante) == True):
        regEstudiantes = open(rutaEstudiante, "r+b")
    
    if (os.path.exists(rutaModeradores) == False):
        regModeradores = open(rutaModeradores, "w+b")
        inicializar_moderadores_mock(regModeradores)
        primeraVez = 1
    elif(os.path.exists(rutaModeradores) == True):
        regModeradores = open(rutaModeradores, "r+b")

    if (os.path.exists(rutaAdministradores) == False):
        regAdministradores = open(rutaAdministradores, "w+b")
        primeraVez = 1
    elif(os.path.exists(rutaAdministradores) == True):
        regAdministradores = open(rutaAdministradores, "r+b")    
    
    if (os.path.exists(rutaLikes) == False):
        regLikes = open(rutaLikes, "w+b")
        inicializar_likes_mock(regLikes)
        primeraVez = 1
    elif(os.path.exists(rutaLikes) == True):
        regLikes = open(rutaLikes, "r+b")    

    if (os.path.exists(rutaReportes) == False):
        regReportes = open(rutaReportes, "w+b")
        inicializar_reportes_mock(regReportes)
        primeraVez = 1
    elif(os.path.exists(rutaReportes) == True):
        regReportes = open(rutaReportes, "r+b")

def CerrarArchivo(regEstudiantes, regModeradores, regAdministradores, regLikes, regReportes):
    regEstudiantes.close()
    regModeradores.close()
    regAdministradores.close()
    regLikes.close()
    regReportes.close()

#endregion

#region validaciones y Shareds

def limpiar_consola():
    so = platform.system()

    if so == "Windows":
        comando = "cls"
    else:
        comando = "clear"

    os.system(comando)
    

def en_construccion():
    limpiar_consola()
    print("En construcción.")
    input("Presiona Enter para continuar... ")
    

def validar_continuacion(opc): #LISTO
    while opc != "S" and opc != "N":
        opc = input("Opción incorrecta S o N: ").upper()

    limpiar_consola()

    return opc


def ingresar_fecha():
    fecha = [""] * 3

    while fecha[0] == "":
        fecha[0] = input("Ingresa el día de nacimiento: ")

    while fecha[1] == "":
        fecha[1] = input("Ingresa el mes de nacimiento: ")

    while fecha[2] == "":
        fecha[2] = input("Ingresa el año de nacimento: ")

    return fecha


def validar_valores_fecha(dia, mes, anio):
    es_valido = True

    if mes < 1 or mes > 12:
        es_valido = False
    elif (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and (dia < 1 or dia > 31):
        es_valido = False
    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and (dia < 1 or dia > 30):
        es_valido = False
    elif mes == 2:
        max_dia_febrero = 28

        if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
            max_dia_febrero = max_dia_febrero + 1

        if dia < 1 or dia > max_dia_febrero:
            es_valido = False
    elif anio > 2006 or anio < 1959:
        es_valido = False

    return es_valido


def validar_fecha(fecha):
    while not (fecha[0].isdigit() and fecha[1].isdigit() and fecha[2].isdigit()):
        print("Los datos ingresados no son válidos")
        print("\n")
        fecha = ingresar_fecha()

    while not validar_valores_fecha(int(fecha[0]), int(fecha[1]), int(fecha[2])):
        print("Los datos ingresados no son válidos")
        print("\n")
        fecha = ingresar_fecha()
    input(fecha)


def mostrar_edades(edades):
    for ind in range(6):
        print(f"- {edades[ind]} años")


def mostrar_valores_faltantes(edad_1, edad_2):
    print("\nSe detectó un hueco.")
    print(f"Los valores faltantes entre {edad_1} y {edad_2} años son:\n")

    for edad in range(edad_1 + 1, edad_2):
        print("-", edad)

    print("\n")


def detectar_huecos_entre_edades(edades):
    cant_huecos = 0

    for ind in range(5):
        edad_1 = edades[ind]
        edad_2 = edades[ind + 1]

        if edad_2 - edad_1 != 1:
            cant_huecos = cant_huecos + 1
            mostrar_valores_faltantes(edad_1, edad_2)

    if cant_huecos != 0:
        print(f"Se encontraron {cant_huecos} huecos entre las edades de los 6 estudiantes.")
    else:
        print("No se encontrarón huecos entra las edades los 6 estudiantes.")


def ordenar_edades_creciente(edades):
    for i in range(5):
        for j in range(i + 1, 6):
            if edades[i] > edades[j]:
                aux = edades[j]
                edades[j] = edades[i]
                edades[i] = aux


def calcular_edad(fecha):
    fecha_actual = datetime.now()
    fecha_nros = obtener_valores_fecha(fecha)

    dia = fecha_nros[0]
    mes = fecha_nros[1]
    anio = fecha_nros[2]
    edad = fecha_actual.year - anio

    if fecha_actual.month <= mes and fecha_actual.day < dia:
        edad = edad - 1

    return edad


def huecos_edades():
    edades = [21, 18, 20, 19, 23, 24]

    limpiar_consola()
    print("Las edades de los estudiantes obtenidas del reporte son:")
    mostrar_edades(edades)

    print("\nLas edades de los estudiantes ordenadas de forma creciente son:")
    ordenar_edades_creciente(edades)
    mostrar_edades(edades)
    detectar_huecos_entre_edades(edades[:])

    input("Presiona Enter para volver al inicio...")


def obtener_valores_fecha(fecha):
    fecha_nros = [0] * 3

    f = datetime.fromisoformat(fecha)

    fecha_nros[0] = f.day
    fecha_nros[1] = f.month
    fecha_nros[2] = f.year

    return fecha_nros


def formatear_fecha_espaniol(fecha):
    fecha_nros = obtener_valores_fecha(fecha)
    formato_espaniol_nacimiento = (str(fecha_nros[0]) + "/" + str(fecha_nros[1]) + "/" + str(fecha_nros[2]))

    return formato_espaniol_nacimiento


def solicitar_fecha_nacimiento():
    fecha = ingresar_fecha()
    validar_fecha(fecha)

    f = date(int(fecha[2]), int(fecha[1]), int(fecha[0]))

    return f.isoformat()


def matcheos_combinados(): #EN TEORIA ESTA LISTO
    limpiar_consola()
    cant_est = contar_estudiantes_activos()  #LISTO
    cant_matcheos = cant_est * (cant_est - 1) // 2

    print( f"La cantidad de matcheos posibles entre los {cant_est} estudiantes actuales es igual a {cant_matcheos}.")
    input("\nPresiona Enter para volver al inicio...")


def ingresar_contrasenia():
    password = getpass("Ingrese su contraseña: ")

    while password == "":
        password = getpass("Debe ingresar una contraseña: ")

    return password


def email_existente(email, estudiantes, moderadores):
    valido = True

    ind = 0
    while ind < 8 and estudiantes[ind][0] != email:
        ind = ind + 1

    if ind < 8:
        valido = False
    else:
        ind = 0
        while ind < 4 and moderadores[ind][0] != email:
            ind = ind + 1

        if ind != 4:
            valido = False

    return valido


def validar_acceso(acceso_valido, estudiantes, moderadores, estados):
    intentos = 3

    while intentos > 0 and acceso_valido[0] == "":
        email = input("Ingrese su email: ")
        password = getpass("Ingrese su contraseña: ")

        ind = 0
        while ind < 8 and (estudiantes[ind][0] != email or estudiantes[ind][1] != password):
            ind = ind + 1

        if ind < 8 and estados[ind]:
            acceso_valido[0] = ind
            acceso_valido[1] = 1
        else:
            ind = 0
            while ind < 4 and (moderadores[ind][0] != email or moderadores[ind][1] != password):
                ind = ind + 1

            if ind < 4:
                acceso_valido[0] = ind
                acceso_valido[1] = 0
            else:
                limpiar_consola()
                intentos = intentos - 1
                print("Datos incorrectos. Intentos restantes:", intentos, "\n")

    if intentos == 0:
        print("Ha superado el número máximo de intentos. El programa se cerrará.")
        input("Presione Enter para continuar... ")
    limpiar_consola()

def log_in():
    acceso_valido = [-1] * 2
    intentos = 3
    encontrado = False

    limpiar_consola()
    print("\n........Ingreso........\n")

    while intentos > 0 and acceso_valido[0] == -1:
        email = input("Ingrese su email: ").ljust(32, ' ')
        password = getpass("Ingrese su contraseña: ").ljust(32, ' ')
        ind = 0
        regEstudiantes.seek(0,0)
        while(regEstudiantes.tell() < os.path.getsize(rutaEstudiante) and encontrado != True):
            est = pickle.load(regEstudiantes)
            if(email == est.email and password == est.contrasenia and est.estado == True):
                acceso_valido[0] = ind
                acceso_valido[1] = 0
                encontrado = True
            if encontrado == False:
                ind = ind + 1
        
        if encontrado == False:
            ind = 0
            regModeradores.seek(0,0)
            while(regModeradores.tell() < os.path.getsize(rutaModeradores)):
                mod = pickle.load(regModeradores)
                if(email == mod.email and password == mod.contrasenia and mod.estado == True):
                    acceso_valido[0] = ind
                    acceso_valido[1] = 1
                    encontrado = True
                if encontrado == False:
                    ind = ind + 1
            if encontrado == False:
                limpiar_consola()
                intentos = intentos - 1
                print("Datos incorrectos. Intentos restantes:", intentos, "\n")

    if intentos == 0:
        print("Ha superado el número máximo de intentos. El programa se cerrará.")
        input("Presione Enter para continuar... ")
    limpiar_consola()

    return acceso_valido


def registrar(estudiantes, moderadores, estados):
    registrado = False
    decision = ""

    limpiar_consola()
    while not registrado and decision != "N":
        print("\n........Registro........\n")

        email = ingresar_propiedad("email")
        password = ingresar_contrasenia()
        rol = input("Ingrese el rol estudiante(E) o moderador(M). (E/M): ").upper()

        while rol != "E" and rol != "M":
            print("\nNo es un rol válido.")
            rol = input("ingrese E (Estudiante) o M (Moderador): ")

        if rol == "E":
            registrado = registrar_estudiante(email, password, estudiantes, moderadores, estados)

        elif rol == "M":
            registrado = registrar_moderador(email, password, estudiantes, moderadores)

        if not registrado:
            decision = input("\nIntentar registrarse nuevamente. S/N ").upper()
            decision = validar_continuacion(decision) #LISTO

    limpiar_consola()

#endregion

#region Estudiantes

def contar_estudiantes(estudiantes): #LISTO
    ind = 0

    while ind < 8 and estudiantes.email != "":
        ind = ind + 1

    return ind


def ingresar_propiedad(prop):
    if prop == PROPS_ESTUDIANTE[4]:
        valor = input(f"Ingrese {GENERO[1]} o {GENERO[0]}: ").upper()

        while valor != GENERO[0] and valor != GENERO[1]:
            valor = input(f"Debe ingresar {prop}:\n\t").upper()
    elif prop == PROPS_ESTUDIANTE[1]:
        print("\nFecha de nacimiento")
        valor = solicitar_fecha_nacimiento()
    else:
        valor = input(f"Ingrese {prop}:\n\t")
        while valor == "":
            valor = input(f"Debe ingresar {prop}:\n\t")

    return valor


def registrar_estudiante(email, password, estudiantes, moderadores, estados):
    registrado = False
    cant = contar_estudiantes(estudiantes[:])

    if cant == 8:
        print("Por el momento no se pueden registrar nuevos estudiantes.")
    elif not email_existente(email, estudiantes[:], moderadores[:]):
        print("El email ingresado ya está en uso.")
    else:
        estudiantes[cant][0] = email
        estudiantes[cant][1] = password
        estados[cant] = True

        for ind in range(2, 9):
            estudiantes[cant][ind] = ingresar_propiedad(PROPS_ESTUDIANTE[ind - 2])

        registrado = True
        print("\nRegistro exitoso!!!")

    input("Presione Enter para continuar...")

    return registrado


def validar_id_estudiante(est_id, estudiantes): #LISTO
    return 0 <= est_id and est_id <= contar_estudiantes(estudiantes[:]) #LISTO


def contar_estudiantes_activos(): #LISTO
    regEstudiantes.seek(0,0)
    cant = 0

    while (regEstudiantes.tell() < os.path.getsize(rutaEstudiante)):
        estudiantes = pickle.load(regEstudiantes)
        if (estudiantes.email != "" and estudiantes.estado == True):
            cant = cant + 1

    return cant


def contar_estudiantes_activos_no_matcheados(est_id, estudiantes, estados, me_gusta):
    cant = 0
    ind = 0

    while ind < 8 and estudiantes[ind][0] != "":
        if ind != est_id and estados[ind] and not me_gusta[est_id][ind]:
            cant = cant + 1

        ind = ind + 1

    return cant


def obtener_id_estudiante_por_nombre(nombre, estudiante): #LISTO
    ind = 0

    while ind < 8 and estudiante.nombre != nombre:
        ind = ind + 1

    return ind

def obtener_nombre_estudiante_por_id(est_id, estudiantes):
    ind = 0

    while ind < 8 and ind != est_id:
        ind = ind + 1

    return estudiantes[ind][2]


def eliminar_perfil(est_id, estudiante):
    regEstudiantes.seek(0,0)
    pickle.load(regEstudiantes)
    tamEst = regEstudiantes.tell()
    print("\n")
    opc = input("¿Desea eliminar su perfil? (S/N) ").upper()
    opc = validar_continuacion(opc) #LISTO

    if opc == "S":
        estudiante.estado = False
        regEstudiantes.seek(tamEst*est_id, 0)
        formatearEstudiante(estudiante)
        pickle.dump(estudiante, regEstudiantes)
        regEstudiantes.flush()

        print("Perfil borrado con exito.")
        input("Presione Enter para continuar ")


def reportar_candidato(est_id, estudiantes): #LISTO
    decision = ""
    reportado_id = -1

    while decision != "N":
        reportado = input("Ingrese el nombre o el id del candidato: ")

        if not reportado.isdigit():
            reportado_id = obtener_id_estudiante_por_nombre(reportado, estudiantes) #LISTO
        else:
            reportado_id = int(reportado)

        if (est_id == reportado_id or not validar_id_estudiante(reportado_id, estudiantes[:]) or not estudiantes.estado): #LISTO 
            print("El usuario ha reportar no es válido.\n")
        else:
            limpiar_consola()
            opc = input("Seguro que desea continuar con reporte del candidato. S/N ").upper()
            opc = validar_continuacion(opc) #LISTO

            if opc == "S":
                motivo = input("Motivo:\n\t")

                while motivo == "":
                    print("Debe ingresar el motivo del reporte.")
                    motivo = input("Por favor. Ingrese el motivo:\n\t")

                reporte_ind = contar_reportes() #LISTO

                if reporte_ind == 40:
                    print("\nError al generar el reporte.")
                else:
                    reporte = REPORTE()
                    reporte.estado = 1
                    reporte.id_reportado = reportado_id
                    reporte.id_reportante = est_id
                    reporte.razon_reporte = motivo
                    regReportes.seek(2, 0)
                    pickle.dump(reporte)
                    regReportes.flush()

                    print("Reporte generado con éxito.")

                input("Presione Enter para continuar... ")
                decision = input("\nGenerar un nuevo reporte. S/N: ").upper()
                decision = validar_continuacion(decision) #LISTO


def mostrar_datos_estudiante(est_id, estudiantes):
    print("Datos de usuario\n")
    print(estudiantes.id_estudiante)
    print(estudiantes.email)
    print(estudiantes.nombre)
    print(estudiantes.sexo)
    print(estudiantes.estado)
    print(estudiantes.hobbies)
    print(estudiantes.materia_favorita)
    print(estudiantes.deporte_favorito)
    print(estudiantes.materia_fuerte)
    print(estudiantes.materia_debil)
    print(estudiantes.biografia)
    print(estudiantes.pais)
    print(estudiantes.ciudad)
    print(estudiantes.fecha_nacimiento)


def manejador_submenu_gestionar_perfil(est_id, estudiante):
    opc = ""

    while opc != "c":
        limpiar_consola()
        print("........Gestionar Perfil........\n")
        print("a. Editar mis datos personales")
        print("b. Eliminar mi perfil")
        print("c. Volver")

        opc = input("\nSeleccione una opción: ")

        while opc != "a" and opc != "b" and opc != "c":
            print("\nNo es una opción válida.")
            opc = input("Ingrese una opción válida: ")

        if opc == "a":
            editar_datos_estudiante(est_id, estudiante)
        elif opc == "b":
            eliminar_perfil(est_id, estudiante)


def validar_nombre(nombre, estudiantes): #LISTO
    est_id = obtener_id_estudiante_por_nombre(nombre, estudiantes) #LISTO

    while est_id == -1:
        print("No existe el estudiante", nombre)
        nombre = input("Ingrese un nombre de estudiante: ")
        est_id = obtener_id_estudiante_por_nombre(nombre, estudiantes[:]) #LISTO

    return nombre


def ver_perfil_estudiante(est_id, estudiante): #LISTO
    ind = 0
    regEstudiantes.seek(0, 0)

    limpiar_consola()
    while regEstudiantes.tell() < os.path.getsize(rutaEstudiante):
        estudiante = pickle.load(regEstudiantes)
        if ind != est_id:
            edad = calcular_edad(estudiante.fecha_nacimiento)
            formato_espaniol_nacimiento = formatear_fecha_espaniol(estudiante.fecha_nacimiento)

            print("Nombre:", estudiante.nombre)
            print("Fecha de nacimiento:", formato_espaniol_nacimiento)
            print("Edad:", edad)
            print("Biografía:\n\t" + estudiante.biografia)
            print("Hobbies:\n\t", estudiante.hobbies)

            while(regLikes.tell() < os.path.getsize(rutaLikes) and match !=True):
                match = False
                likes = pickle.load(regLikes)
                if(likes.remitente == est_id and likes.destinatario == ind):
                    match = True
            if match == True:
                print("Estado del Match: Tienes match ✔️")
            else:
                print("Estado del Match: No tienes match ❌")

            print("\n")

        ind = ind + 1

def marcar_match(est_id, estudiante):
    decision = "S"
    marcado = False
    if decision == "S":
        nombre_estudiante = input("\nIngrese el nombre del estudiante con el que quiere hacer matcheo: ")

        nombre_estudiante = validar_nombre(nombre_estudiante, estudiante) #LISTO
        match_id = obtener_id_estudiante_por_nombre(nombre_estudiante, estudiante[:]) #LISTO

        while(regLikes.tell() < os.path.getsize(rutaLikes) and marcado == False):
            like = pickle.load(regLikes)
            if like.remitente == est_id and like.destinatario == match_id:
                print("\nYa tiene match con", nombre_estudiante)
                marcado = True
            else:
                like.remitente = est_id
                like.destinatario = match_id
                limpiar_consola()
                ver_perfil_estudiante(est_id, estudiante[:]) #LISTO
                print("Se envío el match a", nombre_estudiante)

        input("Presione Enter para continuar... ")


def manejador_matcheo_estudiantes(est_id, estudiante): #LISTO
    opc = ""

    ver_perfil_estudiante(est_id, estudiante) #LISTO
    decision = input("Le gustaría en un futuro hacer matcheo con algún estudiante. (S/N) ").upper()

    while decision != "S" and decision != "N":
        decision = input("Desea hacer matcheo con algún estudiante S o N: ").upper()

    while opc != "N" and decision != "N":
        ver_perfil_estudiante(est_id, estudiante) #LISTO
        marcar_match(est_id, estudiante) #LISTO

        opc = input("\nRealizar un nuevo match, S/N: ").upper()

        while opc != "S" and opc != "N":
            limpiar_consola()
            opc = input("Realizar un nuevo match, S/N: ").upper()


def manejador_submenu_gestionar_candidatos(est_id, estudiante): #LISTO
    opc = ""

    while opc != "c":
        limpiar_consola()
        print("........Gestionar Candidatos........\n")
        print("a. Ver candidatos")
        print("b. Reportar un candidato")
        print("c. Volver")

        opc = input("\nSeleccione una opción: ")

        while opc != "a" and opc != "b" and opc != "c":
            print("\nNo es una opción válida.")
            opc = input("\nSeleccione una opción: ")

        if opc == "a":
            manejador_matcheo_estudiantes(est_id, estudiante) #LISTO

        if opc == "b":
            reportar_candidato(est_id, estudiante) #LISTO 


def manejador_submenu_matcheos():  #LISTO
    opc = ""

    while opc != "c":
        limpiar_consola()
        print("........Matcheos........\n")
        print("a. Ver matcheos")
        print("b. Eliminar un matcheo")
        print("c. Volver")

        opc = input("\nSeleccione una opción: ")

        while opc != "a" and opc != "b" and opc != "c":
            print("\nNo es una opción válida.")
            opc = input("\nSeleccione una opción: ")

        if opc == "a" or opc == "b":
            en_construccion()


def editar_datos_estudiante(est_id, estudiantes):
    opc = ""
    t = int(os.path.getsize(rutaEstudiante))
    regEstudiantes.seek(0,0)
    pickle.load(regEstudiantes)
    tamEst = regEstudiantes.tell()
    
    while opc != "n":
        limpiar_consola()
        mostrar_datos_estudiante(est_id, estudiantes)

        print("\n\n........Actualizar perfil........\n")
        print("a. Cambiar fecha de nacimiento")
        print("b. Editar biografía")
        print("c. Editar hobbies")
        print("d. Cambiar género")
        print("e. Cambiar ciudad")
        print("f. Cambiar país")
        print("n. Finalizar\n")

        opc = input("Seleccione una opción: ")

        print("\n")
        while (opc != "a" and opc != "b" and opc != "c" and opc != "d" and opc != "e" and opc != "f" and opc != "n"):
            print("No es una opción válida.")
            opc = input("Ingrese una opción válida: ")

        match opc:
            case "a":
                valor = solicitar_fecha_nacimiento()
                estudiantes.fecha_nacimiento = valor
                regEstudiantes.seek(tamEst*est_id, 0)
                formatearEstudiante(estudiantes)
                pickle.dump(estudiantes, regEstudiantes)
                regEstudiantes.flush()
            case "b":
                valor = ingresar_propiedad(PROPS_ESTUDIANTE[2])
                estudiantes.biografia = valor
                regEstudiantes.seek(tamEst*est_id, 0)
                formatearEstudiante(estudiantes)
                pickle.dump(estudiantes, regEstudiantes)
                regEstudiantes.flush()
            case "c":
                valor = ingresar_propiedad(PROPS_ESTUDIANTE[3])
                estudiantes.hobbies = valor
                regEstudiantes.seek(tamEst*est_id, 0)
                formatearEstudiante(estudiantes)
                pickle.dump(estudiantes, regEstudiantes)
                regEstudiantes.flush()

            case "d":
                valor = ingresar_propiedad(PROPS_ESTUDIANTE[4])
                estudiantes.sexo = valor
                regEstudiantes.seek(tamEst*est_id, 0)
                formatearEstudiante(estudiantes)
                pickle.dump(estudiantes, regEstudiantes)
                regEstudiantes.flush()
            case "e":
                valor = ingresar_propiedad(PROPS_ESTUDIANTE[5])
                estudiantes.ciudad = valor
                regEstudiantes.seek(tamEst*est_id, 0)
                formatearEstudiante(estudiantes)
                pickle.dump(estudiantes, regEstudiantes)
                regEstudiantes.flush()
            case "f":
                valor = ingresar_propiedad(PROPS_ESTUDIANTE[6])
                estudiantes.pais = valor
                regEstudiantes.seek(tamEst*est_id, 0)
                formatearEstudiante(estudiantes)
                pickle.dump(estudiantes, regEstudiantes)
                regEstudiantes.flush()


def reportes_estadisticos_estudiante(est_id, estudiantes, estados, me_gusta): #VER MAS ADELANTE
    likes_dados = 0
    likes_recibidos = 0
    matches = 0

    cant_estudiantes = contar_estudiantes_activos()  #LISTO

    for ind in range(cant_estudiantes):
        if est_id != ind and estados[ind]:
            like_dado = me_gusta[est_id][ind]
            like_recibido = me_gusta[ind][est_id]

            if like_dado and like_recibido:
                matches = matches + 1
            elif like_dado and not like_recibido:
                likes_dados = likes_dados + 1
            elif not like_dado and like_recibido:
                likes_recibidos = likes_recibidos + 1

    porcentaje = 0.0

    if likes_dados != 0 or likes_recibidos != 0 or matches != 0:
        porcentaje = matches / (likes_recibidos + likes_dados + matches) * 100

    limpiar_consola()
    print(f"Matcheados sobre el % posible: {porcentaje:.1f}%")
    print("Likes dados y no recibidos:", likes_dados)
    print("Likes recibidos y no respondidos:", likes_recibidos)
    input("Presiona Enter para volver al menú... ")


def desactivar_usuario(estudiantes, estados):
    decision = ""

    while decision != "N":
        limpiar_consola()
        estudiante = input("Ingrese el ID o el nombre del usuario: ")
        est_id = -1

        if not estudiante.isdigit():
            est_id = obtener_id_estudiante_por_nombre(estudiante, estudiantes[:]) #LISTO
        else:
            est_id = int(estudiante)

        if not validar_id_estudiante(est_id, estudiantes[:]) or not estados[est_id]: #LISTO PRIMERO
            print("El usuario no existe.\n")
        elif not estados[est_id]:
            print("El usuario ya está desactivado.\n")
        else:
            limpiar_consola()
            opc = input(
                "Seguro que desea continuar con la desactivación del usuario. S/N "
            ).upper()
            opc = validar_continuacion(opc) #LISTO

            if opc == "S":
                estados[est_id] = False

                print("Perfil borrado con exito.")

        input("Presione Enter para continuar ")

        limpiar_consola()
        decision = input("Desactivar otra cuenta. S/N: ").upper()
        decision = validar_continuacion(decision)#LISTO


def calcular_eleccion_candidatos(valores, cand):
    for ind in range(3):
        valores[ind] = random.randint(0, 100) * cand[ind][1]


def comprobar_nuevo_candidato(est_id, candidatos):
    ind = 0

    while ind < 3 and candidatos[ind][0] != est_id:
        ind = ind + 1

    return ind == 3


def calcular_probabilidad_total_candidatos(cand):
    total = 0

    for ind in range(3):
        total = total + cand[ind][1]

    return total


def mostrar_candidatos(cand, estudiantes):
    for ind in range(3):
        est_id = cand[ind][0]

        print(f"{ind + 1}. {obtener_nombre_estudiante_por_id(est_id, estudiantes[:])}")


def buscar_candidato_mayor_valor(valores):
    mayor = -1
    pos = 0

    for ind in range(3):
        valor = valores[ind]

        if valores[ind] > mayor:
            mayor = valor
            pos = ind

    return pos


def obtener_candidatos(usuario_id, candidatos, estudiantes):
    for candidato_ind in range(3):
        cant_est_totales = contar_estudiantes(estudiantes[:]) #LISTO
        est_id = random.randint(0, cant_est_totales - 1)

        while est_id == usuario_id or not comprobar_nuevo_candidato(est_id, candidatos[:]):
            est_id = random.randint(0, cant_est_totales - 1)

        candidatos[candidato_ind][0] = est_id


def matchear_candidato(usuario_id, valores, candidatos, me_gusta, estudiantes):
    pos_elegido = buscar_candidato_mayor_valor(valores[:])

    nombre_match = obtener_nombre_estudiante_por_id(candidatos[pos_elegido][0], estudiantes[:])
    pos_match = candidatos[pos_elegido][0]
    me_gusta[usuario_id][pos_match] = True

    print("\nTu match es la persona", nombre_match)


def ruleta(usuario_id, estudiantes, estados, me_gusta):
    cant_est_posibles = contar_estudiantes_activos_no_matcheados(usuario_id, estudiantes[:], estados[:], me_gusta[:])

    if cant_est_posibles < 3:
        print("No hay suficientes estudiantes activos para esta función.")
    else:
        continuar = ""

        while continuar != "N" and cant_est_posibles >= 3:
            limpiar_consola()

            candidatos = [[-1] * 2 for n in range(3)]
            obtener_candidatos(usuario_id, candidatos, estudiantes[:])

            print("........RULETA........")
            print("A continuación, se le pedirá ingresar la probabilidad de matcheo con tres estudiantes.")
            print("Los valores ingresados deben ser enteros y su suma igual a 100.\n")

            while calcular_probabilidad_total_candidatos(candidatos[:]) != 100:
                mostrar_candidatos(candidatos[:], estudiantes[:])

                print("\n")
                for probabilidad_ingresada in range(3):
                    valor = input(f"Ingresar la probabilidad del estudiante {probabilidad_ingresada + 1}: ")

                    while not valor.isnumeric():
                        valor = input("Por favor ingrese un valor numérico entero: ")

                    candidatos[probabilidad_ingresada][1] = int(valor)

                probabilidad_total = calcular_probabilidad_total_candidatos(candidatos[:])

                if probabilidad_total != 100:
                    limpiar_consola()
                    print("La probabilidad total debe ser igual a 100 y el introducido es", probabilidad_total, ".")
                    print("Vuelva a introducir los valores.\n")

            valores_eleccion_candidatos = [0] * 3

            calcular_eleccion_candidatos(valores_eleccion_candidatos, candidatos[:])
            matchear_candidato(usuario_id, valores_eleccion_candidatos[:], candidatos[:], me_gusta, estudiantes[:])

            continuar = input("Usar la ruleta nuevamente. S/N ").upper()
            continuar = validar_continuacion(continuar) #LISTO
            cant_est_posibles = contar_estudiantes_activos_no_matcheados(usuario_id, estudiantes[:], estados[:], me_gusta[:])

        if cant_est_posibles < 3 and continuar == "S":
            print("No hay suficientes estudiantes activos para esta función.")
            input("Presione Enter para volver al inicio... ")

#endregion

#region Reportes

def contar_reportes(): #LISTO
    ind = 0

    while regReportes.tell() < os.path.getsize(rutaReportes):
        pickle.load(regReportes)
        ind = ind + 1

    return ind


def mostrar_reporte(reporte_id, reportes,  motivo_reportes, estudiantes):
    nombre_reportante = obtener_nombre_estudiante_por_id(reportes[reporte_id][1], estudiantes[:])
    nombre_reportado = obtener_nombre_estudiante_por_id(reportes[reporte_id][2], estudiantes[:])

    print(f"........Reporte {reporte_id + 1}........\n")
    print("Reportante:", nombre_reportante)
    print("Reportado:", nombre_reportado)
    print(f"Motivo:\n\t{motivo_reportes[reporte_id]}\n\n")
    

def procesar_reporte(reporte_id, reportes, estados):
    print("Procesamiento de reporte\n")
    print("1. Ignorar reporte")
    print("2. Bloquear al reportado")

    opc = input("\n\nSeleccione una opción: ")

    while opc != "1" and opc != "2":
        print("\nNo es una opción válida.")
        opc = input("Ingrese una opción válida: ")

    if opc == "1":
        reportes[reporte_id][0] = 2
    elif opc == "2":
        reportado_id = reportes[reporte_id][2]
        estados[reportado_id] = False

        ind = 0
        while ind < 40 and reportes[ind][0] != -1:
            if reportes[ind][2] == reportado_id:
                reportes[ind][0] = 1

            ind = ind + 1


def ver_reportes(reportes, motivo_reportes, estudiantes, estados):
    ind = 0
    opc = ""

    cant_reportes = contar_reportes() #LIST

    while ind < cant_reportes and opc != "N" and reportes[ind][0] != -1:

        limpiar_consola()
        estudiantes_activos = estados[reportes[ind][1]] and estados[reportes[ind][2]]

        if estudiantes_activos and reportes[ind][0]:
            mostrar_reporte(ind, reportes[:], motivo_reportes[:], estudiantes[:])
            procesar_reporte(ind, reportes, estados)

            opc = input("Continuar revisando reportes. (S/N) ").upper()
            opc = validar_continuacion(opc) #LISTO

        ind = ind + 1

    if ind == cant_reportes:
        print("No quedan más reportes pendientes.")
        input("Presione Enter para continuar... ")

#endregion

#region Moderadores

def contar_moderadores(moderadores):
    ind = 0

    while ind < 4 and moderadores[ind][0] != "":
        ind = ind + 1

    return ind


def registrar_moderador(email, password, estudiantes, moderadores):
    registrado = False
    cant = contar_moderadores(moderadores[:])

    if cant == 4:
        print("Por el momento no se pueden registrar nuevos moderadores.")
    elif not email_existente(email, estudiantes[:], moderadores[:]):
        print("El email ingresado ya está en uso.")
    else:
        moderadores[cant][0] = email
        moderadores[cant][1] = password
        registrado = True
        print("\nRegistro exitoso!!!")

    input("Presione Enter para continuar...")

    return registrado


def manejador_submenu_gestionar_usuarios(estudiantes, estados):
    opc = ""

    while opc != "b":
        limpiar_consola()
        print("........Gestionar Usuarios........\n")
        print("a. Desactivar usuario")
        print("b. Volver")

        opc = input("\nSeleccione una opción: ")

        while opc != "a" and opc != "b":
            print("\nNo es una opción válida.")
            opc = input("Ingrese una opción válida: ")

        if opc == "a":
            desactivar_usuario(estudiantes[:], estados)


def manejador_submenu_gestionar_reportes(estudiantes, reportes, motivo_reportes, estados):
    opc = ""

    while opc != "b":
        limpiar_consola()
        print("........Gestionar Reportes........\n")
        print("a. Ver reportes")
        print("b. Volver")

        opc = input("\nSeleccione una opción: ")

        while opc != "a" and opc != "b":
            print("\nNo es una opción válida.")
            opc = input("Ingrese una opción válida: ")

        if opc == "a":
            ver_reportes(reportes, motivo_reportes, estudiantes, estados)

#endregion

#region Mostrar

def mostrar_menu_principal_estudiante():
    limpiar_consola()

    print("\n........Home........")
    print("1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadísticos")
    print("5. Ruleta")
    print("6. Hueco edades estudiantes")
    print("7. Matcheos combinandos")
    print("0. Salir")

    opcion = input("\nSeleccione una opción: ")

    while (
        opcion != "1"
        and opcion != "2"
        and opcion != "3"
        and opcion != "4"
        and opcion != "5"
        and opcion != "6"
        and opcion != "7"
        and opcion != "0"
    ):
        print("La opción introducida no es válida.")
        opcion = input("Por favor, introduzca una opción válida: ")

    return opcion


def mostrar_menu_principal_moderadores():
    limpiar_consola()

    print("\n........Home........")
    print("1. Gestionar Usuarios")
    print("2. Gestionar Reportes")
    print("3. Reportes Estadísticos")
    print("0. Salir")

    opc = input("\nSeleccione una opción: ")

    while opc != "1" and opc != "2" and opc != "3" and opc != "0":
        print("\nLa opción introducida no es válida.")
        opc = input("Por favor, introduzca una opción válida: ")

    return opc


def mostrar_menu_usuario(usuario_id, rol):
    if rol == 0:
        gestionador_menu_principal_estudiante(usuario_id)
    elif rol == 1:
        manejador_menu_principal_moderador(usuario_id)


def mostrar_menu_principal():
    limpiar_consola()

    print("\n........Bienvenido........\n")
    print("1. Conectarse")
    print("2. Registrarse")
    print("0. Salir")

    opcion = input("\nSeleccione una opción: ")

    while opcion != "1" and opcion != "2" and opcion != "0":
        print("La opción introducida no es válida.")
        opcion = input("Por favor, introduzca una opción válida: ")

    return opcion

#endregion

### Gestionar ###


def gestionador_menu_principal_estudiante(est_id):
    opc = ""
    regEstudiantes.seek(0,0)
    validado = False
    while(regEstudiantes.tell() < os.path.getsize(rutaEstudiante) and validado == False):
        estudiante = pickle.load(regEstudiantes)
        if(est_id == estudiante.id_estudiante  and estudiante.estado == True):
                validado = True

    while opc != "0":
        opc = mostrar_menu_principal_estudiante()

        match opc:
            case "1":
                manejador_submenu_gestionar_perfil(est_id, estudiante) #LISTO

            case "2":
                manejador_submenu_gestionar_candidatos(est_id, estudiante) #LISTO

            case "3":
                manejador_submenu_matcheos() #LISTO

            case "4":
                reportes_estadisticos_estudiante(est_id, estudiante) #VER MAS ADELANTE 

            case "5":
                ruleta(est_id, estudiante)

            case "6":
                huecos_edades()

            case "7":
                matcheos_combinados(estudiante)

            case "0":
                limpiar_consola()


def manejador_menu_principal_moderador(usuarioId):
    opc = "1"

    regModeradores.seek(0,0)
    validado = False
    while(regModeradores.tell() < os.path.getsize(rutaModeradores) and validado == False):
        moderador = pickle.load(regModeradores)
        if(usuarioId == moderador.id_moderador  and moderador.estado == True):
                validado = True

    while opc != "0":
        opc = mostrar_menu_principal_moderadores()

        match opc:
            case "1":
                manejador_submenu_gestionar_usuarios(estudiantes, estados)

            case "2":
                manejador_submenu_gestionar_reportes(estudiantes, reportes, motivo_reportes, estados)

            case "3":
                en_construccion()

            case "0":
                limpiar_consola()
                print("¡Hasta luego!")


def main():  

    AbrirArchivo(rutaCarpetaDatos, rutaEstudiante, rutaModeradores, rutaAdministradores, rutaLikes, rutaReportes)

    opc = ""
    usuario = [0] * 2

    while opc != "0" and usuario[0] != -1:
        opc = mostrar_menu_principal()
        match opc:
            case "0":
                limpiar_consola()
                print("¡Hasta luego!")
            case "1":
                usuario = log_in()
                if usuario[0] != -1:
                    mostrar_menu_usuario(usuario[0], usuario[1])
            case "2":
                registrar()


main()
