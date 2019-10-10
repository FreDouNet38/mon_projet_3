"""The labyritnh's classes"""

import pygame
from pygame.locals import *
from constants import *
import random
import time

class Map:
    """Class which allow the creation of the map"""
    def __init__(self,folder):
        self.folder = folder
        self.structure = []
    
    def generate(self):
        """Create lists from the level.txt"""
        with open(self.folder, "r") as folder:
            level_structure = []
            for line in folder:
                level_line = []
                for sprite in line:
                    if sprite != '\n':
                        level_line.append(sprite)
                level_structure.append(level_line)
            self.structure = level_structure
            print(level_structure[0])
            print(level_structure[1])
            print(level_structure[2])
            print(level_structure[3])
            print(level_structure[4])
            print(level_structure[5])
            print(level_structure[6])
            print(level_structure[7])
            print(level_structure[8])
            print(level_structure[9])
            print(level_structure[10])
            print(level_structure[11])
            print(level_structure[12])
            print(level_structure[13])
            print(level_structure[14])

    def show(self, window):
        """From the lists generated above it creates a map with the different images"""
        wall = pygame.image.load(image_wall).convert_alpha()
        floor = pygame.image.load(image_floor).convert_alpha()
        guard = pygame.image.load(image_guard).convert_alpha()

        line_nb = 0
        for line in self.structure:
            sprite_nb = 0
            for sprite in line:
                x = sprite_nb * sprite_size
                y = line_nb * sprite_size
                if sprite == 'm':
                    window.blit(wall, (x, y))
                elif sprite == '0':
                    window.blit(floor, (x, y))
                elif sprite == 'f':
                    window.blit(guard, (x, y))
                sprite_nb += 1
            line_nb += 1

    
class Player:
    """Class to create a player"""
    def __init__(self, player, level):
        self.player = pygame.image.load(player).convert_alpha()
        self.level = level
        #Position en sprite et en pixels
        self.sprite_x = 0
        self.sprite_y = 0 
        self.x = 0
        self.y = 0
        self.ITEMS = []

    def move(self, direction):
        """Function which deals with the player's movements"""
        if direction == 'right':
            #We check MG doesn't get out of the map
            if self.sprite_x < (number_of_sprite - 1):
                #We check if the sprite is available
                if self.level.structure[self.sprite_y][self.sprite_x+1] != 'm':
                    self.sprite_x += 1
                    self.x = self.sprite_x * sprite_size
            

        if direction == 'left':
            if self.sprite_x > 0:
                if self.level.structure[self.sprite_y][self.sprite_x-1] != 'm':
                    self.sprite_x -= 1
                    self.x = self.sprite_x * sprite_size

        if direction == 'up':
            if self.sprite_y > 0:
                if self.level.structure[self.sprite_y-1][self.sprite_x] != 'm':
                    self.sprite_y -= 1
                    self.y = self.sprite_y * sprite_size

        if direction == 'down':
            if self.sprite_y < (number_of_sprite - 1):
                if self.level.structure[self.sprite_y+1][self.sprite_x] != 'm':
                    self.sprite_y += 1
                    self.y = self.sprite_y * sprite_size

    def check_item(self, name, window):
        """Here we check if the player is on a sprite already occupied by an item"""
        gotneedle = pygame.image.load(got_needle).convert_alpha()
        gottube = pygame.image.load(got_tube).convert_alpha()
        gotether = pygame.image.load(got_ether).convert_alpha()
        

        if self.level.structure[self.sprite_x][self.sprite_y] == 'needle':
            self.level.structure[self.sprite_x][self.sprite_y] = 'm'
            self.ITEMS.append('needle')
            window.blit(gotneedle, (20, 50))
            

        elif self.level.structure[self.sprite_x][self.sprite_y] == 'ether':
            self.level.structure[self.sprite_x][self.sprite_y] = 'm'
            self.ITEMS.append('ether')
            window.blit(gotether, (20, 50))
            
            
        elif self.level.structure[self.sprite_x][self.sprite_y] == 'tube':
            self.level.structure[self.sprite_x][self.sprite_y] = 'm'
            self.ITEMS.append('tube')
            window.blit(gottube, (20, 50))
           

    def end(self, level, window):
        """We check here if the player has what's necessary to win"""
        gotall = pygame.image.load(got_all).convert_alpha() 
        loser = pygame.image.load(lose).convert_alpha()

        if level.structure[self.sprite_x][self.sprite_y] == 'f':
            if len(self.ITEMS) < 3:
                window.blit(loser, (20, 50))
                pygame.display.flip()
                time.sleep(2)
                exit()
            elif len(self.ITEMS) == 3:
                window.blit(gotall, (20, 50))
                pygame.display.flip()
                time.sleep(2)
                exit()
            

class Item:
    """Classwhich place the items on the map"""
    def __init__ (self, image,name, level):
        self.image = pygame.image.load(image).convert_alpha()
        self.level = level
        self.sprite_x = 0 
        self.sprite_y = 0 
        self.x = 0
        self.y = 0
        self.name = name
    

    def place_item(self):
        """Creates a list of all the free sprites and place the items at those coordinates"""
        position = []
        coordinates = ()
        for k, line in enumerate(self.level.structure):
            for j, sprite in enumerate(line):
                if self.level.structure[k][j] == '0':
                    coordinates = (k, j)
                    position.append(coordinates)

        item_coordinates = random.choice(position)
        self.sprite_y = item_coordinates[0]
        self.sprite_x = item_coordinates[1]
        self.x = self.sprite_x * sprite_size
        self.y = self.sprite_y * sprite_size
        self.level.structure[self.sprite_x][self.sprite_y] = self.name

        
    def display_item(self, window):
        """Place the image of the item"""
        if self.level.structure[self.sprite_x][self.sprite_y] == self.name:
            window.blit(self.image, (self.x, self.y))
