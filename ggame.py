# <-------------------------------------IMPORT------------------------------------->#
import pygame
import sys
import os
import random
import math
import time
from pygame import mixer

if getattr(sys,'frozen',False):
    current_path = os.path.dirname(sys.executable)
else:
    current_path = os.path.dirname(__file__)
spiriteFolderPath = os.path.join(current_path,'media')

# --------------------------------------------------------------------------------------------------------------#
# <-------------------------------------INITIALIZE------------------------------------->#
pygame.init()
# --------------------------------------------------------------------------------------------------------------#
# <-------------------------------------SCREEN , CAPTION, ICON------------------------------------->#
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")

icon = pygame.image.load(os.path.join(spiriteFolderPath,"extraterrestrial.png"))
pygame.display.set_icon(icon)
delay = 0
close_time = 0
# --------------------------------------------------------------------------------------------------------------#
# <-------------------------------------MUSIC------------------------------------->#
sound = mixer.Sound(os.path.join(spiriteFolderPath,"Boom.wav"))
# --------------------------------------------------------------------------------------------------------------#
# <-------------------------------------PAGE ONE------------------------------------->#
# <-------------------------------------MAIN MENU------------------------------------->#
m_page = pygame.image.load(os.path.join(spiriteFolderPath,"Asset 2.png"))
text1 = pygame.font.Font(os.path.join(spiriteFolderPath,"Heaters.otf"), 170)
text2 = pygame.font.Font(os.path.join(spiriteFolderPath,"Balming.ttf"), 40)


def main_menu():
    run = True
    while run:
        screen.blit(m_page, (0, 0))
        title1 = text1.render("Space Invaders", True, (255, 255, 255))
        screen.blit(title1, (60, 40))
        title2 = text2.render("Press ENTER to continue...", True, (255, 255, 255))
        screen.blit(title2, (280, 490))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    sound.play()
                    run = False
        pygame.display.update()


# --------------------------------------------------------------------------------------------------------------#
# <-------------------------------------PAGE TWO------------------------------------->#
# <-------------------------------------USER LOGIN------------------------------------->#
user_img = pygame.image.load(os.path.join(spiriteFolderPath,"User (2).png"))
text7 = pygame.font.Font(os.path.join(spiriteFolderPath,"CaviarDreams_Bold.ttf"), 30)
text3 = pygame.font.Font(os.path.join(spiriteFolderPath,"Balming.ttf"), 30)
text4 = pygame.font.Font(os.path.join(spiriteFolderPath,"Balming.ttf"), 50)

def login():
    clock = pygame.time.Clock()
    global name_of_user
    user_name = ''
    name_of_user = ''
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_name = user_name[:-1]
                else:
                    user_name += event.unicode
                    name_of_user = user_name
                if (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT) and user_name.isalnum():
                    run = False

        screen.blit(user_img, (0, 0))
        title1 = text4.render("Enter  your  username : ", True, (255, 255, 255))
        screen.blit(title1, (280, 30))
        title1 = text3.render("(Username should contain alphabets ", True, (255, 255, 255))
        screen.blit(title1, (280, 95))
        title1 = text3.render("and numbers only)", True, (255, 255, 255))
        screen.blit(title1, (350, 130))
        title1 = text3.render("Press shift to continue.", True, (255, 255, 255))
        screen.blit(title1, (560, 545))
        title = text7.render(user_name, True, (255, 255, 255))
        screen.blit(title, (310, 200))
        pygame.display.flip()
        clock.tick(30)


# --------------------------------------------------------------------------------------------------------------#
# <-------------------------------------PAGE THREE------------------------------------->#
# <-------------------------------------CONVO (PLAYER AND US)------------------------------------->#
convo_us = pygame.image.load(os.path.join(spiriteFolderPath,"hi.png"))


