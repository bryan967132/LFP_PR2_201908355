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