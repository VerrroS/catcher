#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'simmering'

import pygame
from settings import FPS, TOP_LEFT_CORNER
import game_functions as gf


def run_game():
    """
    run the game

    """
    pygame.init()
    background, font, screen = gf.set_up_screen()
    ball, player, sprite_group = gf.instantiate_game_entities(screen)

    program_running = True
    game_over = False

    clock = pygame.time.Clock()

    while program_running:
        # Timer
        clock.tick(FPS)
        program_running = gf.check_for_quit(program_running)
        gf.move_player(player)
        ball.update()
        gf.detect_collision(ball, player)

        screen.blit(background, TOP_LEFT_CORNER)
        game_over = gf.detect_game_over(ball, game_over)

        if game_over:
            gf.show_end_screen(player, screen, font)
            game_over = gf.check_for_restart(player, ball)
        else:
            gf.display_running_game(font, player, screen, sprite_group)

        pygame.display.update()


run_game()
