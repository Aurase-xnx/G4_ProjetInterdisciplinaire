__all__ = ['main']

import os
import sys

import pygame
import pygame_menu
from pygame_menu.examples import create_example_window

from random import randrange
from typing import Tuple, Any, Optional, List

# Var
FPS = 60
WINDOW_SIZE = (1280, 720)

clock: Optional['pygame.time.Clock'] = None
main_menu: Optional['pygame_menu.Menu'] = None
surface: Optional['pygame.Surface'] = None





def invader_special():
    os.system(os.path.join(os.getcwd(),"Pac-Patrouille", "pacpatrouille.py"))


def main_background() -> None:
    """
    Function used by menus, draw on background while menu is active.

    :return: None
    """
    global surface
    surface.fill((128, 0, 128))


def pac2pac():
    os.system(os.path.join(os.getcwd(),"pacman", "pacman.pyw"))


def main(test: bool = False) -> None:
    """
    Main program.

    :param test: Indicate function is being tested
    :return: None
    """

    # -------------------------------------------------------------------------
    # Globals
    # -------------------------------------------------------------------------
    global clock
    global main_menu
    global surface

    # -------------------------------------------------------------------------
    # Create window
    # -------------------------------------------------------------------------
    surface = create_example_window('2PacMan', WINDOW_SIZE)
    clock = pygame.time.Clock()

    # -------------------------------------------------------------------------
    # Create menus: Play Menu
    # -------------------------------------------------------------------------
    play_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 1,
        title='Jouer au jeu !',
        width=WINDOW_SIZE[0] * 1
    )

    global user_name

    submenu_theme = pygame_menu.themes.THEME_DEFAULT.copy()
    # submenu_theme.widget_font_size = 15
    play_submenu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 1,
        theme=submenu_theme,
        title='Mode spécial',
        width=WINDOW_SIZE[0] * 1
    )
    play_submenu.add.button('Mode Pac Patrouille', invader_special)
    play_submenu.add.button('Retour', pygame_menu.events.BACK)

    # user_name = play_menu.add.text_input('Name: ', default='John Doe', maxchar=10)
    # Essai d'exporter un nom choisi vers le programme du jeu
    play_menu.add.button('Jouer !', pac2pac)
    play_menu.add.button('Secrets', play_submenu)
    play_menu.add.button('Retour', pygame_menu.events.BACK)

    # -------------------------------------------------------------------------
    # Create menus:About
    # -------------------------------------------------------------------------
    about_theme = pygame_menu.themes.THEME_DEFAULT.copy()
    about_theme.widget_margin = (0, 0)

    about_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 1,
        theme=about_theme,
        title='A propos',
        width=WINDOW_SIZE[0] * 1
    )

    about_menu.add.label('Groupe 4')
    about_menu.add.button('Retour', pygame_menu.events.BACK)

    # -------------------------------------------------------------------------
    # Create menus: Main
    # -------------------------------------------------------------------------
    main_theme = pygame_menu.themes.THEME_DEFAULT.copy()

    main_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 1,
        theme=main_theme,
        title='Menu principal',
        width=WINDOW_SIZE[0] * 1
    )

    main_menu.add.button('Jouer', play_menu)
    main_menu.add.button('A propos', about_menu)
    main_menu.add.button('Quitter', pygame_menu.events.EXIT)

    # -------------------------------------------------------------------------
    # Main loop
    # -------------------------------------------------------------------------
    while True:

        # Tick
        clock.tick(FPS)

        # Paint background
        main_background()

        # Application events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        # Main menu
        if main_menu.is_enabled():
            main_menu.mainloop(surface, main_background,
                               disable_loop=test, fps_limit=FPS)

        # Flip surface
        pygame.display.flip()

        # At first loop returns
        if test:
            break


if __name__ == '__main__':
    main()
