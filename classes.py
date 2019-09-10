"""The labyritnh's classes"""

import pygame
from pygame.locals import *
from constantes import *

class Map:
	"""Classe permettant de créer la map"""
	def __init__(self,fichier):
		self.fichier = fichier
		self.structure = 0