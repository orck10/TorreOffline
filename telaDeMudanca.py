import pygame, sys
from pygame.locals import *

largura = 750
altura = 560

class Tela(object):
    def __init__(self, f):
        super(Tela, self).__init__()

        self.tela = pygame.display.set_mode((largura, altura))
        self.imagemFundo = pygame.image.load('imagens/imagemfundo2.png')
        self.relogio = pygame.time.Clock()

        self.fase = f

    def sair(self):
        pygame.quit()

    def telaDeMudanca(self):
        pygame.init()

        tela = self.tela
        imagemFundo = self.imagemFundo
        relogio = self. relogio

        pygame.font.init()
        font_padrao = pygame.font.get_default_font()
        fonte_texto = pygame.font.SysFont(font_padrao, 50)

        temp = 0

        while temp == 0:
            relogio.tick(60)

            tempo = float(pygame.time.get_ticks()/1000)

            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == MOUSEBUTTONDOWN:
                    temp = 1
                    
            tela.blit(imagemFundo, (0,0))

            testo = fonte_texto.render('Fase: '+ self.fase,1,(255, 255, 255))
            xDotexto = 300
            testo2 = fonte_texto.render('Clique para continuar',1,(255, 255, 255))
            if self.fase == "Fim doTeste e o Usuario será deslogado.":
                testo = fonte_texto.render( self.fase,1,(255, 255, 255))
                xDotexto = 30

            tela.blit(testo, (xDotexto, 20))
            tela.blit(testo2, (210, 55))
            
            pygame.display. update()

        
