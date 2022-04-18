import pygame
pygame.init()

#LEVEL 1 SCREEN SETUP
window = [800, 600]
screen = pygame.display.set_mode(window)
white = pygame.color.Color('#FFFFFF')
text_font = pygame.font.Font('fonts/ARCADECLASSIC.ttf',45)
level1Text = text_font.render('LEVEL 1', False, "Purple")
health = text_font.render('HEALTH', False, "Purple")
player = pygame.image.load('graphics/UziVlone.png')


#PLAYER STARTING POSITION
Playerx = 360
Playery = 360



dead = False
while not dead:

    screen.fill(white)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        Playerx += 0.1
    if keys[pygame.K_a]:
        Playerx -= 0.1
    if keys[pygame.K_w]:
        Playery -= 0.1
    if keys[pygame.K_s]:
        Playery += 0.1
    screen.blit(player, (Playerx,Playery))
    screen.blit(level1Text,(300,15))
    pygame.display.flip()
    


    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            pygame.quit()
            exit()