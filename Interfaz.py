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

        repErr = tk.Button(self,text = 'Reporte de Errores',bg = '#1CB49C',fg = 'white',activebackground = '#1A9E8A',activeforeground = 'white',font='lucida 11 bold',borderwidth = 0)
        repErr.place(width = 180,height = 30,x = 670,y = 100)

        clLErr = tk.Button(self,text = 'Limpiar Log de Errores',bg = '#1CB49C',fg = 'white',activebackground = '#1A9E8A',activeforeground = 'white',font='lucida 11 bold',borderwidth = 0)
        clLErr.place(width = 180,height = 30,x = 670,y = 140)

        repTkn = tk.Button(self,text = 'Reporte de Tokens',bg = '#1CB49C',fg = 'white',activebackground = '#1A9E8A',activeforeground = 'white',font='lucida 11 bold',borderwidth = 0)
        repTkn.place(width = 180,height = 30,x = 670,y = 180)

        clLTkn = tk.Button(self,text = 'Limpiar Log de Tokens',bg = '#1CB49C',fg = 'white',activebackground = '#1A9E8A',activeforeground = 'white',font='lucida 11 bold',borderwidth = 0)
        clLTkn.place(width = 180,height = 30,x = 670,y = 220)

        mnlUsr = tk.Button(self,text = 'Manual de Usuario',bg = '#1CB49C',fg = 'white',activebackground = '#1A9E8A',activeforeground = 'white',font='lucida 11 bold',borderwidth = 0)
        mnlUsr.place(width = 180,height = 30,x = 670,y = 260)

        mnlTcn = tk.Button(self,text = 'Manual Técnico',bg = '#1CB49C',fg = 'white',activebackground = '#1A9E8A',activeforeground = 'white',font='lucida 11 bold',borderwidth = 0)
        mnlTcn.place(width = 180,height = 30,x = 670,y = 300)

        self.mensajeNuevo = tk.Text(self,font = 'lucida 10',highlightcolor = 'blue',highlightthickness = 0)
        self.mensajeNuevo.place(width = 600,height = 30,x = 50, y = 520)
        self.mensajeNuevo.focus_set()

        enviar = tk.Button(self,text = 'Enviar',bg = '#1CB49C',fg = 'white',activebackground = '#1A9E8A',activeforeground = 'white',font='lucida 11 bold',borderwidth = 0)
        enviar.place(width = 180,height = 30,x = 670,y = 520)

        frameContacto = tk.Frame(self.frameScroll,bg = '#d9d5d4')

        hora = tk.Label(frameContacto,bg='#d9d5d4',text=datetime.now().strftime('%H:%M'),font='lucida 9 bold')
        hora.pack()

        contacto = tk.Label(frameContacto,wraplength = 450,text = 'La Liga Bot Chat',font = 'lucida 10 bold',bg = 'orange')
        contacto.pack(fill = 'x')

        frameContacto.pack(pady = 15,padx = 15,fill = 'x',expand = True,anchor = 'e')

        self.pack(fill = 'both',expand = True)