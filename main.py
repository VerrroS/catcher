#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'simmering'

# IDEA
# Import and Initialization
import random
import pygame
pygame.init()

# Display configuration
size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Test')
background = pygame.Surface(size)
background.fill((255, 255, 255))


# Entities
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.left = random.randint(0, size[0])
        self.rect.top = 0
        self.vel_x = 5
        self.vel_y = 5


    def update(self, hit=False):
        if self.rect.right >= size[0] or self.rect.left <= 0:
            self.vel_x *= -1
        if self.rect.top < 0 or hit:
            self.vel_y *= -1
        self.rect.top += self.vel_y
        self.rect.left += self.vel_x


    def destroy(self):
        self.kill()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 20))
        self.rect = self.image.get_rect()
        self.rect.top = size[1] - 20
        self.rect.left = 320
        self.speed = 10
        self.score = 0
        self.level = 1

    def update(self, direction):
        self.image.fill((0, 0, 0))
        if direction == 'left':
            self.rect.left -= self.speed
        if direction == 'right':
            self.rect.left += self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 640:
            self.rect.right = 640

    def catch(self):
        self.score += 1
        self.image.fill((0, 255, 0))




ball = Ball()
player = Player()

sprite_group = pygame.sprite.Group()
sprite_group.add(ball)
sprite_group.add(player)

font = pygame.font.Font(None, 25)

# Action --> ALTER
# Assign Variables
KeepGoing = True
clock = pygame.time.Clock()

# Loop
while KeepGoing:
    # Timer
    clock.tick(30)
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            KeepGoing = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.update('left')
    if keys[pygame.K_RIGHT]:
        player.update('right')
    ball.update()

    # Collision Detection
    if player.rect.colliderect(ball.rect):
        ball.update(hit=True)
        player.catch()

    if ball.rect.top > size[1]:
        ball.destroy()
        # create new ball
        ball = Ball()
        sprite_group.add(ball)

    screen.blit(background, (0, 0))
    sprite_group.draw(screen)
    punkte = font.render("Punkte: " + str(player.score), 1, 'black')
    screen.blit(punkte, (20, 20))
    level = font.render("Level: " + str(player.level), 1, 'black')
    screen.blit(level, (20, 40))
    pygame.display.update()
