from prettytable import PrettyTable
from Posicion import Posicion
class Ctrl:
    def __init__(self,db):
        self.db = db

    def resultado(self,local,visitante,año1,año2):
        temporada = año1 + '-' + año2
        for partido in self.db:
            if partido.getLocal() == local and partido.getVisitante() == visitante and partido.getTemporada() == temporada:
                print('El resultado del partido fue:',partido.getLocal(),partido.getGolesL(),'-',partido.getVisitante(),partido.getGolesV())
                return
        print('No hay resgistro del partido')
    
    def jornada(self,numero,año1,año2,archivo = 'jornada'):
        archivo += '.html'
        temporada = año1 + '-' + año2
        for partido in self.db:
            if partido.getTemporada() == temporada and partido.getJornada() == numero:
                print(partido.getJornada(),partido.getLocal(),partido.getGolesL(),'-',partido.getVisitante(),partido.getGolesV())
    
    def goles(self,condicion,equipo,año1,año2):
        temporada = año1 + '-' + año2
        if condicion == 'TOTAL':
            goles = 0
            for partido in self.db:
                if partido.getTemporada() == temporada:
                    if partido.getLocal() == equipo:
                        goles += partido.getGolesL()
                    elif partido.getVisitante() == equipo:
                        goles += partido.getGolesV()
            print('Los goles anotados por',equipo,'en total en la temporada',temporada,'fueron',goles)
        elif condicion == 'LOCAL':
            self.golesL(equipo,temporada)
        elif condicion == 'VISITANTE':
            self.golesV(equipo,temporada)
    
    def golesL(self,equipo,temporada):
        goles = 0
        for partido in self.db:
            if partido.getTemporada() == temporada:
                if partido.getLocal() == equipo:
                    goles += partido.getGolesL()
        print('Los goles anotados por',equipo,'de local en la temporada',temporada,'fueron',goles)

    def golesV(self,equipo,temporada):
        goles = 0
        for partido in self.db:
            if partido.getTemporada() == temporada:
                if partido.getVisitante() == equipo:
                    goles += partido.getGolesV()
        print('Los goles anotados por',equipo,'de visitante en la temporada',temporada,'fueron',goles)
    
    def tablaTemporada(self,año1,año2,archivo = 'temporada'):
        archivo += '.html'
        temporada = año1 + '-' + año2
        tabla = []
        for partido in self.db:
            if partido.getTemporada() == temporada:
                if partido.getJornada() == 1:
                    tabla.append(Posicion(partido.getLocal(),0,0,0,0))
                    tabla.append(Posicion(partido.getVisitante(),0,0,0,0))
                elif partido.getJornada() == 2:
                    break
        
        for posicion in tabla:
            for partido in self.db:
                if partido.getTemporada() == temporada:
                    if partido.getLocal() == posicion.getEquipo():
                        if partido.getGolesL() > partido.getGolesV():
                            posicion.setPG(posicion.getPG() + 1)
                            posicion.setPuntos(posicion.getPuntos() + 3)
                        elif partido.getGolesL() == partido.getGolesV():
                            posicion.setPE(posicion.getPE() + 1)
                            posicion.setPuntos(posicion.getPuntos() + 1)
                        elif partido.getGolesL() < partido.getGolesV():
                            posicion.setPP(posicion.getPP() + 1)
                    elif partido.getVisitante() == posicion.getEquipo():
                        if partido.getGolesL() < partido.getGolesV():
                            posicion.setPG(posicion.getPG() + 1)
                            posicion.setPuntos(posicion.getPuntos() + 3)
                        elif partido.getGolesL() == partido.getGolesV():
                            posicion.setPE(posicion.getPE() + 1)
                            posicion.setPuntos(posicion.getPuntos() + 1)
                        elif partido.getGolesL() > partido.getGolesV():
                            posicion.setPP(posicion.getPP() + 1)
        
        for i in range(len(tabla) - 1):
            for j in range(len(tabla) - i - 1):
                if tabla[j].getPuntos() < tabla[j + 1].getPuntos():
                    tabla[j],tabla[j + 1] = tabla[j + 1],tabla[j]

        clasificacion = PrettyTable()
        clasificacion.field_names = ['','Equipo','G','E','P','Pts']
        num = 1
        for posicion in tabla:
            clasificacion.add_row([num,posicion.getEquipo(),posicion.getPG(),posicion.getPE(),posicion.getPP(),posicion.getPuntos()])
            num += 1
        print(clasificacion)