from operator import truediv
import pygame
import random
import time
clock = pygame.time.Clock()
from pygame import mixer
pygame.init()

#SCREEN WINDOW SETUP
window = [800,600]
screen = pygame.display.set_mode(window)
pygame.display.set_caption('Lil Uzi Vert Simulator By Jobega')
text_font = pygame.font.Font('fonts/ARCADECLASSIC.ttf',45)
title = text_font.render('Lil Uzi Vert Simulator',False,'Purple')
background_surface2 = pygame.image.load('graphics/city.png').convert_alpha()
background_surface1 = pygame.image.load('graphics/uzi_menu.jpg').convert_alpha()
start_img = pygame.image.load('graphics/start_btn.png').convert_alpha()
exit_img = pygame.image.load('graphics/exit_btn.png').convert_alpha()
level1Text = text_font.render('LEVEL 1', False, "Purple")
healthText = text_font.render('HEALTH-', False, "Purple")
scoreText = text_font.render('SCORE-', False, "Purple")
health = text_font.render('HEALTH', False, "Purple")
white = pygame.color.Color('#FFFFFF')
black = (0,0,0) 
rect1 = pygame.Rect(0,550,800,60)

#MENU MUSIC
mixer.music.load('sounds/XOTOUR_8bit.wav')
mixer.music.play(-1)

#CREATING BUTTONS
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

#BUTTON INTERACTION
    def draw(self):
        action  = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                level1()

        if pygame.mouse.get_pressed()[0] == [0]:
            self.clicked = False
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

#BUTTON POSITION
start_button = Button(100, 350, start_img, 0.6)
exit_button = Button(100, 450, exit_img, 0.6)

#LEVEL 1
def level1():
    mixer.music.load('sounds/PATEK_8bit.wav')
    mixer.music.play(-1)
    player = pygame.image.load('graphics/UziVlone.png')
    Playerx = 360
    Playery = 360
    dead = False
    while not dead:
        Playery += 1
        score = 0
        health = 100
        scoreDisplay = text_font.render(str(score), 1, black)
        healthDisplay = text_font.render(str(health), 1, black)
        screen.fill('white')
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            Playerx += 0.1
        if keys[pygame.K_a]:
            Playerx -= 0.1
        if keys[pygame.K_RIGHT]:
            Playerx += 0.1
        if keys[pygame.K_LEFT]:
            Playerx -= 0.1
            
#LEVEL 1 SCREEN DRAWING
        pygame.draw.rect(screen, black, rect1)
        screen.blit(scoreDisplay, (170,60))
        screen.blit(level1Text,(300,15))
        screen.blit(healthText, (10,15))
        screen.blit(scoreText, (10,60))
        screen.blit(healthDisplay, (190,14))
        screen.blit(player, (Playerx,Playery))
        

#LEVEL 1 QUIT GAME LOOP
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

#TITLE GAME LOOP
run = True
while run:

#SCREEN DRAWING
    screen.blit(background_surface1,(0,0))
    screen.blit(title,(150,15))

#IF BUTTTON PRESSED
    if exit_button.draw() == True:
                exit()
    if start_button.draw() == True:
        print("PLAY")

#END GAME LOOP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
 
    pygame.display.update()
    clock.tick(60)