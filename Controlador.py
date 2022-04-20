class Ctrl:
    def __init__(self,db):
        self.db = db

    def resultado(self,local,visitante,año1,año2):
        temporada = str(año1) + '-' + str(año2)
        for partido in self.db:
            if partido.getLocal() == local and partido.getVisitante() == visitante and partido.getTemporada() == temporada:
                print(partido.getTemporada())
                print(partido.getLocal(),partido.getGolesL(),'-',partido.getGolesV(),partido.getVisitante())