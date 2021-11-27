#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'simmering'

import pygame
from game import Game
import game_functions as gf


def run_game():
    """
    run the game

    This function is the main function of the game. It checks the python version, initializes pygame, initializes the
    display and runs the game loop. While the loop is running , it checks for events and updates the game. When the
    ball is lost to the bottom of the screen, the game is over and the end screen is displayed. The player can restart
    the game by pressing the space bar.
    """
    gf.check_python_version()
    pygame.init()
    game = Game()
    ball, player, sprite_group = gf.instantiate_game_entities(game)

    program_running = True
    game_running = True

    clock = pygame.time.Clock()

    while program_running:
        # Timer
        clock.tick(game.fps)
        program_running = gf.check_for_quit(program_running)
        gf.update_entities(ball, player)
        gf.detect_collision(ball, player)
        game_running = gf.detect_game_over(game, ball, game_running)

        game.screen.blit(game.background, game.top_left_corner)

        if game_running:
            gf.display_running_game(game, player, sprite_group)
        else:
            gf.show_end_screen(game, player)
            game_running = gf.check_for_restart(player, ball)

        pygame.display.update()


if __name__ == '__main__':
    run_game()
