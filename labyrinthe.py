#!/usr/bin/python3
# -*- coding: Utf-8 -*

""" The labyrinth game """

import pygame
from pygame.locals import *
from constantes import *
from classes import *
import random

pygame.init()

def main():
    #To open the window
    window = pygame.display.set_mode((side, side))
    pygame.display.set_caption(window_title)

    #To display the level
    level = Map('niveau.txt')
    level.generate()
    level.show(window)

    #To display MacGyver
    mg = Player(image_mac, level)
    window.blit(mg.player, (mg.x, mg.y))

    #To display the items
    needle = Item(image_needle, "needle", level)
    needle.place_item()

    ether = Item(image_ether, "ether", level)
    ether.place_item()

    tube = Item(image_tube, "tube", level)
    tube.place_item()


    #Game loop
    while True:
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    mg.move('right')

                elif event.key == K_LEFT:
                    mg.move('left')

                elif event.key == K_UP:
                    mg.move('up')

                elif event.key == K_DOWN:
                    mg.move('down')

        level.show(window)
        needle.display_item(window)
        ether.display_item(window)
        tube.display_item(window)
        mg.check_item(needle, window)
        mg.check_item(ether, window)
        mg.check_item(tube, window)
        mg.end(level, window)
        window.blit(mg.player, (mg.x, mg.y))
        pygame.display.flip()

if __name__ == '__main__':
    main()

