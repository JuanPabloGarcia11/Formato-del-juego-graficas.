import pygame
import sys
import random
from pygame.locals import *
from pygame import gfxdraw

import time


# Definir algunos colores
NEGRO  = (  0,   0,   0)
BLANCO = (255, 255, 255)
VERDE  = (0,   255,   0)
ROJO   = (255,   0,   0)
AMARILLO = (255,255,0)

ANCHO=800
ALTO=600
dimensiones=(700,400)


class Opcion:

    def __init__(self, fuente, titulo, x, y, paridad, funcion_asignada):
        self.imagen_normal = fuente.render(titulo, 1, (255, 255, 255))
        self.imagen_destacada = fuente.render(titulo, 1, (255, 255, 255))
        self.image = self.imagen_normal
        self.rect = self.image.get_rect()
        self.rect.x = 500 * paridad
        self.rect.y = y
        self.funcion_asignada = funcion_asignada
        self.x = float(self.rect.x)

    def actualizar(self):
        destino_x = 105
        self.x += (destino_x - self.x) / 5.0
        self.rect.x = int(self.x)

    def imprimir(self, pantalla):
        pantalla.blit(self.image, self.rect)

    def destacar(self, estado):
        if estado:
            self.image = self.imagen_destacada
        else:
            self.image = self.imagen_normal

    def activar(self):
        self.funcion_asignada()     
class Cursor:

    def __init__(self, x, y, dy):
        self.image = pygame.image.load('esp.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 45
        self.y_inicial = 205
        self.dy = dy
        self.y = 0
        self.seleccionar(0)

    def actualizar(self):
        self.y += (self.to_y - self.y) / 10.0
        self.rect.y = int(self.y)

    def seleccionar(self, indice):
        self.to_y = self.y_inicial + indice * self.dy

    def imprimir(self, pantalla):
        pantalla.blit(self.image, self.rect)
class Menu:
    
    
    def __init__(self, opciones):
        self.opciones = []
        fuente = pygame.font.Font('dejavu.ttf', 20)
        x = 105
        y = 205
        paridad = 1

        self.cursor = Cursor(x - 30, y, 30)

        for titulo, funcion in opciones:
            self.opciones.append(Opcion(fuente, titulo, x, y, paridad, funcion))
            y += 30
            if paridad == 1:
                paridad = -1
            else:
                paridad = 1

        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self):
        

        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:
                
                self.opciones[self.seleccionado].activar()

        
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1
        
        self.cursor.seleccionar(self.seleccionado)

        
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]

        self.cursor.actualizar()
     
        for o in self.opciones:
            o.actualizar()

    def imprimir(self, pantalla):
        

        self.cursor.imprimir(pantalla)

        for opcion in self.opciones:
            opcion.imprimir(pantalla)    



def Instrucciones():
    pygame.mouse.set_visible(False)
    pygame.init()
    reloj=pygame.time.Clock()
    fuente=pygame.font.Font(None,25)
    ver_pag = True 
    pag=1
    terminar = False
    dim=[1100,630]
    while not terminar and ver_pag:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				terminar=True
			if event.type == pygame.MOUSEBUTTONDOWN:
			   pag +=1
			   if pag == 2:
				  ver_pag = False
		pantalla.fill(NEGRO)
		if pag == 1:
			fondo=pygame.image.load('Instrf.png')
			fondo=pygame.transform.scale(fondo, dim)
			pantalla.blit(fondo,[0,0])
			texto=fuente.render('Historia parte 1: ', True, BLANCO)
			pantalla.blit(texto, [10,10])
				
		
		reloj.tick(20)
		pygame.display.flip()   
		#time.sleep(5)


def Historia():
    pygame.mouse.set_visible(False)
    pygame.init()
    reloj=pygame.time.Clock()
    fuente=pygame.font.Font(None,25)
    ver_pag = True 
    pag=1
    terminar = False
    dim=[1100,630]
    while not terminar and ver_pag:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				terminar=True
			if event.type == pygame.MOUSEBUTTONDOWN:
			   pag +=1
			   if pag == 4:
				  ver_pag = False
		pantalla.fill(NEGRO)
		if pag == 1:
			fondo=pygame.image.load('h1.png')
			fondo=pygame.transform.scale(fondo, dim)
			pantalla.blit(fondo,[0,0])
			texto=fuente.render('Historia parte 1: ', True, BLANCO)
			pantalla.blit(texto, [10,10])
			
		if pag == 2:
			fondo=pygame.image.load('h2.png')
			fondo=pygame.transform.scale(fondo, dim)
			pantalla.blit(fondo,[0,0])
			texto=fuente.render('Historia parte 1: ', True, BLANCO)
			pantalla.blit(texto, [10,10])	
		
		if pag == 3:
			fondo=pygame.image.load('h3.png')
			fondo=pygame.transform.scale(fondo, dim)
			pantalla.blit(fondo,[0,0])
			texto=fuente.render('Historia parte 1: ', True, BLANCO)
			pantalla.blit(texto, [10,10])
		
		
		
		
		
		
		
		
		reloj.tick(20)
		pygame.display.flip()   
		#time.sleep(5)
def Salir():
    print " Gracias por utilizar este programa."
    sys.exit(0)



def Jugar():
    datos=JugarNivel1(0)
    puntos = datos[0]
    perder = datos[1]
    print "Puntos final : " + str(puntos)
    print "Perder : " + str(perder)
    if(perder==False):
        datos=JugarNivel2(puntos)
        puntos = datos[0]
        perder = datos[1]
        if(perder==False):
            datos= JugarBoss(puntos)
            puntos = datos[0]
            perder = datos[1]
            if(perder==False):
                print"CREDITOS"


    
if __name__ == '__main__':
    
    salir = False
    opciones = [
        ("Jugar", Jugar),
        ("Historia", Historia),
        ("Instrucciones", Instrucciones),
        ("Salir", Salir)
        ]
    

    pygame.font.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    fuente=pygame.font.Font('Wedgie Regular.ttf',80)
    texto=fuente.render('THE BAD ADVENTURE ', True, BLANCO)
    pantalla.blit(texto, [400,200])
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    fondo = pygame.image.load("fondop1.jpg").convert()
    menu = Menu(opciones)

    while not salir:

        for e in pygame.event.get():
            if e.type == QUIT:
                salir = True
        for i in opciones:
            if opciones == Instrucciones:
               Instrucciones()
            elif opciones == Salir:
               Salir()
            if opciones==Jugar:
                Jugar()
                
                
               
        pantalla.blit(fondo, (0, 0))

        fuente=pygame.font.Font('BADABB__.ttf',115)
        texto=fuente.render('THE BAD ADVENTURE ', True, BLANCO)
        pantalla.blit(texto, [30,50])
        menu.actualizar()
        menu.imprimir(pantalla)

        pygame.display.flip()
        pygame.time.delay(10)
