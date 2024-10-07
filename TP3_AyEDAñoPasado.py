from calendar import c
import datetime
from datetime import date
from datetime import datetime
from enum import Flag
from importlib import import_module
from json import load
from operator import truediv
import os
import os.path
import io
import pickle
import re
import pwinput
from time import process_time_ns
from tkinter.tix import InputOnly
from turtle import pos
from typing import Self
import sys
from xml import dom

def definicionVariables(): #ACA ESTAN TODAS LAS VARIABLES DEFINIDAD
    print()
    #CLASES
        # Las clases no estan definidas aca ya que se pueden apreciar en los 5 metodos de abajo.

    #ARREGLOS
        # diasSemanas
        # A
        # tamanios
        # rubrosStr
        # rubrosInt

    #STRING (las variables tipo fecha las tabajamos como strings para una mayor comunidad)
        # fecha1
        # fecha2
        # diaFecha1
        # diaFecha2
        # mesFecha1
        # mesFecha2
        # anioFecha1
        # anioFecha2
        # mail
        # contrasena
        # usuario
        # codigoProm
        # fechaDesdePromo
        # fechaHastaPromo
        # fecha
        # mes
        # dia
        # anio
        # fechaHoy
        # opc
        # fechaDesde
        # fechaHasta
        # domin
        # lun
        # mart
        # mier
        # jue
        # vier
        # sab
        # opcMail
        # contra
        # conf
        # nombreLocal
        # ubicaionLocal
        # rubroLocal
        # estadoLocal
        # usuarioEnElPrograma
        # contranaEnElPrograma
        # tipoUsuarioEnElPrograma

    #INT
        # t
        # cod
        # pos
        # codUsuario
        # tamReg
        # tamArch
        # cantReg
        # cont
        # aux
        # codigoProm
        # tltp
        # usoProm
        # auxProm
        # auxLocales
        # cantRegLog
        # posModLog
        # inf
        # sup
        # med
        # j
        # k
        # m
        # codigoDelUsuario
        # codaeliminar
        # posDelUsuarioEnElPrograma
        # codigoUsuarioEnElPrograma
        # primeraVez

    #BOOLEANO
        # ret
        # hay
        # valinp
        # habilitada
        # compFecha1
        # compFecha2
        # salir
        # compFecha
        # opcFecha
        # hayAbierto
        # rut
        # hayLocales
        # checInput
        # vacio
        # check
        # hayDueño
        # opc
        # entre
        # confUsu
        # confCont

    #REGISTRO
        # aux
        # auxi
        # auxj
        # varPromociones
        # varUsuario
        # varLocales
        # varUsoPromociones
        # varNovedades

class USUARIO:
    def _init_(self):
        self.codUsuario = 0
        self.nombreUsuario = " "
        self.claveUsuario = " "
        self.tipoUsuario = ""

class LOCALES:
    def _init_(self):
        self.codLocal = 0
        self.nombreLocal = " "
        self.ubicacionLocal = " "
        self.rubroLocal = " "
        self.codUsuario = 0
        self.estado = " "

class PROMOCIONES:
    def _init_(self):
        self.codPromo = 0
        self.textoPromo = " "
        self.fechaDesdePromo = ""
        self.fechaHastaPromo = ""
        self.diaSemana = [0]*7
        self.estado = " "
        self.codLocal = 0

class USO_PROMOCIONES:
    def _init_(self):
        self.codCliente = 0
        self.codPromo = 0
        self.fechaUsoPromo = ""

class NOVEDADES:
    def _init_(self):
        self.codNovedad = 0
        self.textoNovedad = " "
        self.fechaDesdeNovedad = ""
        self.fechaHastaNovedad = ""
        self.tipoUsuario = " "
        self.estado = " "

def validarInput(input): #LISTO (Retorna TRUE si es INT)
    try:
        float(input)
        return True
    except ValueError:
        return False

def validarFecha(fecha): #LISTO (Retorna TRUE si sirve la fecha)
    try:
        datetime.strptime(fecha, '%d/%m/%y')
        return True
    except ValueError:
        return False

def compararFechas(fecha1, fecha2): #TRUE SI FECHA1 >= FECHA2
    fecha1 = str(fecha1)
    fecha2 = str(fecha2)
    diaFecha1, mesFecha1, anioFecha1 = fecha1.split('/')
    diaFecha2, mesFecha2, anioFecha2 = fecha2.split('/')
    anioFecha1 = anioFecha1[0:2]
    anioFecha2 = anioFecha2[0:2]
    ret = True
    if (anioFecha1 > anioFecha2):
        ret = True
    elif (anioFecha1 < anioFecha2):
        ret = False
    elif (anioFecha1 == anioFecha2):
        if (mesFecha1 > mesFecha2):
            ret = True
        elif (mesFecha1 < mesFecha2):
            ret = False
        elif (mesFecha1 == mesFecha2):
            if (diaFecha1 > diaFecha2):
                ret = True
            elif (diaFecha1 < diaFecha2):
                ret = False
            elif (diaFecha1 == diaFecha2):
                rut = True
    return ret

def formatearUso_Promociones(varUsoPromociones): #LISTO
    varUsoPromociones.codCliente = int(varUsoPromociones.codCliente)
    varUsoPromociones.codPromo = int(varUsoPromociones.codPromo)
    varUsoPromociones.fechaUsoPromo = str(varUsoPromociones.fechaUsoPromo)
    varUsoPromociones.fechaUsoPromo = varUsoPromociones.fechaUsoPromo.ljust(10,' ')

def formatearNovedades(varNovedades): #LISTO
    varNovedades.codNovedad = int(varNovedades.codNovedad)
    varNovedades.textoNovedad = str(varNovedades.textoNovedad)
    varNovedades.textoNovedad = varNovedades.textoNovedad.ljust(200, ' ')
    varNovedades.fechaDesdeNovedad = str(varNovedades.fechaDesdeNovedad)
    varNovedades.fechaDesdeNovedad = varNovedades.fechaDesdeNovedad.ljust(10, ' ') 
    varNovedades.fechaHastaNovedad = str(varNovedades.fechaHastaNovedad)
    varNovedades.fechaHastaNovedad = varNovedades.fechaHastaNovedad.ljust(10, ' ')
    varNovedades.tipoUsuario = str(varNovedades.tipoUsuario)
    varNovedades.tipoUsuario = varNovedades.tipoUsuario.ljust(20, ' ')
    varNovedades.estado = str(varNovedades.estado)
    varNovedades.estado = varNovedades.estado.ljust(1, ' ')

def formatearUsuario(varUsuario): #LISTO
    varUsuario.codUsuario = int(varUsuario.codUsuario)
    varUsuario.nombreUsuario = str(varUsuario.nombreUsuario)
    varUsuario.nombreUsuario = varUsuario.nombreUsuario.ljust(100, ' ')
    varUsuario.claveUsuario = str(varUsuario.claveUsuario)
    varUsuario.claveUsuario = varUsuario.claveUsuario.ljust(8, ' ')
    varUsuario.tipoUsuario = str(varUsuario.tipoUsuario)
    varUsuario.tipoUsuario = varUsuario.tipoUsuario.ljust(20, ' ')

def formatearLocales(varLocales): #LISTO
    varLocales.codLocal = int(varLocales.codLocal)
    varLocales.nombreLocal = str(varLocales.nombreLocal)
    varLocales.nombreLocal = varLocales.nombreLocal.ljust(50, ' ')
    varLocales.ubicacionLocal = str(varLocales.ubicacionLocal)
    varLocales.ubicacionLocal = varLocales.ubicacionLocal.ljust(50, ' ')
    varLocales.rubroLocal = str(varLocales.rubroLocal)
    varLocales.rubroLocal = varLocales.rubroLocal.ljust(50, ' ')
    varLocales.codUsuario = int(varLocales.codUsuario)
    varLocales.estado = str(varLocales.estado)
    varLocales.estado = varLocales.estado.ljust(1, ' ')

def formatearPromociones(varPromociones): #LISTO
    varPromociones.codPromo = int(varPromociones.codPromo) 
    varPromociones.textoPromo = str(varPromociones.textoPromo)
    varPromociones.textoPromo = varPromociones.textoPromo.ljust(200, ' ')
    varPromociones.fechaDesdePromo = str(varPromociones.fechaDesdePromo)
    varPromociones.fechaDesdePromo = varPromociones.fechaDesdePromo.ljust(10, ' ')
    varPromociones.fechaHastaPromo = str(varPromociones.fechaHastaPromo)
    varPromociones.fechaHastaPromo = varPromociones.fechaHastaPromo.ljust(10, ' ')
    varPromociones.estado = str(varPromociones.estado)
    varPromociones.estado = varPromociones.estado.ljust(10, ' ')
    varPromociones.codLocal = int(varPromociones.codLocal)

def buscarUltimoCodUsuario(varUsuario): #LISTO
    t = os.path.getsize(rutaUsuario)
    cod = 0
    regUsuario.seek(0, 0) 
    if t > 0:        
        while (regUsuario.tell() < t):
            varUsuario = pickle.load(regUsuario)
            cod = cod + 1
        return cod
    else:
        return cod

def buscarMailExcistente(mail, varUsuario,): #LISTO
    mail = str(mail).ljust(100, ' ')
    t = os.path.getsize(rutaUsuario)
    regUsuario.seek(0,0)
    if (t > 0):
        varUsuario = pickle.load(regUsuario)
        while((regUsuario.tell() < t) and (str(mail) != varUsuario.nombreUsuario)): #VER
            varUsuario = pickle.load(regUsuario)
        if (varUsuario.nombreUsuario == mail):
            return True
        else:
            return False
    else:
        return False 
    
def buscarcontrasenaExcistente(contrasena, varUsuario): #LISTO
    contrasena = str(contrasena).ljust(8, ' ')
    t = os.path.getsize(rutaUsuario)
    regUsuario.seek(0,0)
    if (t > 0):
        varUsuario = pickle.load(regUsuario)
        while((regUsuario.tell() < t) and (str(contrasena) != varUsuario.claveUsuario)): #VER
            varUsuario = pickle.load(regUsuario)
        if (varUsuario.claveUsuario == contrasena):
            return True
        else:
            return False
    else:
        return False 

def buscarPosUsuarioEnElPrograma(usuario): #LISTO
    usuario = str(usuario).ljust(100, ' ')
    t = os.path.getsize(rutaUsuario)
    pos = 0
    regUsuario.seek(0, 0)  
    if t>0:
        varUsuario = pickle.load(regUsuario)
        #regUsuario.seek(0, 0)
        while (regUsuario.tell() < t) and (str(usuario) != str(varUsuario.nombreUsuario)):
            varUsuario = pickle.load(regUsuario)
        if str(varUsuario.nombreUsuario) == str(usuario):
            pos = regUsuario.tell()      
            return pos
        else:
            return -1
    else:
        return -1

def buscarTipoUsuarioDelPrograma(usuario): #LISTO
    usuario = str(usuario).ljust(100, ' ')
    t = os.path.getsize(rutaUsuario)
    regUsuario.seek(0, 0)  
    if t > 0:
        varUsuario = pickle.load(regUsuario)
        while (str(usuario) != str(varUsuario.nombreUsuario)):
            varUsuario = pickle.load(regUsuario)
        if (str(varUsuario.nombreUsuario) == str(usuario)): 
            tipoUsuario = varUsuario.tipoUsuario
            return tipoUsuario
        else:
            return ""
    else:
        return ""

def buscarCodigoUsuarioEnElPrograma(usuario): #LISTO
    usuario = str(usuario).ljust(100, ' ')
    t = os.path.getsize(rutaUsuario)
    regUsuario.seek(0, 0)  
    if t > 0:
        varUsuario = pickle.load(regUsuario)
        while (str(usuario) != str(varUsuario.nombreUsuario)):
            varUsuario = pickle.load(regUsuario)
        if (str(varUsuario.nombreUsuario) == str(usuario)): 
            codUsuario = varUsuario.codUsuario     
            return codUsuario
        else:
            return ""
    else:
        return ""

