import pygame
from settings import WHITE, SCREEN_HEIGHT, SCREEN_WIDTH, CAPTION, FONT_SIZE, BLACK
from entities import Ball, Player


def set_up_screen():
    screen = configure_screen()
    background = configure_background()
    set_caption()
    font = configure_font()
    return background, font, screen


def instantiate_game_entities(screen):
    ball = Ball(screen)
    player = Player(screen)
    sprite_group = create_sprite_group(ball, player)
    return ball, player, sprite_group


def show_end_screen(player, screen, font):
    screen.fill(WHITE)
    game_over, points, try_again = render_end_screen_text(font, player)
    blit_end_screen_text(game_over, points, screen, try_again)


def check_for_restart(player, ball):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        game_over = False
        restart(player, ball)
        return game_over


def restart(player, ball):
    player.restart()
    ball.restart()


def configure_background():
    background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    background.fill(WHITE)
    return background


def configure_font():
    font = pygame.font.SysFont('arial', FONT_SIZE)
    return font


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


def detect_game_over(ball, game_over):
    if ball.rect.top > SCREEN_HEIGHT:
        game_over = True
    return game_over


def create_sprite_group(ball, player):
    sprite_group = pygame.sprite.Group()
    sprite_group.add(ball)
    sprite_group.add(player)
    return sprite_group


def display_running_game(font, player, screen, sprite_group):
    sprite_group.draw(screen)
    points = font.render("Punkte: " + str(player.score), True, BLACK)
    screen.blit(points, (20, 20))


def blit_end_screen_text(game_over, points, screen, try_again):
    screen.blit(game_over, center_plus_x(game_over, -FONT_SIZE))
    screen.blit(try_again, center_plus_x(try_again))
    screen.blit(points, center_plus_x(points, FONT_SIZE))


def render_end_screen_text(font, player):
    game_over = font.render('Game Over', True, 'black')
    try_again = font.render('Press SPACEBAR key to try again', True, 'black')
    points = font.render("Punkte: " + str(player.score), True, 'black')
    return game_over, points, try_again

def check_python_version():
    if version_info[0] < 3:
        raise ImportError('Only Python 3 is supported.')

def center_plus_x(text, x=0):
    return SCREEN_WIDTH / 2 - text.get_width() / 2, (SCREEN_HEIGHT / 2 - text.get_height() / 2)+x


def set_caption():
    pygame.display.set_caption(CAPTION)


def configure_screen():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    return screen