class Partido:
    def __init__(self,fecha,temporada,jornada,local,visitante,golesL,golesV):
        self.setFecha(fecha)
        self.setTemporada(temporada)
        self.setJornada(jornada)
        self.setLocal(local)
        self.setVisitante(visitante)
        self.setGolesL(golesL)
        self.setGolesV(golesV)

    def getFecha(self):
        return self.fecha
    
    def setFecha(self,fecha):
        self.fecha = fecha

    def getTemporada(self):
        return self.temporada
    
    def setTemporada(self,temporada):
        self.temporada = temporada

    def getJornada(self):
        return self.jornada
    
    def setJornada(self,jornada):
        self.jornada = jornada

    def getLocal(self):
        return self.local

    def setLocal(self,local):
        self.local = local
    
    def getVisitante(self):
        return self.visitante

    def setVisitante(self,visitante):
        self.visitante = visitante
    
    def getGolesL(self):
        return self.golesL
    
    def setGolesL(self,golesL):
        self.golesL = golesL

    def getGolesV(self):
        return self.golesV
    
    def setGolesV(self,golesV):
        self.golesV = golesV