def menuAdministrador(): #LISTO
    print("|-------------------------------------------|")
    print("|                                           |")
    print("| 1- Gestión de locales                     |")
    print("| 2- Crear cuenta de dueño de locales       |")
    print("| 3- Aprobar/denegar solicitud de descuento |")
    print("| 4- Gestión de novedades                   |")
    print("| 5- Reporte de utilizacion de descuentos   |")
    print("| 0- Salir                                  |")
    print("|-------------------------------------------|")

def menuDuenioLocal(): #LISTO
    print("|---------------------------------|")
    print("|                                 |")
    print("| 1- Crear descuento              |")
    print("| 2- Reporte de uso de descuentos |")
    print("| 3- Ver novedades                |")
    print("| 0- Salir                        |")
    print("|---------------------------------|")
    
def menuCliente(): #LISTO
    print("|--------------------------------|")
    print("|                                |")
    print("| 1- Buscar descuento en locales |")
    print("| 2- Solicitar descuento         |")
    print("| 3- Ver novedades               |")
    print("| 0- Salir                       |")
    print("|--------------------------------|")

def subMenuGestionDeLocales(): #LISTO
    print("|----------------------|")
    print("|                      |")
    print("| A- Crear locales     |")
    print("| B- Modificar locales |")
    print("| C- Eliminar locales  |")
    print("| D- Mapa locales      |")
    print("| E- Volver            |")
    print("|----------------------|")

def ordenarXNombre(): #LISTO
    t = os.path.getsize(rutaLocales)
    if t != 0:
        regLocales.seek (0, 0)
        aux = pickle.load(regLocales)
        tamReg = regLocales.tell() 
        tamArch = os.path.getsize(rutaLocales)
        cantReg = int(tamArch / tamReg) 
        for i in range(0, cantReg-1):
            for j in range (i+1, cantReg):
                regLocales.seek (i*tamReg, 0)
                auxi = pickle.load(regLocales)
                regLocales.seek (j*tamReg, 0)
                auxj = pickle.load(regLocales)
                if (auxi.nombreLocal < auxj.nombreLocal):
                    regLocales.seek (i*tamReg, 0)
                    pickle.dump(auxj, regLocales)
                    regLocales.seek (j*tamReg, 0)
                    pickle.dump(auxi, regLocales)
                    regLocales.flush()

def mostrarLocalesXNombres(): #LISTO
    os.system("cls")
    print("                       Listado de locales ya creados")
    print("--------------------------------------------------------------------------------")
    t = os.path.getsize(rutaLocales)
    if t==0:
        print ("No hay locales creados")
    else:
        cont = 0
        ordenarXNombre()
        print("Codigo local      Nombre local               Ubicación local               Rubro local            Codigo Usuario      Estado local")
        print('----------------------------------------------------------------------------------------------------------------------------------')
        regLocales.seek(0, 0)
        varLocales = pickle.load(regLocales)
        tamReg = regLocales.tell()
        cantReg = int(os.path.getsize(rutaLocales) / tamReg)
        while cont < cantReg:
            cont = cont + 1
            print(varLocales.codLocal, "               ", varLocales.nombreLocal, "                     ", varLocales.ubicacionLocal, "                 ", varLocales.rubroLocal, "                 ", varLocales.codUsuario, "                 ", varLocales.estado)
            if cont < cantReg:
                varLocales = pickle.load(regLocales)
    input()

def mostrarPromociones(): #LISTO
    os.system("cls")
    print("              Listado de promociones que aun estan pendientes")
    print("--------------------------------------------------------------------------------")
    t = os.path.getsize(rutaPromociones)
    if t == 0:
        os.system("cls")
        print ("No hay promociones")
        hay = False
    else:
        aux = 0
        print("Codigo promoción --- Codigo local de la promo --- Fecha inicial de la promo --- Fecha final de la promo --- Observaciones promo")
        print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        regPromociones.seek(0, 0)
        varPromociones = PROMOCIONES()
        while regPromociones.tell()<t:
            varPromociones = pickle.load(regPromociones)
            if (varPromociones.estado == "aprobada  "):
                print(varPromociones.codPromo, "                    ", varPromociones.codLocal, "                           ", varPromociones.fechaDesdePromo, "                    ", varPromociones.fechaHastaPromo, "                  ", varPromociones.textoPromo)
                aux = aux + 1
                hay = True
            if (regPromociones.tell() < t):
                varPromociones = pickle.load(regPromociones)
        if aux == 0:
            os.system("cls")
            print("No hay promociones")
            hay = False
    input()
    return hay

def validarCodLocal(codLocal): #LISTO
    t = os.path.getsize(rutaLocales)
    regLocales.seek(0,0)
    if (t > 0):
        varLocales = pickle.load(regLocales)
        while((regLocales.tell() < t) and (int(codLocal) != varLocales.codLocal)):
            varLocales = pickle.load(regLocales)
        if (int(codLocal) == varLocales.codLocal):
            return True
        else:
            return False
    else:
        return False 

def validarCodProm(codProm): #LISTO
    t = os.path.getsize(rutaPromociones)
    regPromociones.seek(0,0)
    if (t > 0):
        varPromociones = pickle.load(regPromociones)
        while((regPromociones.tell() < t) and (int(codProm) != varPromociones.codPromo)):
            varPromociones = pickle.load(regPromociones)
        if (int(codProm) == varPromociones.codPromo):
            return True
        else:
            return False
    else:
        return False 
    
def posPromocion(codigoProm): #LISTO
    t = os.path.getsize(rutaPromociones)
    pos=0
    regPromociones.seek(0, 0)  
    if t>0:
        varPromociones = pickle.load(regPromociones)
        while (regPromociones.tell()<t) and (int(codigoProm) != int(varPromociones.codPromo)):
            pos = regPromociones.tell()
            varPromociones = pickle.load(regPromociones)
        if int(varPromociones.codPromo) == int(codigoProm):
            return pos

def solicitarDescuento(): #LISTO
    os.system("cls")
    hay = mostrarPromociones()
    if hay == True:
        codigoProm = input("Por favor ingrese el codigo de promocion de la cual quiere gozar; para salir presione '*'")
        if codigoProm != "*":
            valInp = validarInput(codigoProm)
            while valInp == False and codigoProm != "*":
                os.system("cls")
                print("Por favor ingrese un codigo numerico")
                codigoProm = input("Por favor ingrese el codigo de promocion de la cual quiere gozar; para salir presione '*'")
                if codigoProm != "*":
                    valInp = validarInput(codigoProm)
            if codigoProm != "*":
                codProm = validarCodProm(codigoProm)
                habilitada = False
                while (codProm == False and codigoProm != "*" and habilitada != True):
                    habilitada = False
                    codProm = False
                    if codProm == False:
                        os.system("cls")
                        print("ingrese un codigo valido por favor")
                    elif codProm == True:
                        posProm = posPromocion()
                        regPromociones.seek(0,0)
                        tamReg = regPromociones.tell()
                        regPromociones.seek(pos * tamReg,0)
                        varPromociones = pickle,load(regPromociones)
                        diaSem = datetime.today().weekday()
                        diasSemana = varPromociones.diaSemana
                        if (diasSemana[diaSem] == 1):
                            habilitada = True
                        else:
                            os.system("cls")
                            print("La promocion no esta habilitada el dia de hoy")
                    if (codProm == False and habilitada == False):
                        mostrarPromociones()
                        codigoProm = input("Por favor ingrese el codigo de promocion de la cual quiere gozar; para salir presione '*'")
                        if codigoProm != "*":
                            codProm = validarCodProm(codigoProm)
                            while valInp == False and codigoProm != "*":
                                os.system("cls")
                                print("Por favor ingrese un codigo numerico")
                                codigoProm = input("Por favor ingrese el codigo de promocion de la cual quiere gozar; para salir presione '*'")
                                if codigoProm != "*":
                                    valInp = validarInput(codigoProm)

                varUsoPromociones.codCliente = codigoUsuarioEnElPrograma
                varUsoPromociones.codPromo = codigoProm
                fecha = datetime.now().strftime("%x")
                mes, dia, anio = fecha.split("/")
                fecha = str(dia + "/" + mes + "/" + anio)
                fecha = datetime.strptime(fecha, "%d/%m/%y")
                varUsoPromociones.fechaUsoPromo = fecha
                formatearUso_Promociones(varUsoPromociones)
                pickle.dump(varUsoPromociones, regUsoPromociones)
                regUsoPromociones.flush()
                os.system("cls")
                input("Datos guardados exitosamente")
        else:
            os.system("cls")

def mostrarPromocionesDeEseDia(diaSemana, fecha): #LISTO
    os.system("cls")
    print("    Promociones del dia de hoy")
    print("--------------------------------------")
    tl = os.path.getsize(rutaLocales)
    if tl == 0:
        os.system("cls")
        print("No hay locales creados, por lo tanto tampoco hay promociones creadas")
    else:
        print()
        print()
        regLocales.seek(0,0)
        while (tl > regLocales.tell()):
            varLocales = pickle.load(regLocales)
            print()
            print()
            print("Local ", varLocales.codLocal, ": ", varLocales.nombreLocal)
            tp = os.path.getsize(rutaPromociones)
            if tp == 0:
                print("---No hay promociones el dia de hoy para este local---")
            else:
                print("Codigo promoción --- Observaciones promo --- Fecha desde --- Fecha hasta")
                print('------------------------------------------------------------------------')
                regPromociones.seek(0,0)
                contProm = 0
                while (tp > regPromociones.tell()):
                    varPromociones = pickle.load(regPromociones)
                    diasSemana = varPromociones.diaSemana
                    fechaDesdePromo = varPromociones.fechaDesdePromo
                    fechaHastaPromo = varPromociones.fechaHastaPromo
                    compFecha1 = compararFechas(fechaDesdePromo, fecha)
                    compFecha2 = compararFechas(fechaHastaPromo, fecha)
                    if (varPromociones.estado == "aprobada  " and compFecha1 == False and compFecha2 == True and diasSemana[diaSemana] == 1):
                        contProm = contProm + 1
                        print(varPromociones.codPromo, " ", varPromociones.textoPromo, " ", varPromociones.fechaDesdePromo, " ", varPromociones.fechaHastaPromo)
                    if (tp > regPromociones.tell()):
                        varPromociones = pickle.load(regPromociones)
                if (contProm == 0):
                    print("---No hay promociones el dia de hoy para este local---")
            if (tl > regLocales.tell()):
                varLocales = pickle.load(regLocales)
    input()

def buscarDescuentoEnLocales(): #LISTO
    os.system("cls")
    salir = False
    compFecha = True
    fecha = str("99/99/99")
    fechaHoy = datetime.now().strftime("%x")
    mes, dia, anio = fechaHoy.split("/")
    fechaHoy = str(dia + "/" + mes + "/" + anio)
    compFecha = compararFechas(fecha,fechaHoy)
    while compFecha == True and salir == False:
        fecha = input("Por favor ingrese una fecha en formato dd/mm/aaaa, para salir ingrese '*'")
        if fecha != "*":
            opcFecha = validarFecha(fecha)
            if opcFecha == True:
                compFecha = compararFechas(fecha,fechaHoy)
            while (opcFecha == False and fecha == "*" and compFecha == False):
                os.system("cls")
                print("Por favor ingrese la fecha de forma correcta o que la fecha ingresada sea a futuro o en el presente")
                fecha = input("Por favor ingrese una fecha en formato dd/mm/aa, para salir ingrese '*'")
                if fecha != '*':
                    opcFecha = validarFecha(fecha)
                    if opcFecha == True:
                        compFecha = compararFechas(fecha, fechaHoy)
                else:
                    salir = True
            if fecha != "*":
                fecha = datetime.strptime(fecha, "%d/%m/%y")
                diaSemana = fecha.weekday()
                fecha = str(fecha)
                fecha = fecha[0:10]
                anioo, mess, diaa = fecha.split("-")
                anioo = anioo[2:]
                fecha = diaa + "/" + mess + "/" + anioo
                mostrarPromocionesDeEseDia(diaSemana, fecha)
                os.system("cls")
                fecha = input("Por favor ingrese una fecha en formato dd/mm/aaaa, para salir ingrese '*'")
                if fecha != '*':
                    opcFecha = validarFecha(fecha)
                    if opcFecha == True:
                        compFecha = compararFechas(fecha, fechaHoy)
                    while (opcFecha == False and fecha == "*" and compFecha == False):
                        os.system("cls")
                        print("Por favor ingrese la fecha de forma correcta o que la fecha ingresada sea a futuro o en el presente")
                        fecha = input("Por favor ingrese una fecha en formato dd/mm/aaaa, para salir ingrese '*'")
                        if fecha != '*':
                            opcFecha = validarFecha(fecha)
                            if opcFecha == True:
                                compFecha = compararFechas(fecha, fechaHoy)
                        else:
                            salir = True
                else:
                    salir = True
        else:
            salir = True
        
