from pickle import FALSE
from numpy import blackman
import pygame
import math
import random
import os

pygame.font.init()

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
WHITERECT = pygame.Rect(0, 0, WIDTH, 35)
BLUE_POSX = 50
BLUE_POSY = HEIGHT-15
RED_POSX = WIDTH-50
RED_POSY = HEIGHT-15
PLAYER_HEIGHT = 80
PLAYER_WIDTH = 70
BOX_START_POS_BLUE = BLUE_POSX+BOX_LENGTH+20
BOX_START_POS_RED = RED_POSX-BOX_LENGTH-20
VEL_PENELTY = 1.1
ARROW_LENGTH = 120
ARROW_WIDTH = 20
HP_WIDTH = 4

HP_FONT = pygame.font.SysFont('comicsans', 12)
WIND_FONT = pygame.font.SysFont('comicsans', 30)

# https://www.freepik.com/vectors/alien-planet Alien planet vector created by upklyak
BACKGROUND = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'BG.jpg')), (WIDTH, HEIGHT))
FLOOR = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'platform2.png')), (WIDTH, 25))

'''The arrow only works between 1 to 179 degrees'''
ARROW = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'Arrow.png')), (ARROW_LENGTH, ARROW_WIDTH))

# All animations are from Walfie https://walfiegif.wordpress.com
GURA1 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'Gura_1.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
GURA2 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'Gura_2.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
GURA3 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'Gura_3.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
GURA4 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'Gura_4.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
GURA5 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'Gura_5.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
GURA6 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'Gura_6.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
GURA7 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'Gura_7.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))

GURA = [GURA1, GURA2, GURA3, GURA4, GURA5, GURA6, GURA7]

CALLIOPE1 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'Calliope_1.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLIOPE2 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'Calliope_2.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLIOPE3 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'Calliope_3.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLIOPE4 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'Calliope_4.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLIOPE5 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'Calliope_5.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLIOPE6 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'Calliope_6.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))

CALLIOPE = [CALLIOPE1, CALLIOPE2, CALLIOPE3, CALLIOPE4, CALLIOPE5, CALLIOPE6]


class Box(object):
    def __init__(self, x, y, length, color):
        self.x = x
        self.y = y
        self.length = length
        self.color = color

    def box(self):
        return pygame.Rect(self.x, self.y, self.length, self.length)

    def draw(self, WIN):
        pygame.draw.rect(WIN, self.color, self.box())

    def box_path(nowx, starty, velx, vely, time_relative, time_absolute, wind_speed):

        velx += wind_speed
        distX = velx * time_relative
        distY = (vely * time_absolute) + ((-GRAV * (time_absolute**2))/2)

        newX = round(nowx + distX)
        newY = round(starty - distY)

        return (newX, newY)

    def touch_ground(self):
        if self.y > HEIGHT - self.length - 1:
            return True

    def collide_gura(self):
        if (BLUE_POSX - PLAYER_WIDTH - PLAYER_WIDTH//2 < self.x < BLUE_POSX + PLAYER_WIDTH - PLAYER_WIDTH//2
                and self.y + BOX_LENGTH > HEIGHT - PLAYER_HEIGHT):
            return True

    def collide_calli(self):
        if (RED_POSX - PLAYER_WIDTH - PLAYER_WIDTH//2 < self.x < RED_POSX + PLAYER_WIDTH - PLAYER_WIDTH//2
                and self.y + BOX_LENGTH > HEIGHT - PLAYER_HEIGHT):
            return True


