from prettytable import PrettyTable
from Token import Token
from Controlador import Ctrl
class AnalizadorSintactico:
    def __init__(self,ctrl : Ctrl,tokens : list):
        self.ctrl = ctrl
        self.listaErrores = []
        self.listaTokens = tokens
    
    def agregarError(self,esperado,obtenido):
        self.listaErrores.append('ERROR SINTÁCTICO: Se obtuvo {} se esperaba {}'.format(obtenido,esperado))
    
    def sacarToken(self) -> Token:
        try:
            return self.listaTokens.pop(0)
        except:
            return None
    
    def observarToken(self) -> Token:
        try:
            return self.listaTokens[0]
        except:
            return None

    def analizar(self):
        self.S()

    def S(self):
        self.INICIO()
    
    def INICIO(self):
        self.COMANDO()
    
    def COMANDO(self):
        temporal = self.observarToken()
        if not temporal:
            self.agregarError('pr_RESULTADO | pr_JORNADA | pr_GOLES | pr_TABLA | pr_PARTIDOS | pr_TOP | pr_ADIOS','EOF')
        elif temporal.tipo == 'pr_RESULTADO':
            print('Encontrado: pr_RESULTADO')
        elif temporal.tipo == 'pr_JORNADA':
            print('Encontrado: pr_JORNADA')
        elif temporal.tipo == 'pr_GOLES':
            print('Encontrado: pr_GOLES')
        elif temporal.tipo == 'pr_TABLA':
            print('Encontrado: pr_TABLA')
        elif temporal.tipo == 'pr_PARTIDOS':
            self.PARTIDOS()
        elif temporal.tipo == 'pr_TOP':
            print('Encontrado: pr_TOP')
        elif temporal.tipo == 'pr_ADIOS':
            print('Encontrado: pr_ADIOS')
        else:
            self.agregarError('pr_RESULTADO | pr_JORNADA | pr_GOLES | pr_TABLA | pr_PARTIDOS | pr_TOP | pr_ADIOS',temporal.tipo)
    
    def PARTIDOS(self):
        token = self.sacarToken()
        if token.tipo == 'pr_PARTIDOS':
            token = self.sacarToken()
            if not token:
                self.agregarError('nomEquipo','EOF')
                return
            elif token.tipo == 'nomEquipo':
                equipo = token.lexema.replace('"','')
                token = self.sacarToken()
                if not token:
                    self.agregarError('pr_TEMPORADA','EOF')
                    return
                elif token.tipo == 'pr_TEMPORADA':
                    token = self.sacarToken()
                    if not token:
                        self.agregarError('menorQue','EOF')
                        return
                    elif token.tipo == 'menorQue':
                        token = self.sacarToken()
                        if not token:
                            self.agregarError('numero','EOF')
                            return
                        elif token.tipo == 'numero':
                            año1 = token.lexema
                            token = self.sacarToken()
                            if not token:
                                self.agregarError('guion','EOF')
                                return
                            elif token.tipo == 'guion':
                                token = self.sacarToken()
                                if not token:
                                    self.agregarError('numero','EOF')
                                    return
                                elif token.tipo == 'numero':
                                    año2 = token.lexema
                                    token = self.sacarToken()
                                    if not token:
                                        self.agregarError('mayorQue','EOF')
                                        return
                                    elif token.tipo == 'mayorQue':
                                        archivo = 'partidos'
                                        token = self.sacarToken()
                                        if token and token.tipo == 'bandera_f':
                                            token = self.sacarToken()
                                            if not token:
                                                self.agregarError('cadena','EOF')
                                                return
                                            elif token.tipo == 'cadena':
                                                archivo = token.lexema.strip()
                                            else:
                                                self.agregarError('cadena',token.tipo)
                                        numJi = 1
                                        numJf = 38
                                        token = self.observarToken()
                                        if token and token.tipo == 'bandera_ji' or 'bandera_jf':
                                            token = self.observarToken()
                                            if token and token.tipo == 'bandera_ji':
                                                token = self.sacarToken()
                                                token = self.sacarToken()
                                                if not token:
                                                    self.agregarError('numero','EOF')
                                                    return
                                                elif token.tipo == 'numero':
                                                    numJi = int(token.lexema)
                                                else:
                                                    self.agregarError('numero',token.tipo)
                                            token = self.observarToken()
                                            if token and token.tipo == 'bandera_jf':
                                                token = self.sacarToken()
                                                token = self.sacarToken()
                                                if not token:
                                                    self.agregarError('numero','EOF')
                                                    return
                                                elif token.tipo == 'numero':
                                                    numJf = int(token.lexema)
                                                else:
                                                    self.agregarError('numero',token.tipo)

                                        self.ctrl.partidos(equipo,año1,año2,archivo,numJi,numJf)
                                    else:
                                        self.agregarError('mayorQue',token.tipo)
                                else:
                                    self.agregarError('numero',token.tipo)
                            else:
                                self.agregarError('guion',token.tipo)
                        else:
                            self.agregarError('numero',token.tipo)
                    else:
                        self.agregarError('menorQue',token.tipo)
                else:
                    self.agregarError('pr_TEMPORADA',token.tipo)
            else:
                self.agregarError('nomEquipo',token.tipo)
        else:
            self.agregarError('pr_PARTIDOS',token.tipo)

    def imprimirErrores(self):
        x = PrettyTable()
        x.field_names = ['Descripcion']
        for error in self.listaErrores:
            x.add_row([error])
        print(x)   