def logeadoCliente(): #LISTO
    os.system("cls")
    menuCliente()
    opc = input("Selecciones una opción: ")
    while (opc != "0" and opc != "1" and opc != "2" and opc != "3"):
        os.system("cls")
        print("Por favor ingrese un valor valido")
        print()
        menuCliente()
        opc = input("Selecciones una opción: ")
    while (opc != "0"):
        match opc:
            case "1":
                buscarDescuentoEnLocales()
            case "2":
                solicitarDescuento()
            case "3":
                input("En construcción...")               

        os.system("cls")
        menuCliente()
        opc = input("Selecciones una opción: ")
        while (opc != "0" and opc != "1" and opc != "2" and opc != "3"):
            os.system("cls")
            print("Por favor ingrese un valor valido")
            print()
            menuCliente()
            opc = input("Selecciones una opción: ")

def contarUsoProm(codPromo): #LISTO
    usoProm = 0
    tamArch = os.path.getsize(rutaUsoPromociones)
    if (tamArch > 0):
        regUsoPromociones.seek(0, 0)
        aux = pickle.load(regUsoPromociones)
        tamReg = regUsoPromociones.tell() 
        cantReg = int(tamArch / tamReg)
        regUsoPromociones.seek(0,0)
        for i in range(0, cantReg):
            varUsoPromociones = pickle.load(regUsoPromociones)
            if (codPromo == varUsoPromociones.codPromo):
                usoProm = usoProm + 1
            #aux = pickle.load(regUsoPromociones)
    return usoProm

def mostarUtilizacionDePromociones(fechaDesde, fechaHasta): #LISTO
    os.system("cls")
    print("            uso de las promociones vigentes en ese lapso de tiempo")
    print("--------------------------------------------------------------------------------")
    tl = os.path.getsize(rutaLocales)
    if tl == 0:
        os.system("cls")
        print("No hay locales creados, por lo tanto tampoco hay promociones creadas")
    else:
        print("Informe de uso de promociones")
        print()
        print("Fecha desde: ", fechaDesde, " ----- Fecha hasta: ", fechaHasta)
        regLocales.seek(0,0)
        while (tl > regLocales.tell()):
            varLocales = pickle.load(regLocales)
            print()
            print()
            print("Local ", varLocales.codLocal, ": ", varLocales.nombreLocal)
            tp = os.path.getsize(rutaPromociones)
            if tp == 0:
                print("---No hay promociones para este local---")
            else:
                print("Codigo promoción --- Observaciones promo --- Fecha desde --- Fecha hasta --- Cant de usos")
                print('-----------------------------------------------------------------------------------------')
                regPromociones.seek(0,0)
                while (tp > regPromociones.tell()):
                    varPromociones = pickle.load(regPromociones)
                    valFecha1 = False
                    valFecha2 = False
                    fechaDesdePromo = varPromociones.fechaDesdePromo
                    valFecha1 = compararFechas(fechaDesde, fechaDesdePromo)
                    fechaHastaPromo = varPromociones.fechaHastaPromo
                    valFecha2 = compararFechas(fechaHastaPromo, fechaHasta)
                    if (varPromociones.estado == "aprobada  " and valFecha1 == True and valFecha2 == True):
                        usoProm = 0
                        codPromo = varPromociones.codPromo
                        usoProm = contarUsoProm(codPromo)
                        print(varPromociones.codPromo, " ", varPromociones.textoPromo, " ", varPromociones.fechaDesdePromo, " ", varPromociones.fechaHastaPromo, " ", usoProm )
                    if tp > regPromociones.tell():
                        varPromociones = pickle.load(regPromociones)
            if tl > regLocales.tell():
                varLocales = pickle.load(regLocales)
    input()

def reporteDeUsoDeDescuentos(): #LISTO
    os.system("cls")
    print("Por favor ingrese la fecha de inicio en la que desea ver los usos de sus promociones")
    fechaDesde = input("Por favor ingrese la fecha en el siguiente formato 'dd/mm/aa'; para salir presione '*'")
    while (fechaDesde != "*"):
        fechaValida = validarFecha(fechaDesde)
        while (fechaValida == False and fechaDesde != "*"):
            os.system("cls")
            print("Por favor ingrese una fecha valida")
            print()
            print("Por favor ingrese la fecha de inicio en la que desea ver los usos de sus promociones")
            fechaDesde = input("Por favor ingrese la fecha en el siguiente formato 'dd/mm/aa'; para salir presione '*'")
            if (fechaDesde != "*"):
                fechaValida = validarFecha(fechaDesde)
        os.system("cls")
        if (fechaDesde != "*"):
            print("Por favor ingrese la fecha de fin en la que que desea ver los usos de sus promociones")
            fechaHasta = input("Por favor ingrese la fecha en el siguiente formato 'dd/mm/aa'; para salir presione '*'")
            fechaValida = validarFecha(fechaHasta)
            while (fechaHasta != "*" and fechaValida == False):
                os.system("cls")
                print("Por favor ingrese una fecha valida")
                print()
                print("Por favor ingrese la fecha de fin en la que que desea ver los usos de sus promociones")
                fechaHasta = input("Por favor ingrese la fecha en el siguiente formato 'dd/mm/aa'; para salir presione '*'")
                if (fechaHasta != "*"):
                    fechaHasta = validarFecha(fechaHasta)
            os.system("cls")
            if (fechaHasta != "*"):
                mostarUtilizacionDePromociones(fechaDesde, fechaHasta)
        else:
            fechaHasta = "*" 
        os.system("cls")
        if fechaHasta != "*" or fechaDesde != "*":
            print("Si desea seguir viendo otras promociones pero en distinta fecha, por favor ingrese la fecha de inicio en la que desea ver los usos de sus promociones")
            fechaDesde = input("Por favor ingrese la fecha en el siguiente formato 'dd/mm/aa'; para salir presione '*'")

def listarDescuentosOPromociones(): #LISTO
    tamProm = os.path.getsize(rutaPromociones)
    hayAbierto = False
    if tamProm > 0:
        os.system("cls")
        print("       Listado de promociones vigentes")
        print("---------------------------------------------")
        regLocales.seek(0,0)
        varLocales = pickle.load(regLocales)
        tamRegLoc = regLocales.tell() 
        tamLoc = os.path.getsize(rutaLocales)
        cantRegLoc = int(tamLoc / tamRegLoc)
        regLocales.seek(0,0)
        regPromociones.seek(0,0)
        varPromociones = pickle.load(regPromociones)
        tamRegProm = regPromociones.tell() 
        cantRegProm = int(tamProm / tamRegProm)
        regPromociones.seek(0,0)
        if (tamLoc != 0):
            hayAbierto = False
            for i in range(0,cantRegLoc):
                if (varLocales.estado == "A"):
                    hayAbierto = True
                varLocales = pickle.load(regLocales)
            if hayAbierto == False:
                os.system("cls")
                print("No hay locales abiertos, por lo tanto no hay promociones vigentes")
            else:
                regLocales.seek(0,0)
                varLocales = pickle.load(regLocales)
                tamLoc = os.path.getsize(rutaLocales)
                auxLocales = 0
                while(auxLocales < cantRegLoc):
                    auxLocales = auxLocales + 1
                    if varLocales.estado == "A":
                        print()
                        print("El local ", varLocales.nombreLocal, " tiene las siguientes promociones")
                        print()
                        regPromociones.seek(0,0)
                        varPromociones = pickle.load(regPromociones)
                        tamProm = os.path.getsize(rutaPromociones)
                        auxProm = 1
                        aux = 0
                        while(auxProm <= cantRegProm):
                            fechaHoy = datetime.now().strftime("%x")
                            mes, dia, anio = fechaHoy.split("/")
                            fechaHoy = dia + "/" + mes + "/" + anio
                            fechaDesdePromo = varPromociones.fechaDesdePromo
                            fechaHastaPromo = varPromociones.fechaHastaPromo
                            comFecha1 = compararFechas(fechaHoy,fechaDesdePromo)
                            comFecha2 = compararFechas(fechaHastaPromo,fechaHoy)
                            if (varPromociones.codLocal == varLocales.codLocal and comFecha1 == False and comFecha2 == False):
                                diasSemana = varPromociones.diaSemana
                                print("Codigo promoción --- Estado promoción --- Codigo local de la promo --- Fecha inicial de la promo --- Fecha final de la promo --- D L M M J V S (1 dia habilitado) --- Observaciones promo")
                                print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                                print(varPromociones.codPromo, "                   ", varPromociones.estado ,"           ", varPromociones.codLocal, "                           ", varPromociones.fechaDesdePromo, "                    ", varPromociones.fechaHastaPromo, "                  ", diasSemana[0], " ", diasSemana[1], " ", diasSemana[2], " ", diasSemana[3], " ", diasSemana[4], " ", diasSemana[5], " ", diasSemana[6], "                    ", varPromociones.textoPromo)
                                aux = aux + 1
                            auxProm = auxProm + 1
                            if (auxProm < cantRegProm):
                                varPromociones = pickle.load(regPromociones)
                        if (aux == 0):
                            print("Este local no tiene promociones vigentes")
                    if (auxLocales < cantRegLoc):
                        varLocales = pickle.load(regLocales)
        else:
            os.system("cls")
            print("No hay locales creados, por lo tanto no hay promociones")
    else:
        os.system("cls")
        print("No hay promociones creadas")
    input()

def buscarCodProm(varPromociones):
    t = os.path.getsize(rutaPromociones)
    cod = 0
    if t > 0:
        regPromociones.seek(0, 0)        
        while (regPromociones.tell() < t):
            varPromociones = pickle.load(regPromociones)
            cod = cod + 1
        return cod
    else:
        return cod

def buscarCodLoc(codLocal): #LISTO
    posModLoc = 0
    t = os.path.getsize(rutaLocales)
    rut = False
    regLocales.seek(0, 0) 
    if t > 0:        
        while (regLocales.tell() < t and rut == False):
            varLocales = pickle.load(regLocales)
            if (varLocales.codLocal == codLocal):
                rut = True
                tamRegMod = regLocales.tell()
            posModLoc = posModLoc + 1
        return rut
    else:
        return rut

def verSiHayLocales():
    t = os.path.getsize(rutaLocales)
    aux = 0
    if t > 0:
        regLocales.seek(0,0)
        varLocales = pickle.load(regLocales)
        while (regLocales.tell() < t):
            if (varLocales.estado == "A"):
                aux = 1
                varPromociones = pickle.load(regLocales)
        if (varLocales.estado == "A"):
            aux = 1
        if aux == 1:
            return True
        else:
            return False
    else:
        return False 

