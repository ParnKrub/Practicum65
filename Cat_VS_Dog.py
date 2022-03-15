from contextlib import redirect_stderr
import pygame
import math
import random
import os

pygame.font.init()

P_BLUE = 1
P_RED = 2
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cat VS Dog")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FPS = 60
GRAV = 5
BOX_LENGTH = 30
BOX_FPS = 0.15
POWER_FACTOR = 4
WALL_WIDTH = 30
WALL_HEIGHT = HEIGHT//3
WALL = pygame.Rect(WIDTH//2 - WALL_WIDTH//2, HEIGHT -
                   WALL_HEIGHT, WALL_WIDTH, WALL_HEIGHT)
BLUE_POSX = 50
BLUE_POSY = HEIGHT-15
RED_POSX = WIDTH-50
RED_POSY = HEIGHT-15
PLAYER_HEIGHT = 80
PLAYER_WIDTH = 70
BOX_START_POS_BLUE = BLUE_POSX+BOX_LENGTH+1
BOX_START_POS_RED = RED_POSX-BOX_LENGTH-1

# https://www.freepik.com/vectors/alien-planet Alien planet vector created by upklyak
BACKGROUND = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'BG.jpg')), (WIDTH, HEIGHT))
FLOOR = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'platform2.png')), (WIDTH, 25))
GURA = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Gura3.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLIOPE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Calliope3.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))


class Box(object):
    def __init__(self, x, y, length, color):
        self.x = x
        self.y = y
        self.length = length
        self.color = color

    def draw(self, WIN):
        box = pygame.Rect(self.x, self.y, self.length, self.length)
        pygame.draw.rect(WIN, self.color, box)

    def box_path(nowx, starty, velx, vely, time_relative, time_absolute, wind_speed):

        velx += wind_speed
        distX = velx * time_relative
        distY = (vely * time_absolute) + ((-GRAV * (time_absolute**2))/2)

        newX = round(nowx + distX)
        newY = round(starty - distY)

        return (newX, newY)


def draw_window(line, redBox, shoot):
    WIN.blit(BACKGROUND, (0, 0))
    pygame.draw.rect(WIN, BLACK, WALL)
    if shoot:
        redBox.draw(WIN)
    WIN.blit(GURA, (BLUE_POSX, BLUE_POSY-PLAYER_HEIGHT))
    WIN.blit(CALLIOPE, (RED_POSX-PLAYER_WIDTH, RED_POSY-PLAYER_HEIGHT))
    WIN.blit(FLOOR, (0, HEIGHT-15))

    pygame.draw.line(WIN, BLACK, line[0], line[1])
    pygame.display.update()


def find_angle(pos):
    sX = WIDTH//2
    sY = HEIGHT-BOX_LENGTH
    try:
        angle = math.atan((sY-pos[1])/(sX-pos[0]))
    except:
        angle = math.pi/2

    if pos[1] < sY and pos[0] > sX:
        angle = abs(angle)
    elif pos[1] < sY and pos[0] < sX:
        angle = math.pi - abs(angle)
    elif pos[1] > sY and pos[0] < sX:
        angle = math.pi + abs(angle)
    elif pos[1] > sY and pos[0] > sX:
        angle = (math.pi*2) - abs(angle)

    return angle


def block_collide_wall(po):
    if (WIDTH//2 - WALL_WIDTH//2 - WALL_WIDTH < po[0] < WIDTH//2 - WALL_WIDTH//2 + WALL_WIDTH) and (po[1] + BOX_LENGTH > HEIGHT - WALL_HEIGHT):
        return True
    # if (po[0] < 0 or po[0] > WIDTH-BOX_LENGTH):
    #     return True
    return False


# def handle_shooting(box, y, velx, vely,
#                     BOX_FPS, time, wind_speed):

#     shoot = True
#     if box.y < HEIGHT - box.length:
#         time += BOX_FPS
#         if block_collide_wall(Box.box_path(box.x, y, velx, vely,
#                                            BOX_FPS, time, wind_speed)):
#             VEL_PENELTY = random.randint(20, 80)/100
#             velx = -velx*VEL_PENELTY

#             po = Box.box_path(box.x, y, velx, vely,
#                               BOX_FPS, time, wind_speed)
#             box.x = po[0]
#             box.y = po[1]

#     if box.y >= HEIGHT - box.length:
#         shoot = False
#         wind_speed = random.randint(-20, 20)
#         print(wind_speed)
#         box.y = HEIGHT-BOX_LENGTH - 51
#         box.x = BOX_START_POS

#     return (box.x, box.y, shoot, time)


def main():

    clock = pygame.time.Clock()
    redBox = Box(BOX_START_POS_BLUE, HEIGHT-BOX_LENGTH-51, BOX_LENGTH, WHITE)
    wind_speed = random.randint(-20, 20)
    x = 0
    y = 0
    time = 0
    velx = 0
    vely = 0
    shoot = False
    run = True
    player = P_BLUE
    while run:
        clock.tick(FPS)
        pos = pygame.mouse.get_pos()
        line = [(WIDTH//2, HEIGHT-BOX_LENGTH), pos]

        if shoot:
            # nowPos = handle_shooting(redBox, y, velx, vely,
            #                          BOX_FPS, time, wind_speed)
            # redBox.x = nowPos[0]
            # redBox.y = nowPos[1]
            # shoot = nowPos[2]
            # time = nowPos[3]

            # print(redBox.x, redBox.y, shoot)
            if redBox.y < HEIGHT - redBox.length:
                time += BOX_FPS

                if block_collide_wall(Box.box_path(redBox.x, y, velx, vely,
                                                   BOX_FPS, time, wind_speed)):
                    VEL_PENELTY = random.randint(20, 80)/100
                    velx = -velx*VEL_PENELTY

                po = Box.box_path(redBox.x, y, velx, vely,
                                  BOX_FPS, time, wind_speed)
                redBox.x = po[0]
                redBox.y = po[1]
            elif redBox.y >= HEIGHT - redBox.length:
                shoot = False
                wind_speed = random.randint(-20, 20)
                print(wind_speed)
                redBox.y = HEIGHT-BOX_LENGTH - 51
                if player == P_RED:
                    redBox.x = BOX_START_POS_BLUE
                    player = P_BLUE
                else:
                    redBox.x = BOX_START_POS_RED
                    player = P_RED

        draw_window(line, redBox, shoot)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if shoot == False:
                    shoot = True
                    y = redBox.y
                    time = 0
                    power = 250/POWER_FACTOR
                    angle = find_angle(pos)
                    velx = math.cos(angle) * power
                    vely = math.sin(angle) * power

    pygame.quit()


if __name__ == "__main__":
    main()
