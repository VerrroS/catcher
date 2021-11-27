from sys import version_info
import pygame
from entities import Ball, Player


def instantiate_game_entities(game):
    ball = Ball(game)
    player = Player(game)
    sprite_group = create_sprite_group(ball, player)
    return ball, player, sprite_group


def create_sprite_group(ball, player):
    sprite_group = pygame.sprite.Group()
    sprite_group.add(ball)
    sprite_group.add(player)
    return sprite_group


def display_running_game(game, player, sprite_group):
    sprite_group.draw(game.screen)
    points = game.font.render("Punkte: " + str(player.score), True, game.fg_color)
    game.screen.blit(points, (20, 20))


def show_end_screen(game, player):
    game.screen.fill(game.bg_color)
    game_over, points, try_again = render_end_screen_text(game.font, player)
    blit_end_screen_text(game, game_over, points, try_again)


def blit_end_screen_text(game, game_over, points, try_again):
    game.screen.blit(game_over, center_plus_x(game, game_over, -game.font_size))
    game.screen.blit(try_again, center_plus_x(game, try_again))
    game.screen.blit(points, center_plus_x(game, points, game.font_size))


def render_end_screen_text(font, player):
    game_over = font.render('Game Over', True, 'black')
    try_again = font.render('Press SPACEBAR key to try again', True, 'black')
    points = font.render("Punkte: " + str(player.score), True, 'black')
    return game_over, points, try_again


def check_for_restart(player, ball):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        game_over = False
        restart(player, ball)
        return game_over


def restart(player, ball):
    player.restart()
    ball.restart()


def move_player(player):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.update('left')
    if keys[pygame.K_RIGHT]:
        player.update('right')


def check_for_quit(program_running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_running = False
    return program_running


def detect_collision(ball, player):
    if player.rect.colliderect(ball.rect):
        ball.update(hit=True)
        player.update_score()


def detect_game_over(game, ball, game_over):
    if ball.rect.top > game.screen_height:
        game_over = True
    return game_over


def center_plus_x(game, text, x=0):
    return game.screen_width / 2 - text.get_width() / 2, (game.screen_height / 2 - text.get_height() / 2) + x



def check_python_version():
    if version_info[0] < 3:
        raise ImportError('Only Python 3 is supported.')


