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
    sprite_group.add(ball, player)
    return sprite_group


def display_running_game(game, player, sprite_group):
    sprite_group.draw(game.screen)
    score_text = render_score_text(game, player)
    game.screen.blit(score_text, (game.buffer, game.buffer))


def render_score_text(game, player):
    score_text = game.font.render("Punkte: " + str(player.score), True, game.fg_color)
    return score_text


def show_end_screen(game, player):
    game.screen.fill(game.bg_color)
    end_screen_texts = render_end_screen_text(game.font, player)
    blit_end_screen_text(game, end_screen_texts)


def render_end_screen_text(font, player):
    end_screen_texts = {'game_over': font.render('Game Over', True, 'black'),
                        'end_score': font.render("Punkte: " + str(player.score), True, 'black'),
                        'try_again': font.render('Press SPACEBAR key to try again', True, 'black')}
    return end_screen_texts


def blit_end_screen_text(game, end_screen_text):
    game.screen.blit(end_screen_text['game_over'],
                     center_text_plus_x(game, end_screen_text['game_over'], -game.font_size))
    game.screen.blit(end_screen_text['end_score'],
                     center_text_plus_x(game, end_screen_text['end_score']))
    game.screen.blit(end_screen_text['try_again'],
                     center_text_plus_x(game, end_screen_text['try_again'], game.font_size))


def check_for_restart(player, ball):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        game_running = True
        restart(player, ball)
        return game_running


def restart(player, ball):
    player.restart()
    ball.restart()


def update_entities(ball, player):
    move_player(player)
    ball.update()


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
        return True


def detect_game_over(game, ball, game_running):
    if ball.rect.top > game.screen_height:
        game_running = False
    return game_running


def center_text_plus_x(game, text, x=0):
    return game.screen_width / 2 - text.get_width() / 2, (game.screen_height / 2 - text.get_height() / 2) + x


def check_python_version():
    if version_info[0] < 3:
        raise ImportError('Only Python 3 is supported.')


