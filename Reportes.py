import webbrowser
class Reportes:
    def repJornada(self,archivo,temporada,jornada,partidos):
        html = """<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Jornada """ + str(jornada) + """ Temporada """ + temporada + """</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    <!--===============================================================================================-->	
        <link rel="icon" type="image/png" href="Reporte/images/icons/logousac.png"/>
    <!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="Reporte/vendor/bootstrap/css/bootstrap.min.css">
    <!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="Reporte/fonts/font-awesome-4.7.0/css/font-awesome.min.css">
    <!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="Reporte/vendor/animate/animate.css">
    <!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="Reporte/vendor/select2/select2.min.css">
    <!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="Reporte/vendor/perfect-scrollbar/perfect-scrollbar.css">
    <!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="Reporte/css/util.css">
        <link rel="stylesheet" type="text/css" href="Reporte/css/main.css">
    <!--===============================================================================================-->
    </head>
    <body>
        <div class="limiter">
            <div class="container-table100">
                <div class="wrap-table100">
                    <p style="color:#fff;margin-bottom:15px;font-size:30px">Resumen Jornada """ + str(jornada) + """ Temporada """ + temporada + """</p>
                    <div class="table100">
                        <table style="margin-bottom: 50px;">
                            <thead>
                                <tr class="table100-head">
                                    <th class="column1">No</th>
                                    <th class="column3">Local</th>
                                    <th class="column3"></th>
                                    <th class="column3"></th>
                                    <th class="column3"></th>
                                    <th class="column6">Visitante</th>
                                </tr>
                            </thead>
                            <tbody>"""
        for i in range(len(partidos)):
            html += """
                                <tr>
                                    <td class="column1">""" + str(i + 1) + """</td>
                                    <td class="column3">""" + partidos[i].getLocal() + """</td>
                                    <td class="column3">""" + str(partidos[i].getGolesL()) + """</td>
                                    <td class="column3">-</td>
                                    <td class="column3">""" + str(partidos[i].getGolesV()) + """</td>
                                    <td class="column6">""" + partidos[i].getVisitante() + """</td>
                                </tr>"""
        html += """
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
        <script src="Reporte/vendor/jquery/jquery-3.2.1.min.js"></script>
        <script src="Reporte/vendor/bootstrap/js/popper.js"></script>
        <script src="Reporte/vendor/bootstrap/js/bootstrap.min.js"></script>
        <script src="Reporte/vendor/select2/select2.min.js"></script>
        <script src="Reporte/js/main.js"></script>
    </body>
</html>"""
        open(archivo,'w',encoding = 'utf-8').write(html)
        webbrowser.open(archivo)
    
    def repTabla(self,archivo,temporada,tabla):
        html = """<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Temporada """ + temporada + """</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    <!--===============================================================================================-->	
        <link rel="icon" type="image/png" href="Reporte/images/icons/logousac.png"/>
    <!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="Reporte/vendor/bootstrap/css/bootstrap.min.css">
    <!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="Reporte/fonts/font-awesome-4.7.0/css/font-awesome.min.css">
    <!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="Reporte/vendor/animate/animate.css">
    <!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="Reporte/vendor/select2/select2.min.css">
    <!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="Reporte/vendor/perfect-scrollbar/perfect-scrollbar.css">
    <!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="Reporte/css/util.css">
        <link rel="stylesheet" type="text/css" href="Reporte/css/main.css">
    <!--===============================================================================================-->
    </head>
    <body>
        <div class="limiter">
            <div class="container-table100">
                <div class="wrap-table100">
                    <p style="color:#fff;margin-bottom:15px;font-size:30px">Resumen Temporada """ + temporada + """</p>
                    <div class="table100">
                        <table style="margin-bottom: 50px;">
                            <thead>
                                <tr class="table100-head">
                                    <th class="column1">No</th>
                                    <th class="column3">Equipo</th>
                                    <th class="column2">Pts.</th>
                                    <th class="column2">PJ</th>
                                    <th class="column2">G</th>
                                    <th class="column2">E</th>
                                    <th class="column2">P</th>
                                    <th class="column2">GF</th>
                                    <th class="column2">GC</th>
                                    <th class="column6">DG</th>
                                </tr>
                            </thead>
                            <tbody>"""
        for i in range(len(tabla)):
            html += """
                                <tr>
                                    <td class="column1">""" + str(i + 1) + """</td>
                                    <td class="column3">""" + tabla[i].getEquipo() + """</td>
                                    <td class="column2">""" + str(tabla[i].getPuntos()) + """</td>
                                    <td class="column2">""" + str(tabla[i].getPG() + tabla[i].getPE() + tabla[i].getPP()) + """</td>
                                    <td class="column2">""" + str(tabla[i].getPG()) + """</td>
                                    <td class="column2">""" + str(tabla[i].getPE()) + """</td>
                                    <td class="column2">""" + str(tabla[i].getPP()) + """</td>
                                    <td class="column2">""" + str(tabla[i].getGF()) + """</td>
                                    <td class="column2">""" + str(tabla[i].getGC()) + """</td>
                                    <td class="column6">""" + str(tabla[i].getGF() - tabla[i].getGC()) + """</td>
                                </tr>"""
        html += """
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
        <script src="Reporte/vendor/jquery/jquery-3.2.1.min.js"></script>
        <script src="Reporte/vendor/bootstrap/js/popper.js"></script>
        <script src="Reporte/vendor/bootstrap/js/bootstrap.min.js"></script>
        <script src="Reporte/vendor/select2/select2.min.js"></script>
        <script src="Reporte/js/main.js"></script>
    </body>
</html>"""
        open(archivo,'w',encoding = 'utf-8').write(html)
        webbrowser.open(archivo)

    def repPartidos(self,archivo,temporada,equipo,partidos):
        html = """<!DOCTYPE html>
<html lang="en">
    <head>
        <title>""" + equipo + """ """ + temporada + """</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    <!--===============================================================================================-->	
        <link rel="icon" type="image/png" href="Reporte/images/icons/logousac.png"/>
    <!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="Reporte/vendor/bootstrap/css/bootstrap.min.css">
    <!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="Reporte/fonts/font-awesome-4.7.0/css/font-awesome.min.css">
    <!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="Reporte/vendor/animate/animate.css">
    <!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="Reporte/vendor/select2/select2.min.css">
    <!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="Reporte/vendor/perfect-scrollbar/perfect-scrollbar.css">
    <!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="Reporte/css/util.css">
        <link rel="stylesheet" type="text/css" href="Reporte/css/main.css">
    <!--===============================================================================================-->
    </head>
    <body>
        <div class="limiter">
            <div class="container-table100">
                <div class="wrap-table100">
                    <p style="color:#fff;margin-bottom:15px;font-size:30px">Resumen """ + equipo +  """ Temporada """ + temporada + """</p>
                    <div class="table100">
                        <table style="margin-bottom: 50px;">
                            <thead>
                                <tr class="table100-head">
                                    <th class="column1">Jornada</th>
                                    <th class="column3">Local</th>
                                    <th class="column3"></th>
                                    <th class="column3"></th>
                                    <th class="column3"></th>
                                    <th class="column6">Visitante</th>
                                </tr>
                            </thead>
                            <tbody>"""
        for partido in partidos:
            html += """
                                <tr>
                                    <td class="column1">""" + str(partido.getJornada()) + """</td>
                                    <td class="column3">""" + partido.getLocal() + """</td>
                                    <td class="column3">""" + str(partido.getGolesL()) + """</td>
                                    <td class="column3">-</td>
                                    <td class="column3">""" + str(partido.getGolesV()) + """</td>
                                    <td class="column6">""" + partido.getVisitante() + """</td>
                                </tr>"""
        html += """
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
        <script src="Reporte/vendor/jquery/jquery-3.2.1.min.js"></script>
        <script src="Reporte/vendor/bootstrap/js/popper.js"></script>
        <script src="Reporte/vendor/bootstrap/js/bootstrap.min.js"></script>
        <script src="Reporte/vendor/select2/select2.min.js"></script>
        <script src="Reporte/js/main.js"></script>
    </body>
</html>"""
        open(archivo,'w',encoding = 'utf-8').write(html)
        webbrowser.open(archivo)

    def repTokens(self,tokens):
        html = """<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Reporte de Tokens</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    <!--===============================================================================================-->	
        <link rel="icon" type="image/png" href="Reporte/images/icons/logousac.png"/>
    <!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="Reporte/vendor/bootstrap/css/bootstrap.min.css">
    <!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="Reporte/fonts/font-awesome-4.7.0/css/font-awesome.min.css">
    <!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="Reporte/vendor/animate/animate.css">
    <!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="Reporte/vendor/select2/select2.min.css">
    <!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="Reporte/vendor/perfect-scrollbar/perfect-scrollbar.css">
    <!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="Reporte/css/util.css">
        <link rel="stylesheet" type="text/css" href="Reporte/css/main.css">
    <!--===============================================================================================-->
    </head>
    <body>
        <div class="limiter">
            <div class="container-table100">
                <div class="wrap-table100">
                    <p style="color:#fff;margin-bottom:15px;font-size:30px">Reporte de Tokens</p>
                    <div class="table100">
                        <table style="margin-bottom: 50px;">
                            <thead>
                                <tr class="table100-head">
                                    <th class="column1">Lexema</th>
                                    <th class="column2">L&iacute;nea</th>
                                    <th class="column2">Columna</th>
                                    <th class="column6">Tipo</th>
                                </tr>
                            </thead>
                            <tbody>"""
        for token in tokens:
            html += """
                                <tr>
                                    <td class="column1">""" + token.lexema + """</td>
                                    <td class="column2">""" + str(token.linea) + """</td>
                                    <td class="column3">""" + str(token.columna) + """</td>
                                    <td class="column6">""" + token.tipo + """</td>
                                </tr>"""
        html += """
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
        <script src="Reporte/vendor/jquery/jquery-3.2.1.min.js"></script>
        <script src="Reporte/vendor/bootstrap/js/popper.js"></script>
        <script src="Reporte/vendor/bootstrap/js/bootstrap.min.js"></script>
        <script src="Reporte/vendor/select2/select2.min.js"></script>
        <script src="Reporte/js/main.js"></script>
    </body>
</html>"""
        open('ReporteTokens.html','w',encoding = 'utf-8').write(html)
        webbrowser.open('ReporteTokens.html')
    
    def repErrores(self,erroresL,erroresS):
        html = """<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Reporte de Errores</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    <!--===============================================================================================-->	
        <link rel="icon" type="image/png" href="Reporte/images/icons/logousac.png"/>
    <!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="Reporte/vendor/bootstrap/css/bootstrap.min.css">
    <!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="Reporte/fonts/font-awesome-4.7.0/css/font-awesome.min.css">
    <!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="Reporte/vendor/animate/animate.css">
    <!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="Reporte/vendor/select2/select2.min.css">
    <!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="Reporte/vendor/perfect-scrollbar/perfect-scrollbar.css">
    <!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="Reporte/css/util.css">
        <link rel="stylesheet" type="text/css" href="Reporte/css/main.css">
    <!--===============================================================================================-->
    </head>
    <body>
        <div class="limiter">
            <div class="container-table100">
                <div class="wrap-table100">
                    <p style="color:#fff;margin-bottom:15px;font-size:30px">Reporte de Errores Léxicos</p>
                    <div class="table100">
                        <table style="margin-bottom: 50px;">
                            <thead>
                                <tr class="table100-head">
                                    <th class="column1">Descripcion</th>
                                    <th class="column2">L&iacute;nea</th>
                                    <th class="column6">Columna</th>
                                </tr>
                            </thead>
                            <tbody>"""
        for error in erroresL:
            html += """
                                <tr>
                                    <td class="column1">""" + error.descripcion + """</td>
                                    <td class="column2">""" + str(error.linea) + """</td>
                                    <td class="column6">""" + str(error.columna) + """</td>
                                </tr>"""
        html += """
                            </tbody>
                        </table>
                    </div>
                </div>
                <div class="wrap-table100">
                    <p style="color:#fff;margin-bottom:15px;font-size:30px">Reporte de Errores Sintácticos</p>
                    <div class="table100">
                        <table style="margin-bottom: 50px;">
                            <thead>
                                <tr class="table100-head">
                                    <th class="column1">Descripcion</th>
                                </tr>
                            </thead>
                            <tbody>"""
        for error in erroresS:
            html += """
                                <tr>
                                    <td class="column1">""" + error + """</td>
                                </tr>"""
        html += """
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
        <script src="Reporte/vendor/jquery/jquery-3.2.1.min.js"></script>
        <script src="Reporte/vendor/bootstrap/js/popper.js"></script>
        <script src="Reporte/vendor/bootstrap/js/bootstrap.min.js"></script>
        <script src="Reporte/vendor/select2/select2.min.js"></script>
        <script src="Reporte/js/main.js"></script>
    </body>
</html>"""
        open('ReporteErrores.html','w',encoding = 'utf-8').write(html)
        webbrowser.open('ReporteErrores.html')