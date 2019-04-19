#appVersao1.1 - Está versão foi retirada as classes BolaVerde, BolaVermelha e BolaRoxa,
#que foram substituidas pela classe Bola que agora recebe como parametro
#uma string com o nome da cor.

import pygame, sys
from pygame.locals import *

largura = 750
altura = 560

coluna1 = 73
coluna2 = 303
coluna3 = 526
fundo = 410
meio = 311
topo = 212

class Bola(pygame.sprite.Sprite):
    def __init__(self, posx, posy, cor):
        pygame.sprite.Sprite.__init__(self)
        self.cor = cor
        self.imagemBola = pygame.image.load('imagens/bolaVerde.png')
        self.imagemBolaSelecionada = pygame.image.load('imagens/bolaVerde.png')

        self.defineCor()

        self.selecao = 0
        self.listaImagens = [self.imagemBola, self.imagemBolaSelecionada]
        self.imagemBola = self.listaImagens[self.selecao]
        
        self.rect = self.imagemBola.get_rect()
        self.rect.top = posy
        self.rect.left = posx

    def defineCor(self):
        if self.cor == 'verde':
            self.imagemBola = pygame.image.load('imagens/bolaVerde.png')
            self.imagemBolaSelecionada = pygame.image.load('imagens/bolaVerdeSelecionada.png')
        if self.cor == 'vermelho':
            self.imagemBola = pygame.image.load('imagens/bolaVermelha.png')
            self.imagemBolaSelecionada = pygame.image.load('imagens/bolaVermelhaSelecianada.png')
        if self.cor == 'roxo':
            self.imagemBola = pygame.image.load('imagens/bolaRoxa.png')
            self.imagemBolaSelecionada = pygame.image.load('imagens/bolaRoxaSelecionada.png')

    def colocar(self, superficie):
        self.imagemBola = self.listaImagens[self.selecao]
        superficie.blit(self.imagemBola, self.rect)

    def comportamento(self):
        if self.selecao == 0:
            self.selecao = 1
        else:
            self.selecao = 0
    def mudaPos(self, x, y):
        self.rect.top = y
        self.rect.left = x

    def retornaX(self):
        return self.rect.left

    def retornaY(self):
        return self.rect.top

    
    
