class Posicion:
    def __init__(self,equipo,pG,pE,pP,puntos):
        self.setEquipo(equipo)
        self.setPG(pG)
        self.setPE(pE)
        self.setPP(pP)
        self.setPuntos(puntos)

    def getEquipo(self):
        return self.equipo
    
    def setEquipo(self,equipo):
        self.equipo = equipo
    
    def getPG(self):
        return self.pG

    def setPG(self,pG):
        self.pG = pG

    def getPE(self):
        return self.pE

    def setPE(self,pE):
        self.pE = pE

    def getPP(self):
        return self.pP

    def setPP(self,pP):
        self.pP = pP

    def getPuntos(self):
        return self.puntos

    def setPuntos(self,puntos):
        self.puntos = puntos