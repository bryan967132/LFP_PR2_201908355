from Lector import Lector
from Analizador import Analizador

leer = Lector()
analizar = Analizador()

partidos = leer.leer()

comando = 'RESULTADO "Real Madrid" VS "Villarreal" TEMPORADA <2019-2020>'

analizar.analizar(comando)
analizar.imprimirTokens()
analizar.imprimirErrores()

comando = 'JORNADA 15 TEMPORADA <2019-2020>'

analizar.analizar(comando)
analizar.imprimirTokens()
analizar.imprimirErrores()

comando = 'GOLES TOTAL "Real Madrid" TEMPORADA <2019-2020>'

analizar.analizar(comando)
analizar.imprimirTokens()
analizar.imprimirErrores()