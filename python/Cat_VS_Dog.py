import pygame
import math
import random
import os
from practicum import find_mcu_boards, McuBoard, PeriBoard

pygame.font.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cat VS Dog")
mcu = McuBoard(find_mcu_boards()[0])
peri = PeriBoard(mcu)

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
VEL_PENELTY = 1.1
ARROW_LENGTH = 120
ARROW_WIDTH = 20

# https://www.freepik.com/vectors/alien-planet Alien planet vector created by upklyak
BACKGROUND = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'BG.bmp')), (WIDTH, HEIGHT))
FLOOR = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'platform2.bmp')), (WIDTH, 25))

'''The arrow only works between 1 to 179 degrees'''
ARROW = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Arrow.bmp')), (ARROW_LENGTH, ARROW_WIDTH))

# All animations are from Walfie https://walfiegif.wordpress.com
GURA1 = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Gura_1.bmp')), (PLAYER_WIDTH, PLAYER_HEIGHT))
GURA2 = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Gura_2.bmp')), (PLAYER_WIDTH, PLAYER_HEIGHT))
GURA3 = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Gura_3.bmp')), (PLAYER_WIDTH, PLAYER_HEIGHT))
GURA4 = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Gura_4.bmp')), (PLAYER_WIDTH, PLAYER_HEIGHT))
GURA5 = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Gura_5.bmp')), (PLAYER_WIDTH, PLAYER_HEIGHT))
GURA6 = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Gura_6.bmp')), (PLAYER_WIDTH, PLAYER_HEIGHT))
GURA7 = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Gura_7.bmp')), (PLAYER_WIDTH, PLAYER_HEIGHT))

GURA = [GURA1, GURA2, GURA3, GURA4, GURA5, GURA6, GURA7]

CALLIOPE1 = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Calliope_1.bmp')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLIOPE2 = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Calliope_2.bmp')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLIOPE3 = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Calliope_3.bmp')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLIOPE4 = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Calliope_4.bmp')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLIOPE5 = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Calliope_5.bmp')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLIOPE6 = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Calliope_6.bmp')), (PLAYER_WIDTH, PLAYER_HEIGHT))

CALLIOPE = [CALLIOPE1, CALLIOPE2, CALLIOPE3, CALLIOPE4, CALLIOPE5, CALLIOPE6]
print("Cover the light sensor and press the button...")
while(True):
    if(peri.get_switch()):
        light_min = peri.get_light()
        break
print("Remove your hand and press the button...")
while(True):
    if(peri.get_switch()):
        light_max = peri.get_light()
        break


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


def draw_window(line, redBox, shoot, framenum, angle, player):
    WIN.fill((255, 255, 255))
    WIN.blit(BACKGROUND, (0, 0))
    extra = 0
    if shoot:
        redBox.draw(WIN)
    if not shoot:
        pygame.draw.line(WIN, BLACK, line[0], line[1])
        arrow = pygame.transform.rotate(ARROW, round((angle*180)/math.pi))
        if angle >= math.pi/2:
            extra = math.cos(angle)*ARROW_LENGTH
        if player == 'BLUE':
            WIN.blit(arrow, (BOX_START_POS_BLUE-(math.sin(angle)*10)+extra, HEIGHT -
                             BOX_LENGTH-(math.sin(angle)*ARROW_LENGTH)-40))
        else:
            WIN.blit(arrow, (BOX_START_POS_RED-(math.sin(angle)*10)+extra, HEIGHT -
                             BOX_LENGTH-(math.sin(angle)*ARROW_LENGTH)-40))
    pygame.draw.rect(WIN, BLACK, WALL)
    WIN.blit(GURA[framenum//4 % len(GURA)],
             (BLUE_POSX, BLUE_POSY-PLAYER_HEIGHT))
    WIN.blit(CALLIOPE[framenum//4 % len(CALLIOPE)],
             (RED_POSX-PLAYER_WIDTH, RED_POSY-PLAYER_HEIGHT))
    WIN.blit(FLOOR, (0, HEIGHT-15))
    pygame.display.update()


def find_power(light):
    if light > light_max:
        power = 1000
    elif light < light_min:
        power = 0
    else:
        power = ((light-light_min)/(light_max-light_min))*1000
    return power


def find_angle(light):
    if light > light_max:
        angle = 179*math.pi/180
    elif light < light_min:
        angle = math.pi/180
    else:
        angle = ((light-light_min)/(light_max-light_min))*math.pi
    return angle


def block_collide_wall(po):
    if (WIDTH//2 - WALL_WIDTH - WALL_WIDTH//2 < po[0] < WIDTH//2 - WALL_WIDTH//2 + WALL_WIDTH
            and po[1] + BOX_LENGTH > HEIGHT - WALL_HEIGHT):
        return True
    '''Block touch the border'''
    if (po[0] < 0 or po[0] > WIDTH-BOX_LENGTH):
        return True
    return False


def block_touch_ground(box):
    if box.y > HEIGHT - box.length - 1:
        return True


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
    redBox = Box(BOX_START_POS_BLUE, HEIGHT-BOX_LENGTH-30, BOX_LENGTH, WHITE)
    wind_speed = random.randint(-20, 20)
    framenum = 0
    x = 0
    y = 0
    time = 0
    velx = 0
    vely = 0
    shoot = False
    angset = False
    run = True
    player = 'BLUE'
    peri.set_led(0, 1)
    while run:

        clock.tick(FPS)
        pos = pygame.mouse.get_pos()
        if player == 'BLUE':
            line = [(BOX_START_POS_BLUE, HEIGHT-BOX_LENGTH-30), pos]
        else:
            line = [(BOX_START_POS_RED, HEIGHT-BOX_LENGTH-30), pos]

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
                print(velx)
                if block_collide_wall(Box.box_path(redBox.x, y, velx, vely,
                                                   BOX_FPS, time, wind_speed)):
                    if (abs(velx) < 300):
                        velx = velx*VEL_PENELTY
                    velx = -velx
                    wind_speed = 0

                po = Box.box_path(redBox.x, y, velx, vely,
                                  BOX_FPS, time, wind_speed)
                redBox.x = po[0]
                redBox.y = po[1]
            elif block_touch_ground(redBox):
                shoot = False
                wind_speed = random.randint(-20, 20)
                print('Wind speed =', wind_speed)
                redBox.y = HEIGHT-BOX_LENGTH - 30
                if player == 'RED':
                    redBox.x = BOX_START_POS_BLUE
                    peri.set_led(0, 1)
                    peri.set_led(2, 0)
                    player = 'BLUE'
                else:
                    redBox.x = BOX_START_POS_RED
                    peri.set_led(0, 0)
                    peri.set_led(2, 1)
                    player = 'RED'
        if not shoot:
            while(True):
                light = peri.get_light()
                if not angset:
                    angle = find_angle(light)
                elif not shoot:
                    power = find_power(light)/POWER_FACTOR

                draw_window(line, redBox, shoot, framenum, angle, player)
                framenum = framenum+1

                if peri.get_switch():
                    if not angset:
                        angset = True
                        angle = find_angle(light)
                    elif not shoot:
                        shoot = True
                        y = redBox.y
                        time = 0
                        power = find_power()/POWER_FACTOR
                        velx = math.cos(angle) * power
                        vely = math.sin(angle) * power
                        break

        draw_window(line, redBox, shoot, framenum, angle, player)
        framenum = framenum+1

    pygame.quit()


if __name__ == "__main__":
    main()
