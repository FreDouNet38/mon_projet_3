#!/usr/bin/python3
# -*- coding: Utf-8 -*

""" The labyrinth game """

import pygame
from pygame.locals import *
from constantes import *
from classes import *
import random

pygame.init()

#Ouverture de la fenêtre
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))

pygame.display.set_caption(titre_fenetre)



niveau = Map('niveau.txt')
niveau.generer()
niveau.afficher(fenetre)

mg = Perso("images/MacGyver.png", niveau)
fenetre.blit(mg.perso, (mg.x, mg.y))

aiguille = Item("images/aiguille.png", "aiguille", niveau)
aiguille.place_item()

ether = Item("images/ether.png", "ether", niveau)
ether.place_item()

tube = Item("images/tube_plastique.png", "tube", niveau)
tube.place_item()

continuer = 1
while continuer:
    ITEMS = []
    pygame.time.Clock().tick(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0

        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                mg.deplacer('droite')

        elif event.key == K_LEFT:
            mg.deplacer('gauche')

        elif event.key == K_UP:
            mg.deplacer('haut')

        elif event.key == K_DOWN:
            mg.deplacer('bas')

    niveau.afficher(fenetre)
    fenetre.blit(mg.perso, (mg.x, mg.y))
    aiguille.get_item(fenetre, mg, ITEMS)
    ether.get_item(fenetre, mg, ITEMS)
    tube.get_item(fenetre, mg, ITEMS)
    pygame.display.flip()

    if niveau.structure[mg.case_x][mg.case_y] == 'f':
        if len(ITEMS) < 2:
            print("you lose")
            continuer = 0
        if len(ITEMS) == 3:
            print("you win")
            continuer = 0
