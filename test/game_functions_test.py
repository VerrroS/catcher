#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import pygame
from game import Game
import game_functions as gf
from entities import Player, Ball


class TestGf(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.game = Game()
        self.player = Player(self.game)
        self.ball = Ball(self.game)

    def test_collision(self):
        self.player.rect.x = 0
        self.player.rect.y = 0
        self.ball.rect.x = 0
        self.ball.rect.y = 0
        actual = gf.detect_collision(self.ball, self.player)
        self.assertEqual(actual, True)


if __name__ == '__main__':
    unittest.main()
