import webbrowser
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from AnalizadorLexico import AnalizadorLexico
from AnalizadorSintactico import AnalizadorSintactico
from Controlador import Ctrl

class Inicio:
    def __init__(self,ctrl : Ctrl):
        self.tokens = None
        self.errores = None
        self.ctrl = ctrl
        self.fuente = 'Helvética'

    def iniciar(self):
        self.raiz = tk.Tk()
        self.raiz.title('LFP - Práctica 1')
        self.raiz.resizable(0,0)
        self.raiz.geometry('850x500')
        self.raiz.config(bg = 'white')

        tk.Label(self.raiz,text = 'La Liga Bot',font = (self.fuente, 30),background='#0059b3',foreground = 'white').pack(fill = tk.X)

        self.areatexto = tk.Text(font = (self.fuente,12),borderwidth = 2,fg = '#0060B2')
        self.areatexto.place(width = 500,height = 30,x = 50,y = 400)
        
        enviar = tk.Button(self.raiz,text = 'Enviar',font = (self.fuente,12),borderwidth = 1,bg = '#107C41',fg = 'white',activebackground = '#107C41',activeforeground = 'white',command = self.analizar)
        enviar.place(width = 100,height = 30,x = 570,y = 400)

        self.raiz.mainloop()
    
    def analizar(self):
        contenido = self.areatexto.get('1.0','end').strip()
        if len(contenido) > 0:
            lexico = AnalizadorLexico()
            lexico.analizar(contenido)
            self.tokens = lexico.listaTokens
            self.errores = lexico.listaErrores
            if len(self.tokens) > 0:
                sintactico = AnalizadorSintactico(self.ctrl,lexico.listaTokensC)
                sintactico.analizar()
                sintactico.imprimirErrores()
                self.clear()
            else:
                tk.messagebox.showinfo(message = "Sin tokens detectados",title = "Tokens")
    
    def chooseReport(self):
        reporte = self.combo.get()
        if reporte == 'Manual de Usuario':
            webbrowser.open('Manual De Usuario.pdf')
        elif reporte == 'Manual Técnico':
            webbrowser.open('Manual Técnico.pdf')
        else:
            contenido = self.areatexto.get('1.0','end').strip()
            if len(contenido) > 0:
                if reporte == 'Reporte de Tokens':
                    if self.tokens:
                        '''Reportes().repTokens(self.tokens)'''
                    else:
                        tk.messagebox.showinfo(message = "No se encontraron tokens",title = "Análisis")
                elif reporte == 'Reporte de Errores':
                    if self.errores:
                        '''Reportes().repErrores(self.errores)'''
                    else:
                        tk.messagebox.showinfo(message = "No se encontraron errores",title = "Análisis")
            else:
                tk.messagebox.showinfo(message = "No hay un archivo cargado",title = "Archivo")
    
    def clear(self):
        self.areatexto.delete('1.0','end')