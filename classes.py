"""The labyritnh's classes"""

import pygame
from pygame.locals import *
from constantes import *

class Map:
	"""Classe permettant de créer la map"""
	def __init__(self,fichier):
		self.fichier = fichier
		self.structure = 0

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




