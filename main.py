import pygame
import random
import math
from pygame import mixer
#INITialize pygame
pygame.init()



WIDTH = 1000;
HEIGHT = 700;

#score
score_value = 0
font = pygame.font.Font('PressStart2P-Regular.ttf', 32)

textX = 10
textY = 10

def show_score(x, y):
    #different for texting
    score = font.render("score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y));


#screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#sound
mixer.music.load('Naruto Theme - The Raising Fighting Spirit.mp3')
mixer.music.play(-1)

#title and icon
pygame.display.set_caption("you already know what it is")
icon = pygame.image.load('enemy.png')

pygame.display.set_icon(icon)

#background
background = pygame.image.load('Z8yjXc.png')

#Player
playerImg = pygame.image.load('ninja.png')
playerx = WIDTH/2 - 25
playery = HEIGHT-120
playerX_change = 0;

def player(x, y):
    #blit - drawing an image of player frame
    screen.blit(playerImg, (x, y))

#Enemy
enemyImg = pygame.image.load('enemy.png')
enemyx = random.randint(0, 736)
enemyy = 120
enemyY_change = 0.1

def enemy(x, y):
    screen.blit(enemyImg, (x, y))
    #gameOver
    if enemyy > 200:
        enemyY = 2000


#lasershow
laserImg = pygame.image.load('laser.png')
laserx = -35
lasery = playery-16
laserX_change = 0;
def laser(x, y):
   screen.blit(laserImg, (x, y))

#bullet
bulletImg = pygame.image.load('power.png')
bulletx = -35;
bullety = playery - 16;
bulletY_change = 0;
def bullet(x, y):
    screen.blit(bulletImg, (x, y))



#collision detection
def isCollided(x1, x2, y1, y2):
    distance = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))
    if distance < 27:
        return True
    return False

    

#infinite loop{
running = True
#how the game runs forever
while running:
    #rgb - red, green, blue/ MAX : 255
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    playerx += playerX_change
    enemyy += enemyY_change
    if enemyy >= playery:
        enemyy = 2000
        playery = 2000
        textX = WIDTH/2 - 128;
        textY = HEIGHT/2 - 16;
    bullety += bulletY_change


    if playerx <= 0:
        playerx = 0
    if playerx >= WIDTH-64:
        playerx = WIDTH-64;
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #keyup, keydown is released, pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                playerX_change = +0.5
        if event.type == pygame.KEYUP:
            playerX_change = 0
            laserx = -35
    
    #smoothen out keypressed
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
        laserx = playerx + 16
        laserX_change = playerX_change
        bulletx = playerx + 16
        bullety = playery - 32
        bulletY_change = -1
        bullet_Sound = mixer.Sound('Punch - Gaming Sound Effect (HD).mp3')
        bullet_Sound.play()
    else: 
        laserX_change = 0
        laserx = -35

    #render player
    player(playerx, playery)

    #render enemy
    enemy(enemyx, enemyy)

    #laser
    laser(laserx, lasery)

    #bullet
    bullet(bulletx, bullety)

    #score
    show_score(textX, textY)

    #collision
    collision = isCollided(enemyx, bulletx, enemyy, bullety)
    if collision:
        bulletx = -35
        bulletY_change = 0
        score_value += 1
        enemyx = random.randint(0, 736)
        enemyy = 120
        enemyY_change += 0.01

    #update the pygame - render method
    pygame.display.update()
#}