import pygame

import constants
import platforms






class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    platform_list = None
    enemy_list = None
    enemy_list2 = None
    object_list = None

    # Background image
    background = None

    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = -1000

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.enemy_list2 = pygame.sprite.Group()
        self.object_list = pygame.sprite.Group()
        self.lista_bala = pygame.sprite.Group()
        self.player = player

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        for enemy in self.enemy_list:
            if enemy.rect.x < self.player.rect.x:
                if(enemy.ene == 0 or enemy.ene == 5):
                    enemy.direccion = 1
            else:
                if(enemy.ene == 0 or enemy.ene == 5):
                    enemy.direccion = 0  
            if enemy.disparar == 0 and (abs(enemy.rect.x - self.player.rect.x)<250):
                balae=platforms.Bala('rock.png')
                if enemy.direccion == 1:
                    balae.direccion = "R"
                else:
                    balae.direccion = "L"
                balae.rect.x=enemy.rect.x-5
                balae.rect.y=enemy.rect.y+ 20
                self.lista_bala.add(balae)

            if enemy.disparar == 0 and (abs(enemy.rect.x - self.player.rect.x)<300) and enemy.ene == 5:
                balae=platforms.Bala('poisonball.png')
                if enemy.direccion == 1:
                    balae.direccion = "R"
                else:
                    balae.direccion = "L"
                balae.rect.x=self.player.rect.x+200
                balae.rect.y=self.player.rect.y + 20
                self.lista_bala.add(balae)

            if(enemy.ene == 1):
                if(enemy.atacar == 0 and (self.player.direction != enemy.direction) ):
                    enemy.Attack()

        ls2 = pygame.sprite.Group()
        ls2.add(self.player)

        for enemy in self.enemy_list2:
            if enemy.rect.x < self.player.rect.x:
                if(enemy.ene == 0):
                    enemy.direccion = 1
            else:
                if(enemy.ene == 0):
                    enemy.direccion = 0  
            if enemy.disparar == 0 and (abs(enemy.rect.x - self.player.rect.x)<250):
                balae=platforms.Bala('rock.png')
                if enemy.direccion == 1:
                    balae.direccion = "R"
                else:
                    balae.direccion = "L"
                balae.rect.x=enemy.rect.x-5
                balae.rect.y=enemy.rect.y+ 20
                self.lista_bala.add(balae)

            if(enemy.ene == 1):
                if(enemy.atacar == 0 and (self.player.direction != enemy.direction) ):
                    enemy.Attack()

            ls_choque2 =pygame.sprite.spritecollide(enemy, ls2, False)
            for elemento in ls_choque2:
                if self.player.attack  and enemy.attack:
                    if(self.player.direction=="R"):
                        self.player.rect.x -= 100
                    else:
                        self.player.rect.x += 100

                if self.player.attack==False  and enemy.attack:
                    if(self.player.direction=="R"):
                        self.player.rect.x -= 200
                    else:
                        self.player.rect.x += 200
                    self.player.vida -= 1

                if self.player.attack  and enemy.attack==False:
                    self.enemy_list2.remove(enemy)
                    self.player.puntos += 20


                if self.player.attack==False  and enemy.attack==False:
                    if(self.player.direction=="R"):
                        self.player.rect.x -= 200
                    else:
                        self.player.rect.x += 200
                    self.player.vida -= 1







        ls = pygame.sprite.Group()
        ls.add(self.player)
        for bala in self.lista_bala:
            ls_impactos=pygame.sprite.spritecollide(bala, self.platform_list, False)
            for impacto in ls_impactos:
                self.lista_bala.remove(bala)

            if(bala.jugador == 1):
                ls_impactos=pygame.sprite.spritecollide(bala, self.enemy_list, True)
                for impacto in ls_impactos:
                    self.lista_bala.remove(bala)
                    self.player.puntos += 5

            if(bala.jugador == 1):
                ls_impactos=pygame.sprite.spritecollide(bala, self.enemy_list2, False)
                for impacto in ls_impactos:
                    self.lista_bala.remove(bala)

            ls_impactos=pygame.sprite.spritecollide(bala, ls, False)
            for impacto in ls_impactos:
                if(bala.jugador == 0):
                    self.lista_bala.remove(bala)
                    if(self.player.attack == False):
                        self.player.vida -= 1
                    else:
                        self.player.puntos += 5

        ls_choque =pygame.sprite.spritecollide(self.player, self.enemy_list, self.player.attack)
        for elemento in ls_choque:
            if self.player.attack:
                self.player.puntos += 10
            if self.player.attack ==False and self.player.dead ==False:
                self.player.puntos +=10
            if self.player.attack == False and self.player.dead ==False:
                self.player.puntos -= 10
                if(self.player.inmune<0):
                    self.player.vida -=1
                self.player.inmune = 15
                if self.player.direction == "L":
                    self.player.rect.x += 7
                else:
                    self.player.rect.x -= 7


        

        self.lista_bala.update()
        self.platform_list.update()
        self.enemy_list.update()
        self.enemy_list2.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.BLUE)
        screen.blit(self.background,(self.world_shift // 3,0))

        # Draw all the sprite lists that we have
        self.object_list.draw(screen)
        self.lista_bala.draw(screen)
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.enemy_list2.draw(screen)
        

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for bala in self.lista_bala:
            bala.rect.x += shift_x

        for three in self.object_list:
            three.rect.x += shift_x

        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

        for enemy in self.enemy_list2:
            enemy.rect.x += shift_x

# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("Background2.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -3300

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.GRASS2, 200, 536],
                  [platforms.GRASS2, 320, 536],
                  [platforms.GRASS3, 550, 500],
                  [platforms.TIERRA3, 550, 564],
                  [platforms.TIERRA3, 737, 564],
                  [platforms.GRASS3, 737, 500],
                  [platforms.GRASS1, 1000, 450],
                  [platforms.GRASS1, 1070, 400],
                  [platforms.GRASS1, 1190, 280],
                  [platforms.GRASS3, 1850, 450],
                  [platforms.TIERRA3, 1850, 514],
                  [platforms.TIERRA3, 1850, 578],
                  [platforms.GRASS3, 2037, 450],
                  [platforms.TIERRA3, 2037, 514],
                  [platforms.TIERRA3, 2037, 578],
                  [platforms.GRASS3, 2224, 450],
                  [platforms.TIERRA3, 2224, 514],
                  [platforms.TIERRA3, 2224, 578],
                  [platforms.GRASS1, 2566, 430],
                  [platforms.GRASS3, 2965, 300],
                  [platforms.TIERRA3, 2965, 360],
                  [platforms.TIERRA3, 2965, 424],
                  [platforms.TIERRA3, 2965, 488],
                  [platforms.TIERRA3, 2965, 552],
                  [platforms.TIERRA3, 2965, 616],
                  [platforms.GRASS3, 3620, 300],
                  [platforms.TIERRA3, 3620, 360],
                  [platforms.TIERRA3, 3620, 424],
                  [platforms.TIERRA3, 3620, 488],
                  [platforms.TIERRA3, 3620, 552],
                  [platforms.TIERRA3, 3620, 616],
                  [platforms.GRASS3, 3807, 300],
                  [platforms.TIERRA3, 3807, 360],
                  [platforms.TIERRA3, 3807, 424],
                  [platforms.TIERRA3, 3807, 488],
                  [platforms.TIERRA3, 3807, 552],
                  [platforms.TIERRA3, 3807, 616],
                  [platforms.GRASS3, 3994, 300],
                  [platforms.TIERRA3, 3994, 360],
                  [platforms.TIERRA3, 3994, 424],
                  [platforms.TIERRA3, 3994, 488],
                  [platforms.TIERRA3, 3994, 552],
                  [platforms.TIERRA3, 3994, 616],
                  [platforms.GRASS3, 4186, 300],
                  [platforms.TIERRA3, 4186, 360],
                  [platforms.TIERRA3, 4186, 424],
                  [platforms.TIERRA3, 4186, 488],
                  [platforms.TIERRA3, 4186, 552],
                  [platforms.TIERRA3, 4186, 616],
                  [platforms.GRASS3, 4373, 300],
                  [platforms.TIERRA3, 4373, 360],
                  [platforms.TIERRA3, 4373, 424],
                  [platforms.TIERRA3, 4373, 488],
                  [platforms.TIERRA3, 4373, 552],
                  [platforms.TIERRA3, 4373, 616],

                  ]

        objetos = [
                    [platforms.ARBOL,270,344],
                    [platforms.FLORES,600,465],
                    [platforms.FLORES,670,465],
                    [platforms.FLORES,740,465],
                    [platforms.FLORES,810,465],
                    [platforms.ARBOL,1925,258],
                    [platforms.ROCA,2117,391],
                    [platforms.FLORES,3000,265],
                    [platforms.ARBOL,3750,108],
                    [platforms.ROCA,3950,241],
                    [platforms.FLORES,4136,265],
                    [platforms.FLORES,4250,265],
                    [platforms.ARBOL,4300,108],


                  ]

        enemigos = [
                    ["rock-monster.png",200,895,450],
                    ["rock-monster.png",200,2000,400],
                    ["rock-obstacle.png",200,2200,410],
                    ["rock-monster.png",200,2300,400],
                    ["rock-monster.png",200,3050,250],
                    ["rock-monster.png",200,3700,250],
                    ["rock-monster.png",200,3900,250],
                    ["rock-monster.png",200,4100,250],
                   ]

        for enemigo in enemigos:
            print enemigo[0]
            ene = platforms.Enemigo(enemigo[0],enemigo[1])
            ene.rect.x=enemigo[2]
            ene.rect.y=enemigo[3]
            self.enemy_list.add(ene)

        


        for obj in objetos:
            three_ob = platforms.Objeto(obj[0],1)
            three_ob.rect.x = obj[1]
            three_ob.rect.y = obj[2]
            self.object_list.add(three_ob)


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0],1)
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.GRASS1,1)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.GRASS1,1)
        block.rect.x = 2666
        block.rect.y = 300
        block.boundary_left = 2666
        block.boundary_right = 2850
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.GRASS1,1)
        block.rect.x = 3320
        block.rect.y = 400
        block.boundary_left = 3320
        block.boundary_right = 3550
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.GRASS1,1)
        block.rect.x = 1690
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


