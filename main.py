#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'simmering'

# IDEA
# Import and Initialization
import pygame
import random
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
        self.speed = 5

    def update(self):
        self.rect.top += self.speed
        if self.rect.top < 0:
            self.speed = -self.speed

    def destroy(self):
        self.kill()



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 20))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.top = size[1] - 20
        self.rect.left = 320
        self.speed = 10
        self.score = 0

    def update(self, direction):
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


ball = Ball()
player = Player()

sprite_group = pygame.sprite.Group()
sprite_group.add(ball)
sprite_group.add(player)

font = pygame.font.Font(None, 25)

# Action --> ALTER
# Assign Variables
keepGoing = True
clock = pygame.time.Clock()

# Loop
while keepGoing:
    # Timer
    clock.tick(30)
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.update('left')
    if keys[pygame.K_RIGHT]:
        player.update('right')
    ball.update()

    if player.rect.colliderect(ball.rect):
        ball.speed = -ball.speed
        player.catch()

    if ball.rect.top > size[1]:
        ball.destroy()
        ball = Ball()
        sprite_group.add(ball)

    screen.blit(background, (0, 0))
    sprite_group.draw(screen)
    text = font.render("Punkte: " + str(player.score), 1, 'black')
    screen.blit(text, (20, 20))
    pygame.display.update()