def crearDescuentos(): #LISTO
    listarDescuentosOPromociones()
    hayLocales = verSiHayLocales()
    os.system("cls")
    if (hayLocales == True):
        fechaHoy = datetime.now().strftime("%x")
        mes, dia, anio = fechaHoy.split("/")
        fechaHoy = str(dia + "/" + mes + "/" + anio)
        mostrarLocalesXNombres()
        codlocal = input("Ingrese el codigo del local en el cual se creara la siguiente promoción; para salir presione '-1': ")
        checkInput = validarInput(codlocal)
        while (checkInput == False):
            os.system("cls")
            print("Por favor ingrese un codigo numerico")
            print()
            mostrarLocalesXNombres()
            codlocal = input("Ingrese el codigo del local en el cual se creara la siguiente promoción (para dejar de modificar presione '-1'): ")
            checkInput = validarInput(codlocal)
            os.system("cls")
        codlocal = int(codlocal)
        opccod = buscarCodLocalAModificar(codlocal)
        while (codlocal != -1):
            while (opccod == False and codlocal != -1):
                os.system("cls")
                print("Codigo invalido")
                print()
                mostrarLocalesXNombres()
                print()
                codlocal = input("Ingresar el codigo de local que desea modificar (para dejar de modificar presione '-1'): ")
                while (checkInput == False):
                    os.system("cls")
                    print("Por favor ingrese un codigo numerico")
                    print()
                    mostrarLocalesXNombres()
                    codlocal = input("Ingrese el codigo del local en el cual se creara la siguiente promoción (para dejar de modificar presione '-1'): ")
                    checkInput = validarInput(codlocal)
                    os.system("cls")
                codlocal = int(codlocal)
                opccod = buscarCodLocalAModificar(codlocal)
            if codlocal != -1:
                os.system("cls")
                textoPromocion = input("Por favor ingrese el texto o caracteristica de la promoción; con '*' sale: ")
                os.system("cls")
                if textoPromocion != "*":
                    textoPromocion = str(textoPromocion).ljust(200, ' ')
                    validar = False
                    compFecha = False
                    fechaDesde = input("Por favor ingrese la fecha de inicio de la promoción en el formato 'dd/mm/aaaa'; con '*' sale")
                    if fechaDesde != "*":
                        validar = validarFecha(fechaDesde)
                        if validar == True:
                            compFecha = compararFechas(fechaDesde, fechaHoy)
                        while (compFecha == False and fechaDesde != "*"):
                            os.system("cls")
                            print("Por favor ingrese una fecha coherente")
                            fechaDesde = input("Por favor ingrese la fecha de inicio de la promoción; con '*' sale")
                            validar = validarFecha(fechaDesde)
                            if validar == True:
                                compFecha = compararFechas(fechaDesde, fechaHoy)
                        os.system("cls")
                        if fechaDesde != "*":
                            fechaHasta = input("Por favor ingrese la fecha de cierre de la promoción; con '*' sale")
                            if fechaHasta != "*":
                                validar = False
                                validar = validarFecha(fechaHasta)
                                if validar == True:
                                    compFecha = compararFechas(fechaHasta, fechaDesde)
                                while (compFecha == False and fechaHasta != "*"):
                                    os.system("cls")
                                    print("Por favor ingrese una fecha coherente")
                                    fechaHasta = input("Por favor ingrese la fecha de cierre de la promoción; con '*' sale")
                                    if (fechaHasta != "*"):
                                        validar = validarFecha(fechaHasta)
                                        if validar == True:
                                            compFecha = compararFechas(fechaHasta, fechaDesde)
                                os.system("cls")
                                if (fechaHasta != "*"):
                                    print("Ahora vamos a ver que dias esta habilitada la promocion")
                                    input()
                                    domin = input("¿Usted desea que los domingos este habilitada la promocion? (si-no)").lower()
                                    while(domin != "si" and domin != "no"):
                                        os.system("cls")
                                        print("Por favor ingrese si o no")
                                        domin = input("¿Usted desea que los domingos este habilitada la promocion? (si-no)").lower()
                                    os.system("cls")
                                    lun = input("¿Usted desea que los lunes este habilitada la promocion? (si-no)").lower()
                                    while(lun != "si" and lun != "no"):
                                        os.system("cls")
                                        print("Por favor ingrese si o no")
                                        lun = input("¿Usted desea que los lunes este habilitada la promocion? (si-no)").lower()
                                    os.system("cls")
                                    mart = input("¿Usted desea que los martes este habilitada la promocion? (si-no)").lower()
                                    while(mart != "si" and mart != "no"):
                                        os.system("cls")
                                        print("Por favor ingrese si o no")
                                        mart = input("¿Usted desea que los martes este habilitada la promocion? (si-no)").lower()
                                    os.system("cls")
                                    mier = input("¿Usted desea que los miercoles este habilitada la promocion? (si-no)").lower()
                                    while(mier != "si" and mier != "no"):
                                        os.system("cls")
                                        print("Por favor ingrese si o no")
                                        mier = input("¿Usted desea que los miercoles este habilitada la promocion? (si-no)").lower()
                                    os.system("cls")
                                    jue = input("¿Usted desea que los jueves este habilitada la promocion? (si-no)").lower()
                                    while(jue != "si" and jue != "no"):
                                        os.system("cls")
                                        print("Por favor ingrese si o no")
                                        jue = input("¿Usted desea que los jueves este habilitada la promocion? (si-no)").lower()
                                    os.system("cls")
                                    vier = input("¿Usted desea que los viernes este habilitada la promocion? (si-no)").lower()
                                    while(vier != "si" and vier != "no"):
                                        os.system("cls")
                                        print("Por favor ingrese si o no")
                                        vier = input("¿Usted desea que los viernes este habilitada la promocion? (si-no)").lower()
                                    os.system("cls")
                                    sab = input("¿Usted desea que los sabados este habilitada la promocion? (si-no)").lower()
                                    while(sab != "si" and sab != "no"):
                                        os.system("cls")
                                        print("Por favor ingrese si o no")
                                        sab = input("¿Usted desea que los sabados este habilitada la promocion? (si-no)").lower()
                                    os.system("cls")

                                    codprom = buscarCodProm(varPromociones)
                                    varPromociones.codPromo = codprom + 1
                                    textoPromocion = str(textoPromocion).ljust(200, ' ')
                                    varPromociones.textoPromo = textoPromocion
                                    fechaDesde = str(fechaDesde).ljust(10, ' ')
                                    varPromociones.fechaDesdePromo = fechaDesde
                                    fechaHasta = str(fechaHasta).ljust(10, ' ')
                                    varPromociones.fechaHastaPromo = fechaHasta
                                    diasSemana = [0] * 7
                                    if lun == "si":
                                        diasSemana[0] = 1
                                    elif lun == "no":
                                        diasSemana[0] = 0
                                    if mart == "si":
                                        diasSemana[1] = 1
                                    elif mart == "no":
                                        diasSemana[1] = 0
                                    if mier == "si":
                                        diasSemana[2] = 1
                                    elif mier == "no":
                                        diasSemana[2] = 0
                                    if jue == "si":
                                        diasSemana[3] = 1
                                    elif jue == "no":
                                        diasSemana[3] = 0
                                    if vier == "si":
                                        diasSemana[4] = 1
                                    elif vier == "no":
                                        diasSemana[4] = 0
                                    if sab == "si":
                                        diasSemana[5] = 1
                                    elif sab == "no":
                                        diasSemana[5] = 0
                                    if domin == "si":
                                        diasSemana[6] = 1
                                    elif domin == "no":
                                        diasSemana[6] = 0
                                    varPromociones.diaSemana = diasSemana
                                    varPromociones.estado = "pendiente "
                                    varPromociones.codLocal = codlocal
                                    formatearPromociones(varPromociones)
                                    pickle.dump(varPromociones, regPromociones)
                                    regPromociones.flush()
                                    os.system("cls")
                                    input("La carga del local ah sido completada")   
                else:
                    codlocal = -1
    else:
        print("No hay locales, por lo tanto no hay promociones")
    input()
    os.system("cls")

def logeadoDuenioLocal(): #LISTO
    os.system("cls")
    menuDuenioLocal()
    opc = input("Selecciones una opción: ")
    while (opc != "0" and opc != "1" and opc != "2" and opc != "3"):
        os.system("cls")
        print("Por favor ingrese un valor valido")
        print()
        menuDuenioLocal()
        opc = input("Selecciones una opción: ")
    while (opc != "0"):
        match opc:
            case "1":
                crearDescuentos()
            case "2":
                reporteDeUsoDeDescuentos()
            case "3":
                os.system("cls")
                input("En construcción...")               

        os.system("cls")
        menuDuenioLocal()
        opc = input("Selecciones una opción: ")
        while (opc != "0" and opc != "1" and opc != "2" and opc != "3"):
            os.system("cls")
            print("Por favor ingrese un valor valido")
            print()
            menuDuenioLocal()
            opc = input("Selecciones una opción: ")

def mostarUtilizacionDeReportes(fechaDesde, fechaHasta): #LISTO
    os.system("cls")
    print("                   promociones en ese lapso de tiempo")
    print("--------------------------------------------------------------------------------")
    t = os.path.getsize(rutaPromociones)
    if t == 0:
        print ("No hay promociones en ese lapso de tiempo")
    else:
        aux = 0
        print("Codigo promoción --- Cant de usos --- Codigo local de la promo --- L M M J V S D (1 dia habilitado) --- Observaciones promo")
        print('----------------------------------------------------------------------------------------------------------')
        regPromociones.seek(0, 0)
        varPromociones = PROMOCIONES()
        while regPromociones.tell()<t:
            varPromociones = pickle.load(regPromociones)
            diasSemana = varPromociones.diaSemana
            fechaDesdePromo = varPromociones.fechaDesdePromo
            fechaHastaPromo = varPromociones.fechaHastaPromo
            compFecha1 = compararFechas(fechaDesde, fechaDesdePromo)
            compFecha2 = compararFechas(fechaHastaPromo, fechaHasta)
            if (varPromociones.estado == "aprobada  " and compFecha1 == True and compFecha2 == True):
                usoProm = 0
                codPromo = varPromociones.codPromo
                usoProm = contarUsoProm(codPromo)
                diasSemana = varPromociones.diaSemana
                print(varPromociones.codPromo, "                   ", usoProm, "               ", varPromociones.codLocal, "                           ", diasSemana[0], " ", diasSemana[1], " ", diasSemana[2], " ", diasSemana[3], " ", diasSemana[4], " ", diasSemana[5], " ", diasSemana[6], "                    ", varPromociones.textoPromo)
                aux = aux + 1
            if (regPromociones.tell()<t):
                varPromociones = pickle.load(regPromociones)
        if aux == 0:
            os.system("cls")
            print("No hay promociones en ese lapso de tiempo")
    input()

def reporteDeUtilizacionDeRoportes(): #LISTO
    t = os.path.getsize(rutaPromociones)
    if t > 0:
        os.system("cls")
        print("Por favor ingrese la fecha de inicio en la que dese ver las promociones vigentes")
        fechaDesde = input("Por favor ingrese la fecha en el siguiente formato 'dd/mm/aa'; para salir presione '*'")
        while (fechaDesde != "*"):
            fechaValida = validarFecha(fechaDesde)
            while (fechaValida == False and fechaDesde != "*"):
                os.system("cls")
                print("Por favor ingrese una fecha valida")
                print()
                print("Por favor ingrese la fecha de inicio en la que dese ver las promociones vigentes")
                fechaDesde = input("Por favor ingrese la fecha en el siguiente formato 'dd/mm/aa'; para salir presione '*'")
                if (fechaDesde != "*"):
                    fechaValida = validarFecha(fechaDesde)
            os.system("cls")
            if (fechaDesde != "*"):
                print("Por favor ingrese la fecha de fin en la que dese ver las promociones vigentes")
                fechaHasta = input("Por favor ingrese la fecha en el siguiente formato 'dd/mm/aa'; para salir presione '*'")
                fechaValida = validarFecha(fechaHasta)
                while (fechaHasta != "*" and fechaValida == False):
                    while (fechaValida == False and fechaHasta != "*"):
                        os.system("cls")
                        print("Por favor ingrese una fecha valida")
                        print()
                        print("Por favor ingrese la fecha de fin en la que dese ver las promociones vigentes")
                        fechaHasta = input("Por favor ingrese la fecha en el siguiente formato 'dd/mm/aa'; para salir presione '*'")
                        if (fechaHasta != "*"):
                            fechaHasta = validarFecha(fechaHasta)
                os.system("cls")
                if (fechaHasta != "*"):
                    mostarUtilizacionDeReportes(fechaDesde, fechaHasta)
            os.system("cls")
            print("Por favor ingrese la fecha de inicio en la que dese ver las promociones vigentes")
            fechaDesde = input("Por favor ingrese la fecha en el siguiente formato 'dd/mm/aa'; para salir presione '*'")
    else:
        os.system("cls")
        input("Aun no hay promociones creadas")