# Create platforms for the level
class Level_02(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("snow1.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -5650

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.GRASS2, 200, 536],
                  [platforms.GRASS2, 320, 536],
                  [platforms.GRASS3, 550, 500],
                  [platforms.TIERRA3, 550, 564],
                  [platforms.TIERRA3, 737, 564],
                  [platforms.GRASS3, 737, 500],
                  [platforms.GRASS1, 1000, 400],
                  [platforms.GRASS1, 1200, 400],
                  [platforms.GRASS1, 1190, 280],
                  [platforms.GRASS3, 1850, 450],
                  [platforms.TIERRA3, 1850, 514],
                  [platforms.TIERRA3, 1850, 578],
                  [platforms.GRASS3, 2037, 450],
                  [platforms.TIERRA3, 2037, 514],
                  [platforms.TIERRA3, 2037, 578],
                  [platforms.GRASS3, 2224, 450],
                  [platforms.TIERRA3, 2224, 514],
                  [platforms.TIERRA3, 2224, 578],
                  [platforms.GRASS1, 2466, 100],
                  [platforms.GRASS3, 2965, 300],
                  [platforms.TIERRA3, 2965, 360],
                  [platforms.TIERRA3, 2965, 424],
                  [platforms.TIERRA3, 2965, 488],
                  [platforms.TIERRA3, 2965, 552],
                  [platforms.TIERRA3, 2965, 616],
                  [platforms.GRASS3, 3620, 300],
                  [platforms.TIERRA3, 3620, 360],
                  [platforms.TIERRA3, 3620, 424],
                  [platforms.TIERRA3, 3620, 488],
                  [platforms.TIERRA3, 3620, 552],
                  [platforms.TIERRA3, 3620, 616],
                  [platforms.GRASS3, 3807, 300],
                  [platforms.TIERRA3, 3807, 360],
                  [platforms.TIERRA3, 3807, 424],
                  [platforms.TIERRA3, 3807, 488],
                  [platforms.TIERRA3, 3807, 552],
                  [platforms.TIERRA3, 3807, 616],
                  [platforms.GRASS3, 3994, 300],
                  [platforms.TIERRA3, 3994, 360],
                  [platforms.TIERRA3, 3994, 424],
                  [platforms.TIERRA3, 3994, 488],
                  [platforms.TIERRA3, 3994, 552],
                  [platforms.TIERRA3, 3994, 616],
                  [platforms.GRASS3, 4186, 300],
                  [platforms.TIERRA3, 4186, 360],
                  [platforms.TIERRA3, 4186, 424],
                  [platforms.TIERRA3, 4186, 488],
                  [platforms.TIERRA3, 4186, 552],
                  [platforms.TIERRA3, 4186, 616],
                  [platforms.GRASS3, 4373, 300],
                  [platforms.TIERRA3, 4373, 360],
                  [platforms.TIERRA3, 4373, 424],
                  [platforms.TIERRA3, 4373, 488],
                  [platforms.TIERRA3, 4373, 552],
                  [platforms.TIERRA3, 4373, 616],
                  [platforms.GRASS1, 5050,100],
                  [platforms.GRASS1, 5050,100],
                  [platforms.GRASS1,5900,200],

                  ]


        objetos = [
                    [platforms.SNOWMAN,300,412],
                    [platforms.SNOWBAL,600,438],
                    [platforms.SNOWARBOL,710,437],
                    [platforms.SNOWMAN,1960,326],
                    [platforms.SNOWBAL,2100,388],
                    [platforms.SNOWARBOL,2200,387],
                    [platforms.SNOWMAN,3750,176],
                    [platforms.SNOWBAL,3950,238],
                    [platforms.SNOWPLANT,4136,236],
                    [platforms.SNOWPLANT,4250,236],
                    


                    


                  ]


        enemigos = [
                    ["skull-game-obstacle.png",100,1210,345],
                    ["skull-game-obstacle.png",200,2000,395],
                    ["skull-game-obstacle.png",200,2300,395],
                    ["skull-game-obstacle.png",100,3030,245],
                    ["skull-game-obstacle.png",200,3700,245],
                    ["skull-game-obstacle.png",200,3900,245],
                    ["skull-game-obstacle.png",200,4100,245],
                    ["skull-game-obstacle.png",100,5910,145],
                   ]

        enemigos1= [
                    [200,560,423,-1,550,910],
                    [200,2100,373,-1,2010,2400],
                    [200,3750,223,-2,3690,4000],
                    [200,3950,223,-2,3850,4300],
                    [200,4000,223,-1,3950,4450],

                    
                   ]


        for enemigo in enemigos:
            print enemigo[0]
            ene = platforms.Enemigo(enemigo[0],enemigo[1])
            ene.rect.x=enemigo[2]
            ene.rect.y=enemigo[3]
            self.enemy_list.add(ene)

        for enem in enemigos1:
            ene = platforms.Enemigo1(enem[0])
            ene.rect.x = enem[1]
            ene.rect.y = enem[2]
            ene.change_x = enem[3]
            ene.boundary_left = enem[4]
            ene.boundary_right = enem[5]
            ene.level = self
            self.enemy_list2.add(ene)

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0],2)
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)


        for obj in objetos:
            three_ob = platforms.Objeto(obj[0],2)
            three_ob.rect.x = obj[1]
            three_ob.rect.y = obj[2]
            self.object_list.add(three_ob)

        # Add a custom moving platform
        # Add a custom moving platform

        movimiento = [
                    [platforms.GRASS1, 1350, 400, "X", 1350, 1600, 1],
                    [platforms.GRASS1, 2566, 430, "Y", 90,500,-1],
                    [platforms.GRASS1, 2666, 100, "X", 2530, 3700, 3],
                    [platforms.GRASS1, 4665, 200, "X", 4666, 5000, 2],
                    [platforms.GRASS1, 5130, 300, "Y", 90,500,-2],
                    [platforms.GRASS1, 5200, 200, "X", 5200, 5800, 2],
                    [platforms.GRASS1, 6000, 200, "X", 6000, 6800, 3],




                   ]

        for mov in movimiento:
            block = platforms.MovingPlatform(mov[0],2)
            block.rect.x = mov[1]
            block.rect.y = mov[2]
            if(mov[3]=="X"):
                block.boundary_left = mov[4]
                block.boundary_right = mov[5]
                block.change_x = mov[6]
            else:
                block.boundary_top = mov[4]
                block.boundary_bottom = mov[5]
                block.change_y = mov[6]
            block.player = self.player
            block.level = self
            self.platform_list.add(block)



        block = platforms.MovingPlatform(platforms.GRASS1,2)
        block.rect.x = 2666
        block.rect.y = 300
        block.boundary_left = 2666
        block.boundary_right = 2850
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.GRASS1,2)
        block.rect.x = 1690
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


