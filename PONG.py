import pygame
from pygame import mixer

clock = pygame.time.Clock()
pygame.init()
# WINDOW UPDATED
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("PONG")
wall = pygame.image.load("space.png")
pygame.display.set_icon(wall)

player = pygame.Rect((0, screen_height / 2, 10, 50))
player_speed = 0


def player_motion():
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


comp = pygame.Rect((screen_width - 10, screen_height / 2, 10, 50))
comp_speed = 6


def comp_motion():
    if comp.top < ball.y:
        comp.y += comp_speed
    if comp.bottom > ball.y:
        comp.bottom -= comp_speed


ball = pygame.Rect((screen_width / 2 - 15, screen_height / 2 - 15, 10, 10))
ball_speed_x = 5
ball_speed_y = 4


def ball_motion():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    player.y += player_speed

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1

    if ball.colliderect(player) or ball.colliderect(comp):
        ball_speed_x *= -1


player_score = 0
comp_score = 0

mixer.music.load("background_music.mp3")
mixer.music.play(-1)


def Score():
    pla = pygame.font.Font('C:\Program Files (x86)\Adobe\Reader 11.0\Resource\Font\AdobeArabic-Bold.otf', 32)
    pla_x = 10
    pla_y = 10
    pla_score = pla.render(str(player_score), True, (0, 0, 0))
    screen.blit(pla_score, (pla_x, pla_y))

    com = pygame.font.Font('C:\Program Files (x86)\Adobe\Reader 11.0\Resource\Font\AdobeArabic-Bold.otf', 32)
    comp_x = 630
    comp_y = 10
    co_score = com.render(str(comp_score), True, (0, 0, 0))
    screen.blit(co_score, (comp_x, comp_y))


def Winner():
    win = pygame.font.Font('C:\Program Files (x86)\Adobe\Reader 11.0\Resource\Font\AdobeArabic-Bold.otf', 64)
    if player_score == 5:
        ans = win.render("Player Wins The Game", True, (0, 0, 0))
        screen.blit(ans, (300, 300))
        QUIT()
        ball_speed_x, ball_speed_y = 0, 0
    if comp_score == 5:
        ans1 = win.render("Comp Wins The Game", True, (0, 0, 0))
        screen.blit(ans1, (300, 50))
        ball_speed_x, ball_speed_y = 0, 0
        QUIT()


def RESTART():
    if player_score == 5 or comp_score == 5:
        restart_window = pygame.font.Font('C:\Program Files (x86)\Adobe\Reader 11.0\Resource\Font\AdobeArabic-Bold.otf',
                                          22)
        restart = restart_window.render("RESTART__PRESS a", True, (0, 0, 0))
        screen.blit(restart, (screen_width / 2 - 100, 300))


def QUIT():
    if player_score == 5 or comp_score == 5:
        quit_window = pygame.font.Font('C:\Program Files (x86)\Adobe\Reader 11.0\Resource\Font\AdobeArabic-Bold.otf',
                                       22)
        Quit = quit_window.render("QUIT__PRESS q", True, (0, 0, 0))
        screen.blit(Quit, (screen_width / 2 - 100, 500))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 5
            if event.key == pygame.K_UP:
                player_speed -= 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 5
            if event.key == pygame.K_UP:
                player_speed += 5
            if event.key == pygame.K_a:
                player_score = 0
                comp_score = 0
            if event.key == pygame.K_q:
                running = False

    ball_motion()
    player_motion()
    comp_motion()

    screen.fill(("purple"))
    pygame.draw.rect(screen, "Red", player)
    pygame.draw.rect(screen, "navy blue", comp)
    pygame.draw.ellipse(screen, "White", ball)
    # pygame.draw.aaline(screen, "grey35", (screen_width / 2, 0), (screen_width / 2, screen_width))
    pygame.draw.lines(screen, "grey35", False, ([screen_width / 2, 0], [screen_width / 2, screen_width]), 5)
    Score()

    if ball.x == 0:
        comp_score += 1
    if ball.x == screen_width - 10:
        player_score += 1
    if player_score>=5 or comp_score>=5:
        ball.x=500
    Winner()
    RESTART()
    QUIT()

    clock.tick(800)
    pygame.display.update()
