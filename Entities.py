import random
import pygame
from pygame.sprite import Sprite
from settings import BLACK, GREEN, SCREEN_HEIGHT, SCREEN_WIDTH, SPEED, BUFFER

class Entity(Sprite):
    """
    Class to represent an entity

    """
    def __init__(self, screen, width, height):
        Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.screen = screen
        self.image.fill(BLACK)


class Ball(Entity):
    """
    Class to represent the ball
    ...
    Methods
    -------
    update() - updates the ball's position
    restart() - resets the ball's position
    """
    def __init__(self, screen):
        Entity.__init__(self, screen, 20, 20)
        self.rect.left = random.randint(0 + BUFFER, SCREEN_WIDTH- BUFFER)
        self.rect.top = 0
        self.vel_x = SPEED
        self.vel_y = SPEED

    def update(self, hit=False):
        if self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:
            self.vel_x *= -1
        if self.rect.top < 0 or hit:
            self.vel_y *= -1
        self.rect.top += self.vel_y
        self.rect.left += self.vel_x

    def restart(self):
        self.rect.left = random.randint(0, SCREEN_WIDTH)
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
    def __init__(self, screen):
        Entity.__init__(self, screen, 50, 50)
        self.rect.top = SCREEN_HEIGHT - 20
        self.rect.left = SCREEN_WIDTH/2
        self.speed = 10
        self.score = 0

    def update(self, direction):
        self.image.fill(BLACK)
        self.move(direction)

    def move(self, direction):
        if direction == 'left':
            self.move_left()
        if direction == 'right':
            self.move_right()

    def move_right(self):
        self.rect.left += self.speed
        self.rect.right = min(self.rect.right, SCREEN_WIDTH)

    def move_left(self):
        self.rect.left -= self.speed
        self.rect.left = max(self.rect.left, 0)

    def update_score(self):
        self.score += 1
        self.image.fill(GREEN)

    def restart(self):
        self.rect.top = SCREEN_HEIGHT - 20
        self.rect.left = SCREEN_WIDTH/2
        self.score = 0
