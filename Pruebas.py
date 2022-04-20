from Lector import Lector
from Analizador import Analizador
from Controlador import Ctrl

leer = Lector()
lexico = Analizador()

base_datos = leer.leer()

comando = 'RESULTADO "Real Madrid" VS "Villarreal" TEMPORADA <2019-2020>'

#lexico.analizar(comando)
#lexico.imprimirTokens()
#lexico.imprimirErrores()

comando = 'JORNADA 15 TEMPORADA <2019-2020>'
#lexico.analizar(comando)
#lexico.imprimirTokens()
#lexico.imprimirErrores()

comando = 'GOLES TOTAL "Real Madrid" TEMPORADA <2019-2020>'
#lexico.analizar(comando)
#lexico.imprimirTokens()
#lexico.imprimirErrores()

ctrl = Ctrl(base_datos)
ctrl.resultado('Real Madrid','Villarreal','2019','2020')