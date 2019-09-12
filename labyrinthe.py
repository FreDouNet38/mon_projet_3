#!/usr/bin/python3
# -*- coding: Utf-8 -*

""" The labyrinth game """

import pygame
from pygame.locals import *
from constantes import *
from classes import *

pygame.init()

#Ouverture de la fenêtre
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))

pygame.display.set_caption(titre_fenetre)

continuer = 1
while continuer:
	pygame.time.Clock().tick(30)
	niveau = Map('niveau.txt')
	niveau.generer()
	niveau.afficher(fenetre)
	pygame.display.flip()

	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0


