from Lector import Lector
from AnalizadorLexico import AnalizadorLexico
from AnalizadorSintactico import AnalizadorSintactico
from Controlador import Ctrl

leer = Lector()

base_datos = leer.leer()

ctrl = Ctrl(base_datos)

lexico = AnalizadorLexico()

#comandoPrueba = 'RESULTADO "Real Madrid" VS "Villarreal" TEMPORADA <2019-2020>'
comandoPrueba = 'JORNADA 12 TEMPORADA < 2019 - 2020 > -f final12Reporte'
#comandoPrueba = 'GOLES TOTAL "Valencia" TEMPORADA <1998-1999>'
#comandoPrueba = 'TABLA TEMPORADA <2019-2020> -f reporteGlobal1'
#comandoPrueba = 'PARTIDOS "Real Madrid" TEMPORADA <2019-2020> -f reporte20Temporada -ji 6 -jf 10'
#comandoPrueba = 'TOP SUPERIOR TEMPORADA <2011-2012> -n 6'
lexico.analizar(comandoPrueba)
lexico.imprimirTokens()
lexico.imprimirErrores()
sintactico = AnalizadorSintactico(ctrl,lexico.listaTokensC)
sintactico.analizar()
sintactico.imprimirErrores()
#while True:
#    comandoPrueba = input('Ingrese el comando: ')
#    lexico.analizar(comandoPrueba)
#    lexico.imprimirTokens()
#    lexico.imprimirErrores()
#
#    sintactico = AnalizadorSintactico(ctrl,lexico.listaTokensC)
#    sintactico.analizar()
#    sintactico.imprimirErrores()

#comando1 = 'RESULTADO "Real Madrid" VS "Villarreal" TEMPORADA <2019-2020>'
#print(comando1)
#ctrl.resultado('Real Madrid','Villarreal','2019','2020')
#print()
#
#comando2 = 'JORNADA 12 TEMPORADA <2019-2020>'
#print(comando2)
#ctrl.jornada(12,'2019','2020')
#print()
#
#comando3 = 'GOLES TOTAL "Valencia" TEMPORADA <1998-1999>'
#print(comando3)
#ctrl.goles('TOTAL','Valencia','1998','1999')
#print()
#
#comando4 = 'GOLES LOCAL "Valencia" TEMPORADA <1998-1999>'
#print(comando4)
#ctrl.goles('LOCAL','Valencia','1998','1999')
#print()
#
#comando5 = 'GOLES VISITANTE "Valencia" TEMPORADA <1998-1999>'
#print(comando5)
#ctrl.goles('VISITANTE','Valencia','1998','1999')
#print()
#
#comando6 = 'TABLA TEMPORADA <2011-2012>'
#print(comando6)
#ctrl.tabla('2011','2012')
#print()
#
#comando7 = 'PARTIDOS "Espanyol" TEMPORADA <1999-2000>'
#print(comando7)
#ctrl.partidos('Espanyol','1999','2000',numJi = 5,numJf = 7)
#print()
#
#comando8 = 'TOP SUPERIOR TEMPORADA <2011-2012>'
#print(comando8)
#ctrl.top('SUPERIOR','2000','2001')
#print()