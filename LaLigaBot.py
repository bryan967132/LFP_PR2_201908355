from Lector import Lector
from Analizador import Analizador

leer = Lector()
lexico = Analizador()

partidos = leer.leer()

comando = 'RESuLTADO "Real Madrid" VS "Villarreal" TEMPORADA <2019-2020>'

lexico.analizar(comando)
lexico.imprimirTokens()
lexico.imprimirErrores()

comando = 'JORNADA 15 TEMPORADA <2019-2020>'
lexico.analizar(comando)
lexico.imprimirTokens()
lexico.imprimirErrores()

comando = 'GOLES TOTAL "Real Madrid" TEMPORADA <2019-2020>'
lexico.analizar(comando)
lexico.imprimirTokens()
lexico.imprimirErrores()