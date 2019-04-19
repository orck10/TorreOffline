import json
from tkinter import *
from functools import partial

class TelaDeResultados:
    def __init__(self, json):
        self.parent = Tk()

        self.resultados = json["resultados"]
        self.idade = json["idade"]

        self.parent.title("Torre de Londres")
        self.parent.geometry("300x200")
        self.testePadrao = ""
        self.movimentos4 = "Alto"
        self.movimentos5 = "Alto"
        
        self.calcular()

        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(self.parent)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.header = Label(self.primeiroContainer, text=json['nome'])
        self.header["font"] = ("Arial", "10", "bold")

        self.resultado1 = Label(self.primeiroContainer, text="Teste Geral - "+self.testePadrao)
        self.resultado1["font"] = self.fontePadrao

        self.resultado2 = Label(self.primeiroContainer, text="Teste 4 movimentos - "+self.movimentos4)
        self.resultado2["font"] = self.fontePadrao

        self.resultado3 = Label(self.primeiroContainer, text="Teste 5 movimentos - "+self.movimentos5)
        self.resultado3["font"] = self.fontePadrao

        self.botao = Button(self.primeiroContainer, width = 20, text="Fechar")
        self.botao["command"] = partial(self.onClick, "Antronalta de Marmore")

        self.espacao = Label(self.primeiroContainer)

        self.header.pack()
        self.resultado1.pack()
        self.resultado2.pack()
        self.resultado3.pack()
        self.espacao.pack()
        self.botao.pack()


    def abrirTela(self):
        self.parent.mainloop() 
        return None

    def calcular(self):
        pontoPadrao = self.calculoPadrao()
        pontoPadrao = self.tabelaPadrao(pontoPadrao)
        self.testePadrao = self.classificaResultado(pontoPadrao) 

        posto4mov = self.calcular4mov()
        print(posto4mov)
        posto4mov = self.tabela4mov(posto4mov)
        self.movimentos4 = self.classificaResultado(posto4mov)

        posto5mov = self.calcular5mov()
        posto5mov = self.tabela5mov(posto5mov)
        self.movimentos5 = self.classificaResultado(posto5mov)

    def classificaResultado(self, pontos):
        if pontos < 70:
            return "Muito Baixo"
        elif pontos < 85 and pontos >= 70:
            return "Baixo"
        elif pontos < 115 and pontos >= 85:
            return "Média"
        elif pontos < 130 and pontos >= 115:
            return "Alto"
        else:
            return "Muito Alto"
    
    def tabela5mov(self, pontos):
        if self.idade == 11:
            if pontos == 1:
                pontos = 69
            elif pontos == 2:
                pontos = 77
            elif pontos == 3:
                pontos = 84
            elif pontos == 4:
                pontos = 92
            elif pontos == 5:
                pontos = 99
            elif pontos == 6:
                pontos = 107
            elif pontos == 7:
                pontos = 115
            elif pontos == 8:
                pontos = 122
            elif pontos == 9:
                pontos = 130
            elif pontos == 10:
                pontos = 137
            elif pontos == 11:
                pontos = 145
            elif pontos == 12:
                pontos = 152
        elif self.idade == 12:
            if pontos == 1:
                pontos = 59
            elif pontos == 2:
                pontos = 67
            elif pontos == 3:
                pontos = 76
            elif pontos == 4:
                pontos = 84
            elif pontos == 5:
                pontos = 93
            elif pontos == 6:
                pontos = 101
            elif pontos == 7:
                pontos = 110
            elif pontos == 8:
                pontos = 118
            elif pontos == 9:
                pontos = 127
            elif pontos == 10:
                pontos = 135
            elif pontos == 11:
                pontos = 144
            elif pontos == 12:
                pontos = 152
        elif self.idade == 13:
            if pontos == 1:
                pontos = 58
            elif pontos == 2:
                pontos = 66
            elif pontos == 3:
                pontos = 74
            elif pontos == 4:
                pontos = 82
            elif pontos == 5:
                pontos = 90
            elif pontos == 6:
                pontos = 98
            elif pontos == 7:
                pontos = 106
            elif pontos == 8:
                pontos = 114
            elif pontos == 9:
                pontos = 122
            elif pontos == 10:
                pontos = 130
            elif pontos == 11:
                pontos = 138
            elif pontos == 12:
                pontos = 146
        elif self.idade == 14:
            if pontos == 1:
                pontos = 71
            elif pontos == 2:
                pontos = 77
            elif pontos == 3:
                pontos = 83
            elif pontos == 4:
                pontos = 90
            elif pontos == 5:
                pontos = 96
            elif pontos == 6:
                pontos = 102
            elif pontos == 7:
                pontos = 108
            elif pontos == 8:
                pontos = 114
            elif pontos == 9:
                pontos = 120
            elif pontos == 10:
                pontos = 126
            elif pontos == 11:
                pontos = 132
            elif pontos == 12:
                pontos = 138
        else:
            if pontos == 1:
                pontos = 7
            elif pontos == 2:
                pontos = 21
            elif pontos == 3:
                pontos = 34
            elif pontos == 4:
                pontos = 47
            elif pontos == 5:
                pontos = 61
            elif pontos == 6:
                pontos = 74
            elif pontos == 7:
                pontos = 88
            elif pontos == 8:
                pontos = 101
            elif pontos == 9:
                pontos = 114
            elif pontos == 10:
                pontos = 128
            elif pontos == 11:
                pontos = 141
            elif pontos == 12:
                pontos = 155
        return pontos

    def tabela4mov(self, pontos):
        if self.idade == 11:
            if pontos == 1:
                pontos = 56
            elif pontos == 2:
                pontos = 64
            elif pontos == 3:
                pontos = 72
            elif pontos == 4:
                pontos = 80
            elif pontos == 5:
                pontos = 89
            elif pontos == 6:
                pontos = 97
            elif pontos == 7:
                pontos = 105
            elif pontos == 8:
                pontos = 113
            elif pontos == 9:
                pontos = 122
            elif pontos == 10:
                pontos = 130
            elif pontos == 11:
                pontos = 138
            elif pontos == 12:
                pontos = 146
        elif self.idade == 12:
            if pontos == 1:
                pontos = 56
            elif pontos == 2:
                pontos = 65
            elif pontos == 3:
                pontos = 73
            elif pontos == 4:
                pontos = 81
            elif pontos == 5:
                pontos = 89
            elif pontos == 6:
                pontos = 97
            elif pontos == 7:
                pontos = 106
            elif pontos == 8:
                pontos = 114
            elif pontos == 9:
                pontos = 122
            elif pontos == 10:
                pontos = 130
            elif pontos == 11:
                pontos = 139
            elif pontos == 12:
                pontos = 147
        elif self.idade == 13:
            if pontos == 1:
                pontos = 44
            elif pontos == 2:
                pontos = 54
            elif pontos == 3:
                pontos = 63
            elif pontos == 4:
                pontos = 73
            elif pontos == 5:
                pontos = 82
            elif pontos == 6:
                pontos = 92
            elif pontos == 7:
                pontos = 101
            elif pontos == 8:
                pontos = 111
            elif pontos == 9:
                pontos = 120
            elif pontos == 10:
                pontos = 129
            elif pontos == 11:
                pontos = 139
            elif pontos == 12:
                pontos = 148
        elif self.idade == 14:
            if pontos == 1:
                pontos = 55
            elif pontos == 2:
                pontos = 62
            elif pontos == 3:
                pontos = 69
            elif pontos == 4:
                pontos = 76
            elif pontos == 5:
                pontos = 84
            elif pontos == 6:
                pontos = 91
            elif pontos == 7:
                pontos = 98
            elif pontos == 8:
                pontos = 106
            elif pontos == 9:
                pontos = 113
            elif pontos == 10:
                pontos = 120
            elif pontos == 11:
                pontos = 127
            elif pontos == 12:
                pontos = 135
        else:
            if pontos == 1:
                pontos = 15
            elif pontos == 2:
                pontos = 15
            elif pontos == 3:
                pontos = 15
            elif pontos == 4:
                pontos = 31
            elif pontos == 5:
                pontos = 47
            elif pontos == 6:
                pontos = 64
            elif pontos == 7:
                pontos = 80
            elif pontos == 8:
                pontos = 96
            elif pontos == 9:
                pontos = 112
            elif pontos == 10:
                pontos = 128
            elif pontos == 11:
                pontos = 144
            elif pontos == 12:
                pontos = 161
        return pontos

    def tabelaPadrao(self, padrao):
        if self.idade == 11:
            if padrao == 9:
                padrao = 3
            elif padrao == 10:
                padrao = 8
            elif padrao == 11:
                padrao = 13
            elif padrao == 12:
                padrao = 18
            elif padrao == 13:
                padrao = 24
            elif padrao == 14:
                padrao = 29
            elif padrao == 15:
                padrao = 34
            elif padrao == 16:
                padrao = 39
            elif padrao == 17:
                padrao = 44
            elif padrao == 18:
                padrao = 50
            elif padrao == 19:
                padrao = 55
            elif padrao == 20:
                padrao = 60
            elif padrao == 21:
                padrao = 65
            elif padrao == 22:
                padrao = 70
            elif padrao == 23:
                padrao = 76
            elif padrao == 24:
                padrao = 81
            elif padrao == 25:
                padrao = 86
            elif padrao == 26:
                padrao = 91
            elif padrao == 27:
                padrao = 96
            elif padrao == 28:
                padrao = 102
            elif padrao == 29:
                padrao = 107
            elif padrao == 30:
                padrao = 112
            elif padrao == 31:
                padrao = 117
            elif padrao == 32:
                padrao = 122
            elif padrao == 33:
                padrao = 128
            elif padrao == 34:
                padrao = 133
            elif padrao == 35:
                padrao = 138
            elif padrao == 36:
                padrao = 143
            else:
                padrao = 3

        elif self.idade == 12:
            if padrao == 13:
                padrao = 4
            elif padrao == 14:
                padrao = 10
            elif padrao == 15:
                padrao = 16
            elif padrao == 16:
                padrao = 22
            elif padrao == 17:
                padrao = 28
            elif padrao == 18:
                padrao = 34
            elif padrao == 19:
                padrao = 40
            elif padrao == 20:
                padrao = 46
            elif padrao == 21:
                padrao = 51
            elif padrao == 22:
                padrao = 57
            elif padrao == 23:
                padrao = 63
            elif padrao == 24:
                padrao = 69
            elif padrao == 25:
                padrao = 75
            elif padrao == 26:
                padrao = 81
            elif padrao == 27:
                padrao = 87
            elif padrao == 28:
                padrao = 93
            elif padrao == 29:
                padrao = 99
            elif padrao == 30:
                padrao = 105
            elif padrao == 31:
                padrao = 111
            elif padrao == 32:
                padrao = 116
            elif padrao == 33:
                padrao = 122
            elif padrao == 34:
                padrao = 128
            elif padrao == 35:
                padrao = 134
            elif padrao == 36:
                padrao = 140
            else:
                padrao = 4
        elif self.idade == 13:
            if padrao == 9:
                padrao = 1
            elif padrao == 10:
                padrao = 6
            elif padrao == 11:
                padrao = 11
            elif padrao == 12:
                padrao = 15
            elif padrao == 13:
                padrao = 20
            elif padrao == 14:
                padrao = 25
            elif padrao == 15:
                padrao = 29
            elif padrao == 16:
                padrao = 34
            elif padrao == 17:
                padrao = 39
            elif padrao == 18:
                padrao = 43
            elif padrao == 19:
                padrao = 48
            elif padrao == 20:
                padrao = 53
            elif padrao == 21:
                padrao = 58
            elif padrao == 22:
                padrao = 62
            elif padrao == 23:
                padrao = 67
            elif padrao == 24:
                padrao = 72
            elif padrao == 25:
                padrao = 76
            elif padrao == 26:
                padrao = 81
            elif padrao == 27:
                padrao = 86
            elif padrao == 28:
                padrao = 90
            elif padrao == 29:
                padrao = 95
            elif padrao == 30:
                padrao = 100
            elif padrao == 31:
                padrao = 104
            elif padrao == 32:
                padrao = 109
            elif padrao == 33:
                padrao = 114
            elif padrao == 34:
                padrao = 118
            elif padrao == 35:
                padrao = 123
            elif padrao == 36:
                padrao = 128
            else:
                padrao = 1
        elif self.idade == 14:
            if padrao == 5:
                padrao = 4
            elif padrao == 6:
                padrao = 8
            elif padrao == 7:
                padrao = 12
            elif padrao == 8:
                padrao = 16
            elif padrao == 9:
                padrao = 20
            elif padrao == 10:
                padrao = 24
            elif padrao == 11:
                padrao = 27
            elif padrao == 12:
                padrao = 31
            elif padrao == 13:
                padrao = 35
            elif padrao == 14:
                padrao = 39
            elif padrao == 15:
                padrao = 43
            elif padrao == 16:
                padrao = 47
            elif padrao == 17:
                padrao = 50
            elif padrao == 18:
                padrao = 54
            elif padrao == 19:
                padrao = 58
            elif padrao == 20:
                padrao = 62
            elif padrao == 21:
                padrao = 66
            elif padrao == 22:
                padrao = 70
            elif padrao == 23:
                padrao = 74
            elif padrao == 24:
                padrao = 77
            elif padrao == 25:
                padrao = 81
            elif padrao == 26:
                padrao = 85
            elif padrao == 27:
                padrao = 89
            elif padrao == 28:
                padrao = 93
            elif padrao == 29:
                padrao = 97
            elif padrao == 30:
                padrao = 100
            elif padrao == 31:
                padrao = 104
            elif padrao == 32:
                padrao = 108
            elif padrao == 33:
                padrao = 112
            elif padrao == 34:
                padrao = 116
            elif padrao == 35:
                padrao = 120
            elif padrao == 36:
                padrao = 123
            else:
                padrao = 4
        else:
            if padrao == 23:
                padrao = 4
            elif padrao == 24:
                padrao = 13
            elif padrao == 25:
                padrao = 22
            elif padrao == 26:
                padrao = 31
            elif padrao == 27:
                padrao = 39
            elif padrao == 28:
                padrao = 48
            elif padrao == 29:
                padrao = 57
            elif padrao == 30:
                padrao = 66
            elif padrao == 31:
                padrao = 75
            elif padrao == 32:
                padrao = 83
            elif padrao == 33:
                padrao = 92
            elif padrao == 34:
                padrao = 101
            elif padrao == 35:
                padrao = 110
            elif padrao == 36:
                padrao = 119
            else:
                padrao = 4
        return padrao
            
    def calculoPadrao(self):
        pontos = 0
        for r in self.resultados:
            if r[1] == 1:
                if r[0] == 1:
                    pontos += 3
                elif r[0] == 2:
                    pontos += 2
                elif r[0] == 3:
                    pontos += 1
            else:
                pontos += 0
        return pontos

    def calcular4mov(self):
        pontos = 0
        for i in range(4, 8, 1):
            if self.resultados[i][1] == 1:
                if self.resultados[i][0] == 1:
                    pontos += 3
                elif self.resultados[i][0] == 2:
                    pontos += 2
                elif self.resultados[i][0] == 3:
                    pontos += 1
        return pontos

    def calcular5mov(self):
        pontos = 0
        for i in range(8, 12, 1):
            if self.resultados[i][1] == 1:
                if self.resultados[i][0] == 1:
                    pontos += 3
                elif self.resultados[i][0] == 2:
                    pontos += 2
                elif self.resultados[i][0] == 3:
                    pontos += 1
        return pontos

    def fecharJanela(self):
        self.parent.destroy()

    def onClick(self, fechar):
        print(fechar)
        self.fecharJanela()