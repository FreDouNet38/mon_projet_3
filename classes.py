"""The labyritnh's classes"""

import pygame
from pygame.locals import *
from constantes import *
import random

class Map:
    """Class which allow the creation of the map"""
    def __init__(self,folder):
        self.folder = folder
        self.structure = []
    
    def generate(self):
        with open(self.folder, "r") as folder:
            level_structure = []
            for line in folder:
                level_line = []
                for sprite in line:
                    if sprite != '\n':
                        level_line.append(sprite)
                level_structure.append(level_line)
            self.structure = level_structure

    def show(self, window):
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
    def deplacer(self, direction):
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

    def check_item(self, name):
        if self.level.structure[self.sprite_x][self.sprite_y] == 'needle':
            self.level.structure[self.sprite_x][self.sprite_y] = '0'
            self.ITEMS.append('needle')
            print("Good you've got the needle")
            if len(self.ITEMS) == 3:
                print("You can make the guard sleep with that seringe full of ether :)")
        elif self.level.structure[self.sprite_x][self.sprite_y] == 'ether':
            self.level.structure[self.sprite_x][self.sprite_y] = '0'
            self.ITEMS.append('ether')
            print("Nice! You've found some ether")
            if len(self.ITEMS) == 3:
                print("You can make the guard sleep with that seringe full of ether :)")
        elif self.level.structure[self.sprite_x][self.sprite_y] == 'tube':
            self.level.structure[self.sprite_x][self.sprite_y] = '0'
            self.ITEMS.append('tube')
            print("You've got the tube you need to make the seringe")
            if len(self.ITEMS) == 3:
                print("You can make the guard sleep with that seringe full of ether :)")


class Item:
    """Classe permettant de placer les items sur la map"""
    def __init__ (self, image,name, level):
        self.image = pygame.image.load(image).convert_alpha()
        self.level = level
        self.sprite_x = 0 
        self.sprite_y = 0 
        self.x = 0
        self.y = 0
        self.name = name
    

    def place_item(self):
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
        if self.level.structure[self.sprite_x][self.sprite_y] == self.name:
            window.blit(self.image, (self.x, self.y))            