#!/usr/bin/python3
# -*- coding: Utf-8 -*

#pylint: disable=wildcard-import, no-member, unused-wildcard-import, undefined-variable

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
    macgyver = Player(IMAGE_MAC, level)
    window.blit(macgyver.player, (macgyver.x, macgyver.y))

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
                    macgyver.move('right')

                elif event.key == K_LEFT:
                    macgyver.move('left')

                elif event.key == K_UP:
                    macgyver.move('up')

                elif event.key == K_DOWN:
                    macgyver.move('down')

        level.show(window)
        needle.display_item(window)
        ether.display_item(window)
        tube.display_item(window)
        window.blit(macgyver.player, (macgyver.x, macgyver.y))
        macgyver.check_item(window)
        macgyver.end(level, window)
        pygame.display.flip()

if __name__ == '__main__':
    main()