class Level_03(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("night1.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -5670

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.GRASS2, 200, 536],
                  [platforms.GRASS2, 320, 536],
                  [platforms.GRASS3, 550, 500],
                  [platforms.TIERRA3, 550, 564],
                  [platforms.TIERRA3, 737, 564],
                  [platforms.GRASS3, 737, 500],
                  [platforms.GRASS1, 500, 320],
                  [platforms.GRASS1, 390, 410],
                  [platforms.GRASS1, 690, 310],
                  [platforms.GRASS1, 960, 320],
                  [platforms.GRASS2, 1200, 400],
                  [platforms.GRASS3, 1850, 450],
                  [platforms.TIERRA3, 1850, 514],
                  [platforms.TIERRA3, 1850, 578],
                  [platforms.GRASS3, 2037, 450],
                  [platforms.TIERRA3, 2037, 514],
                  [platforms.TIERRA3, 2037, 578],
                  [platforms.GRASS3, 2224, 450],
                  [platforms.TIERRA3, 2224, 514],
                  [platforms.TIERRA3, 2224, 578],
                  [platforms.GRASS1, 2800, 400],
                  [platforms.GRASS3, 3100, 200],
                  [platforms.GRASS3, 3830, 200],
                  [platforms.GRASS3, 5000, 400],
                  [platforms.GRASS3, 5187, 400],
                  [platforms.GRASS3, 6100, 400],


                  

                  ]


        objetos = [
                    [platforms.COFREVERT,300,407],
                    [platforms.COFREHORI,600,436],
                    [platforms.COFREHORI,1860,386],
                    [platforms.COFREVERT,2030,321],
                    [platforms.COFREHORI,6130,336],



                  ]


        enemigos = [
                    ["skull-game-obstacle.png",100,1250,345],
                    ["skull-game-obstacle.png",200,2000,395],
                    ["skull-game-obstacle.png",200,2300,395],
                    ["skull-game-obstacle.png",200,3180,145],
                    ["skull-game-obstacle.png",200,3840,145],
                    ["skull-game-obstacle.png",200,3950,145],
                    ["skull-game-obstacle.png",200,5050,345],
                    ["skull-game-obstacle.png",150,5250,345],
                    ["skull-game-obstacle.png",100,5310,345],

                   ]

        enemigos1= [
                    [200,560,434,-1,550,910],
                    [200,2100,384,-1,2010,2400],
                    [200,3200,136,-1,3110,3240],
                    [200,5110,336,-1,5010,5300],
                    [200,5210,336,-1,5110,5350],

                    
                   ]


        for enemigo in enemigos:
            print enemigo[0]
            ene = platforms.Enemigo(enemigo[0],enemigo[1])
            ene.rect.x=enemigo[2]
            ene.rect.y=enemigo[3]
            self.enemy_list.add(ene)

        for enem in enemigos1:
            ene = platforms.Enemigo2(enem[0])
            ene.rect.x = enem[1]
            ene.rect.y = enem[2]
            ene.change_x = enem[3]
            ene.boundary_left = enem[4]
            ene.boundary_right = enem[5]
            ene.level = self
            self.enemy_list2.add(ene)

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0],3)
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)


        for obj in objetos:
            three_ob = platforms.Objeto(obj[0],3)
            three_ob.rect.x = obj[1]
            three_ob.rect.y = obj[2]
            self.object_list.add(three_ob)

        # Add a custom moving platform
        # Add a custom moving platform

        movimiento = [
                    [platforms.GRASS1, 1350, 400, "Y", 100, 500, -1],
                    [platforms.GRASS1, 1470, 450, "Y", 100, 500, -1],
                    [platforms.GRASS1, 1590, 300, "Y", 100, 500, -1],
                    [platforms.GRASS1, 2520, 380, "X", 2520, 2700, 1],
                    [platforms.GRASS1, 2920, 300, "Y", 100, 500, -1],
                    [platforms.GRASS1, 3300, 200, "X", 3300, 3750, 2],
                    #[platforms.GRASS1, 3950, 400, "Y", 100, 500, -1],
                    [platforms.GRASS1, 4100, 200, "X", 4100, 4530, 2],
                    [platforms.GRASS1, 4600, 450, "Y", 100, 500, -1],
                    [platforms.GRASS1, 4750, 300, "Y", 100, 500, -1],
                    [platforms.GRASS1, 5390, 400, "X", 5390, 6000, 2],
                    [platforms.GRASS2, 6320, 400, "X", 6320, 6800, 3],

                    




                   ]

        for mov in movimiento:
            block = platforms.MovingPlatform(mov[0],3)
            block.rect.x = mov[1]
            block.rect.y = mov[2]
            if(mov[3]=="X"):
                block.boundary_left = mov[4]
                block.boundary_right = mov[5]
                block.change_x = mov[6]
            else:
                block.boundary_top = mov[4]
                block.boundary_bottom = mov[5]
                block.change_y = mov[6]
            block.player = self.player
            block.level = self
            self.platform_list.add(block)



        

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.GRASS1,3)
        block.rect.x = 1690
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