def draw_window(redBox, shoot, framenum, angle, player, wind_spd, blue_hp, red_hp):
    WIN.blit(BACKGROUND, (0, 0))
    extra = 0
    if shoot:
        redBox.draw(WIN)
    if not shoot:
        # pygame.draw.line(WIN, BLACK, line[0], line[1])
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

    pygame.draw.rect(WIN, WHITE, WHITERECT)
    wind_spd_text = HP_FONT.render("Wind Speed", 1, BLACK)
    WIN.blit(wind_spd_text, (WIDTH//2-wind_spd_text.get_width()//2, 3))

    if not shoot:
        wind_spd_text2 = HP_FONT.render(str(wind_spd), 1, BLACK)
    else:
        wind_spd_text2 = HP_FONT.render("-", 1, BLACK)

    WIN.blit(wind_spd_text2, (WIDTH//2-wind_spd_text2.get_width()//2, 18))
    blue_hp_text = HP_FONT.render("HP: " + str(blue_hp), 1, BLACK)
    WIN.blit(blue_hp_text, (3, 3))
    red_hp_text = HP_FONT.render("HP: " + str(red_hp), 1, BLACK)
    WIN.blit(red_hp_text, (WIDTH-red_hp_text.get_width()-3, 3))

    for i in range(1, blue_hp):
        blue_hpbar = pygame.Rect(3+(i*HP_WIDTH), 20, HP_WIDTH, 10)
        pygame.draw.rect(WIN, (round(255-2.5*i), round(2.5*i), 0), blue_hpbar)

    for i in range(1, red_hp):
        blue_hpbar = pygame.Rect(WIDTH-(3+(i*HP_WIDTH)), 20, HP_WIDTH, 10)
        pygame.draw.rect(WIN, (round(255-2.5*i), round(2.5*i), 0), blue_hpbar)

    pygame.display.update()


def find_angle(line, pos):
    sX = line[0][0]
    sY = line[0][1]
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
    if (WIDTH//2 - WALL_WIDTH - WALL_WIDTH//2 < po[0] < WIDTH//2 - WALL_WIDTH//2 + WALL_WIDTH
            and po[1] + BOX_LENGTH > HEIGHT - WALL_HEIGHT):
        return True
    '''Block touch the border'''
    if (po[0] < 0 or po[0] > WIDTH-BOX_LENGTH):
        return True
    return False


def change_player(color, redBox):
    redBox.y = HEIGHT-BOX_LENGTH - 30
    if color == 'RED':
        redBox.x = BOX_START_POS_BLUE
        return 'BLUE'
    else:
        redBox.x = BOX_START_POS_RED
        return 'RED'


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
    run = True
    player = 'BLUE'
    blue_hp = 100
    red_hp = 100
    while run:

        clock.tick(FPS)
        pos = pygame.mouse.get_pos()
        if player == 'BLUE':
            line = [(BOX_START_POS_BLUE, HEIGHT-BOX_LENGTH-30), pos]
        else:
            line = [(BOX_START_POS_RED, HEIGHT-BOX_LENGTH-30), pos]

        if shoot:
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_SPACE]:
                if not skill_used:
                    print("skill used")
                    velx = 0
                    wind_speed = 0
                    skill_used = True
            if redBox.y < HEIGHT - redBox.length:
                time += BOX_FPS
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
            if redBox.touch_ground():
                shoot = False
                wind_speed = random.randint(-20, 20)
                player = change_player(player, redBox)
            elif (framenum > st_frame + 30):
                if redBox.collide_gura():
                    shoot = False
                    blue_hp -= 30
                    player = change_player(player, redBox)
                elif redBox.collide_calli():
                    shoot = False
                    red_hp -= 30
                    player = change_player(player, redBox)

        if not shoot:
            angle = find_angle(line, pos)

        draw_window(redBox, shoot, framenum, angle,
                    player, wind_speed, blue_hp, red_hp)
        framenum = framenum+1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not shoot:
                    shoot = True
                    skill_used = False
                    st_frame = framenum
                    y = redBox.y
                    time = 0
                    power = 300/POWER_FACTOR
                    angle = find_angle(line, pos)
                    velx = math.cos(angle) * power
                    vely = math.sin(angle) * power

    pygame.quit()


if __name__ == "__main__":
    main()