def c_us():
    run = True
    while run:
        screen.blit(convo_us, (0, 0))
        title1 = text4.render("Welcome captain " + name_of_user + " !", True, (255, 255, 255))
        screen.blit(title1, (20, 20))
        title1 = text4.render("We are being attacked by the ", True, (255, 255, 255))
        screen.blit(title1, (20, 80))
        title1 = text4.render("aliens of  \" JINXED COSMOS \" ", True, (255, 255, 255))
        screen.blit(title1, (20, 130))
        title1 = text4.render("Now is the time to save our planet. ", True, (255, 255, 255))
        screen.blit(title1, (300, 400))
        title1 = text4.render("Let's get going!", True, (255, 255, 255))
        screen.blit(title1, (400, 460))
        title1 = text3.render("Keep pressing enter to continue...", True, (255, 255, 255))
        screen.blit(title1, (500, 560))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    run = False
        pygame.display.update()


# --------------------------------------------------------------------------------------------------------------#
# <-------------------------------------PAGE FOUR------------------------------------->#
# <-------------------------------------CONVO (PLAYER & ALIENS)------------------------------------->#
convo_alien = pygame.image.load(os.path.join(spiriteFolderPath,"hello (2).png"))
text8 = pygame.font.Font(os.path.join(spiriteFolderPath,"Balming.ttf"), 40)


def c_alien():
    run = True
    while run:
        screen.blit(convo_alien, (0, 0))
        title1 = text8.render("Look who do we have here!", True, (255, 255, 255))
        screen.blit(title1, (280, 20))
        title1 = text8.render("Well, sadly your planet is in our command.", True, (255, 255, 255))
        screen.blit(title1, (200, 60))
        title1 = text8.render("But we are ready to give it back to you if you defeat us", True, (255, 255, 255))
        screen.blit(title1, (120, 450))
        title1 = text8.render("in the war.", True, (255, 255, 255))
        screen.blit(title1, (340, 480))
        title1 = text8.render("We hope you are not scared, kid.", True, (255, 255, 255))
        screen.blit(title1, (260, 530))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    run = False
        pygame.display.update()


# --------------------------------------------------------------------------------------------------------------#
# <-------------------------------------PAGE FIVE------------------------------------->#
# <-------------------------------------INSTRUCTIONS------------------------------------->#
inst = pygame.image.load(os.path.join(spiriteFolderPath,"inst.png"))



def instructions():
    run = True
    while run:
        screen.blit(inst, (0, 0))
        title3 = text4.render("How to play: ", True, (0, 0, 0))
        screen.blit(title3, (10, 10))
        title4 = text4.render("1. Use left and right arrow keys to", True, (0, 0, 0))
        screen.blit(title4, (160, 170))
        title5 = text4.render(" move.", True, (0, 0, 0))
        screen.blit(title5, (160, 220))
        title6 = text4.render("2. Use the space bar to shoot.", True, (0, 0, 0))
        screen.blit(title6, (160, 270))
        title6 = text4.render("3. Press P to pause.", True, (0, 0, 0))
        screen.blit(title6, (160, 320))
        title6 = text4.render("You have got 3 lives throughout the entire game.", True, (255, 255, 255))
        screen.blit(title6, (100, 500))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    run = False
        pygame.display.update()


# --------------------------------------------------------------------------------------------------------------#
# <-------------------------------------PAGE SIX------------------------------------->#
# <-------------------------------------GAME SCREEN------------------------------------->#
back = pygame.image.load(os.path.join(spiriteFolderPath,"Asset 1.png"))

# --------------------------------------------------------------------------------------------------------------#
# <-------------------------------------PLAYER------------------------------------->#
play = pygame.image.load(os.path.join(spiriteFolderPath,"space-ship.png"))
playerX = 370
playerY = 500
playerX_change = 0
playerY_change = 0


def player(x, y):
    screen.blit(play, (x, y))


# --------------------------------------------------------------------------------------------------------------#
# <-------------------------------------ENEMY------------------------------------->#
enem = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemy = 5

for i in range(num_of_enemy):
    enem.append(pygame.image.load(os.path.join(spiriteFolderPath,"alien.png")))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(40, 140))
    enemyX_change.append(5)
    enemyY_change.append(20)
enemy_count = 0

def enemy(x, y, i):
    screen.blit(enem[i], (x, y))


# --------------------------------------------------------------------------------------------------------------#
# <-------------------------------------BULLET------------------------------------->#
bulletImg = pygame.image.load(os.path.join(spiriteFolderPath,"weapons.png"))
bulletX = 0
bulletY = 500
bulletX_change = 0
bulletY_change = 15
bullet_state = "ready"
bullet_count = 0
bullet_max = 0
bullet_temp = 0


