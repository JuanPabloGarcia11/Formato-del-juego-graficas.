"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/

Main module for platform scroller example.

From:
http://programarcadegames.com/python_examples/sprite_sheets/

Explanation video: http://youtu.be/czBDKWJqOao

Part of a series:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example.py
http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py
http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
http://programarcadegames.com/python_examples/sprite_sheets/

Game art from Kenney.nl:
http://opengameart.org/content/platformer-art-deluxe

"""

import pygame

import sys
import random
from pygame.locals import *
from pygame import gfxdraw

import constants
import levels
import platforms
import time


from player import Player

NEGRO  = (  0,   0,   0)
BLANCO = (255, 255, 255)
VERDE  = (0,   255,   0)
ROJO   = (255,   0,   0)
AMARILLO = (255,255,0)
ANCHO  = 800
ALTO = 600


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








def Jugar():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("The Bad Adventure")

    cargando = pygame.image.load("cargando.png").convert_alpha()
    screen.blit(cargando, (0, 0))
    pygame.display.flip()
   

    # Create the player
    player = Player()

    # Create all the levels
    level_list = []
    level_list.append(levels.Level_01(player))
    level_list.append(levels.Level_02(player))
    level_list.append(levels.Level_03(player))
    level_list.append(levels.Level_04(player))
    level_list.append(levels.Level_05(player))

    # Set the current level
    current_level_no = 0
    
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    primer_ataque=False

    player.rect.x = 250
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height - 60
    active_sprite_list.add(player)

    #Imagen de la vida 
    imagen_vida = pygame.image.load("heart-icon.png").convert_alpha()
    imagen_piedra = pygame.image.load("rock.png").convert_alpha()

    #Loop until the user clicks the close button.
    done = False

    fuente= pygame.font.Font('Adventure.ttf',30)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if(player.dead==False):
                        player.go_left()
                if event.key == pygame.K_RIGHT:
                    if(player.dead==False):
                        player.go_right()
                if event.key == pygame.K_UP:
                    if(player.dead==False):
                        player.jump()
                if event.key == pygame.K_SPACE:
                    if(player.piedra>0):
                        bala = platforms.Bala('rock.png')
                        bala.direccion = player.direction
                        bala.jugador = 1
                        if player.direction =="R":
                            bala.rect.x=player.rect.x+ 50
                            bala.rect.y=player.rect.y+ 45
                        else:
                            bala.rect.x=player.rect.x - 5
                            bala.rect.y=player.rect.y+ 45
                        current_level.lista_bala.add(bala)
                        player.piedra -= 1

                if event.key == pygame.K_ESCAPE:
                	ter=False
                	fuente= pygame.font.Font('Adventure.ttf',180)
                	texto=fuente.render("PAUSA", True, BLANCO)
                	screen.blit(texto,(40,ALTO/2-100))
                	pygame.display.flip()
                	fuente= pygame.font.Font('Adventure.ttf',30)
                	while not ter:
                		for event in pygame.event.get(): # User did something
            				if event.type == pygame.QUIT: # If user clicked close
                				ter = True # Flag that we are done so we exit this loop
                			if event.type == pygame.KEYDOWN:
	                			if event.key == pygame.K_ESCAPE: 
	                				ter = True
	                			if event.key == pygame.K_ESCAPE: 
	                				ter = True

            if event.type == pygame.KEYDOWN:

                    
                if event.key == pygame.K_z:
                    if player.attack == False:
                        s_bala.play()
                        player.Attack()
                        primer_ataque = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()


        
        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        if(player.vida==0 and player.dead==False and player.perdido==False):
            player.dead=True
            player.cont_dead = 0


        # If the player gets near the right side, shift the world left (-x)
        if player.rect.x >= 500:
            diff = player.rect.x - 500
            player.rect.x = 500
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            player.rect.x = 120
            current_level.shift_world(diff)

        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                fuente= pygame.font.Font('Adventure.ttf',180)
                texto=fuente.render("GANASTE", True, VERDE)
                screen.blit(texto,(40,ALTO/2-100))
                #fuente= pygame.font.Font('Adventure.ttf',60)
                #texto=fuente.render("PUNTOS: " + str(puntos), True, VERDE)
                #pantalla.blit(texto,(330,ALTO/2+100))
                #pantalla.blit(tiempo_texto, [ANCHO/2 - 100, ALTO/2+180])
                pygame.display.flip()
                time.sleep(4)
                fuente= pygame.font.Font('Adventure.ttf',30)
                current_level_no += 1
                if(current_level_no ==3):
                    current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
                player.rect.x = 250
                player.vida = 3
                player.piedra = 5
            current_position = player.rect.x + current_level.world_shift
        if(current_level_no==4 and len(current_level.enemy_list)==0):
            fuente= pygame.font.Font('Adventure.ttf',180)
            texto=fuente.render("GANASTE", True, VERDE)
            screen.blit(texto,(40,ALTO/2-100))
            pygame.display.flip()
            time.sleep(4)
            done = True

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT


        current_level.draw(screen)
        active_sprite_list.draw(screen)


        x = 5
        y = 5
        for i in range(player.vida):
            screen.blit(imagen_vida, (x, y))
            x += 25

        x = 5
        y = 30
        for i in range(player.piedra):
            screen.blit(imagen_piedra, (x, y))
            x += 30

        punto=fuente.render("Puntos: " + str(player.puntos), True, constants.BLUE)
        screen.blit(punto, [ANCHO-155, 5])

        if(player.rect.y > ANCHO):
            ayuda = current_level.world_shift * -1
            if((current_level_no==2) and ((player.rect.x + ayuda> 300) and (player.rect.x + ayuda <600))):
                current_level_no = 3
                current_level = level_list[current_level_no]
                player.level = current_level
                player.rect.x = 250
                player.rect.y = 100
            else:
                player.perdido=True
        

        if(player.perdido):
            fuente= pygame.font.Font('youmurdererbb_reg.ttf',200)
            texto=fuente.render("PERDISTE", True, ROJO)
            screen.blit(texto,(ANCHO/2-350,ALTO/2-100))
            #fuente= pygame.font.Font('youmurdererbb_reg.ttf',100)
            #texto=fuente.render("PUNTOS: " + str(puntos), True, BLANCO)
            #pantalla.blit(texto,(ANCHO/2-180,ALTO/2+50))
            #pantalla.blit(tiempo_texto, (ANCHO/2 - 100, ALTO/2+150))
            pygame.display.flip()
            time.sleep(4)
            done = True


        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    return (current_level_no, player.perdido)

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    




   



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
               if pag == 7:
                  ver_pag = False
        pantalla.fill(NEGRO)
        if pag == 1:
            fondo=pygame.image.load('h1.png')
            fondo=pygame.transform.scale(fondo, dim)
            pantalla.blit(fondo,[0,0])
            texto=fuente.render('Historia parte 1: ', True, BLANCO)
            pantalla.blit(texto, [10,10])
            
        if pag == 2:
            fondo=pygame.image.load('night2.png')
            pantalla.blit(fondo,[0,0])
            texto=fuente.render('Historia parte 1: ', True, BLANCO)
            pantalla.blit(texto, [10,10])   

        if pag == 4:
            fondo=pygame.image.load('night3.png')
            pantalla.blit(fondo,[0,0])
            texto=fuente.render('Historia parte 1: ', True, BLANCO)
            pantalla.blit(texto, [10,10]) 

        if pag == 3:
            fondo=pygame.image.load('h2.png')
            fondo=pygame.transform.scale(fondo, dim)
            pantalla.blit(fondo,[0,0])
            texto=fuente.render('Historia parte 1: ', True, BLANCO)
            pantalla.blit(texto, [10,10])   
        
        if pag == 5:
            fondo=pygame.image.load('h3.png')
            fondo=pygame.transform.scale(fondo, dim)
            pantalla.blit(fondo,[0,0])
            texto=fuente.render('Historia parte 1: ', True, BLANCO)
            pantalla.blit(texto, [10,10])

        if pag == 6:
            fondo=pygame.image.load('blablabla.jpg')
            
            pantalla.blit(fondo,[0,0])
            texto=fuente.render('Historia parte 1: ', True, BLANCO)
            pantalla.blit(texto, [10,10])
        
        
        
        
        
        
        
        
        reloj.tick(20)
        pygame.display.flip()   
        #time.sleep(5)
def Salir():
    print " Gracias por utilizar este programa."
    sys.exit(0)




    
if __name__ == '__main__':

    
    pygame.mixer.init(44100, -16, 3, 2048)
    s_menu=pygame.mixer.Sound('menusound2.ogg')
    s_menu.play(loops=-1)

    s_bala=pygame.mixer.Sound('foom_0.wav')

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
    pygame.display.set_caption("The Bad Adventure")
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
                cargando = pygame.image.load("cargando.png").convert_alpha()
                screen.blit(cargando, (0, 0))
                pygame.display.flip()
                Jugar()
                
                
        
                       
        pantalla.blit(fondo, (0, 0))

        fuente=pygame.font.Font('BADABB__.ttf',115)
        texto=fuente.render('THE BAD ADVENTURE ', True, BLANCO)
        pantalla.blit(texto, [30,50])
        menu.actualizar()
        menu.imprimir(pantalla)

        pygame.display.flip()
        pygame.time.delay(10)

