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
BLUE = (0, 0, 255)
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
POWERRECT1 = pygame.Rect(0, HEIGHT-230, 20, 230)
POWERRECT2 = pygame.Rect(WIDTH-20, HEIGHT-230, 20, 230)
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
POWER_HEIGHT = 2

HP_FONT = pygame.font.SysFont('comicsans', 12)
POWER_FONT = pygame.font.SysFont('comicsans', 8)
WIND_FONT = pygame.font.SysFont('comicsans', 30)
WIN_FONT = pygame.font.SysFont('comicsans', 80)

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

GURA_SPIN1 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'spin1.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
GURA_SPIN2 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'spin2.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
GURA_SPIN3 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'spin3.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
GURA_SPIN4 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'spin4.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
GURA_SPIN5 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'spin5.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
GURA_SPIN6 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'spin6.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
GURA_SPIN7 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'spin7.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
GURA_SPIN8 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'spin8.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
GURA_SPIN9 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'spin9.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
GURA_SPIN10 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'spin10.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
GURA_SPIN11 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'spin11.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
GURA_SPIN12 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'spin12.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))

GURA_SPIN = [GURA_SPIN1, GURA_SPIN2, GURA_SPIN3,
             GURA_SPIN4, GURA_SPIN5, GURA_SPIN6, GURA_SPIN7, GURA_SPIN8, GURA_SPIN9, GURA_SPIN10, GURA_SPIN11, GURA_SPIN12]

CALLI_DYING1 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'calldying1.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLI_DYING2 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'calldying2.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLI_DYING3 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'calldying3.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLI_DYING4 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'calldying4.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLI_DYING5 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'calldying5.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLI_DYING6 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'calldying6.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLI_DYING7 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'calldying7.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLI_DYING8 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'calldying8.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLI_DYING9 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'calldying9.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLI_DYING10 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'calldying10.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLI_DYING11 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'calldying11.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLI_DYING12 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'calldying12.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLI_DYING13 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'calldying13.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLI_DYING14 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'calldying14.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLI_DYING15 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'calldying15.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLI_DYING16 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'calldying16.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLI_DYING17 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'calldying17.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLI_DYING18 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'calldying18.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLI_DYING19 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'calldying19.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLI_DYING20 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'calldying20.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLI_DYING21 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'calldying21.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLI_DYING22 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'calldying22.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))
CALLI_DYING23 = pygame.transform.scale(pygame.image.load(
    os.path.join('python', 'Assets', 'calldying23.png')), (PLAYER_WIDTH, PLAYER_HEIGHT))

CALLI_DYING = [CALLI_DYING1, CALLI_DYING2, CALLI_DYING3, CALLI_DYING4,
               CALLI_DYING5, CALLI_DYING6, CALLI_DYING7, CALLI_DYING8,
               CALLI_DYING9, CALLI_DYING10, CALLI_DYING11, CALLI_DYING12,
               CALLI_DYING13, CALLI_DYING14, CALLI_DYING15, CALLI_DYING16,
               CALLI_DYING17, CALLI_DYING18, CALLI_DYING19, CALLI_DYING20,
               CALLI_DYING21, CALLI_DYING22, CALLI_DYING23]


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


