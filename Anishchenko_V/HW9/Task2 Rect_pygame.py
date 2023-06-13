import pygame

# NB for Liubov: changes in line 23, introduction of variable
#                'screen size' in line 33 and moving 'WIDTH_DISPLAY' and
#                'HEIGHT_DISPLAY' to line 34-35 is to ensure that if the
#                gamescreen is resized by the user, the retangle still
#                behaves as required by the Task terms.
FPS = 60

COORD_X = 50
COORD_Y = 50
WIDTH_RECTANGLE = 40
HEIGHT_RECTANGLE = 60
DELTA_STEP = 5

BLACK_COLOR = (0, 0, 0)
RED_COLOR = (250, 0, 0)

pygame.init()


gameDisplay = pygame.display.set_mode(
    (500, 500), pygame.RESIZABLE)


pygame.display.set_caption("My first game")


run = True
clock = pygame.time.Clock()

while run:
    screen_size = pygame.display.get_window_size()
    WIDTH_DISPLAY = screen_size[0]
    HEIGHT_DISPLAY = screen_size[1]
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and COORD_X >= DELTA_STEP * 2:
        COORD_X = COORD_X-DELTA_STEP
    if keys[pygame.K_RIGHT] and COORD_X <= WIDTH_DISPLAY - (WIDTH_RECTANGLE + DELTA_STEP * 2):
        COORD_X = COORD_X+DELTA_STEP
    if keys[pygame.K_UP] and COORD_Y >= DELTA_STEP * 2:
        COORD_Y = COORD_Y-DELTA_STEP
    if keys[pygame.K_DOWN] and COORD_Y <= HEIGHT_DISPLAY - (HEIGHT_RECTANGLE + DELTA_STEP * 2):
        COORD_Y = COORD_Y+DELTA_STEP

    gameDisplay.fill(BLACK_COLOR)

    pygame.draw.rect(gameDisplay, RED_COLOR, [COORD_X,
                                              COORD_Y,
                                              WIDTH_RECTANGLE,
                                              HEIGHT_RECTANGLE])
    pygame.display.update()
    clock.tick(FPS)
