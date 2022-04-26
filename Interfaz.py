import tkinter as tk
from PIL import Image,ImageTk
from tkinter import image_names, ttk
from datetime import datetime
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

    def iniciar(self):
        Raiz()

class Raiz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.resizable(0,0)
        self.framePrincipal = tk.Frame(self)
        self.framePrincipal.pack()
        Chat(self,self.framePrincipal)
        self.mainloop()

class Chat(tk.Canvas):
    def __init__(self,raiz : tk.Tk,framePrincipal : tk.Frame):
        super().__init__(raiz,bg = '#202C33')

        self.framePrincipal = framePrincipal
        self.framePrincipal.pack_forget()

        self.raiz = raiz
        self.raiz.geometry('900x600')