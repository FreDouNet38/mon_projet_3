#!/usr/bin/python3
# -*- coding: Utf-8 -*

#pylint: disable=wildcard-import, no-member, undefined-variable, unused-wildcard-import, invalid-name

""" The labyrinth game """

import pygame
from pygame.locals import *
from constants import SIDE, WINDOW_TITLE, IMAGE_MAC, IMAGE_NEEDLE, IMAGE_ETHER, IMAGE_TUBE
from classes import *

pygame.init()

def main():
    """The main function"""
    #To open the window
    window = pygame.display.set_mode((SIDE, SIDE))
    pygame.display.set_caption(WINDOW_TITLE)

    #To display the level
    level = Map('level.txt')
    level.generate()
    level.show(window)

    #To display MacGyver
    mg = Player(IMAGE_MAC, level)
    window.blit(mg.player, (mg.x, mg.y))

    #To display the items
    needle = Item(IMAGE_NEEDLE, "needle", level)
    needle.place_item()

    ether = Item(IMAGE_ETHER, "ether", level)
    ether.place_item()

    tube = Item(IMAGE_TUBE, "tube", level)
    tube.place_item()


    #Game loop
    while True:
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            if event.type == QUIT:
                return

            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    mg.move('right')

                elif event.key == K_LEFT:
                    mg.move('left')

                elif event.key == K_UP:
                    mg.move('up')

                elif event.key == K_DOWN:
                    mg.move('down')


        needle.display_item(window)
        ether.display_item(window)
        tube.display_item(window)
        mg.check_item(window)
        mg.end(level, window)


        level.show(window)
        window.blit(mg.player, (mg.x, mg.y))
        pygame.display.flip()







if __name__ == '__main__':
    main()
