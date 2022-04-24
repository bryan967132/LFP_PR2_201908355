import webbrowser
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

from regex import I
from AnalizadorLexico import AnalizadorLexico
from AnalizadorSintactico import AnalizadorSintactico
from Controlador import Ctrl

class Inicio:
    def __init__(self,ctrl : Ctrl):
        self.lexico = AnalizadorLexico()
        self.tokens = []
        self.erroresL = []
        self.erroresS = []
        self.ctrl = ctrl
        self.fuente = 'Helvética'

    def iniciar(self):
        self.raiz = tk.Tk()
        self.raiz.title('LFP - Práctica 1')
        self.raiz.resizable(0,0)
        self.raiz.geometry('900x600')
        self.raiz.config(bg = '#131B21')

        tk.Label(self.raiz,text = 'La Liga Bot',font = (self.fuente, 30),background='#202C33',foreground = 'white').pack(fill = tk.X)

        w = 180
        h = 30
        i = 670
        sizeFont = 10

        repErr = tk.Button(self.raiz,text = 'Reporte de Errores',font = (self.fuente,sizeFont),borderwidth = 1,bg = '#1CB49C',fg = 'white',activebackground = '#1A9E8A',activeforeground = 'white',command = self.sendReportError)
        repErr.place(width = w,height = h,x = i,y = 100)

        clLErr = tk.Button(self.raiz,text = 'Limpiar Log de Errores',font = (self.fuente,sizeFont),borderwidth = 1,bg = '#1CB49C',fg = 'white',activebackground = '#1A9E8A',activeforeground = 'white',command = self.clearLogError)
        clLErr.place(width = w,height = h,x = i,y = 140)

        repTkn = tk.Button(self.raiz,text = 'Reporte de Tokens',font = (self.fuente,sizeFont),borderwidth = 1,bg = '#1CB49C',fg = 'white',activebackground = '#1A9E8A',activeforeground = 'white',command = self.sendReportToken)
        repTkn.place(width = w,height = h,x = i,y = 180)

        clLTkn = tk.Button(self.raiz,text = 'Limpiar Log de Tokens',font = (self.fuente,sizeFont),borderwidth = 1,bg = '#1CB49C',fg = 'white',activebackground = '#1A9E8A',activeforeground = 'white',command = self.clearLogToken)
        clLTkn.place(width = w,height = h,x = i,y = 220)

        mnlUsr = tk.Button(self.raiz,text = 'Manual de Usuario',font = (self.fuente,sizeFont),borderwidth = 1,bg = '#1CB49C',fg = 'white',activebackground = '#1A9E8A',activeforeground = 'white',command = self.openMnlUsr)
        mnlUsr.place(width = w,height = h,x = i,y = 260)

        mnlUsr = tk.Button(self.raiz,text = 'Manual Técnico',font = (self.fuente,sizeFont),borderwidth = 1,bg = '#1CB49C',fg = 'white',activebackground = '#1A9E8A',activeforeground = 'white',command = self.openMnlTcn)
        mnlUsr.place(width = w,height = h,x = i,y = 300)

        self.areatexto = tk.Text(font = (self.fuente,sizeFont),borderwidth = 2,fg = '#0060B2')
        self.areatexto.place(width = 600,height = 30,x = 50,y = 520)
        
        enviar = tk.Button(self.raiz,text = 'Enviar',font = (self.fuente,sizeFont),borderwidth = 1,bg = '#1CB49C',fg = 'white',activebackground = '#1A9E8A',activeforeground = 'white',command = self.analizar)
        enviar.place(width = w,height = h,x = i,y = 520)

        self.raiz.mainloop()
    
    def analizar(self):
        contenido = self.areatexto.get('1.0','end').strip()
        if len(contenido) > 0:
            self.lexico.analizar(contenido)
            self.tokens = self.lexico.listaTokens
            self.erroresL = self.lexico.listaErrores
            if len(self.tokens) > 0:
                self.lexico.imprimirTokens()
                sintactico = AnalizadorSintactico(self.ctrl,self.lexico.listaTokensC)
                sintactico.analizar()
                sintactico.imprimirErrores()
                self.addSintaxErrors(sintactico.listaErrores)
                self.clear()
            else:
                tk.messagebox.showinfo(message = "Sin tokens detectados",title = "Tokens")

    def sendReportError(self):
        if len(self.erroresL) > 0 and len(self.erroresS) > 0:
            '''Reportes().repTokens(self.tokens)'''
        else:
            tk.messagebox.showinfo(message = "No hay errores reconocidos",title = "Errores")

    def clearLogError(self):
        self.lexico.limpiarErrores()
        self.erroresS = []

    def sendReportToken(self):
        if len(self.tokens) > 0:
            '''Reportes().repTokens(self.tokens)'''
        else:
            tk.messagebox.showinfo(message = "No hay tokens reconocidos",title = "Tokens")

    def clearLogToken(self):
        self.lexico.limpiarTokens()

    def openMnlUsr(self):
        webbrowser.open('Manual de Usuario.pdf')
    
    def openMnlTcn(self):
        webbrowser.open('Manual Técnico.pdf')

    def addSintaxErrors(self,errores):
        for error in errores:
            self.erroresS.append(error)
    

    def clear(self):
        self.areatexto.delete('1.0','end')