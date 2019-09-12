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

niveau = Map('niveau.txt')
niveau.generer()
niveau.afficher(fenetre)
mg = Perso("images/MacGyver.png", niveau)
fenetre.blit(mg.perso,(mg.x, mg.y))

continuer = 1
while continuer:
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
	pygame.display.flip()