def mostrarPromocionesPendientes(): #LISTO
    aux = 0
    os.system("cls")
    print("              Listado de promociones que aun estan pendientes")
    print("--------------------------------------------------------------------------------")
    t = os.path.getsize(rutaPromociones)
    if t == 0:
        os.system("cls")
        print ("No hay promociones pendientes")
    else:
        aux = 0
        print("Codigo promoción --- Codigo local de la promo --- Fecha inicial de la promo --- Fecha final de la promo --- D L M M J V S (1 dia habilitado) --- Observaciones promo")
        print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        regPromociones.seek(0, 0)
        varPromociones = PROMOCIONES()
        while regPromociones.tell()<t:
            varPromociones = pickle.load(regPromociones)
            if (varPromociones.estado == "pendiente "):
                diasSemana = varPromociones.diaSemana
                print(varPromociones.codPromo, "                    ", varPromociones.codLocal, "                           ", varPromociones.fechaDesdePromo, "                    ", varPromociones.fechaHastaPromo, "                  ", diasSemana[0], " ", diasSemana[1], " ", diasSemana[2], " ", diasSemana[3], " ", diasSemana[4], " ", diasSemana[5], " ", diasSemana[6], "                    ", varPromociones.textoPromo)
                aux = aux + 1
            if (regPromociones.tell()<t):
                varPromociones = pickle.load(regPromociones)
        if aux == 0:
            os.system("cls")
            print("No hay promociones pendientes")
    input()
    if aux == 0:
        return True
    else:
        return False

def buscarPromocionADenegarAceptar(codprom): #LISTO
    t = os.path.getsize(rutaPromociones)
    rut = False
    regPromociones.seek(0, 0) 
    if t > 0:        
        while (regPromociones.tell() < t):
            varPromociones = pickle.load(regPromociones)
            if (varPromociones.codPromo == codprom):
                rut = True
        return rut
    else:
        return rut 

def BuscarCodPromocionADenegarOAceptar(codProm): #LISTO
    t = os.path.getsize(rutaPromociones)
    pos=0
    regPromociones.seek(0, 0)  
    if t>0:
        varPromociones = pickle.load(regPromociones)
        while (regPromociones.tell()<t) and (int(codProm) != int(varPromociones.codPromo)):
            pos = regPromociones.tell()
            varPromociones = pickle.load(regPromociones)
        if int(varPromociones.codPromo) == int(codProm):
            return pos

def aprobarDenegarSolicitudDeDescuento(): #LISTO
    vacio = mostrarPromocionesPendientes()
    #os.system("cls")
    while vacio == False:
        codProm = input("Ingresar el codigo de  la promoción que desea aceptar / denegar (para dejar de aceptar / denegar promociones presione '-1'): ")
        checkInput = validarInput(codProm)
        while (checkInput == False):
            os.system("cls")
            print("Por favor ingrese un codigo numerico")
            print()
            vacio = mostrarPromocionesPendientes()
            codProm = input("Ingresar el codigo de  la promoción que desea aceptar / denegar (para dejar de aceptar / denegar promociones presione '-1'): ")
            checkInput = validarInput(codProm)
        codProm = int(codProm)
        opcPromocion = buscarPromocionADenegarAceptar(codProm)
        while (codProm != -1):
            while (opcPromocion == False and codProm != -1):
                os.system("cls")
                print("Codigo invalido")
                print()
                vacio = mostrarPromocionesPendientes()
                print()
                codProm = input("Ingresar el codigo de local que desea modificar (para dejar de modificar presione '*'): ")
                checkInput = validarInput(codProm)
                while (checkInput == False):
                    os.system("cls")
                    print("Por favor ingrese un codigo numerico")
                    print()
                    vacio = mostrarPromocionesPendientes()
                    codProm = input("Ingresar el codigo de  la promoción que desea aceptar / denegar (para dejar de aceptar / denegar promociones presione '-1'): ")
                    checkInput = validarInput(codProm)
                codProm = int(codProm)
                opcPromocion = buscarPromocionADenegarAceptar(codProm)

            if ((codProm != -1) and (opcPromocion == True)):
                pos = BuscarCodPromocionADenegarOAceptar(codProm)
                regPromociones.seek(pos,0)
                varPromociones = pickle.load(regPromociones)
                codLocal = varPromociones.codLocal
                codPromocion = varPromociones.codPromo
                diasSemana = varPromociones.diaSemana
                estadoProm = varPromociones.estado
                fechaInicioPromo = varPromociones.fechaDesdePromo
                fechaFinPromo = varPromociones.fechaHastaPromo
                textoProm = varPromociones.textoPromo

            if codProm != -1:
                os.system("")
                print("Codigo de la promoción: ", codPromocion)
                print("Codigo del local: ", codLocal)
                print("La promoción iniciaria el: ", fechaInicioPromo)
                print("La promoción finalizaria el: ", fechaFinPromo)
                print("Los días habiles de la promoción serian: ")
                print("Los 1 indican día habil, los 0 indican día inhabil")
                print("Domingo: ", diasSemana[0])
                print("Lunes: ", diasSemana[1])
                print("Martes: ", diasSemana[2])
                print("Miercoles: ", diasSemana[3])
                print("jueves: ", diasSemana[4])
                print("Viernes: ", diasSemana[5])
                print("Sábado: ", diasSemana[6])
                print("Las observaciones de la promocion son; ", textoProm)
                print()
                print()
                opcAceptar = input("¿Desea denegar o aceptar esta promoción? (denegar-aceptar) para dejar pendiente coloque '*'").lower()

                while (opcAceptar != "denegar" and opcAceptar != "aceptar" and opcAceptar != "*"):
                    os.system("cls")
                    print("Por favor ingrese un valor valido")
                    print()
                    print("Codigo de la promoción: ", codPromocion)
                    print("Codigo del local: ", codLocal)
                    print("La promoción iniciaria el: ", fechaInicioPromo)
                    print("La promoción finalizaria el: ", fechaFinPromo)
                    print("Los días habiles de la promoción serian: ")
                    print("Los 1 indican día habil, los 0 indican día inhabil")
                    print("Domingo: ", diasSemana[0])
                    print("Lunes: ", diasSemana[1])
                    print("Martes: ", diasSemana[2])
                    print("Miercoles: ", diasSemana[3])
                    print("jueves: ", diasSemana[4])
                    print("Viernes: ", diasSemana[5])
                    print("Sábado: ", diasSemana[6])
                    print("Las observaciones de la promocion son; ", textoProm)
                    print()
                    print()
                    opcAceptar = input("¿Desea denegar o aceptar esta promoción?(denegar-aceptar) para dejar pendiente coloque '*'").lower()
                
                if (opcAceptar == "aceptar"):
                    varPromociones.estado = "aprobada  "
                    pos = BuscarCodPromocionADenegarOAceptar(codProm)
                    regPromociones.seek(pos,0)
                    formatearPromociones(varPromociones)
                    pickle.dump(varPromociones, regPromociones)
                    regPromociones.flush()
                    print("Promoción aceptada con exito")

                elif (opcAceptar == "denegar"):
                    varPromociones.estado = "rechazada "
                    pos = BuscarCodPromocionADenegarOAceptar(codProm)
                    regPromociones.seek(pos,0)
                    formatearPromociones(varPromociones)
                    pickle.dump(varPromociones, regPromociones)
                    regPromociones.flush()
                    print("Promoción denegada con exito")

                codProm = -1
        os.system("cls")
        vacio = mostrarPromocionesPendientes()

def crearCuentasDeDueniosDeLocales(): #LISTO
    opcMail = "si"
    os.system("cls")
    opc = input("¿Desea crear un nuevo usuario de tipo 'Dueño de local'? ").lower()
    os.system("cls")
    while (opc != "si" and opc != "no"):
        print("Por favor ingrese 'si' o 'no'")
        opc = input("¿Desea crear un nuevo usuario de tipo 'Dueño de local'? ").lower()
        os.system("cls")
    while (opc == "si"):
        mail = str(input("Por favor ingrese su mail, (No mas de 100 caracteres): "))
        os.system("cls")
        while(len(mail) >= 100):
            print("Usted ingreso un mail con exceso de caracteres, por favor ingrese uno nuevo")
            mail = str(input("Por favor ingrese su mail, (No mas de 100 caracteres): "))
            os.system("cls")
        mail = str(mail).ljust(100, ' ')
        check = buscarMailExcistente(mail, varUsuario)
        while (check == True):
            print("Ya existe un mail con esas caracteristicas")
            opcMail = input("¿Desea ingresar otro?").lower()
            os.system("cls")
            while (opcMail != "si" and opcMail != "no"):
                print("Por favor ingrese 'si' o 'no'")
                print("Ya existe un mail con esas caracteristicas")
                opcMail = input("¿Desea ingresar otro?").lower()
                os.system("cls")
            if (opcMail == "si"):
                mail = str(input("Por favor ingrese su mail, (No mas de 100 caracteres): "))
                os.system("cls")
                while(len(mail) >= 100):
                    print("Usted ingreso un mail con exceso de caracteres, por favor ingrese uno nuevo")
                    mail = str(input("Por favor ingrese su mail, (No mas de 100 caracteres): "))
                    os.system("cls")
                mail = str(mail).ljust(100, ' ')
                check = buscarMailExcistente(mail, varUsuario)
            else:
                check = False
        if (check == False and opcMail == "si"):
            contra = input("Escoja su contraseña, (Exactamente de 8 caracteres)")
            os.system("cls")
            while (len(contra) != 8):
                print("Contraseña invalida, tiene que ser si o si de 8 caracteres")
                print()
                contra = input("Escoja su contraseña, (Exactamente de 8 caracteres)")
                os.system("cls")
            contra = str(contra).ljust(8, ' ')
            os.system("cls")
            print("Usted finalizo la carga del nuevo usuario, Confirme para guardar.")
            conf = input("¿Desea guardar este usuario?, ingrese 'si' o 'no'").lower()
            os.system("cls")
            while (conf != "si" and conf != "no"):
                print("Por favor ingrese si o no")
                conf = input("¿Desea guardar este usuario?, ingrese 'si' o 'no'").lower()
                os.system("cls")
            if (conf == "si"):
                codUsu = buscarUltimoCodUsuario(varUsuario)
                varUsuario.codUsuario = codUsu + 1
                mail = str(mail).ljust(100, ' ')
                varUsuario.nombreUsuario = mail
                contra = str(contra).ljust(8, ' ')
                varUsuario.claveUsuario = contra
                varUsuario.tipoUsuario = "Dueño local         "
                formatearUsuario(varUsuario)
                pickle.dump(varUsuario, regUsuario)
                regUsuario.flush()
                input("Datos guardados exitosamente")
            else:
                input("Los datos que usted ingreso previamnete han sido borrados")
            os.system("cls")

        os.system("cls")
        opc = input("¿Desea crear un nuevo usuario de tipo 'Dueño de local'? ").lower()
        os.system("cls")
        while (opc != "si" and opc != "no"):
            print("Por favor ingrese 'si' o 'no'")
            opc = input("¿Desea crear un nuevo usuario de tipo 'Dueño de local'? ").lower()
            os.system("cls")

def cuantosReg(rutaLocales,regLocales): #LISTO
    A = [0] * 2
    regLocales.seek(0,0)
    aux = pickle.load(regLocales)
    tamreg = regLocales.tell()
    tamarchivo = os.path.getsize(rutaLocales)
    cantreg = tamarchivo//tamreg
    A[0] = cantreg
    A[1] = tamreg 
    return A

def busquedaDosNombresIguales(nombreLocal): #LISTO
    t = os.path.getsize(rutaLocales)
    if t != 0:
        nombreLocal = str(nombreLocal).ljust(50, ' ')
        tamanios = cuantosReg(rutaLocales,regLocales)
        inf = 0
        sup = tamanios[0] - 1
        med = (inf + sup) // 2
        regLocales.seek(med * tamanios[1],0)
        varLocales = pickle.load(regLocales)
        while (inf < sup and sup >= 0 and varLocales.nombreLocal != nombreLocal):
            regLocales.seek(0,0)
            if nombreLocal < varLocales.nombreLocal:
                sup = med - 1
            else:
                inf = med + 1
            med = (sup + inf) // 2
            if sup >= 0:
                regLocales.seek(med * tamanios[1],0)
                #varLocales = pickle,load(regLocales)
        if varLocales.nombreLocal == nombreLocal:
            return True
        else:
            return False
    else:
        return False
    
