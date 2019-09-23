"""The labyritnh's classes"""

import pygame
from pygame.locals import *
from constantes import *
import random

class Map:
    """Classe permettant de créer la map"""
    def __init__(self,fichier):
        self.fichier = fichier
        self.structure = []
    
    def generer(self):
        with open(self.fichier, "r") as fichier:
            structure_niveau = []
            for ligne in fichier:
                ligne_niveau = []
                for sprite in ligne:
                    if sprite != '\n':
                        ligne_niveau.append(sprite)
                structure_niveau.append(ligne_niveau)
            self.structure = structure_niveau

    def afficher(self, fenetre):
        mur = pygame.image.load(image_wall).convert_alpha()
        sol = pygame.image.load(image_floor).convert_alpha()
        gardien = pygame.image.load(image_guard).convert_alpha()

        num_ligne = 0
        for ligne in self.structure:
            num_case = 0
            for sprite in ligne:
                x = num_case * taille_sprite
                y = num_ligne * taille_sprite
                if sprite == 'm':
                    fenetre.blit(mur, (x, y))
                elif sprite == '0':
                    fenetre.blit(sol, (x, y))
                elif sprite == 'f':
                    fenetre.blit(gardien, (x, y))
                num_case += 1
            num_ligne += 1

    
class Perso:
    """Classe permettant de créer le personnage du jeu"""
    def __init__(self, perso, niveau):
        self.perso = pygame.image.load(perso).convert_alpha()
        self.niveau = niveau
        #Position en case et en pixels
        self.case_x = 0
        self.case_y = 0 
        self.x = 0
        self.y = 0
        self.ITEMS = []
    def deplacer(self, direction):
        if direction == 'droite':
            #On verifie qu'il ne sort pas de la map
            if self.case_x < (nombre_sprite_cote - 1):
                #On vérifie que ce ne soit pas un mur
                if self.niveau.structure[self.case_y][self.case_x+1] != 'm':
                    self.case_x += 1
                    self.x = self.case_x * taille_sprite
            

        if direction == 'gauche':
            if self.case_x > 0:
                if self.niveau.structure[self.case_y][self.case_x-1] != 'm':
                    self.case_x -= 1
                    self.x = self.case_x * taille_sprite

        if direction == 'haut':
            if self.case_y > 0:
                if self.niveau.structure[self.case_y-1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.y = self.case_y * taille_sprite

        if direction == 'bas':
            if self.case_y < (nombre_sprite_cote - 1):
                if self.niveau.structure[self.case_y+1][self.case_x] != 'm':
                    self.case_y += 1
                    self.y = self.case_y * taille_sprite

    def check_item(self, name):
        if self.niveau.structure[self.case_x][self.case_y] == 'aiguille':
            self.niveau.structure[self.case_x][self.case_y] = '0'
            self.ITEMS.append('aiguille')
        elif self.niveau.structure[self.case_x][self.case_y] == 'ether':
            self.ITEMS.append('ether')
            self.niveau.structure[self.case_x][self.case_y] = '0'
        elif self.niveau.structure[self.case_x][self.case_y] == 'tube':
            self.ITEMS.append('tube')
            self.niveau.structure[self.case_x][self.case_y] = '0'
        return len(self.ITEMS)


class Item:
    """Classe permettant de placer les items sur la map"""
    def __init__ (self, image,name, niveau):
        self.image = pygame.image.load(image).convert_alpha()
        
        self.niveau = niveau
        self.case_x = 0 
        self.case_y = 0 
        self.x = 0
        self.y = 0
        self.name = name
    

    def place_item(self):
        position = []
        coordinates = ()
        num_ligne = 0
        while num_ligne < len(self.niveau.structure):
            num_case = 1
            while num_case < len(self.niveau.structure[0]):
                if self.niveau.structure[num_ligne][num_case] == '0':
                    coordinates = (num_ligne, num_case)
                    position.append(coordinates)
                num_case += 1
            num_ligne += 1

        item_coordinates = random.choice(position)
        self.case_y = item_coordinates[0]
        self.case_x = item_coordinates[1]
        self.x = self.case_x * taille_sprite
        self.y = self.case_y * taille_sprite
        self.niveau.structure[self.case_x][self.case_y] = self.name

        
    def display_item(self, fenetre):
        if self.niveau.structure[self.case_x][self.case_y] == self.name:
            fenetre.blit(self.image, (self.x, self.y))            