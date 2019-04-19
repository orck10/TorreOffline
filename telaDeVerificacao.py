from tkinter import *

class TelaDeVerificacao:
    def __init__(self,str):
        super(TelaDeVerificacao, self).__init__()

        self.root = Tk()
        self.root.title("Tela de Seleção")
        self.root.geometry("400x300")

        self.espacao = Label(self.root)
        self.espacao1 = Label(self.root)
        self.espacao2 = Label(self.root)
        self.espacao3 = Label(self.root)

        self.texto = Label(self.root, text="Deseja Fazer o Teste em:")
        self.texto["font"] = ("Arial", "10", "bold")
        self.texto1 = Label(self.root, text=str)
        self.texto1["font"] = ("Arial", "12", "bold")
        self.texto2 = Label(self.root, text="Após iniciar o Teste ele \nsó será Salvo após todas as Fases Comcluidas")
        self.texto2["font"] = ("Arial", "10", "bold")
        
        
        botao = Button(self.root, width = 20, text="Sim")
        botao["command"] = self.onClickS

        botao1 = Button(self.root, width = 20, text="Não")
        botao1["command"] = self.onClickN

        self.espacao.pack()
        self.espacao1.pack()
        self.espacao2.pack()
        self.texto.pack()
        self.texto1.pack()
        self.texto2.pack()
        self.espacao3.pack()
        botao.pack()
        botao1.pack()
            
    def abrirTela(self):
        self.retorno = None
        self.root.mainloop()
        return self.retorno
    
    def fecharJanela(self):
        self.root.destroy()

    def onClickS(self):
        self.fecharJanela()
        self.retorno = True
    
    def onClickN(self):
        self.retorno = False
        self.fecharJanela()
        
