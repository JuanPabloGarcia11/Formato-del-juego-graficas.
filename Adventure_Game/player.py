"""
This module is used to hold the Player class. The Player represents the user-
controlled sprite on the screen.
"""
import pygame

import constants

from platforms import MovingPlatform
from spritesheet_functions import SpriteSheet

class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """

    # -- Attributes
    # Set speed vector of player
    change_x = 0
    change_y = 0

    # This holds all the images for the animated walk left/right
    # of our player
    walking_frames_l = []
    walking_frames_r = []
    stay_frame=[]
    attack_frames_r=[]
    attack_frames_l=[]
    dead_frames_r=[]
    dead_frames_l=[]

    dead = False
    perdido = False

    attack = False
    cont_attack = -1
    cont_even = 0 
    cont_dead = -1
    inmune = 0


    # What direction is the player facing?
    direction = "R"

    # List of sprites we can bump against
    level = None

    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        image = pygame.image.load("Idle (1).png").convert_alpha()
        self.stay_frame.append(image)
        image = pygame.transform.flip(image, True, False)
        self.stay_frame.append(image)
        image = pygame.image.load("Jump (2).png").convert_alpha()
        self.stay_frame.append(image)
        image = pygame.transform.flip(image, True, False)
        self.stay_frame.append(image)

        image = pygame.image.load("Dead (1).png").convert_alpha()
        self.dead_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.dead_frames_l.append(image)
        image = pygame.image.load("Dead (2).png").convert_alpha()
        self.dead_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.dead_frames_l.append(image)
        image = pygame.image.load("Dead (3).png").convert_alpha()
        self.dead_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.dead_frames_l.append(image)
        image = pygame.image.load("Dead (4).png").convert_alpha()
        self.dead_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.dead_frames_l.append(image)
        image = pygame.image.load("Dead (5).png").convert_alpha()
        self.dead_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.dead_frames_l.append(image)
        image = pygame.image.load("Dead (6).png").convert_alpha()
        self.dead_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.dead_frames_l.append(image)
        image = pygame.image.load("Dead (7).png").convert_alpha()
        self.dead_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.dead_frames_l.append(image)
        image = pygame.image.load("Dead (8).png").convert_alpha()
        self.dead_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.dead_frames_l.append(image)
        image = pygame.image.load("Dead (9).png").convert_alpha()
        self.dead_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.dead_frames_l.append(image)
        image = pygame.image.load("Dead (10).png").convert_alpha()
        self.dead_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.dead_frames_l.append(image)


        image = pygame.image.load("Attack (1).png").convert_alpha()
        self.attack_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.attack_frames_l.append(image)
        image = pygame.image.load("Attack (2).png").convert_alpha()
        self.attack_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.attack_frames_l.append(image)
        image = pygame.image.load("Attack (3).png").convert_alpha()
        self.attack_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.attack_frames_l.append(image)
        image = pygame.image.load("Attack (4).png").convert_alpha()
        self.attack_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.attack_frames_l.append(image)
        image = pygame.image.load("Attack (5).png").convert_alpha()
        self.attack_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.attack_frames_l.append(image)
        image = pygame.image.load("Attack (6).png").convert_alpha()
        self.attack_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.attack_frames_l.append(image)
        image = pygame.image.load("Attack (7).png").convert_alpha()
        self.attack_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.attack_frames_l.append(image)
        image = pygame.image.load("Attack (8).png").convert_alpha()
        self.attack_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.attack_frames_l.append(image)
        image = pygame.image.load("Attack (9).png").convert_alpha()
        self.attack_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.attack_frames_l.append(image)
        image = pygame.image.load("Attack (10).png").convert_alpha()
        self.attack_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.attack_frames_l.append(image)

        image = pygame.image.load("Walk (1).png").convert_alpha()
        self.walking_frames_r.append(image)
        image = pygame.image.load("Walk (2).png").convert_alpha()
        self.walking_frames_r.append(image)
        image = pygame.image.load("Walk (3).png").convert_alpha()
        self.walking_frames_r.append(image)
        image = pygame.image.load("Walk (4).png").convert_alpha()
        self.walking_frames_r.append(image)
        image = pygame.image.load("Walk (5).png").convert_alpha()
        self.walking_frames_r.append(image)
        image = pygame.image.load("Walk (6).png").convert_alpha()
        self.walking_frames_r.append(image)
        image = pygame.image.load("Walk (7).png").convert_alpha()
        self.walking_frames_r.append(image)
        image = pygame.image.load("Walk (8).png").convert_alpha()
        self.walking_frames_r.append(image)
        image = pygame.image.load("Walk (9).png").convert_alpha()
        self.walking_frames_r.append(image)
        image = pygame.image.load("Walk (10).png").convert_alpha()
        self.walking_frames_r.append(image)

        image = pygame.image.load("Walk (1).png").convert_alpha()
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = pygame.transform.flip(image, True, False)
        image = pygame.image.load("Walk (2).png").convert_alpha()
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = pygame.image.load("Walk (3).png").convert_alpha()
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = pygame.image.load("Walk (4).png").convert_alpha()
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = pygame.image.load("Walk (5).png").convert_alpha()
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = pygame.image.load("Walk (6).png").convert_alpha()
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = pygame.image.load("Walk (7).png").convert_alpha()
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = pygame.image.load("Walk (8).png").convert_alpha()
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = pygame.image.load("Walk (9).png").convert_alpha()
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = pygame.image.load("Walk (10).png").convert_alpha()
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        

        # Set the image the player starts with
        self.image = self.stay_frame[0]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

        self.vida = 3

        self.piedra = 5

        self.puntos = 0

    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift

        self.inmune -= 1

        if (self.dead == False and self.perdido == False):
            if self.attack:
                print "en ataque"
                if self.direction == "R":
                    self.image=self.attack_frames_r[self.cont_attack]
                    self.cont_even += 1
                    if (self.cont_even % 5) == 0 :
                        self.cont_attack += 1
                    if(self.cont_attack == 10):
                        print"se termino"
                        self.cont_attack = -1
                        self.attack = False
                        self.cont_even = 0
                else:
                    self.image=self.attack_frames_l[self.cont_attack]
                    self.cont_even += 1
                    if (self.cont_even % 5) == 0 :
                        self.cont_attack += 1
                    if(self.cont_attack == 10):
                        print"se termino"
                        self.cont_attack = -1
                        self.attack = False
                        self.cont_even = 0
                    

            else:
                if self.direction == "R":
                    if self.change_x == 0:
                        if self.change_y < 0:
                            self.image=self.stay_frame[2]
                        else:
                            self.image=self.stay_frame[0]
                    else:
                        if self.change_y < 0:
                            self.image=self.stay_frame[2]
                        else: 
                            frame = (pos // 30) % len(self.walking_frames_r)
                            self.image = self.walking_frames_r[frame]
                else:
                    if self.change_x == 0:
                        if self.change_y < 0:
                            self.image=self.stay_frame[3]
                        else:
                            self.image=self.stay_frame[1]
                    else:
                        if self.change_y < 0:
                            self.image=self.stay_frame[3]
                        else:
                            frame = (pos // 30) % len(self.walking_frames_l)
                            self.image = self.walking_frames_l[frame]
        else:
            if self.direction == "R":
                    self.image=self.dead_frames_r[self.cont_dead]
                    self.cont_even += 1
                    if (self.cont_even % 6) == 0 :
                        self.cont_dead += 1
                        #self.rect.y += 5
                    if(self.cont_dead == 10):
                        self.cont_dead = -1
                        self.dead= False
                        self.perdido = True
                        self.cont_even = 0
            else:
                self.image=self.dead_frames_l[self.cont_dead]
                self.cont_even += 1
                if (self.cont_even % 6) == 0 :
                    self.cont_dead += 1
                    #self.rect.y += 5
                if(self.cont_dead == 10):
                    self.cont_dead = -1
                    self.dead = False
                    self.perdido=True
                    self.cont_even = 0



        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if(self.dead==False and self.perdido==False):
                if self.change_x > 0:
                    self.rect.right = block.rect.left
                elif self.change_x < 0:
                    # Otherwise if we are moving left, do the opposite.
                    self.rect.left = block.rect.right

        # Move up/down
        #if(self.dead == False):
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if(self.dead==False and self.perdido==False):
                if self.change_y > 0:
                    self.rect.bottom = block.rect.top
                elif self.change_y < 0:
                    self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT + 1000 and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -10

    def Attack(self):
        self.attack = True
        self.cont_attack = 0



    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -4
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 4
        self.direction = "R"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
