from Lector import Lector
from Analizador import Analizador
from Controlador import Ctrl

leer = Lector()
lexico = Analizador()

base_datos = leer.leer()

comando1 = 'RESULTADO "Real Madrid" VS "Villarreal" TEMPORADA <2019-2020>'

#lexico.analizar(comando1)
#lexico.imprimirTokens()
#lexico.imprimirErrores()

comando2 = 'JORNADA 15 TEMPORADA <2019-2020>'
#lexico.analizar(comando2)
#lexico.imprimirTokens()
#lexico.imprimirErrores()

comando3 = 'GOLES TOTAL "Real Madrid" TEMPORADA <2019-2020>'
#lexico.analizar(comando3)
#lexico.imprimirTokens()
#lexico.imprimirErrores()

ctrl = Ctrl(base_datos)

print(comando1)
ctrl.resultado('Real Madrid','Villarreal','2019','2020')
print()

print(comando2)
ctrl.jornada(15,'2019','2020')
print()