class Seta(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.imagemSeta = pygame.image.load('imagens/seta.png')
        self.imagemSetaSelecionada = pygame.image.load('imagens/setaSelecionada.png')

        self.selecao = 0
        self.listaImagens = [self.imagemSeta, self.imagemSetaSelecionada]
        self.seta = self.listaImagens[self.selecao]

        self.rect = self.seta.get_rect()
        self.rect.top = posy
        self.rect.left = posx

    def colocar(self, superficie):
        self.seta = self.listaImagens[self.selecao]
        superficie.blit(self.seta, self.rect)
    
    def comportamento1(self):            
        self.selecao = 1
        
    def comportamento2(self):
        self.selecao = 0
            
class Torre(object):
    def __init__(self, res1, res2, res3, m, i, f):
        super (Torre, self).__init__()

        self.tela = pygame.display.set_mode((largura, altura))
        self.imagemFundo = pygame.image.load('imagens/imagemfundo.png')
        self.relogio = pygame.time.Clock()
        
        
        self.res1 = res1
        self.res2 = res2
        self.res3 = res3
        self.mov = m
        self.ima = i
        self.fase = f

        self.bola1 = Bola(0,0,'verde')
        self.bola2 = Bola(0,0,'vermelho')
        self.bola3 = Bola(0,0,'roxo')

        self.seta1 = Seta(77 , 105)
        self.seta2 = Seta(307 , 105)
        self.seta3 = Seta(529 , 105)

    def sair(self):
        pygame.quit()
    
    def jogoTorre(self):
        pygame.init()

        tela = self.tela
        imagemFundo = self.imagemFundo
        relogio = self.relogio

        pygame.font.init()
        font_padrao = pygame.font.get_default_font()
        fonte_pontos = pygame.font.SysFont(font_padrao, 30)
        
        bola1 = self.bola1
        bola2 = self.bola2
        bola3 = self.bola3

        col1 = [bola1, bola2]
        col2 = [bola3]
        col3 = []

        seta1 = self.seta1
        seta2 = self.seta2
        seta3 = self.seta3

        movimentos = 0
        selBola = 0
        verifica = 0

        while movimentos <= self.mov:
            relogio.tick(60)

            tempo = float(pygame.time.get_ticks()/1000)

            for b in col1:
                x = col1.index(b)
                if x == 0:
                    b.mudaPos(coluna1, fundo)
                if x == 1:
                    b.mudaPos(coluna1, meio)
                if x == 2:
                    b.mudaPos(coluna1, topo)

            for b in col2:
                x = col2.index(b)
                if x == 0:
                    b.mudaPos(coluna2, fundo)
                if x == 1:
                    b.mudaPos(coluna2, meio)
            for b in col3:
                x = col3.index(b)
                if x == 0:
                    b.mudaPos(coluna3, fundo)    

            posBo1 = [bola1.retornaX(), bola1.retornaY()]
            posBo2 = [bola2.retornaX(), bola2.retornaY()]
            posBo3 = [bola3.retornaX(), bola3.retornaY()]
            
            
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    sys.exit()

                posMouse = pygame.mouse.get_pos()

                if evento.type == MOUSEBUTTONDOWN:
                    
                    if (posMouse[0] > posBo1[0]) and (posMouse[0] < posBo1[0] + 94) and (posMouse[1] > posBo1[1]) and (posMouse[1] < posBo1[1] + 99):
                        if bola1 in col1:
                            if col1.index(bola1) >= len(col1)-1:
                                bola1.comportamento()
                                selBola = bola1
                        if bola1 in col2:
                            if col2.index(bola1) >= len(col2)-1:
                                bola1.comportamento()
                                selBola = bola1
                        if bola1 in col3:
                            bola1.comportamento()
                            selBola = bola1

                    posMouse = pygame.mouse.get_pos()
                    if (posMouse[0] > posBo2[0]) and (posMouse[0] < posBo2[0] + 94) and (posMouse[1] > posBo2[1]) and (posMouse[1] < posBo2[1] + 99):
                        if bola2 in col1:
                            if col1.index(bola2) >= len(col1)-1:
                                bola2.comportamento()
                                selBola = bola2
                        if bola2 in col2:
                            if col2.index(bola2) >= len(col2)-1:
                                bola2.comportamento()
                                selBola = bola2
                        if bola2 in col3:
                            bola2.comportamento()
                            selBola = bola2

                    posMouse = pygame.mouse.get_pos()
                    if (posMouse[0] > posBo3[0]) and (posMouse[0] < posBo3[0] + 94) and (posMouse[1] > posBo3[1]) and (posMouse[1] < posBo3[1] + 99):
                        if bola3 in col1:
                            if col1.index(bola3) >= len(col1)-1:
                                bola3.comportamento()
                                selBola = bola3
                        if bola3 in col2:
                            if col2.index(bola3) >= len(col2)-1:
                                bola3.comportamento()
                                selBola = bola3
                        if bola3 in col3:
                            bola3.comportamento()
                            selBola = bola3
                            
                    if (posMouse[0] > 77) and (posMouse[0] < 162) and (posMouse[1] > 105) and (posMouse[1] < 186):
                        if selBola != 0 and selBola in col2:
                            col2.remove(selBola)
                            col1.append(selBola)
                            movimentos = movimentos + 1

                        if selBola != 0 and selBola in col3:
                            col3.remove(selBola)
                            col1.append(selBola)
                            movimentos = movimentos + 1
                            
                        if selBola != 0 :
                            selBola.comportamento()
                            selBola = 0
                            
                    if (posMouse[0] > 307) and (posMouse[0] < 392) and (posMouse[1] > 105) and (posMouse[1] < 186):
                        if selBola != 0 and selBola in col1 and len(col2) < 2:
                            col1.remove(selBola)
                            col2.append(selBola)
                            movimentos = movimentos + 1

                        if selBola != 0 and selBola in col3 and len(col2) < 2:
                            col3.remove(selBola)
                            col2.append(selBola)
                            movimentos = movimentos + 1

                        if selBola != 0 :
                            selBola.comportamento()
                            selBola = 0

                    if (posMouse[0] > 529) and (posMouse[0] < 614) and (posMouse[1] > 105) and (posMouse[1] < 186):
                        if selBola != 0 and selBola in col1 and len(col3) < 1:
                            col1.remove(selBola)
                            col3.append(selBola)
                            movimentos = movimentos + 1

                        if selBola != 0 and selBola in col2 and len(col3) < 1:
                            col2.remove(selBola)
                            col3.append(selBola)
                            movimentos = movimentos + 1

                        if selBola != 0 :
                            selBola.comportamento()
                            selBola = 0

                #seleção setas
                if (posMouse[0] > 77) and (posMouse[0] < 162) and (posMouse[1] > 105) and (posMouse[1] < 186):
                    seta1.comportamento1()

                if not((posMouse[0] > 77) and (posMouse[0] < 162) and (posMouse[1] > 105) and (posMouse[1] < 186)):
                    seta1.comportamento2()

                if (posMouse[0] > 307) and (posMouse[0] < 392) and (posMouse[1] > 105) and (posMouse[1] < 186):
                    seta2.comportamento1()

                if not((posMouse[0] > 307) and (posMouse[0] < 392) and (posMouse[1] > 105) and (posMouse[1] < 186)):
                    seta2.comportamento2()

                if (posMouse[0] > 529) and (posMouse[0] < 614) and (posMouse[1] > 105) and (posMouse[1] < 186):
                    seta3.comportamento1()

                if not((posMouse[0] > 529) and (posMouse[0] < 614) and (posMouse[1] > 105) and (posMouse[1] < 186)):
                    seta3.comportamento2()
                    
                
            tela.blit(imagemFundo, (0,0))
            tela.blit(self.ima, (5, 5))
            seta1.colocar(tela)
            seta2.colocar(tela)
            seta3.colocar(tela)

            bola1.colocar(tela)
            bola2.colocar(tela)
            bola3.colocar(tela)
            
            testo = fonte_pontos.render('Fase: '+ self.fase,1,(255, 255, 255))
            testo1 = fonte_pontos.render('Movimentos: '+str(self.mov),1,(255, 255, 255))
            testo2 = fonte_pontos.render('Realizados: '+str(movimentos),1,(255, 255, 255))

            tela.blit(testo, (300, 20))
            tela.blit(testo1, (500, 20))
            tela.blit(testo2, (500, 40))

            pygame.display.update()            

            
            if bola1.retornaX() == self.res1.retornaX() and bola1.retornaY() == self.res1.retornaY() and bola2.retornaX() == self.res2.retornaX() and bola2.retornaY() == self.res2.retornaY() and bola3.retornaX() == self.res3.retornaX() and bola3.retornaY() == self.res3.retornaY():
                return 1
            if verifica == 1 :
                return 0
            if movimentos == self.mov:
                verifica = 1
            
        
