import pygame
pygame.init()


win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("POPSMOKE SIMULATOR")

player = pygame.image.load('graphics/popSmoke.jpg').convert_alpha()

x = 250
y = 250
velocity = 10


#GAME LOOP
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    userInput = pygame.key.get_pressed()

    if userInput[pygame.K_LEFT]:
        x -= velocity
        print('left')
    if userInput[pygame.K_RIGHT]:
        x += velocity
        print('right')
    if userInput[pygame.K_UP]:
        y -= velocity
        print('up')
    if userInput[pygame.K_DOWN]:
        y += velocity
        print('down')
        
    win.blit(player, (250, 250))
   

    pygame.display.update()