def bullet(x, y):
    global num_of_bullet
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def show_bullets(x, y):
    bull = t_live.render("BULLETS : " + str(bullet_temp), True, (255, 255, 255))
    screen.blit(bull, (x, y))


# --------------------------------------------------------------------------------------------------------------#
# <-------------------------------------BOMB------------------------------------->#
bomb = pygame.image.load(os.path.join(spiriteFolderPath,"bomb.png"))
bombX = 0
bombY = 100
bombY_change = 5
bomb_state = "aim"


def attack(x, y):
    global bomb_state
    bomb_state = "shoot"
    screen.blit(bomb, (x, y))


def bomb_collision(playerY, bombY, bombX, playerX):
    dist = math.sqrt((playerX - bombX) ** 2 + (playerY - bombY) ** 2)
    if bombX >= playerX and bombX <= (playerX + 64) or (playerX - bombX) <= 30:
        if dist <= 54:
            return True
        else:
            return False


# --------------------------------------------------------------------------------------------------------------#
# <-------------------------------------COLLISION------------------------------------->#
def collision(enemyX, enemyY, bulletX, bulletY):
    dist = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    if dist < 30:
        return True
    else:
        return False


# --------------------------------------------------------------------------------------------------------------#
# <-------------------------------------PAUSED------------------------------------->#
pause_start = 0
pause_img = pygame.image.load(os.path.join(spiriteFolderPath,"paused.png"))
texted = pygame.font.Font(os.path.join(spiriteFolderPath,"Heaters.otf"), 220)


def pause():
    global delay, close_time
    run = True
    while run:
        screen.blit(pause_img, (0, 0))
        title = texted.render("PAUSED", True, (234, 207, 97))
        screen.blit(title, (200, 170))
        title = text4.render("Press C to continue", True, (234, 207, 97))
        screen.blit(title, (285, 470))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    count = 0
                    if level_count == 7 or level_count == 8:
                        # print(delay)
                        count = count + int(time.time() - pause_start)
                        if level_count == 7:
                            close_time = close_time + count
                        elif level_count == 8:
                            close_time = close_time + count
                        run = False
                    else:
                        run = False
        pygame.display.update()


def toPause(x, y):
    title = text3.render("Press P to pause", True, (0, 0, 0))
    screen.blit(title, (x, y))


# --------------------------------------------------------------------------------------------------------------#
# <-------------------------------------BONUS------------------------------------->#
bon = pygame.image.load(os.path.join(spiriteFolderPath,"bonus.png"))


def bonus():
    end_time = time.time() + 1
    run = True
    while run:
        screen.blit(bon, (0, 0))
        title = text1.render("BONUS", True, (0, 0, 0))
        screen.blit(title, (260, 60))
        title = text1.render("+I", True, (0, 0, 0))
        screen.blit(title, (350, 160))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        if time.time() > end_time:
            run = False
        pygame.display.update()


# --------------------------------------------------------------------------------------------------------------#
# <------------------------------------- SCORE------------------------------------->#
score_val = 0
font = pygame.font.Font(os.path.join(spiriteFolderPath,"Balming.ttf"), 45)
gamer = pygame.font.Font(os.path.join(spiriteFolderPath,"Heaters.otf"), 200)


def show_score(x, y):
    score = font.render("SCORE : " + str(score_val), True, (255, 255, 255))
    screen.blit(score, (x, y))


# --------------------------------------------------------------------------------------------------------------#
# <-------------------------------------TIMER------------------------------------->#
frame_rate = 60
start_time = 15
clock = pygame.time.Clock()


def time_r(counter):
    minutes = counter // 60
    seconds = counter % 60
    output_string = "Time : {0:02}:{1:02}".format(minutes, seconds)
    text = t_live.render(output_string, True, (255, 255, 255))
    screen.blit(text, [10, 60])


# ------------------------------------------------------------------------------------------------#
# <-------------------------------------ENEMY REGENERATE------------------------------------->#

def regenerate():
    for i in range(num_of_enemy):
        enem.append(pygame.image.load(os.path.join(spiriteFolderPath,"alien.png")))
        enemyX.append(random.randint(0, 736))
        enemyY.append(random.randint(40, 140))
        enemyX_change.append(5)
        enemyY_change.append(20)


