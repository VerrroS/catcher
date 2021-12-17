#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest



class TestGf(unittest.TestCase):
    def setUp(self):
        pass

    #def test_collision(self):
        #self.player.rect.x = 0
        #self.player.rect.y = 0
        #self.ball.rect.x = 0
        #self.ball.rect.y = 0
        #actual = gf.detect_collision(self.ball, self.player)
        #self.assertEqual(actual, True)


    def test_test(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
  unittest.main()
