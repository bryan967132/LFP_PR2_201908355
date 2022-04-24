from Controlador import Ctrl
from Interfaz import Inicio
from Lector import Lector
leer = Lector()
base_datos = leer.leer()
ctrl = Ctrl(base_datos)
Inicio(ctrl).iniciar()