import json

from tkinter import *
from functools import partial
from telaDeResultados import *

class TelaDeSelecao:
    def __init__(self, jsonBase,master=None):
        super(TelaDeSelecao, self).__init__()
        
        self.parent = Tk()
        master = self.parent

        self.parent.title("Torre de Londres")
        self.parent.geometry("800x600")

        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
  
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
  
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.header1 = Label(self.primeiroContainer, text="Novo paciente")
        self.header1["font"] = ("Arial", "10", "bold")

        self.titulo = Label(self.primeiroContainer, text="Nome do Paciente (obrigatorio)")
        self.titulo["font"] = ("Arial", "10")
        self.titulo1 = Label(self.primeiroContainer, text="Idade do Paciente (obrigatorio, somente números inteiros)")
        self.titulo1["font"] = ("Arial", "10")

        self.nome = Entry(self.primeiroContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        
        self.idade = Entry(self.primeiroContainer)
        self.idade["width"] = 30
        self.idade["font"] = self.fontePadrao

        self.botaoIniciar = Button(self.primeiroContainer, width = 20, text="Iniciar Teste")
        self.botaoIniciar["command"] = partial(self.iniciarTeste)
        

        self.titulo2 = Label(self.segundoContainer, text="Resultado de Testes Anteriores")
        self.titulo2["font"] = ("Arial", "10", "bold")

        self.espacao = Label(self.primeiroContainer)
        self.espacao1 = Label(self.primeiroContainer)
        self.espacao2 = Label(self.segundoContainer)

        self.botoes = []

        for p in jsonBase:
            nome = p['nome']
            botao = Button(self.segundoContainer, width = 20, text=nome)
            botao["command"] = partial(self.onClick, nome, p)
            self.botoes.append(botao)
        

        self.header1.pack()
        self.espacao.pack()
        self.titulo.pack()
        self.nome.pack()
        self.titulo1.pack()
        self.idade.pack()
        self.espacao1.pack()
        self.botaoIniciar.pack()
        self.espacao2.pack()
        self.titulo2.pack()
        for b in self.botoes:
            b.pack()

    def abrirTela(self):
        self.retorno = []
        self.parent.mainloop()   
        return self.retorno
        
        
    def fecharJanela(self):
        self.parent.destroy()

    def iniciarTeste(self):
        if(self.nome.get() != ""):
            try:
                idade = int(self.idade.get())
            except ValueError:
                print("NAN")
            if(isinstance(idade, int) and (idade >= 11)):
                self.retorno.append(self.nome.get())
                self.retorno.append(idade)
                print(self.retorno)
                self.fecharJanela()
    
    def onClick(self, nome, row):
        print(row)
        TelaDeResultados(row).abrirTela()

