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
            self.RESULTADO()
        elif temporal.tipo == 'pr_JORNADA':
            self.JORNADA()
        elif temporal.tipo == 'pr_GOLES':
            self.GOLES()
        elif temporal.tipo == 'pr_TABLA':
            self.TABLA()
        elif temporal.tipo == 'pr_PARTIDOS':
            self.PARTIDOS()
        elif temporal.tipo == 'pr_TOP':
            self.TOP()
        elif temporal.tipo == 'pr_ADIOS':
            quit()
        else:
            self.agregarError('pr_RESULTADO | pr_JORNADA | pr_GOLES | pr_TABLA | pr_PARTIDOS | pr_TOP | pr_ADIOS',temporal.tipo)
    
    def RESULTADO(self):
        token = self.sacarToken()
        if token.tipo == 'pr_RESULTADO':
            token = self.sacarToken()
            if not token:
                self.agregarError('nomEquipo','EOF')
                return
            elif token.tipo == 'nomEquipo':
                local = token.lexema.replace('"','')
                token = self.sacarToken()
                if not token:
                    self.agregarError('pr_VS','EOF')
                    return
                elif token.tipo == 'pr_VS':
                    token = self.sacarToken()
                    if not token:
                        self.agregarError('nomEquipo','EOF')
                        return
                    elif token.tipo == 'nomEquipo':
                        visitante = token.lexema.replace('"','')
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
                                    if len(token.lexema) == 4:
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
                                                if len(token.lexema) == 4:
                                                    año2 = token.lexema
                                                    token = self.sacarToken()
                                                    if not token:
                                                        self.agregarError('mayorQue','EOF')
                                                        return
                                                    elif token.tipo == 'mayorQue':
                                                        self.ctrl.resultado(local,visitante,año1,año2)
                                                    else:
                                                        self.agregarError('mayorQue',token.tipo)
                                                else:
                                                    self.agregarError('numero de 4 cifras','numero de ' + str(len(token.lexema)) + ' cifras')
                                            else:
                                                self.agregarError('numero',token.tipo)
                                        else:
                                            self.agregarError('guion',token.tipo)
                                    else:
                                        self.agregarError('numero de 4 cifras','numero de ' + str(len(token.lexema)) + ' cifras')
                                else:
                                    self.agregarError('numero',token.tipo)
                            else:
                                self.agregarError('menorQue',token.tipo)
                        else:
                            self.agregarError('pr_TEMPORADA',token.tipo)
                    else:
                        self.agregarError('nomEquipo',token.tipo)
                else:
                    self.agregarError('pr_VS',token.tipo)
            else:
                self.agregarError('nomEquipo',token.tipo)
        else:
            self.agregarError('pr_RESULTADO',token.tipo)

    def JORNADA(self):
        token = self.sacarToken()
        if token.tipo == 'pr_JORNADA':
            token = self.sacarToken()
            if not token:
                self.agregarError('numero','EOF')
                return
            elif token.tipo == 'numero':
                if len(token.lexema) == 1 or len(token.lexema) == 2:
                    jornada = int(token.lexema)
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
                                if len(token.lexema) == 4:
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
                                            if len(token.lexema) == 4:
                                                año2 = token.lexema
                                                token = self.sacarToken()
                                                if not token:
                                                    self.agregarError('mayorQue','EOF')
                                                    return
                                                elif token.tipo == 'mayorQue':
                                                    archivo = 'jornada'
                                                    token = self.sacarToken()
                                                    if token and token.tipo == 'bandera_f':
                                                        token = self.sacarToken()
                                                        if not token:
                                                            self.agregarError('cadena','EOF')
                                                        elif token.tipo == 'cadena':
                                                            archivo = token.lexema.strip()
                                                        else:
                                                            self.agregarError('numero',token.tipo)
                                                    self.ctrl.jornada(jornada,año1,año2,archivo)
                                                else:
                                                    self.agregarError('mayorQue',token.tipo)
                                            else:
                                                self.agregarError('numero de 4 cifras','numero de ' + str(len(token.lexema)) + ' cifras')
                                        else:
                                            self.agregarError('numero',token.tipo)
                                    else:
                                        self.agregarError('guion',token.tipo)
                                else:
                                    self.agregarError('numero de 4 cifras','numero de ' + str(len(token.lexema)) + ' cifras')
                            else:
                                self.agregarError('numero',token.tipo)
                        else:
                            self.agregarError('menorQue',token.tipo)
                    else:
                        self.agregarError('pr_TEMPORADA',token.tipo)
                else:
                    self.agregarError('numero de 2 cifras como maximo','numero de ' + str(len(token.lexema)) + ' cifras')
            else:
                self.agregarError('numero',token.tipo)
        else:
            self.agregarError('pr_JORNADA',token.tipo)

    def GOLES(self):
        token = self.sacarToken()
        if token.tipo == 'pr_GOLES':
            token = self.sacarToken()
            if not token:
                self.agregarError('pr_TOTAL | pr_LOCAL | pr_VISITANTE','EOF')
                return
            elif token.tipo == 'pr_TOTAL' or token.tipo == 'pr_LOCAL' or token.tipo ==  'pr_VISITANTE':
                condicion = token.lexema.strip()
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
                                if len(token.lexema) == 4:
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
                                            if len(token.lexema) == 4:
                                                año2 = token.lexema
                                                token = self.sacarToken()
                                                if not token:
                                                    self.agregarError('mayorQue','EOF')
                                                    return
                                                elif token.tipo == 'mayorQue':
                                                    self.ctrl.goles(condicion,equipo,año1,año2)
                                                else:
                                                    self.agregarError('mayorQue',token.tipo)
                                            else:
                                                self.agregarError('numero de 4 cifras','numero de ' + str(len(token.lexema)) + ' cifras')
                                        else:
                                            self.agregarError('numero',token.tipo)
                                    else:
                                        self.agregarError('guion',token.tipo)
                                else:
                                    self.agregarError('numero de 4 cifras','numero de ' + str(len(token.lexema)) + ' cifras')
                            else:
                                self.agregarError('numero',token.tipo)
                        else:
                            self.agregarError('menorQue',token.tipo)
                    else:
                        self.agregarError('pr_TEMPORADA',token.tipo)
                else:
                    self.agregarError('nomEquipo',token.tipo)
            else:
                self.agregarError('pr_TOTAL | pr_LOCAL | pr_VISITANTE',token.tipo)
        else:
            self.agregarError('pr_GOLES',token.tipo)

    def TABLA(self):
        token = self.sacarToken()
        if token.tipo == 'pr_TABLA':
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
                        if len(token.lexema) == 4:
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
                                    if len(token.lexema) == 4:
                                        año2 = token.lexema
                                        token = self.sacarToken()
                                        if not token:
                                            self.agregarError('mayorQue','EOF')
                                            return
                                        elif token.tipo == 'mayorQue':
                                            archivo = 'temporada'
                                            token = self.sacarToken()
                                            if token and token.tipo == 'bandera_f':
                                                token = self.sacarToken()
                                                if not token:
                                                    self.agregarError('cadena','EOF')
                                                elif token.tipo == 'cadena':
                                                    archivo = token.lexema.strip()
                                                else:
                                                    self.agregarError('numero',token.tipo)
                                            self.ctrl.tabla(año1,año2,archivo)
                                        else:
                                            self.agregarError('mayorQue',token.tipo)
                                    else:
                                        self.agregarError('numero de 4 cifras','numero de ' + str(len(token.lexema)) + ' cifras')
                                else:
                                    self.agregarError('numero',token.tipo)
                            else:
                                self.agregarError('guion',token.tipo)
                        else:
                            self.agregarError('numero de 4 cifras','numero de ' + str(len(token.lexema)) + ' cifras')
                    else:
                        self.agregarError('numero',token.tipo)
                else:
                    self.agregarError('menorQue',token.tipo)
            else:
                self.agregarError('pr_TEMPORADA',token.tipo)
        else:
            self.agregarError('pr_TABLA',token.tipo)

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
                            if len(token.lexema) == 4:
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
                                        if len(token.lexema) == 4:
                                            año2 = token.lexema
                                            token = self.sacarToken()
                                            if not token:
                                                self.agregarError('mayorQue','EOF')
                                                return
                                            elif token.tipo == 'mayorQue':
                                                archivo = 'partidos'
                                                numJi = 1
                                                numJf = 38
                                                for i in range(0,len(self.listaTokens)):
                                                    token = self.listaTokens[i]
                                                    if token and token.tipo == 'bandera_f':
                                                        try:
                                                            token = self.listaTokens[i + 1]
                                                            if token.tipo == 'cadena':
                                                                archivo = token.lexema
                                                            else:
                                                                self.agregarError('cadena',token.tipo)
                                                        except:
                                                            self.agregarError('cadena','EOF')
                                                    elif token and token.tipo == 'bandera_ji':
                                                        try:
                                                            token = self.listaTokens[i + 1]
                                                            if token.tipo == 'numero':
                                                                numJi = int(token.lexema)
                                                            else:
                                                                self.agregarError('numero',token.tipo)
                                                        except:
                                                            self.agregarError('cadena','EOF')
                                                    elif token and token.tipo == 'bandera_jf':
                                                        try:
                                                            token = self.listaTokens[i + 1]
                                                            if token.tipo == 'numero':
                                                                numJf = int(token.lexema)
                                                            else:
                                                                self.agregarError('numero',token.tipo)
                                                        except:
                                                            self.agregarError('cadena','EOF')
                                                self.ctrl.partidos(equipo,año1,año2,archivo,numJi,numJf)
                                            else:
                                                self.agregarError('mayorQue',token.tipo)
                                        else:
                                            self.agregarError('numero de 4 cifras','numero de ' + str(len(token.lexema)) + ' cifras')
                                    else:
                                        self.agregarError('numero',token.tipo)
                                else:
                                    self.agregarError('guion',token.tipo)
                            else:
                                self.agregarError('numero de 4 cifras','numero de ' + str(len(token.lexema)) + ' cifras')
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

    def TOP(self):
        token = self.sacarToken()
        if token.tipo == 'pr_TOP':
            token = self.sacarToken()
            if not token:
                self.agregarError('pr_SUPERIOR | pr_INFERIOR','EOF')
                return
            elif token.tipo == 'pr_SUPERIOR' or token.tipo == 'pr_INFERIOR':
                condicion = token.lexema.strip()
                token = self.sacarToken()
                if not token:
                    self.agregarError('pr_SUPERIOR | pr_INFERIOR','EOF')
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
                            if len(token.lexema) == 4:
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
                                        if len(token.lexema) == 4:
                                            año2 = token.lexema
                                            token = self.sacarToken()
                                            if not token:
                                                self.agregarError('mayorQue','EOF')
                                                return
                                            elif token.tipo == 'mayorQue':
                                                top = 5
                                                token = self.sacarToken()
                                                if token and token.tipo == 'bandera_n':
                                                    token = self.sacarToken()
                                                    if not token:
                                                        self.agregarError('numero','EOF')
                                                    elif token.tipo == 'numero':
                                                        top = int(token.lexema)
                                                    else:
                                                        self.agregarError('numero',token.tipo)
                                                self.ctrl.top(condicion,año1,año2,top)
                                            else:
                                                self.agregarError('mayorQue',token.tipo)
                                        else:
                                            self.agregarError('numero de 4 cifras','numero de ' + str(len(token.lexema)) + ' cifras')
                                    else:
                                        self.agregarError('numero',token.tipo)
                                else:
                                    self.agregarError('guion',token.tipo)
                            else:
                                self.agregarError('numero de 4 cifras','numero de ' + str(len(token.lexema)) + ' cifras')
                        else:
                            self.agregarError('numero',token.tipo)
                    else:
                        self.agregarError('menorQue',token.tipo)
                else:
                    self.agregarError('pr_TEMPORADA',token.tipo)    
            else:
                self.agregarError('pr_SUPERIOR | pr_INFERIOR',token.tipo)
        else:
            self.agregarError('pr_TOP',token.tipo)

    def imprimirErrores(self):
        x = PrettyTable()
        x.field_names = ['Descripcion']
        for error in self.listaErrores:
            x.add_row([error])
        print(x)   