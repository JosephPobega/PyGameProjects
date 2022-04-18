from operator import truediv
import pygame
from sys import exit
clock = pygame.time.Clock()
from pygame import mixer
pygame.init()

#window display
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('PopSmoke Simulator')
text_font = pygame.font.Font('fonts/ARCADECLASSIC.ttf',50)
title = text_font.render('POPSMOKE SIMULATOR',False,'Red')
background_surface2 = pygame.image.load('graphics/city.png').convert_alpha()
background_surface1 = pygame.image.load('graphics/newyork_background.jpg').convert_alpha()
start_img = pygame.image.load('graphics/start_btn.png').convert_alpha()
exit_img = pygame.image.load('graphics/exit_btn.png').convert_alpha()


#main menu music
mixer.music.load('sounds/Dior_8bit.wav')
mixer.music.play(-1)


#button variables
x = 200
y = 200
scale = 3
transparent  = (0,0,0,0)
white = (0,0,0)

#button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

#make buttons interactive
    def draw(self):
        action  = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                print('PLAY')

        if pygame.mouse.get_pressed()[0] == [0]:
            self.clicked = False
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

#create button instance / position
start_button = Button(100, 200, start_img, 0.6)
exit_button = Button(100, 300, exit_img, 0.6)

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
   
#screen drawing
    screen.blit(background_surface1,(0,0))
    screen.blit(title,(300,15))

    if start_button.draw() == True:
        screen.blit(background_surface2,(0,0))
        mixer.music.load('sounds/party_8bit.wav')
        mixer.music.play(-1)
            
           
        

    if exit_button.draw() == True:
        sys.exit()

    pygame.display.update()
    clock.tick(60)