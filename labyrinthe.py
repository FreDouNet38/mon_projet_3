#!/usr/bin/python3
# -*- coding: Utf-8 -*

""" The labyrinth game """

import pygame
from pygame.locals import *
from constantes import *
form classes import *

pygame.init()

#Ouverture de la fenêtre
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))

#Affichage du titre
pygame.display.set_caption(titre_fenetre)


