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