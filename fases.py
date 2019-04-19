#Classe que implementa a respostas das fases dos testes
from pygame.locals import *

from torre import *

class Fases(object):
    def __init__(self):
        pass
    
    def faseExemplo(self):
        b1 = Bola(coluna1, fundo,'verde')
        b2 = Bola(coluna3, fundo, 'vermelha')
        b3 = Bola(coluna1, meio, 'roxo')
        i = pygame.image.load('imagens/imagemexemplo.png')
        return (b1, b2, b3, 2, i, 'Exemplo')

    def fase1(self):
        b1 = Bola(coluna2, meio,'verde')
        b2 = Bola(coluna3, fundo, 'vermelha')
        b3 = Bola(coluna2, fundo, 'roxo')
        i = pygame.image.load('imagens/fase1.png')
        return (b1, b2, b3, 2, i, '1')

    def fase2(self):
        b1 = Bola(coluna1, fundo,'verde')
        b2 = Bola(coluna2, fundo, 'vermelha')
        b3 = Bola(coluna3, fundo, 'roxo')
        i = pygame.image.load('imagens/fase2.png')
        return (b1, b2, b3, 2, i, '2')

    def fase3(self):
        b1 = Bola(coluna1, fundo,'verde')
        b2 = Bola(coluna2, fundo, 'vermelha')
        b3 = Bola(coluna1, meio, 'roxo')
        i = pygame.image.load('imagens/fase3.png')
        return (b1, b2, b3, 3, i, '3')

    def fase4(self):
        b1 = Bola(coluna1, fundo,'verde')
        b2 = Bola(coluna2, fundo, 'vermelha')
        b3 = Bola(coluna2, meio, 'roxo')
        i = pygame.image.load('imagens/fase4.png')
        return (b1, b2, b3, 3, i, '4')

    def fase5(self):
        b1 = Bola(coluna1, meio,'verde')
        b2 = Bola(coluna1, fundo, 'vermelha')
        b3 = Bola(coluna2, fundo, 'roxo')
        i = pygame.image.load('imagens/fase5.png')
        return (b1, b2, b3, 4, i, '5')

    def fase6(self):
        b1 = Bola(coluna2, meio,'verde')
        b2 = Bola(coluna2, fundo, 'vermelha')
        b3 = Bola(coluna1, fundo, 'roxo')
        i = pygame.image.load('imagens/fase6.png')
        return (b1, b2, b3, 4, i, '6')

    def fase7(self):
        b1 = Bola(coluna3, fundo,'verde')
        b2 = Bola(coluna1, fundo, 'vermelha')
        b3 = Bola(coluna1, meio, 'roxo')
        i = pygame.image.load('imagens/fase7.png')
        return (b1, b2, b3, 4, i, '7')

    def fase8(self):
        b1 = Bola(coluna3, fundo,'verde')
        b2 = Bola(coluna2, fundo, 'vermelha')
        b3 = Bola(coluna2, meio, 'roxo')
        i = pygame.image.load('imagens/fase8.png')
        return (b1, b2, b3, 4, i, '8')

    def fase9(self):
        b1 = Bola(coluna1, meio,'verde')
        b2 = Bola(coluna1, fundo, 'vermelha')
        b3 = Bola(coluna1, topo, 'roxo')
        i = pygame.image.load('imagens/fase9.png')
        return (b1, b2, b3, 5, i, '9')
    
    def fase10(self):
        b1 = Bola(coluna1, topo,'verde')
        b2 = Bola(coluna1, fundo, 'vermelha')
        b3 = Bola(coluna1, meio, 'roxo')
        i = pygame.image.load('imagens/fase10.png')
        return (b1, b2, b3, 5, i, '10')

    def fase11(self):
        b1 = Bola(coluna1, meio,'verde')
        b2 = Bola(coluna2, fundo, 'vermelha')
        b3 = Bola(coluna1, fundo, 'roxo')
        i = pygame.image.load('imagens/fase11.png')
        return (b1, b2, b3, 5, i, '11')

    def fase12(self):
        b1 = Bola(coluna3, fundo,'verde')
        b2 = Bola(coluna2, fundo, 'vermelha')
        b3 = Bola(coluna1, fundo, 'roxo')
        i = pygame.image.load('imagens/fase12.png')
        return (b1, b2, b3, 5, i, '12')

    def telaDeFechamento(self):
        return ("Fim doTeste e o Usuario será deslogado.")