def validarCodUs(codigoDelUsuario): #LISTO
    t = os.path.getsize(rutaUsuario)
    regUsuario.seek(0,0)
    if (t > 0):
        varUsuario = pickle.load(regUsuario)
        while((regUsuario.tell() < t) and (int(codigoDelUsuario) != varUsuario.codUsuario) and (varUsuario.tipoUsuario != "Dueño local         ")):
            varUsuario = pickle.load(regUsuario)
        if ((int(codigoDelUsuario) == varUsuario.codUsuario) and (varUsuario.tipoUsuario == "Dueño local         ")):
            return True
        else:
            return False
    else:
        return False 

def buscarCodLocalMax(varLocales): #LISTO
    t = os.path.getsize(rutaLocales)
    cod = 0
    if t > 0:
        regLocales.seek(0, 0)        
        while (regLocales.tell() < t):
            varLocales = pickle.load(regLocales)
            cod = cod + 1
        return cod
    else:
        return cod

def ordenarXCantDeRubros(rubrosInt, rubrosStr): #LISTO
    rubrosStr[0] = "Comida"
    rubrosStr[1] = "Perfumeria"
    rubrosStr[2] = "Indumentaria"
    rubrosInt[0] = 0
    rubrosInt[1] = 0
    rubrosInt[2] = 0
    t = os.path.getsize(rutaLocales)
    regLocales.seek(0, 0) 
    if t > 0:        
        while (regLocales.tell() < t):
            varLocales = pickle.load(regLocales)
            if (varLocales.rubroLocal == "comida                                            " and varLocales.estado == "A"):
                rubrosInt[0] = rubrosInt[0] + 1
            elif (varLocales.rubroLocal == "perfumeria                                        " and varLocales.estado == "A"):
                rubrosInt[1] = rubrosInt[1] + 1
            elif (varLocales.rubroLocal == "indumentaria                                      " and varLocales.estado == "A"):
                rubrosInt[2] = rubrosInt[2] + 1

    for j in range(0,2):
        for k in range((j+1),3):
            if (rubrosInt[j] < rubrosInt[k]):
                auxi = rubrosInt[j]
                rubrosInt[j] = rubrosInt[k]
                rubrosInt[k] = auxi
                auxs = rubrosStr[j]
                rubrosStr[j] = rubrosStr[k]
                rubrosStr[k] = auxs

    print("Locales ordenados por cantidad")
    print()
    for m in range(3):
        print(rubrosStr[m], ", con ", rubrosInt[m], " locales")
    input()
    os.system("cls")

def hayDueniosDeLocales(): #LISTO 
    t = os.path.getsize(rutaUsuario)
    hay = False
    regUsuario.seek(0, 0)
    if t > 0:        
        while (regUsuario.tell() < t):
            varUsuario = pickle.load(regUsuario)
            if (varUsuario.tipoUsuario == "Dueño local         "):
                hay = True
        return hay
    else:
        return hay
    
def mostrarDueniosLocales(): #LISTO
    os.system("cls")
    print("             Listado de usuarios tipo 'dueños de local' ya creados")
    print("--------------------------------------------------------------------------------")
    t = os.path.getsize(rutaUsuario)
    if t==0:
        print()
        print("No hay usuarios de ese tipo creados")
    else:
        print("Codigo usuario      Nombre usuario")
        print("----------------------------------")
        regUsuario.seek(0, 0)
        varUsuario = USUARIO()
        while regUsuario.tell()<t:
            varUsuario = pickle.load(regUsuario)
            if (varUsuario.tipoUsuario == "Dueño local         "):
                print(varUsuario.codUsuario, "                  ", varUsuario.nombreUsuario)
    input()

def crearLocales(): #LISTO
    mostrarLocalesXNombres()
    hayDuenio = hayDueniosDeLocales()
    os.system("cls")
    if hayDuenio == True:
        opc = False
        nombreLocal = input("Ingresar nombre del local, con un * sale; ")
        if (nombreLocal != "*"):
            nombreLocal = str(nombreLocal).ljust(50, ' ')
            opc = busquedaDosNombresIguales(nombreLocal)
        while (opc == True and nombreLocal != "*"):
            os.system("cls")
            print("El local que usted ingreso ya esta registrado en el rpgrama")
            print()
            nombreLocal = input("Ingresar nombre del local, con un * sale; ")
            if (nombreLocal != "*"):
                nombreLocal = str(nombreLocal).ljust(50, ' ')
                opc = busquedaDosNombresIguales(nombreLocal)
        os.system("cls")
        while (nombreLocal != "*"):
            ubicacionLocal = input("Ingrese la ubicación del local: ")
            os.system("cls")
            rubroLocal = input("Ingrese el rubro del local: (indumentaria - comida - perfumeria) ").lower()
            while (rubroLocal != "indumentaria" and rubroLocal != "comida" and rubroLocal != "perfumeria"):
                os.system("cls")
                print("Por favor ingrese un rubro exixtente...")
                print()
                rubroLocal = input("Ingrese el rubro del local: (indumentaria - comida - perfumeria) ").lower()
            os.system("cls")
            mostrarDueniosLocales()
            codigoDelUsuario = input("Ingrese el codigo del usuario del dueño del local: ")
            opccod = validarCodUs(codigoDelUsuario)
            while (opccod == False and nombreLocal != "*"):
                os.system("cls")
                mostrarDueniosLocales()
                print("Por favor ingrse un codigo de usuario existente, coloque '*' para salir de la carga de locales")
                print()
                codigoDelUsuario = input("Ingrese el codigo del usuario del dueño del local: ")
                opccod = validarCodUs(codigoDelUsuario)
                if (codigoDelUsuario == "*"):
                    nombreLocal = "*"
            os.system("cls")
            if (nombreLocal != "*"):
                codLocal = buscarCodLocalMax(varLocales)
                varLocales.codLocal = codLocal + 1
                nombreLocal = str(nombreLocal).ljust(50, ' ')
                varLocales.nombreLocal = nombreLocal
                ubicacionLocal = str(ubicacionLocal).ljust(50, ' ')
                varLocales.ubicacionLocal = ubicacionLocal
                rubroLocal = str(rubroLocal).ljust(50, ' ')
                varLocales.rubroLocal = rubroLocal
                codigoDelUsuario = int(codigoDelUsuario)
                varLocales.codUsuario = codigoDelUsuario
                varLocales.estado = "A"
                formatearLocales(varLocales)
                pickle.dump(varLocales, regLocales)
                regLocales.flush()
                os.system("cls")
                input("La carga del local ah sido completada")

            nombreLocal = input("Ingresar nombre del local, con un '*' sale: ")
            if (nombreLocal != "*"):
                nombreLocal = str(nombreLocal).ljust(50, ' ') 
                opc = busquedaDosNombresIguales(nombreLocal)
            while (opc == True and nombreLocal != "*"):
                os.system("cls")
                print("El local que usted ingreso ya esta registrado en el rpgrama")
                print()
                nombreLocal = input("Ingresar nombre del local, con un * sale")
                if (nombreLocal != "*"):
                    nombreLocal = str(nombreLocal).ljust(50 , ' ')
                    opc = busquedaDosNombresIguales(nombreLocal)
                os.system("cls")

        os.system("cls")
        rubrosInt = [0] * 3
        rubrosStr = [""] * 3
        ordenarXCantDeRubros(rubrosInt, rubrosStr)

    else:
        print("No hay dueños de locales existentes")
        input("Por favor cree un usuario 'dueño de local' antes de crear un local")

def buscarCodLocalAModificar(codAModificar): #LISTO
    global tamRegMod, posModLoc
    posModLoc = 0
    t = os.path.getsize(rutaLocales)
    rut = False
    regLocales.seek(0, 0) 
    if t > 0:        
        while (regLocales.tell() < t and rut == False):
            varLocales = pickle.load(regLocales)
            if (varLocales.codLocal == codAModificar):
                rut = True
                tamRegMod = regLocales.tell()
            posModLoc = posModLoc + 1
        return rut
    else:
        return rut

def buscarPosDelLocalAModificar(codElimMod): #LISTO
    t = os.path.getsize(rutaLocales)
    pos=0
    regLocales.seek(0, 0)  
    if t>0:
        varLocales = pickle.load(regLocales)
        while (regLocales.tell()<t) and (int(codElimMod) != int(varLocales.codLocal)):
            pos = regLocales.tell()
            varLocales = pickle.load(regLocales)
        if int(varLocales.codLocal) == int(codElimMod):
            return pos

