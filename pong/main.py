import pygame
import random

WIDTH = 650
HEIGHT = 480
FPS = 165

player_1_score = 0
player_2_score = 0

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
y = 50

y2 = 50

ball_x = 325
ball_y = 240
dx = random.choice((-2, 2))
dy = random.choice((-2, 2))
## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pong :)")
clock = pygame.time.Clock()  ## For syncing the FPS

font = pygame.font.Font("entangled.plain-brk.ttf", 72)

## Game loop
running = True
while running:
    paddle1 = pygame.Rect(15,y,15,100)
    paddle2 = pygame.Rect(620, y2, 15, 100)

    ball_x += dx
    ball_y += dy
    ball = pygame.Rect(ball_x, ball_y, 15, 15)

    if ball_y < 0 or ball_y > 465:
        dy *= -1.01
    if ball.colliderect(paddle1):
        dx *= -1.01
        ball_x = paddle1.right
    if ball.colliderect(paddle2):
        dx *= -1.01
        ball_x = paddle2.left - 15

    if ball_x < 0:
        ball_x = 325
        dx = -2
        ball_y = 240
        dy = random.choice((-2, 2))
        player_2_score +=1

    if ball_x > 625:
        ball_x = 325
        dx = 2
        ball_y = 240
        dy = random.choice((-2, 2))
        player_1_score +=1

    text = font.render(str(player_1_score) + "  |  " + str(player_2_score), True, pygame.Color("White"))

    # 1 Process input/events
    clock.tick(FPS)  ## will make the loop run at the same speed all the time
    for event in pygame.event.get():  # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y -= 4
    elif keys[pygame.K_s]:
        y += 4
    if y < 0:
        y = 0
    if y > 380:
        y = 380

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y2 -= 4
    elif keys[pygame.K_DOWN]:
        y2 += 4
    if y2 < 0:
        y2 = 0
    if y2 > 380:
        y2 = 380

    # 3 Draw/render
    screen.fill(BLACK)
    screen.blit(text, (210,10))

    pygame.draw.rect(screen, pygame.Color("White"), paddle1)
    pygame.draw.rect(screen, pygame.Color("White"), paddle2)
    pygame.draw.rect(screen, pygame.Color("White"), ball)
    pygame.display.flip()

pygame.quit()


