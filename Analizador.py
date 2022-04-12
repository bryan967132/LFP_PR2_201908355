from Token import Token
from Error import Error
from prettytable import PrettyTable
class Analizador:
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
        self.linea = 1
        self.columna = 1
        self.buffer = ''
        self.estado = 0
        self.i = 0
    
    def agregarToken(self,caracter,linea,columna,token):
        self.listaTokens.append(Token(caracter,linea,columna,token))
        self.buffer = ''
    
    def agregarError(self,caracter,linea,columna):
        self.listaErrores.append(Error('Caracter \'' + caracter + '\' no reconocido',linea,columna))

    def s0(self,caracter):
        '''Estado 0'''
        if caracter.isalpha():
            self.estado = 1
            self.buffer += caracter
            self.columna += 1
        elif caracter == '"':
            self.estado = 2
            self.buffer += caracter
            self.columna += 1
        elif caracter == '<':
            self.estado = 4
            self.buffer += caracter
            self.columna += 1
        elif caracter == '-':
            self.estado = 5
            self.buffer += caracter
            self.columna += 1
        elif caracter == '>':
            self.estado = 6
            self.buffer += caracter
            self.columna += 1
        elif caracter.isdigit():
            self.estado = 7
            self.buffer += caracter
            self.columna += 1
        elif caracter == '\n':
            self.linea += 1
            self.columna = 1
        elif caracter in ['\t',' ']:
            self.columna += 1
        elif caracter == '$':
            pass
        else:
            self.columna += 1
            self.agregarError(caracter,self.linea,self.columna)
    
    def s1(self,caracter):
        if caracter.upper().isalpha():
            self.estado = 1
            self.buffer += caracter
            self.columna += 1
        else:
            if self.buffer in ['RESULTADO','TEMPORADA','JORNADA','GOLES','TABLA','PARTIDOS','TOP','ADIOS','VS','LOCAL','VISITANTE','TOTAL','SUPERIOR','INFERIOR']:
                self.agregarToken(self.buffer,self.linea,self.columna,'pr_' + self.buffer)
                self.estado = 0
                self.i -= 1
            else:
                self.agregarError(self.buffer,self.linea,self.columna)
                self.estado = 0
                self.i -= 1
    
    def s2(self,caracter):
        if caracter.isalpha() or caracter.isdigit() or caracter in ['\t',' ']:
            self.estado = 2
            self.buffer += caracter
            self.columna += 1
        elif caracter == '"':
            self.estado = 3
            self.buffer += caracter
            self.columna += 1
    
    def s3(self):
        self.agregarToken(self.buffer,self.linea,self.columna,'nomEquipo')
        self.estado = 0
        self.i -= 1
    
    def s4(self):
        self.agregarToken(self.buffer,self.linea,self.columna,'mayorQue')
        self.estado = 0
        self.i -= 1

    def s5(self):
        self.agregarToken(self.buffer,self.linea,self.columna,'guion')
        self.estado = 0
        self.i -= 1

    def s6(self):
        self.agregarToken(self.buffer,self.linea,self.columna,'menorQue')
        self.estado = 0
        self.i -= 1
    
    def s7(self,caracter):
        if caracter.isdigit():
            self.estado = 7
            self.buffer += caracter
            self.columna += 1
        else:
            self.agregarToken(self.buffer,self.linea,self.columna,'numero')
            self.estado = 0
            self.i -= 1

    def analizar(self,cadena):
        cadena += '$'
        self.i = 0
        while self.i < len(cadena):
            if self.estado == 0:
                self.s0(cadena[self.i])
            elif self.estado == 1:
                self.s1(cadena[self.i])
            elif self.estado == 2:
                self.s2(cadena[self.i])
            elif self.estado == 3:
                self.s3()
            elif self.estado == 4:
                self.s4()
            elif self.estado == 5:
                self.s5()
            elif self.estado == 6:
                self.s6()
            elif self.estado == 7:
                self.s7(cadena[self.i])
            self.i += 1

    def imprimirTokens(self):
        x = PrettyTable()
        x.field_names = ["Lexema","Linea","Columna","Tipo"]
        for token in self.listaTokens:
            x.add_row([token.lexema,token.linea,token.columna,token.tipo])
        print(x)
    
    def imprimirErrores(self):
        x = PrettyTable()
        x.field_names = ["Descripción","Linea","Columna"]
        for error in self.listaErrores:
            x.add_row([error.descripcion,error.linea,error.columna])
        print(x)