def modificarLocales(): #LISTO
    t = os.path.getsize(rutaLocales)
    if t > 0:
        nombreLocal = " "
        ubicacionLocal = " "
        rubroLocal = " "
        codUsLocal = 0
        estadoLocal = " "
        mostrarLocalesXNombres()
        codAModificar = input("Ingresar el codigo de local que desea modificar (para dejar de modificar presione '-1'): ")
        checkInput = validarInput(codAModificar)
        while (checkInput == False):
            os.system("cls")
            print("Por favor ingrese un codigo numerico")
            print()
            mostrarLocalesXNombres()
            codAModificar = input("Ingresar el codigo de local que desea modificar (para dejar de modificar presione '-1'): ")
            checkInput = validarInput(codAModificar)
        if (checkInput == True):
            codAModificar = int(codAModificar)
        opccod = buscarCodLocalAModificar(codAModificar)
        while (codAModificar != -1):
            while (opccod == False and codAModificar != -1):
                os.system("cls")
                print("Codigo invalido")
                print()
                mostrarLocalesXNombres()
                print()
                codAModificar = input("Ingresar el codigo de local que desea modificar (para dejar de modificar presione '*'): ")
                checkInput = validarInput(codAModificar)
                while (checkInput == False):
                    os.system("cls")
                    print("Por favor ingrese un codigo numerico")
                    print()
                    mostrarLocalesXNombres()
                    codAModificar = input("Ingresar el codigo de local que desea modificar (para dejar de modificar presione '-1'): ")
                    checkInput = validarInput(codAModificar)
                if (checkInput == True):
                    codAModificar = int(codAModificar)
                opccod = buscarCodLocalAModificar(codAModificar)
            if ((codAModificar != -1) and (opccod == True)):
                pos = buscarPosDelLocalAModificar(codAModificar)
                regLocales.seek(pos,0)
                varLocales = pickle.load(regLocales)
                nombreLocal = varLocales.nombreLocal
                ubicacionLocal = varLocales.ubicacionLocal
                rubroLocal = varLocales.rubroLocal
                codUsLocal = varLocales.codUsuario
                estadoLocal = varLocales.estado

            if codAModificar != -1:
                os.system("cls")
                print("Nombre del local: ", nombreLocal)
                print("Ubicacion del local: ", ubicacionLocal)
                print("Rubro del local: ", rubroLocal)
                print("Codigo del usuario del local: ", codUsLocal)
                print("Estado del local: ", estadoLocal)
                input()
                os.system("cls")
                print("Su nombre actual es: ", nombreLocal, ", si desea modificarlo ingrese su nuevo nombre de lo contrario ingrese '*'")
                opcNombre = input()
                if opcNombre != "*":
                    opcNombre = str(opcNombre).ljust(50, ' ')
                    checkNombre = busquedaDosNombresIguales(opcNombre)
                    while (opcNombre != "*" and checkNombre == True):
                        os.system("cls")
                        print("Nombre existente, por favor ingrse otro")
                        print("Su nombre actual es: ", nombreLocal, ", si desea modificarlo ingrese su nuevo nombre de lo contrario ingrese '*'")
                        opcNombre = input()
                        if opcNombre != "*":
                            opcNombre = str(opcNombre).ljust(50, ' ')
                            checkNombre = busquedaDosNombresIguales(opcNombre)
                os.system("cls")
                print("Su ubicación actual es: ", ubicacionLocal, ", si desea modificarlo ingrese su nueva ubicación de lo contrario ingrse '*'")
                opcUbicacion = input().ljust(50, ' ')
                os.system("cls")
                print("Su rubro actual es: ", rubroLocal, ", si desea modificarlo ingrese su nuevo rubro (perfumeria - comida - indumentaria), de lo contrario ingrese '*'")
                opcRubro = input().lower()
                while(opcRubro != "comida" and opcRubro != "perfumeria" and opcRubro != "indumentaria" and opcRubro != "*"):
                    os.system("cls")
                    print("rubro incorrecto")
                    print()
                    print("Su rubro actual es: ", rubroLocal, ", si desea modificarlo ingrese su nuevo rubro (perfumeria - comida - indumentaria), de lo contrario ingrese '*'")
                    opcRubro = input().lower()
                os.system("cls")
                print("El codigo de usuario de este local es: ", codUsLocal, ", si desea modificarlo ingrese el nuevo codigo de usuario, de lo contrario ingrese '*'")
                opcCodUs = input()
                verSiInput = validarInput(opcCodUs)
                while (verSiInput == False and opcCodUs != "*"):
                    os.system("cls")
                    print("Por favor, ingrese un valor numerico o '*'")
                    print()
                    print("El codigo de usuario de este local es: ", codUsLocal, ", si desea modificarlo ingrese el nuevo codigo de usuario, de lo contrario ingrese '*'")
                    opcCodUs = input()
                if opcCodUs != "*":
                    checkCod = validarCodUs(opcCodUs)
                while(opcCodUs != "*" and checkCod == False):
                    os.system("cls")
                    print("Codigo de usuario incorrecto")
                    print()
                    print("El codigo de usuario de este local es: ", codUsLocal, ", si desea modificarlo ingrese el nuevo codigo de usuario, de lo contrario ingrese '*'")
                    opcCodUs = input()
                    checkCod = validarCodUs(opcCodUs)
                os.system("cls")
                if (varLocales.estado == "A"):
                    opcEstado = input("El estado de este local es 'ALTA', ¿desea modificarlo? (si-no): ").lower()
                    while (opcEstado != "si" and opcEstado != "no"):
                        os.system("cls")
                        print("Por favor ingrese si o no")
                        print()
                        opcEstado = input("El estado de este local es 'ALTA', ¿desea modificarlo? (si-no): ").lower()
                elif (varLocales.estado == "B"):
                    opcEstado = input("El estado de este local es 'BAJA', ¿desea modificarlo? (si-no): ").lower()
                    while (opcEstado != "si" and opcEstado != "no"):
                        os.system("cls")
                        print("Por favor ingrese si o no")
                        print()
                        opcEstado = input("El estado de este local es 'BAJA', ¿desea modificarlo? (si-no): ").lower()

                if (opcNombre != "*"):
                    opcNombre = str(opcNombre).ljust(50, ' ')
                    varLocales.nombreLocal = opcNombre
                else:
                    varLocales.nombreLocal = nombreLocal
                if (opcUbicacion != "*"):
                    opcUbicacion = str(opcUbicacion).ljust(50, ' ')
                    varLocales.ubicacionLocal = opcUbicacion
                else:
                    varLocales.ubicacionLocal = ubicacionLocal
                if (opcRubro != "*"):
                    opcRubro = str(opcRubro).ljust(50, ' ')
                    varLocales.rubroLocal = opcRubro
                else:
                    varLocales.rubroLocal = rubroLocal
                if (opcCodUs != "*"):
                    varLocales.codUsuario = opcCodUs
                else:
                    varLocales.codUsuario = codUsLocal
                if (estadoLocal == "A"):
                    if (opcEstado == "si"):
                        varLocales.estado = "B"
                    else:
                        varLocales.estado = estadoLocal
                elif(estadoLocal =="B"):
                    if (opcEstado =="si"):
                        varLocales.estado = "A"
                    else:
                        varLocales.estado = estadoLocal
                pos = buscarPosDelLocalAModificar(codAModificar)
                regLocales.seek(pos,0)
                formatearLocales(varLocales)
                pickle.dump(varLocales, regLocales)
                regLocales.flush()
                
                os.system("cls")
                input("Modificación guardada con exita")
                os.system("cls")
                mostrarLocalesXNombres()
                codAModificar = input("Ingresar el codigo de local que desea modificar (para dejar de modificar presione '-1'): ")
                checkInput = validarInput(codAModificar)
                while (checkInput == False):
                    os.system("cls")
                    print("Por favor ingrese un codigo numerico")
                    print()
                    mostrarLocalesXNombres()
                    codAModificar = input("Ingresar el codigo de local que desea modificar (para dejar de modificar presione '-1'): ")
                    checkInput = validarInput(codAModificar)
                codAModificar = int(codAModificar)
                if codAModificar != -1:
                    opccod = buscarCodLocalAModificar(codAModificar)
    else:
        os.system("cls")
        print("No hay locales para modificar, por favor primero cree un local antes de modificarlo")
        input()

def buscarCodLocalAEliminar(codAEliminar): #LISTO
    t = os.path.getsize(rutaLocales)
    rut = False
    regLocales.seek(0, 0) 
    if t > 0:        
        while (regLocales.tell() < t):
            varLocales = pickle.load(regLocales)
            if (varLocales.codLocal == codAEliminar and varLocales.estado == "A"):
                rut = True
        return rut
    else:
        return rut

def VerSiHayLocalesParaEliminar(): #LISTO
    t = os.path.getsize(rutaLocales)
    hay = False
    if t > 0:
        regLocales.seek(0, 0)
        varLocales = pickle.load(regLocales)
        while (regLocales.tell() < t and varLocales.estado == "B"):
            varLocales = pickle.load(regLocales)
        if (varLocales.estado == "A"):
            hay = True
        return hay
    else:
        return hay

def mostrarLocalesXNombresAEliminar(): #LISTO
    os.system("cls")
    print("                       Listado de locales ah eliminar")
    print("--------------------------------------------------------------------------------")
    t = os.path.getsize(rutaLocales)
    if t==0:
        print ("No hay locales creados")
    else:
        cont = 0
        ordenarXNombre()
        print("Codigo local      Nombre local               Ubicación local               Rubro local            Codigo Usuario")
        print('----------------------------------------------------------------------------------------------------------------')
        regLocales.seek(0, 0)
        varLocales = pickle.load(regLocales)
        tamReg = regLocales.tell()
        cantReg = int(os.path.getsize(rutaLocales) / tamReg)
        while cont < cantReg:
            cont = cont + 1
            if (varLocales.estado == "A"):
                print(varLocales.codLocal, "               ", varLocales.nombreLocal, "                     ", varLocales.ubicacionLocal, "                 ", varLocales.rubroLocal, "                 ", varLocales.codUsuario)
            if cont < cantReg:
                varLocales = pickle.load(regLocales)
    input()

def eliminarLocal(): #LISTO
    entre = False
    codAEliminar = 0
    hay = VerSiHayLocalesParaEliminar()
    while (hay == True and codAEliminar != -1):
        entre = True
        nombreLocal = " "
        ubicacionLocal = " "
        rubroLocal = " "
        codUsLocal = 0
        estadoLocal = " "
        mostrarLocalesXNombresAEliminar()
        codAEliminar = input("Ingresar el codigo de local que desea eliminar (para dejar de modificar presione '-1'): ")
        checkInput = validarInput(codAEliminar)
        while (checkInput == False):
            os.system("cls")
            print("Por favor ingrese un codigo numerico")
            print()
            mostrarLocalesXNombresAEliminar()
            codAEliminar = input("Ingresar el codigo de local que desea eliminar (para dejar de modificar presione '-1'): ")
            checkInput = validarInput(codAEliminar)
        if (checkInput == True):
            codAEliminar = int(codAEliminar)
        opccod = buscarCodLocalAModificar(codAEliminar)
        if (codAEliminar != -1):
            while (opccod == False and codAEliminar != -1):
                os.system("cls")
                print("Codigo invalido")
                print()
                mostrarLocalesXNombres()
                print()
                codAEliminar = input("Ingresar el codigo de local que desea eliminar (para dejar de modificar presione '*'): ")
                checkInput = validarInput(codAEliminar)
                while (checkInput == False):
                    os.system("cls")
                    print("Por favor ingrese un codigo numerico")
                    print()
                    mostrarLocalesXNombresAEliminar()
                    codAEliminar = input("Ingresar el codigo de local que desea eliminar (para dejar de modificar presione '-1'): ")
                    checkInput = validarInput(codAEliminar)
                if (checkInput == True):
                    codAEliminar = int(codAEliminar)
                opccod = buscarCodLocalAModificar(codAEliminar)

            if ((codAEliminar != -1) and (opccod == True)):
                pos = buscarPosDelLocalAModificar(codAEliminar)
                regLocales.seek(pos,0)
                varLocales = pickle.load(regLocales)
                nombreLocal = varLocales.nombreLocal
                ubicacionLocal = varLocales.ubicacionLocal
                rubroLocal = varLocales.rubroLocal
                codUsLocal = varLocales.codUsuario
                estadoLocal = varLocales.estado
            
            if codAEliminar != -1:
                os.system("cls")
                print("Nombre del local: ", nombreLocal)
                print("Ubicacion del local: ", ubicacionLocal)
                print("Rubro del local: ", rubroLocal)
                print("Codigo del usuario del local: ", codUsLocal)
                print("Estado del local: ", estadoLocal)
                print()
                opcEliminar = input("¿Usted desea eliminar este local? (si-no)").lower()
                while (opcEliminar != "si" and opcEliminar != "no"):
                    os.system("cls")
                    print("Por favor escoja si o no")
                    print()
                    print("Nombre del local: ", nombreLocal)
                    print("Ubicacion del local: ", ubicacionLocal)
                    print("Rubro del local: ", rubroLocal)
                    print("Codigo del usuario del local: ", codUsLocal)
                    print("Estado del local: ", estadoLocal)
                    print()
                    opcEliminar = input("¿Usted desea eliminar este local? (si-no)").lower()

                if opcEliminar == "si":
                    varLocales.estado = "B"
                    pos = buscarPosDelLocalAModificar(codAEliminar)
                    regLocales.seek(pos,0)
                    formatearLocales(varLocales)
                    pickle.dump(varLocales, regLocales)
                    regLocales.flush()
        hay = VerSiHayLocalesParaEliminar()
    if entre == False:
        os.system("cls")
        input("No hay locales para eliminar")

def mapaLocal(): #LISTO 1
    ordenarXNombre()
    t = os.path.getsize(rutaLocales)
    if t == 0:
        os.system("cls")
        print("\n+ - + - + - + - + - +")
        for f in range(0,10):
            for c in range(0,5):
                print ("| " "0", end=" ")
            print("|\n+ - + - + - + - + - +")
        print()
        input("Si presiona una tecla, vuelve al menú")
    else:
        os.system("cls")
        cantLoc = 0
        regLocales.seek(0,0)
        varLocales = pickle.load(regLocales)
        tamreg = regLocales.tell()
        tamarchivo = os.path.getsize(rutaLocales)
        cantLoc = tamarchivo//tamreg
        auxLoc = 0
        regLocales.seek(0,0)
        print("\n+ - + - + - + - + - +")
        for f in range(0,10):
            for c in range(0,5):
                if(cantLoc > auxLoc and (varLocales.estado =="A" or varLocales.estado =="B")):
                    auxLoc = auxLoc + 1
                    varLocales = pickle.load(regLocales)
                    print ("|", varLocales.codLocal, end=" ")
                else: 
                    print ("| " "0", end=" ")
            print("|\n+ - + - + - + - + - +")
        print()
        input("Si presiona una tecla, vuelve al menú")

def gestionDeLocales(): #LISTO
    os.system("cls")
    subMenuGestionDeLocales()
    opc = input("Selecciones una opción: ").lower()
    while (opc != "a" and opc != "b" and opc != "c" and opc != "d" and opc != "e"):
        os.system("cls")
        print("Por favor ingrese un valor valido")
        print()
        subMenuGestionDeLocales()
        opc = input("Selecciones una opción: ").lower()
    while (opc != "e"):
        match opc:
            case "a":
                crearLocales()
            case "b":
                modificarLocales()
            case "c":
                eliminarLocal()
            case "d":
                mapaLocal()                

        os.system("cls")
        subMenuGestionDeLocales()
        opc = input("Selecciones una opción: ").lower()
        while (opc != "a" and opc != "b" and opc != "c" and opc != "d" and opc != "e"):
            os.system("cls")
            print("Por favor ingrese un valor valido")
            print()
            subMenuGestionDeLocales()
            opc = input("Selecciones una opción: ").lower()