class Level_04(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("snow1.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1000

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.GRASS2, 200, 536],
                  [platforms.GRASS2, 320, 536],
                  [platforms.GRASS3, 550, 500],
                  [platforms.TIERRA3, 550, 564],
                  [platforms.TIERRA3, 737, 564],
                  [platforms.GRASS3, 737, 500],
                  [platforms.GRASS3, 924, 500],
                  [platforms.TIERRA3, 924, 564],
                  [platforms.GRASS3, 1111, 500],
                  [platforms.TIERRA3, 1111, 564],
                  [platforms.GRASS3, 1111, 500],
                  [platforms.TIERRA3, 1111, 564],
                  [platforms.GRASS3, 1298, 500],
                  [platforms.TIERRA3, 1298, 564],
                  [platforms.GRASS3, 1485, 500],
                  [platforms.TIERRA3, 1485, 564],
                  [platforms.GRASS3, 1672, 500],
                  [platforms.TIERRA3, 1672, 564],
                  [platforms.GRASS3, 1859, 500],
                  [platforms.TIERRA3, 1859, 564],
                  [platforms.GRASS3, 2051, 500],
                  [platforms.TIERRA3, 2051, 564],

                  


                  

                  ]


        objetos = [
                    



                  ]


        enemigos = [
                    ["skull-game-obstacle.png",100,1250,445],
                    ["skull-game-obstacle.png",200,1000,445],
                    ["skull-game-obstacle.png",100,600,445],
                    ["skull-game-obstacle.png",200,800,445],
                

                   ]

        enemigos1= [
                    
                   ]


        

        for enemigo in enemigos:
            print enemigo[0]
            ene = platforms.Enemigo(enemigo[0],enemigo[1])
            ene.rect.x=enemigo[2]
            ene.rect.y=enemigo[3]
            self.enemy_list.add(ene)

        for enem in enemigos1:
            ene = platforms.Enemigo2(enem[0])
            ene.rect.x = enem[1]
            ene.rect.y = enem[2]
            ene.change_x = enem[3]
            ene.boundary_left = enem[4]
            ene.boundary_right = enem[5]
            ene.level = self
            self.enemy_list2.add(ene)

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0],2)
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)


        for obj in objetos:
            three_ob = platforms.Objeto(obj[0],2)
            three_ob.rect.x = obj[1]
            three_ob.rect.y = obj[2]
            self.object_list.add(three_ob)

        # Add a custom moving platform
        # Add a custom moving platform

        movimiento = [

                    




                   ]

        for mov in movimiento:
            block = platforms.MovingPlatform(mov[0],3)
            block.rect.x = mov[1]
            block.rect.y = mov[2]
            if(mov[3]=="X"):
                block.boundary_left = mov[4]
                block.boundary_right = mov[5]
                block.change_x = mov[6]
            else:
                block.boundary_top = mov[4]
                block.boundary_bottom = mov[5]
                block.change_y = mov[6]
            block.player = self.player
            block.level = self
            self.platform_list.add(block)



        

        


