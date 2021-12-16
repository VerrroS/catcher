import random
import pygame
from pygame.sprite import Sprite


class Entity(Sprite):
    """
    Class to represent an entity

    """
    def __init__(self, game, entity_size):
        Sprite.__init__(self)
        self.image = pygame.Surface(entity_size)
        self.rect = self.image.get_rect()
        self.screen_width = game.screen_width
        self.screen_height = game.screen_height
        self.fg_color = game.fg_color
        self.image.fill(self.fg_color)
        self.buffer = game.buffer


class Ball(Entity):
    """
    Class to represent the ball
    ...
    Methods
    -------
    update() - updates the ball's position
    restart() - resets the ball's position
    """
    def __init__(self, game):
        Entity.__init__(self, game, game.ball_size)
        self.rect.left = random.randint(0 + game.buffer, self.screen_width - self.buffer)
        self.rect.top = 0
        self.vel_x = game.ball_speed
        self.vel_y = game.ball_speed

    def update(self, hit=False):
        if self.rect.right >= self.screen_width or self.rect.left <= 0:
            self.vel_x *= -1
        if self.rect.top < 0 or hit:
            self.vel_y *= -1
        self.rect.top += self.vel_y
        self.rect.left += self.vel_x

    def restart(self):
        self.rect.left = random.randint(0, self.screen_width)
        self.rect.top = 0


class Player(Entity):
    """
    Class to represent the player
    ...
    Methods
    -------
    update() - updates the player's position
    move() - moves the player
    move_left() - moves the player left
    move_right() - moves the player right
    update_score() - updates the player's score
    restart() - resets the player's position and score
    """
    def __init__(self, game):
        Entity.__init__(self, game, game.player_size)
        self.rect.top = self.screen_height-self.buffer
        self.rect.left = self.screen_width/2
        self.speed = game.player_speed
        self.score = 0
        self.hl_color = game.hl_color

    def update(self, direction):
        self.image.fill(self.fg_color)
        self.move(direction)

    def move(self, direction):
        if direction == 'left':
            self.move_left()
        if direction == 'right':
            self.move_right()

    def move_right(self):
        self.rect.left += self.speed
        self.rect.right = min(self.rect.right, self.screen_width)

    def move_left(self):
        self.rect.left -= self.speed
        self.rect.left = max(self.rect.left, 0)

    def update_score(self):
        self.score += 1
        self.image.fill(self.hl_color)

    def restart(self):
        self.rect.top = self.screen_height-self.buffer
        self.rect.left = self.screen_width/2
        self.score = 0
