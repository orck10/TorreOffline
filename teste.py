from tkinter import *
from telaDeLogin import *
from telaDeTeste import *
from baseJson import *
import json


def main():   

    root = Tk()
    base = BaseJson()
    usuario = TelaDeSelecao(root,base.getAllPacientes())
    nome = usuario.abrirTela() 
    print(nome)

    
'''
def main():
    with open('testesSalvos/Usuarios.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(' '.join(row))
'''
'''
def main():
    base = BaseJson()
    paciente = {"nome":"Jorge", "fases":[1,1,1,1]}
    base.salvarPaciente(paciente) 
'''


main()
