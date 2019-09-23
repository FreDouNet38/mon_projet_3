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

mg = Perso(image_mac, niveau)
fenetre.blit(mg.perso, (mg.x, mg.y))

aiguille = Item(image_needle, 'aiguille', niveau)
aiguille.place_item()


ether = Item(image_ether, "ether", niveau)
ether.place_item()


tube = Item(image_tube, "tube", niveau)
tube.place_item()

while True:
    pygame.time.Clock().tick(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            break

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
    aiguille.display_item(fenetre)
    ether.display_item(fenetre)
    tube.display_item(fenetre)
    mg.check_item(aiguille)
    mg.check_item(ether)
    mg.check_item(tube)
    fenetre.blit(mg.perso, (mg.x, mg.y))
    pygame.display.flip()



    if niveau.structure[mg.case_x][mg.case_y] == 'f':
    	if len(mg.ITEMS) < 3:
    		print("you lose")
    		break
    	elif len(mg.ITEMS) == 3:
    		print("you win")
    		break
