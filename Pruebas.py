from Lector import Lector
from AnalizadorLexico import AnalizadorLexico
from Controlador import Ctrl

leer = Lector()
lexico = AnalizadorLexico()

base_datos = leer.leer()

ctrl = Ctrl(base_datos)
print()

comando1 = 'RESULTADO "Real Madrid" VS "Villarreal" TEMPORADA <2019-2020>'
print(comando1)
ctrl.resultado('Real Madrid','Villarreal','2019','2020')
print()
#lexico.analizar(comando1)
#lexico.imprimirTokens()
#lexico.imprimirErrores()

comando2 = 'JORNADA 12 TEMPORADA <2019-2020>'
print(comando2)
ctrl.jornada(12,'2019','2020')
print()
#lexico.analizar(comando2)
#lexico.imprimirTokens()
#lexico.imprimirErrores()

comando3 = 'GOLES TOTAL "Valencia" TEMPORADA <1998-1999>'
print(comando3)
ctrl.goles('TOTAL','Valencia','1998','1999')
print()
#lexico.analizar(comando3)
#lexico.imprimirTokens()
#lexico.imprimirErrores()

comando4 = 'GOLES LOCAL "Valencia" TEMPORADA <1998-1999>'
print(comando4)
ctrl.goles('LOCAL','Valencia','1998','1999')
print()
#lexico.analizar(comando5)
#lexico.imprimirTokens()
#lexico.imprimirErrores()

comando5 = 'GOLES VISITANTE "Valencia" TEMPORADA <1998-1999>'
print(comando5)
ctrl.goles('VISITANTE','Valencia','1998','1999')
print()
#lexico.analizar(comando5)
#lexico.imprimirTokens()
#lexico.imprimirErrores()

comando6 = 'TABLA TEMPORADA <2019-2020>'
print(comando6)
ctrl.tablaTemporada('2019','2020')
print()