import tkinter as tk
import time
from PIL import Image,ImageTk
from tkinter import ttk
from datetime import datetime
from AnalizadorLexico import AnalizadorLexico
from AnalizadorSintactico import AnalizadorSintactico
from Controlador import Ctrl
from Lector import Lector
from Reportes import Reportes

class Inicio:
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

        self.inicializar()

        self.framePrincipal = framePrincipal
        self.framePrincipal.pack_forget()

        self.raiz = raiz
        self.raiz.geometry('900x600')

        global imagenes
        imagenes = Image.open('images/laligalogo.png')
        imagenes = imagenes.resize((60,60),Image.ANTIALIAS)
        imagenes = ImageTk.PhotoImage(imagenes)

        self.create_image(82,51,image = imagenes)

        tk.Label(self,font = 'lucida 15 bold',bg = '#0060B2').place(width = 50,height = 30,x = 2, y = 40)
        tk.Label(self,text = 'La Liga Bot',font = 'lucida 15 bold',padx = 20, fg = 'white',bg = '#0060B2',anchor = 'w',justify = 'left').place(width = 786,height = 30,x = 112, y = 40)

        contenedor = tk.Frame(self)
        contenedor.place(x = 50,y = 100,width = 600,height = 400)

        self.canvas = tk.Canvas(contenedor,bg = '#131B21')
        self.frameScroll = tk.Frame(self.canvas,bg = '#131B21')

        scroll = self.canvas.create_window((0,0),window = self.frameScroll,anchor='nw')

        def configuracionFrameScroll(e):
            self.canvas.configure(scrollregion = self.canvas.bbox('all'))

        def redimensionFrame(e):
            self.canvas.itemconfig(scroll,width = e.width)

        self.frameScroll.bind('<Configure>',configuracionFrameScroll)

        scrollbar = ttk.Scrollbar(contenedor,orient = 'vertical',command=self.canvas.yview)
        self.canvas.configure(yscrollcommand = scrollbar.set)
        self.yview_moveto(1.0)

        scrollbar.pack(side = 'right',fill = 'y')

        self.canvas.bind('<Configure>',redimensionFrame)
        self.canvas.pack(fill = 'both',expand = True)

        repErr = tk.Button(self,text = 'Reporte de Errores',bg = '#1CB49C',fg = 'white',activebackground = '#1A9E8A',activeforeground = 'white',font='lucida 11 bold',borderwidth = 0,command = self.reporteError)
        repErr.place(width = 180,height = 30,x = 670,y = 100)

        clLErr = tk.Button(self,text = 'Limpiar Log de Errores',bg = '#1CB49C',fg = 'white',activebackground = '#1A9E8A',activeforeground = 'white',font='lucida 11 bold',borderwidth = 0,command = self.clearLogError)
        clLErr.place(width = 180,height = 30,x = 670,y = 140)

        repTkn = tk.Button(self,text = 'Reporte de Tokens',bg = '#1CB49C',fg = 'white',activebackground = '#1A9E8A',activeforeground = 'white',font='lucida 11 bold',borderwidth = 0,command = self.reporteToken)
        repTkn.place(width = 180,height = 30,x = 670,y = 180)

        clLTkn = tk.Button(self,text = 'Limpiar Log de Tokens',bg = '#1CB49C',fg = 'white',activebackground = '#1A9E8A',activeforeground = 'white',font='lucida 11 bold',borderwidth = 0,command = self.clearLogToken)
        clLTkn.place(width = 180,height = 30,x = 670,y = 220)

        mnlUsr = tk.Button(self,text = 'Manual de Usuario',bg = '#1CB49C',fg = 'white',activebackground = '#1A9E8A',activeforeground = 'white',font='lucida 11 bold',borderwidth = 0)
        mnlUsr.place(width = 180,height = 30,x = 670,y = 260)

        mnlTcn = tk.Button(self,text = 'Manual Técnico',bg = '#1CB49C',fg = 'white',activebackground = '#1A9E8A',activeforeground = 'white',font='lucida 11 bold',borderwidth = 0)
        mnlTcn.place(width = 180,height = 30,x = 670,y = 300)

        self.mensajeNuevo = tk.Text(self,font = 'lucida 10',highlightcolor = 'blue',highlightthickness = 0)
        self.mensajeNuevo.place(width = 600,height = 30,x = 50, y = 520)
        self.mensajeNuevo.focus_set()

        enviar = tk.Button(self,text = 'Enviar',bg = '#1CB49C',fg = 'white',activebackground = '#1A9E8A',activeforeground = 'white',font='lucida 11 bold',borderwidth = 0,command = self.envioMensaje)
        enviar.place(width = 180,height = 30,x = 670,y = 520)

        frameContacto = tk.Frame(self.frameScroll,bg = '#d9d5d4')

        hora = tk.Label(frameContacto,bg='#d9d5d4',text=datetime.now().strftime('%H:%M'),font='lucida 9 bold')
        hora.pack()

        contacto = tk.Label(frameContacto,wraplength = 450,text = 'La Liga Bot Chat',font = 'lucida 10 bold',bg = 'orange')
        contacto.pack(fill = 'x')

        frameContacto.pack(pady = 15,padx = 15,fill = 'x',expand = True,anchor = 'e')

        self.bienvenidaBot()

        self.pack(fill = 'both',expand = True)

    def envioMensaje(self):
        mensaje = self.mensajeNuevo.get('1.0','end-1c')
        if mensaje:
            self.mensajeNuevo.delete('1.0','end-1c')
            
            frameMensaje = tk.Frame(self.frameScroll,bg = '#131B21')
            frameMensaje.columnconfigure(0,weight = 1)

            mensajeEnviado = tk.Label(frameMensaje,wraplength = 450,text = mensaje,fg = 'white',bg = '#005C4B',font = 'lucida 9 bold',justify = 'left',anchor = 'e',padx = 5,pady = 5)
            mensajeEnviado.grid(row = 0,column = 0,padx = 2,sticky = 'e')

            hora = tk.Label(frameMensaje,bg = '#131B21',fg = 'white',text = datetime.now().strftime('%H:%M'),font = 'lucida 7 bold',justify = 'right',anchor = 'e',padx = 5)
            hora.grid(row = 1,column = 0,padx = 2,sticky = 'e')

            frameMensaje.pack(padx = 10,pady = 5,fill = 'x',expand = True,anchor = 'e')

            self.canvas.update_idletasks()
            self.canvas.yview_moveto(1.0)

            self.analizar(mensaje)
            self.reciboMensaje(self.respuesta)

    def reciboMensaje(self,mensaje):
        frameMensaje = tk.Frame(self.frameScroll,bg = '#131B21')
        frameMensaje.columnconfigure(1,weight = 1)

        mensajeRecibido = tk.Label(frameMensaje,wraplength = 450,fg = 'white',bg = '#202C33',text = mensaje,font = 'lucida 9 bold',justify = 'left',anchor = 'w',padx = 5,pady = 5)
        mensajeRecibido.grid(row = 0,column = 1,padx = 2,sticky = 'w')

        hora = tk.Label(frameMensaje,bg = '#131B21',fg = 'white',text = datetime.now().strftime('%H:%M'),font = 'lucida 7 bold',justify = 'left',anchor = 'w',padx = 5)
        hora.grid(row = 1,column = 1,padx = 2,sticky = 'w')

        frameMensaje.pack(padx = 10,pady = 5,fill = 'x',expand = True,anchor = 'e')
        self.canvas.update_idletasks()
        self.canvas.yview_moveto(1.0)

        if mensaje == 'ADIOS':
            for i in range(10):
                time.sleep(0.1)
            quit()

    def inicializar(self):
        leer = Lector()
        base_datos = leer.leer()
        self.ctrl = Ctrl(base_datos)

        self.lexico = AnalizadorLexico()
        self.tokens = []
        self.erroresL = []
        self.erroresS = []

    def analizar(self,comando):
        self.lexico.analizar(comando)
        self.tokens = self.lexico.listaTokens
        self.erroresL = self.lexico.listaErrores
        sintactico = AnalizadorSintactico(self.ctrl,self.lexico.listaTokensC)
        sintactico.analizar()
        self.respuesta = sintactico.respuesta
        self.addSintaxErrors(sintactico.listaErrores)

    def reporteToken(self):
        Reportes().repTokens(self.tokens)

    def clearLogToken(self):
        self.lexico.limpiarTokens()
        self.tokens = []

    def reporteError(self):
        Reportes().repErrores(self.erroresL,self.erroresS)

    def clearLogError(self):
        self.lexico.limpiarErrores()
        self.erroresL = []
        self.erroresS = []

    def addSintaxErrors(self,errores):
        for error in errores:
            self.erroresS.append(error)

    def bienvenidaBot(self):
        self.reciboMensaje('Hola soy La Liga Bot\nPregúntame lo que sea de La Liga')