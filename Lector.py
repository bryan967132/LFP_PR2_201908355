from Partido import Partido
class Lector:
    def __init__(self):
        self.partidos = []
    
    def leer(self):
        partidosF = open('Datos/LaLigaBot-LFP.csv',encoding = 'utf-8').read()
        partidosF = partidosF.split('\n')
        for i in range(1,len(partidosF)):
            info = partidosF[i].split(',')
            self.partidos.append(Partido(info[0],info[1],int(info[2]),info[3],info[4],int(info[5]),int(info[6])))
        return self.partidos