class Level_05(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("castle1.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -3100

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.GRASS2, 200, 536],
                  [platforms.GRASS2, 320, 536],
                  [platforms.GRASS3, 550, 500],
                  [platforms.TIERRA3, 550, 564],
                  [platforms.TIERRA3, 737, 564],
                  [platforms.GRASS3, 737, 500],
                  [platforms.GRASS3, 924, 500],
                  [platforms.TIERRA3, 924, 564],
                  [platforms.GRASS3, 1111, 500],
                  [platforms.TIERRA3, 1111, 564],
                  [platforms.GRASS3, 1111, 500],
                  [platforms.TIERRA3, 1111, 564],
                  [platforms.GRASS3, 1298, 500],
                  [platforms.TIERRA3, 1298, 564],
                  [platforms.GRASS3, 1485, 500],
                  [platforms.TIERRA3, 1485, 564],
                  [platforms.GRASS3, 1672, 500],
                  [platforms.TIERRA3, 1672, 564],
                  [platforms.GRASS3, 1859, 500],
                  [platforms.TIERRA3, 1859, 564],
                  [platforms.GRASS3, 2051, 500],
                  [platforms.TIERRA3, 2051, 564],
                  [platforms.GRASS3, 2230, 500],
                  [platforms.TIERRA3, 2230, 564],
                  [platforms.GRASS3, 2425, 500],
                  [platforms.TIERRA3, 2425, 564],
                  [platforms.GRASS3, 2612, 500],
                  [platforms.TIERRA3, 2612, 564],
                  [platforms.GRASS3, 2799, 500],
                  [platforms.TIERRA3, 2799, 564],
                  [platforms.GRASS3, 2986, 500],
                  [platforms.TIERRA3, 2986, 564],
                  [platforms.GRASS3, 3173, 500],
                  [platforms.TIERRA3, 3173, 564],
                  [platforms.GRASS3, 3360, 500],
                  [platforms.TIERRA3, 3360, 564],
                  [platforms.GRASS3, 3547, 500],
                  [platforms.TIERRA3, 3547, 564],
                  [platforms.GRASS3, 3734, 500],
                  [platforms.TIERRA3, 3734, 564],
                  [platforms.GRASS3, 3921, 500],
                  [platforms.TIERRA3, 3921, 564],
                  [platforms.GRASS3, 4108, 500],
                  [platforms.TIERRA3, 4108, 564],

                  


                  

                  ]



        objetos = [
                    [platforms.PUERTA,4050,329],
                    [platforms.FUEGO,750,375],
                    [platforms.FUEGO,2250,375],
                    [platforms.FUEGO,3750,375],
                    [platforms.TRAJE,200,373],
                    [platforms.TRAJE,1200,373],
                    [platforms.TRAJE,1900,373],
                    [platforms.TRAJE,2500,373],
                    [platforms.TRAJE,3500,373],
                    [platforms.HERRAMIENTAS,260,373],
                    [platforms.HERRAMIENTAS,1300,373],
                    [platforms.HERRAMIENTAS,2000,373],
                    [platforms.HERRAMIENTAS,2600,373],
                    [platforms.HERRAMIENTAS,3300,373],


                    



                  ]


        enemigos = [
                    ["skull-game-obstacle.png",100,550,445],
                    ["skull-game-obstacle.png",200,800,445],
                    ["skull-game-obstacle.png",200,1000,445],
                    ["skull-game-obstacle.png",200,1100,445],
                    ["skull-game-obstacle.png",200,1500,445],
                    ["skull-game-obstacle.png",200,1800,445],
                    ["skull-game-obstacle.png",200,2000,445],
                    ["skull-game-obstacle.png",150,2200,445],
                    ["skull-game-obstacle.png",100,2500,445],
                    ["skull-game-obstacle.png",100,2800,445],

                   ]

        enemigos1= [
                    [200,560,434,-1,550,910],
                    [200,1050,434,-1,1000,1500],
                    [200,1550,434,-1,1500,1800],
                    [200,1850,434,-1,1800,2000],
                    [200,2150,434,-1,2100,2300],
                    [200,2350,434,-1,2300,2500],
                    [200,2550,434,-1,2500,2700],

                    
                   ]

        enemigos2= [
                    [200,660,424,-1,650,910],
                    [200,1150,424,-1,1100,1600],
                    [200,1650,424,-1,1600,1900],
                    [200,1950,424,-1,1700,2100],
                    [200,2250,424,-1,2200,2400],
                    [200,2450,424,-1,2400,2600],
                    [200,2650,424,-1,2600,2800],

                    
                   ]


        ene = platforms.Enemigo("boss.png",150)
        ene.rect.x=3400
        ene.rect.y=414
        ene.ene = 5
        self.enemy_list.add(ene)


        for enemigo in enemigos:
            print enemigo[0]
            ene = platforms.Enemigo(enemigo[0],enemigo[1])
            ene.rect.x=enemigo[2]
            ene.rect.y=enemigo[3]
            self.enemy_list.add(ene)

        for enem in enemigos1:
            ene = platforms.Enemigo2(enem[0])
            ene.rect.x = enem[1]
            ene.rect.y = enem[2]
            ene.change_x = enem[3]
            ene.boundary_left = enem[4]
            ene.boundary_right = enem[5]
            ene.level = self
            self.enemy_list2.add(ene)

        for enem in enemigos2:
            ene = platforms.Enemigo1(enem[0])
            ene.rect.x = enem[1]
            ene.rect.y = enem[2]
            ene.change_x = enem[3]
            ene.boundary_left = enem[4]
            ene.boundary_right = enem[5]
            ene.level = self
            self.enemy_list2.add(ene)

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0],4)
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)


        for obj in objetos:
            three_ob = platforms.Objeto(obj[0],4)
            three_ob.rect.x = obj[1]
            three_ob.rect.y = obj[2]
            self.object_list.add(three_ob)

        # Add a custom moving platform
        # Add a custom moving platform

        movimiento = [


                   ]

        for mov in movimiento:
            block = platforms.MovingPlatform(mov[0],3)
            block.rect.x = mov[1]
            block.rect.y = mov[2]
            if(mov[3]=="X"):
                block.boundary_left = mov[4]
                block.boundary_right = mov[5]
                block.change_x = mov[6]
            else:
                block.boundary_top = mov[4]
                block.boundary_bottom = mov[5]
                block.change_y = mov[6]
            block.player = self.player
            block.level = self
            self.platform_list.add(block)



        

        
