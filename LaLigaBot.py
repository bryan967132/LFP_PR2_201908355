from Lector import Reader

leer = Reader()

partidos = leer.read()

for i in partidos:
    print('JORNADA {:<5} {:<25} VS    {:<25} FINAL: {}-{}'.format(i.getJornada(),i.getLocal(),i.getVisitante(),i.getGolesL(),i.getGolesV()))

comando = 'RESULTADO "RealMadrid" VS "Villarreal" TEMPORADA <2019-2020>'