def logeadoAdministrador(): #LISTO
    os.system("cls")
    menuAdministrador()
    opc = input("Selecciones una opción: ")
    while (opc != "0" and opc != "1" and opc != "2" and opc != "3" and opc != "4" and opc != "5"):
        os.system("cls")
        print("Por favor ingrese un valor valido")
        print()
        menuAdministrador()
        opc = input("Selecciones una opción: ")
    while (opc != "0"):
        match opc:
            case "1":
                gestionDeLocales()
            case "2":
                crearCuentasDeDueniosDeLocales()
            case "3":
                aprobarDenegarSolicitudDeDescuento()
            case "4":
                os.system("cls")
                input("En construcción...")
            case "5":
                reporteDeUtilizacionDeRoportes()                

        os.system("cls")
        menuAdministrador()
        opc = input("Selecciones una opción: ")
        while (opc != "0" and opc != "1" and opc != "2" and opc != "3" and opc != "4" and opc != "5"):
            os.system("cls")
            print("Por favor ingrese un valor valido")
            print()
            menuAdministrador()
            opc = input("Selecciones una opción: ")
        
def login(): #LISTO
    os.system("cls")
    usuario = input("Usuario: ").ljust(100, ' ')
    contrasena = pwinput.pwinput("Contraseña: ", mask = "*").ljust(8, ' ')
    confusu = buscarMailExcistente(usuario, varUsuario)
    confcont = buscarcontrasenaExcistente(contrasena, varUsuario)
    cont = 0
    os.system("cls")
    if (confusu == True and confcont == True):
        entro = True
    else:
        entro = False
    while(entro == False and cont < 2):
        print("Usuario o contraseña incorrecta")
        usuario = input("Usuario: ").ljust(100, ' ')
        contrasena = pwinput.pwinput("Contraseña: ", mask = "*").ljust(8, ' ')
        confusu = buscarMailExcistente(usuario, varUsuario)
        confcont = buscarcontrasenaExcistente(contrasena, varUsuario)
        if (confusu == True and confcont == True):
            entro = True
        else:
            entro = False
        cont = cont + 1
        os.system("cls")

    if (entro == True):
        global PosDelUsuarioEnElPrograma, codigoUsuarioEnElPrograma, usuarioEnElPrograma, contrasenaEnElPrograma, tipoUsuarioEnElPrograma
        PosDelUsuarioEnElPrograma = buscarPosUsuarioEnElPrograma(usuario)
        if PosDelUsuarioEnElPrograma != -1:
            usuarioEnElPrograma = usuario
            contrasenaEnElPrograma = contrasena
            tipoUsuarioEnElPrograma = buscarTipoUsuarioDelPrograma(usuario)
            codigoUsuarioEnElPrograma = buscarCodigoUsuarioEnElPrograma(usuario)
            match tipoUsuarioEnElPrograma:
                case "Cliente             ":
                    logeadoCliente()
                case "Dueño local         ":
                    logeadoDuenioLocal()
                case "Administrador       ":
                    logeadoAdministrador()
    else:
        os.system("cls")
        input("Usted ya ingreso erroniamente demaciadas veces, vuelva a intentar más tarde")
        sys.exit()

def crearCliente(): #LISTO
    opcMail = "si"
    os.system("cls")
    opc = input("¿Desea crear un nuevo usuario? ").lower()
    os.system("cls")
    while (opc != "si" and opc != "no"):
        print("Por favor ingrese 'si' o 'no'")
        opc = input("¿Desea crear un nuevo usuario? ").lower()
        os.system("cls")
    if (opc == "si"):
        os.system("cls")
        mail = input("Ingrese su mail para luego acceder al programa: ")
        while(len(mail) >= 100):
            print("Usted ingreso un mail con exceso de caracteres, por favor ingrese uno nuevo")
            mail = str(input("Por favor ingrese su mail, (No mas de 100 caracteres): "))
            os.system("cls")
        mail = str(mail).ljust(100, ' ')
        check = buscarMailExcistente(mail, varUsuario)
        while (check == True):
            print("Ya existe un mail con esas caracteristicas")
            opcMail = input("¿Desea ingresar otro?").lower()
            os.system("cls")
            while (opcMail != "si" and opcMail != "no"):
                print("Por favor ingrese 'si' o 'no'")
                print("Ya existe un mail con esas caracteristicas")
                opcMail = input("¿Desea ingresar otro?").lower()
                os.system("cls")
            if (opcMail == "si"):
                os.system("cls")
                mail = input("Ingrese su mail para luego acceder al programa: ")
                while(len(mail) >= 100):
                    print("Usted ingreso un mail con exceso de caracteres, por favor ingrese uno nuevo")
                    mail = str(input("Por favor ingrese su mail, (No mas de 100 caracteres): "))
                    os.system("cls")
                mail = str(mail).ljust(100, ' ')
                check = buscarMailExcistente(mail, varUsuario)
            else:
                check = False
        if (check == False and opcMail == "si"):
            contra = input("Escoja su contraseña, (Exactamente de 8 caracteres)")
            os.system("cls")
            while (len(contra) != 8):
                print("Contraseña invalida, tiene que ser si o si de 8 caracteres")
                print()
                contra = input("Escoja su contraseña, (Exactamente de 8 caracteres)")
                os.system("cls")
            contra = str(contra).ljust(8, ' ')
            os.system("cls")
            print("Usted finalizo la carga del nuevo usuario, Confirme para guardar.")
            conf = input("¿Desea guardar este usuario?, ingrese 'si' o 'no'").lower()
            os.system("cls")
            while (conf != "si" and conf != "no"):
                print("Por favor ingrese si o no")
                conf = input("¿Desea guardar este usuario?, ingrese 'si' o 'no'").lower()
                os.system("cls")
            if (conf == "si"):
                codUsu = buscarUltimoCodUsuario(varUsuario)
                varUsuario.codUsuario = codUsu + 1
                varUsuario.nombreUsuario = mail
                varUsuario.claveUsuario = contra
                varUsuario.tipoUsuario = "Cliente"
                formatearUsuario(varUsuario)
                pickle.dump(varUsuario, regUsuario)
                regUsuario.flush()
                input("Datos guardados exitosamente")
            else:
                input("Los datos que usted ingreso previamnete han sido borrados")
            os.system("cls")
             
def AbrirArchivo(rutaUsuario, rutaLocales, rutaPromociones, rutaUsoPromociones, rutaNovedades): #LISTO
    global primeraVez
    global regUsuario, regLocales, regPromociones, regUsoPromociones, regNovedades

    primeraVez = 0
    if (os.path.exists(rutaUsuario) == False):
        regUsuario = open(rutaUsuario, "w+b")
        primeraVez = 1
    elif(os.path.exists(rutaUsuario) == True):
        regUsuario = open(rutaUsuario, "r+b")

    if (os.path.exists(rutaLocales) == False):
        regLocales = open(rutaLocales, "w+b")
    elif(os.path.exists(rutaLocales) == True):
        regLocales = open(rutaLocales, "r+b")

    if (os.path.exists(rutaPromociones) == False):
        regPromociones = open(rutaPromociones, "w+b")
    elif(os.path.exists(rutaPromociones) == True):
        regPromociones = open(rutaPromociones, "r+b")

    if (os.path.exists(rutaUsoPromociones) == False):
        regUsoPromociones = open(rutaUsoPromociones, "w+b")
    elif(os.path.exists(rutaUsoPromociones) == True):
        regUsoPromociones = open(rutaUsoPromociones, "r+b")

    if (os.path.exists(rutaNovedades) == False):
        regNovedades = open(rutaNovedades, "w+b")
    elif(os.path.exists(rutaNovedades) == True):
        regNovedades = open(rutaNovedades, "r+b")

def CerrarArchivo(regUsuario, regLocales, regPromociones, regUsoPromociones, regNovedades): #LISTO
    regUsuario.close()
    regLocales.close()
    regPromociones.close()
    regUsoPromociones.close()
    regNovedades.close()

sys.stdin.flush()
sys.stdout.flush()

rutaUsuario = "C:\\Users\\Usuario\\Desktop\\Facultad\\1_Anio\\Materias\\Algoritmo_Y_Estructura_De_Datos\\Trabajo_Practico_N3\\USUARIO.DAT"
rutaLocales = "C:\\Users\\Usuario\\Desktop\\Facultad\\1_Anio\\Materias\\Algoritmo_Y_Estructura_De_Datos\\Trabajo_Practico_N3\\LOCALES.DAT"
rutaPromociones = "C:\\Users\\Usuario\\Desktop\\Facultad\\1_Anio\\Materias\\Algoritmo_Y_Estructura_De_Datos\\Trabajo_Practico_N3\\PROMOCIONES.DAT"
rutaUsoPromociones = "C:\\Users\\Usuario\\Desktop\\Facultad\\1_Anio\\Materias\\Algoritmo_Y_Estructura_De_Datos\\Trabajo_Practico_N3\\USO_PROMOCIONES.DAT"
rutaNovedades = "C:\\Users\\Usuario\\Desktop\\Facultad\\1_Anio\\Materias\\Algoritmo_Y_Estructura_De_Datos\\Trabajo_Practico_N3\\NOVEDADES.DAT"

AbrirArchivo(rutaUsuario, rutaLocales, rutaPromociones, rutaUsoPromociones, rutaNovedades)

global varUsuario, varLocales, varPromociones, varUsoPromociones, varNovedades

varUsuario = USUARIO()
varLocales = LOCALES()
varPromociones = PROMOCIONES()
varUsoPromociones = USO_PROMOCIONES()
varNovedades = NOVEDADES()

if (primeraVez == 1):
    varUsuario.codUsuario = 1
    usuadm = "admin@shopping.com"
    usuadm = str(usuadm).ljust(100, ' ')
    varUsuario.nombreUsuario = usuadm
    contad = "12345"
    contad = str(contad).ljust(8, ' ')
    varUsuario.claveUsuario = contad
    tipad = "Administrador"
    tipad = str(tipad).ljust(20, ' ')
    varUsuario.tipoUsuario = tipad
    
    formatearUsuario(varUsuario)
    pickle.dump(varUsuario, regUsuario)
    regUsuario.flush()

os.system("cls")
print("|--------BIENVENIDO AL PROGRAMA--------|")
print("|--------------------------------------|")
print("| 1 - Ingresar con usuario registrado  |")
print("| 2 - Registrarse como cliente         |")
print("| 3 - Salir                            |")
print("|--------------------------------------|")

opLogin = str(input("seleccione una opción: "))
while (opLogin != "3"):
    while (opLogin != "1" and opLogin != "2" and opLogin != "3"):
        os.system("cls")
        print("Por favor ingrese un codigo valido")
        print()
        print()
        print("|--------BIENVENIDO AL PROGRAMA--------|")
        print("|--------------------------------------|")
        print("| 1 - Ingresar con usuario registrado  |")
        print("| 2 - Registrarse como cliente         |")
        print("| 3 - Salir                            |")
        print("|--------------------------------------|")
        opLogin = str(input("seleccione una opción: "))

    os.system("cls")
    match opLogin:
        case "1":
            login()
        case "2":
            crearCliente()
        case "3":
            print("Muchas gracias por su visita")
    
    os.system("cls")
    print("|--------BIENVENIDO AL PROGRAMA--------|")
    print("|--------------------------------------|")
    print("| 1 - Ingresar con usuario registrado  |")
    print("| 2 - Registrarse como cliente         |")
    print("| 3 - Salir                            |")
    print("|--------------------------------------|")

    opLogin = str(input("seleccione una opción: "))

CerrarArchivo(regUsuario, regLocales, regPromociones, regUsoPromociones, regNovedades)

os.system("cls")
input("Muchas gracias por su visita")