def draw_window(redBox, shoot, framenum, angle, player, wind_spd, blue_hp, red_hp, power):
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
    if blue_hp > 0:
        WIN.blit(GURA[framenum//4 % len(GURA)],
                 (BLUE_POSX, BLUE_POSY-PLAYER_HEIGHT))
    else:
        WIN.blit(GURA_SPIN[framenum//4 % len(GURA_SPIN)],
                 (BLUE_POSX, BLUE_POSY-PLAYER_HEIGHT))
        win_text = WIN_FONT.render("RED WINS", 1, RED)
        WIN.blit(win_text, (WIDTH//2-win_text.get_width()//2, 100))
    if red_hp > 0:
        WIN.blit(CALLIOPE[framenum//4 % len(CALLIOPE)],
                 (RED_POSX-PLAYER_WIDTH, RED_POSY-PLAYER_HEIGHT))
    else:
        WIN.blit(CALLI_DYING[framenum//3 % len(CALLI_DYING)],
                 (RED_POSX-PLAYER_WIDTH, RED_POSY-PLAYER_HEIGHT))
        win_text = WIN_FONT.render("BLUE WINS", 1, BLUE)
        WIN.blit(win_text, (WIDTH//2-win_text.get_width()//2, 100))

    WIN.blit(FLOOR, (0, HEIGHT-15))

    pygame.draw.rect(WIN, WHITE, WHITERECT)
    wind_spd_text = HP_FONT.render("Wind Speed", 1, BLACK)
    WIN.blit(wind_spd_text, (WIDTH//2-wind_spd_text.get_width()//2, 3))

    if not shoot:
        wind_spd_text2 = HP_FONT.render(str(wind_spd), 1, BLACK)
    else:
        wind_spd_text2 = HP_FONT.render("-", 1, BLACK)

    WIN.blit(wind_spd_text2, (WIDTH//2-wind_spd_text2.get_width()//2, 18))
    blue_hp_text = HP_FONT.render("BLUE | HP: " + str(blue_hp), 1, BLACK)
    WIN.blit(blue_hp_text, (3, 3))
    red_hp_text = HP_FONT.render("RED | HP: " + str(red_hp), 1, BLACK)
    WIN.blit(red_hp_text, (WIDTH-red_hp_text.get_width()-3, 3))

    for i in range(1, blue_hp):
        blue_hpbar = pygame.Rect(3+(i*HP_WIDTH), 20, HP_WIDTH, 10)
        pygame.draw.rect(WIN, (round(255-2.5*i), round(2.5*i), 0), blue_hpbar)

    for i in range(1, red_hp):
        red_hpbar = pygame.Rect(WIDTH-(3+(i*HP_WIDTH)), 20, HP_WIDTH, 10)
        pygame.draw.rect(WIN, (round(255-2.5*i), round(2.5*i), 0), red_hpbar)

    pygame.draw.rect(WIN, WHITE, POWERRECT1)
    pygame.draw.rect(WIN, WHITE, POWERRECT2)
    for i in range(1, round(power)):
        if player == 'BLUE':
            red_pw_text = POWER_FONT.render("-", 1, BLACK)
            blue_pw_text = POWER_FONT.render(str(power), 1, BLACK)
            power_bar = pygame.Rect(
                5, HEIGHT-(5+(i*POWER_HEIGHT)), 10, POWER_HEIGHT)
        else:
            blue_pw_text = POWER_FONT.render("-", 1, BLACK)
            red_pw_text = POWER_FONT.render(str(power), 1, BLACK)
            power_bar = pygame.Rect(
                WIDTH-15, HEIGHT-(5+(i*POWER_HEIGHT)), 10, POWER_HEIGHT)
        pygame.draw.rect(
            WIN, (round(255-2.5*i), round(2.5*i), 0), power_bar)
    WIN.blit(blue_pw_text, (3, HEIGHT-225))
    WIN.blit(red_pw_text, (WIDTH-red_pw_text.get_width()-3, HEIGHT-225))
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
    redBox.y = HEIGHT - BOX_LENGTH - 30
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
    power = 0
    shoot = False
    run = True
    player = 'BLUE'
    blue_hp = 100
    red_hp = 100
    end_frame = -1
    while run:
        clock.tick(FPS)
        if (blue_hp <= 0 or red_hp <= 0) and end_frame == -1:
            end_frame = framenum + 300
        if end_frame != -1 and framenum >= end_frame:
            run = False
        pos = pygame.mouse.get_pos()
        if player == 'BLUE':
            line = [(BOX_START_POS_BLUE, HEIGHT-BOX_LENGTH-30), pos]
        else:
            line = [(BOX_START_POS_RED, HEIGHT-BOX_LENGTH-30), pos]

        if shoot:
            # keys_pressed = pygame.key.get_pressed()
            # if keys_pressed[pygame.K_SPACE]:
            #     if not skill_used:
            #         print("skill used")
            #         velx = 0
            #         wind_speed = 0
            #         skill_used = True
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
                    player, wind_speed, blue_hp, red_hp, 100)
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