# ------------------------------------------------------------------------------------------------#
# <-------------------------------------LIVES------------------------------------->#
lives = 3
t_live = pygame.font.Font(os.path.join(spiriteFolderPath,"Balming.ttf"), 45)


def show_lives(x, y):
    life = t_live.render("LIVES : " + str(lives), True, (255, 255, 255))
    screen.blit(life, (x, y))


# --------------------------------------------------------------------------------------------------------------#
# <-------------------------------------GAME OVER------------------------------------->#
def over_text(x, y):
    end_time = time.time() + 2
    run = True
    while run:
        screen.blit(back, (0, 0))
        screen.blit(play, (370, 500))
        show_score(650, 10)
        txt = gamer.render("GAME OVER!", True, (255, 255, 255))
        screen.blit(txt, (x, y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        if time.time() > end_time:
            run = False
        pygame.display.update()


# --------------------------------------------------------------------------------------------------------------#
# <-------------------------------------RESTART------------------------------------->#
text5 = pygame.font.Font(os.path.join(spiriteFolderPath,"Balming.ttf"), 60)
text6 = pygame.font.Font(os.path.join(spiriteFolderPath,"Heaters.otf"), 150)
over = pygame.image.load(os.path.join(spiriteFolderPath,"gameover.png"))


def restart():
    run = True
    while run:
        screen.blit(over, (0, 0))
        title1 = text6.render("GAME OVER", True, (255, 255, 255))
        screen.blit(title1, (155, 5))
        title2 = text3.render("Press ESCAPE to quit.", True, (255, 255, 255))
        screen.blit(title2, (305, 460))
        title2 = text3.render("Press R to restart.", True, (0, 0, 0))
        screen.blit(title2, (310, 500))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                if event.key == pygame.K_r:
                    run = False
                    return run
        pygame.display.update()

# --------------------------------------------------------------------------------------------------------------#
# <-------------------------------------END------------------------------------->#
endImg = pygame.image.load(os.path.join(spiriteFolderPath,"Success.png"))
texting = pygame.font.Font(os.path.join(spiriteFolderPath,"Balming.ttf"), 60)


def success():
    run = True
    while run:
        screen.blit(endImg, (0, 0))
        title2 = texting.render("Well done " + name_of_user + " !!", True, (255, 255, 255))
        screen.blit(title2, (120, 40))
        title1 = texting.render("You have successfully saved our planet", True, (255, 255, 255))
        screen.blit(title1, (100, 470))
        title1 = texting.render("from those evil aliens.", True, (255, 255, 255))
        screen.blit(title1, (240, 530))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    sys.exit(0)
        pygame.display.update()


# --------------------------------------------------------------------------------------------------------------#
# <-----------------------------------INSTRUCTIONS FOR EACH LEVEL----------------------------------->
text_inst = pygame.image.load(os.path.join(spiriteFolderPath,"text.png"))
# <-----------------------------------LEVEL 1----------------------------------->
def inst1():
    run = True
    while run:
        screen.blit(text_inst, (0, 0))
        title1 = text6.render("LEVEL ONE", True, (0, 0, 0))
        screen.blit(title1, (175, 20))
        title = text5.render("Kill any 15 enemies to pass this level.", True, (0, 0, 0))
        screen.blit(title, (140, 500))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    sound.play()
                    run = False
        pygame.display.update()


# <-----------------------------------LEVEL 2----------------------------------->
def inst2():
    run = True
    while run:
        screen.blit(text_inst, (0, 0))
        title1 = text6.render("LEVEL TWO", True, (0, 0, 0))
        screen.blit(title1, (175, 20))
        title = text5.render("Kill all 15 enemies to pass this level.", True, (0, 0, 0))
        screen.blit(title, (140, 500))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    sound.play()
                    run = False
        pygame.display.update()


# <-----------------------------------LEVEL 3----------------------------------->
def inst3():
    run = True
    while run:
        screen.blit(text_inst, (0, 0))
        title1 = text6.render("LEVEL THREE", True, (0, 0, 0))
        screen.blit(title1, (155, 20))
        title = text4.render("Kill all 5 enemies before they outnumber the bullets", True, (0, 0, 0))
        screen.blit(title, (80, 470))
        title2 = text4.render(" to pass this level.", True, (0, 0, 0))
        screen.blit(title2, (280, 510))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    sound.play()
                    run = False
        pygame.display.update()


# <-----------------------------------LEVEL 4----------------------------------->
def inst4():
    run = True
    while run:
        screen.blit(text_inst, (0, 0))
        title1 = text6.render("LEVEL FOUR", True, (0, 0, 0))
        screen.blit(title1, (175, 20))
        title = text4.render("Kill all 8 enemies before they outnumber the bullets", True, (0, 0, 0))
        screen.blit(title, (80, 470))
        title2 = text4.render(" to pass this level.", True, (0, 0, 0))
        screen.blit(title2, (280, 510))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    sound.play()
                    run = False
        pygame.display.update()


# <-----------------------------------LEVEL 5----------------------------------->
def inst5():
    run = True
    while run:
        screen.blit(text_inst, (0, 0))
        title1 = text6.render("LEVEL FIVE", True, (0, 0, 0))
        screen.blit(title1, (175, 20))
        title = text4.render("Kill all 11 enemies before they outnumber the bullets", True, (0, 0, 0))
        screen.blit(title, (80, 470))
        title2 = text4.render(" to pass this level.", True, (0, 0, 0))
        screen.blit(title2, (280, 510))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    sound.play()
                    run = False
        pygame.display.update()


# <-----------------------------------LEVEL 6----------------------------------->
def inst6():
    run = True
    while run:
        screen.blit(text_inst, (0, 0))
        title1 = text6.render("LEVEL SIX", True, (0, 0, 0))
        screen.blit(title1, (185, 10))
        title = text4.render("Kill all 15 enemies before they outnumber the bullets", True, (0, 0, 0))
        screen.blit(title, (80, 470))
        title2 = text4.render(" to pass this level.", True, (0, 0, 0))
        screen.blit(title2, (290, 510))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    sound.play()
                    run = False
        pygame.display.update()


# <-----------------------------------LEVEL 7----------------------------------->
def inst7():
    run = True
    while run:
        screen.blit(text_inst, (0, 0))
        title1 = text6.render("LEVEL SEVEN", True, (0, 0, 0))
        screen.blit(title1, (125, 20))
        title = text5.render("Kill all 10 enemies using unlimited number of bullets", True, (0, 0, 0))
        screen.blit(title, (10, 450))
        title2 = text5.render("within 15 seconds to pass this level.", True, (0, 0, 0))
        screen.blit(title2, (140, 510))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    sound.play()
                    run = False
        pygame.display.update()


# <-----------------------------------LEVEL 8----------------------------------->
def inst8():
    run = True
    while run:
        screen.blit(text_inst, (0, 0))
        title1 = text6.render("LEVEL EIGHT", True, (0, 0, 0))
        screen.blit(title1, (155, 20))
        title = text4.render("Kill all 15 enemies before they outnumber the bullets", True, (0, 0, 0))
        screen.blit(title, (80, 470))
        title2 = text4.render("30 seconds to pass this level.", True, (0, 0, 0))
        screen.blit(title2, (210, 510))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    sound.play()
                    run = False
        pygame.display.update()


# --------------------------------------------------------------------------------------------------------------#
# <-------------------------------------CALLING THE FUNCTIONS------------------------------------->#

main_menu()
login()
print(name_of_user)
c_us()
c_alien()
instructions()
inst1()
success()

level_count = 1
temp = 0
# --------------------------------------------------------------------------------------------------------------#
# <-------------------------------------GAME LOOP------------------------------------->#
run = True
while run:
    screen.blit(back, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            # Pause
            if event.key == pygame.K_p:
                if level_count == 7 or level_count == 8:
                    pause_start = time.time()
                pause()
            # Movements
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            # Bullets fire
            if event.key == pygame.K_SPACE:
                if level_count < 3 or level_count == 7:
                    if bullet_state == "ready":
                        bulletSound = mixer.Sound(os.path.join(spiriteFolderPath,"gunshot.wav"))
                        bulletSound.play()
                        bulletX = playerX
                        bullet(bulletX, bulletY)
                elif level_count >= 3 and level_count != 7:
                    if bullet_count < bullet_max:
                        if bullet_state == "ready":
                            bullet_count = bullet_count + 1
                            if bullet_temp < enemy_count:
                                enemyY[num_of_enemy - 1] = 441
                            bullet_temp -= 1
                            bulletSound = mixer.Sound(os.path.join(spiriteFolderPath,"gunshot.wav"))
                            bulletSound.play()
                            bulletX = playerX
                            bullet(bulletX, bulletY)
                    else:
                        enemyY[num_of_enemy - 1] = 441
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0
    if playerX > 736:
        playerX = 736
    if playerX < 0:
        playerX = 0

    playerX += playerX_change

    for i in range(num_of_enemy):
        # Level 7
        if level_count == 7:
            pygame.event.get()
            pygame.event.pump()
            if time.time() > close_time:
                if score_val == 86:
                    inst8()
                    level_count = 8
                else:
                    lives = lives - 1
                    inst7()
                    score_val = 74
                    if lives <= 0:
                        for j in range(num_of_enemy):
                            enemyY[j] = 1000
                        over_text(75, 200)
                        restart()
                        break
                    else:
                        temp = 15
                        close_time = time.time() + delay
            else:
                counter = int(close_time - time.time())
                if counter == temp - 1:
                    time_r(counter)
                    temp = counter
        # Level 8
        if level_count == 8:
            pygame.event.get()
            pygame.event.pump()
            if time.time() > close_time:
                if score_val == 101:
                    over_text(75, 200)
                    restart()
                    break
                else:
                    lives = lives - 1
                    inst8()
                    score_val = 85
                    bullet_temp = bullet_max
                    if lives <= 0:
                        for j in range(num_of_enemy):
                            enemyY[j] = 1000
                        over_text(75, 200)
                        restart()
                        break
                    else:
                        temp = 30
                        close_time = time.time() + delay
            else:
                counter = int(close_time - time.time())
                if counter == temp - 1:
                    time_r(counter)
                    temp = counter
        # When alien reaches the spaceship
        if enemyY[i] > 440:
            lives = lives - 1
            bullet_temp = bullet_max
            if lives > 0:
                if level_count == 1:
                    score_val = 0
                    inst1()
                    num_of_enemy = 5
                    regenerate()
                elif level_count == 2:
                    score_val = 15
                    num_of_enemy = 5
                elif level_count == 3:
                    score_val = 31
                elif level_count == 4:
                    score_val = 37
                elif level_count == 5:
                    score_val = 46
                elif level_count == 6:
                    score_val = 58
                elif level_count == 7:
                    score_val = 74
                elif level_count == 8:
                    score_val = 85
            for j in range(num_of_enemy):
                enemyY[j] = random.randint(40, 140)
            bullet_count = 0
            if lives < 0:
                lives = 0
        if lives == 0:
            for j in range(num_of_enemy):
                enemyY[j] = 1000
            over_text(75, 200)
            if restart() == False:
                run = True
                score_val = 0
                lives = 4
                level_count = 1
                regenerate()
            else:
                run = False
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] >= 736:
            enemyX_change[i] = -5
            enemyY[i] += enemyY_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 5
            enemyY[i] += enemyY_change[i]
        # When bullet collides the spaceship
        coll = collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if coll:
            explosionSound = mixer.Sound(os.path.join(spiriteFolderPath,"shoot.wav"))
            explosionSound.play()
            bulletY = 500
            bullet_state = "ready"
            score_val += 1
            enemy_count -= 1
            if score_val > 26 and level_count == 2:
                num_of_enemy = num_of_enemy - 1
                if num_of_enemy == 0:
                    bonus()
            elif level_count == 3:
                num_of_enemy = num_of_enemy - 1
                if num_of_enemy == 0:
                    bonus()
            elif level_count == 4 and score_val > 41:
                num_of_enemy = num_of_enemy - 1
                if num_of_enemy == 0:
                    bonus()
            elif level_count == 5 and score_val > 53:
                num_of_enemy = num_of_enemy - 1
                if num_of_enemy == 0:
                    bonus()
            elif level_count == 6 and score_val > 69:
                num_of_enemy = num_of_enemy - 1
                if num_of_enemy == 0:
                    bonus()
            elif level_count == 7 and score_val > 80:
                num_of_enemy = num_of_enemy - 1
                if num_of_enemy == 0:
                    bonus()
            elif level_count == 8 and score_val > 96:
                num_of_enemy = num_of_enemy - 1
                if num_of_enemy == 0:
                    bonus()
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(40, 140)
        enemy(enemyX[i], enemyY[i], i)
        # Aliens dropping the bomb
        if ((playerX+64>=enemyX[i] and playerX <= enemyX[i]) ):
            if score_val!=15 or score_val!=31 or score_val!= 37 or score_val!=46 or score_val!=58 or score_val!=74 or score_val!=85:
                if bomb_state == "aim":
                    if playerX>=0 and playerX<=65:
                        bombY = enemyY[i]
                        bombX = enemyX[i]-20
                    else:
                        bombY = enemyY[i]
                        bombX = enemyX[i]
                attack(bombX, bombY)
        bomb_coll = bomb_collision(bombY, playerY, bombX, playerX)
        if bomb_coll:
            bombSound = mixer.Sound(os.path.join(spiriteFolderPath,"Bomb+1.wav"))
            bombSound.play()
            bombY = 100
            bomb_state = "aim"
            lives = lives - 1
    if bomb_state == "shoot":
        attack(bombX, bombY)
        bombY += bombY_change
    if bombY > 600:
        bombY = 100
        bomb_state = "aim"
    if score_val == 15:
        bonus()
        inst2()
        for j in range(num_of_enemy):
            enemyY[j] = random.randint(40, 140)
        score_val = score_val + 1
        level_count = 2
    elif score_val == 31:
        score_val = score_val + 1
        regenerate()
        inst3()
        level_count = 3
        num_of_enemy = 5
        bullet_max = 10
        bullet_count = 0
        bullet_temp = 10
        enemy_count = 5
        for j in range(num_of_enemy):
            enemyY[j] = random.randint(40, 140)


    elif score_val == 37:
        score_val = score_val + 1
        regenerate()
        inst4()
        level_count = 4
        num_of_enemy = 5
        bullet_max = 12
        bullet_temp = 12
        bullet_count = 0
        enemy_count = 8
        for j in range(num_of_enemy):
            enemyY[j] = random.randint(40, 140)

    elif score_val == 46:
        score_val = score_val + 1
        regenerate()
        inst5()
        level_count = 5
        num_of_enemy = 5
        bullet_max = 15
        bullet_temp = 15
        bullet_count = 0
        enemy_count = 11
        for j in range(num_of_enemy):
            enemyY[j] = random.randint(40, 140)

    elif score_val == 58:
        score_val = score_val + 1
        regenerate()
        inst6()
        level_count = 6
        num_of_enemy = 5
        bullet_max = 20
        bullet_temp = 20
        bullet_count = 0
        enemy_count = 15
        for j in range(num_of_enemy):
            enemyY[j] = random.randint(40, 140)

    elif score_val == 74:
        score_val = score_val + 1
        regenerate()
        inst7()
        level_count = 7
        temp = 15
        num_of_enemy = 5
        bullet_count = 0
        delay = 15
        close_time = time.time() + delay
        time_start = close_time - delay
        for j in range(num_of_enemy):
            enemyY[j] = random.randint(40, 140)


    elif score_val == 85:
        score_val = score_val + 1
        regenerate()
        inst8()
        level_count = 8
        num_of_enemy = 5
        bullet_count = 0
        bullet_max = 25
        bullet_temp = 25
        delay = 30
        temp = 30
        enemy_count = 15
        close_time = time.time() + delay
        for j in range(num_of_enemy):
            enemyY[j] = random.randint(40, 140)
    if score_val == 101:
        success()
    if bulletY <= 0:
        bulletY = 500
        bullet_state = "ready"

    if bullet_state == "fire":
        bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    if level_count == 7 or level_count == 8:
        time_r(temp)

    player(playerX, playerY)
    show_score(650, 10)
    show_lives(650, 60)
    toPause(10, 570)

    if level_count >= 3 and level_count != 7:
        show_bullets(10, 10)
    pygame.display.update()
