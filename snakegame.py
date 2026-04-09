import pygame as pg
import random as rn

pg.init()

# Colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Window size
scr_wid = 900
scr_hei = 600

pg.display.set_caption("Snake Game")
gameWindow = pg.display.set_mode((scr_wid, scr_hei))

# Game variables
exit_game = False
snake_x = 100
snake_y = 100
velocity_x = 0
velocity_y = 0
snake_size = 15
fps = 30

food_x = rn.randint(20, scr_wid - 20)
food_y = rn.randint(20, scr_hei - 20)

score = 0

clock = pg.time.Clock()
font = pg.font.SysFont(None, 40)

# Function to display text
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

# Function to draw snake
def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pg.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

snk_list = []
snk_length = 1

# Game loop
while not exit_game:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit_game = True

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                velocity_x = 10
                velocity_y = 0

            elif event.key == pg.K_LEFT:
                velocity_x = -10
                velocity_y = 0

            elif event.key == pg.K_UP:
                velocity_y = -10
                velocity_x = 0

            elif event.key == pg.K_DOWN:
                velocity_y = 10
                velocity_x = 0

    snake_x += velocity_x
    snake_y += velocity_y

    # Game over if snake hits wall
    if snake_x < 0 or snake_x > scr_wid or snake_y < 0 or snake_y > scr_hei:
        gameWindow.fill(black)
        text_screen("Game Over!", red, 350, 250)
        pg.display.update()
        pg.time.wait(2000)
        exit_game = True

    # Check food collision
    if abs(snake_x - food_x) < 12 and abs(snake_y - food_y) < 12:
        score += 1
        food_x = rn.randint(20, scr_wid - 20)
        food_y = rn.randint(20, scr_hei - 20)
        snk_length += 5

    gameWindow.fill(black)

    text_screen(f"Score: {score}", red, 5, 5)

    pg.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

    head = [snake_x, snake_y]
    snk_list.append(head)

    if len(snk_list) > snk_length:
        del snk_list[0]

    plot_snake(gameWindow, white, snk_list, snake_size)

    pg.display.update()
    clock.tick(fps)

pg.quit()
quit()
