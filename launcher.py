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


def play_function(font: 'pygame.font.Font', test: bool = False) -> None:
    """
    Main game function.
    """

    # Define globals
    global main_menu
    global clock

    # Reset main menu and disable
    # You also can set another menu, like a 'pause menu', or just use the same
    # main_menu as the menu that will check all your input.
    main_menu.disable()
    main_menu.full_reset()

    frame = 0

    while True:

        # noinspection PyUnresolvedReferences
        clock.tick(60)
        frame += 1

        # Application events
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    main_menu.enable()

                    # Quit this function, then skip to loop of main-menu on line 256
                    return

        # Pass events to main_menu
        if main_menu.is_enabled():
            main_menu.update(events)

        # Continue playing
        game()

        # If test returns
        if test and frame == 2:
            break


def invader_special():
    # Cool shit
    pass


def main_background() -> None:
    """
    Function used by menus, draw on background while menu is active.

    :return: None
    """
    global surface
    surface.fill((128, 0, 128))


def game():
    os.system("C:/Users/eserd/github/G4_ProjetInterdisciplinaire/pacman/pacman.pyw")
    with open("savegame", "rb") as f:

        pygame.quit()
        sys.exit(0)
        pygame.display.update()


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

    submenu_theme = pygame_menu.themes.THEME_DEFAULT.copy()
    # submenu_theme.widget_font_size = 15
    play_submenu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 1,
        theme=submenu_theme,
        title='Mode spécial',
        width=WINDOW_SIZE[0] * 1
    )
    play_submenu.add.button('Mode Space invader', invader_special)
    play_submenu.add.button('Retour', pygame_menu.events.BACK)

    play_menu.add.button('Jouer !',  # When pressing return -> play(DIFFICULTY[0], font)
                         play_function,
                         pygame_menu.events.EXIT,
                         pygame.font.Font(pygame_menu.font.FONT_FRANCHISE, 30))
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
