import pygame
import sys

pygame.init()

speed = [15, 12]
size = 600, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
logo = pygame.image.load("lil_uzi_head.png")
rect = logo.get_rect()

fps = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    rect.left += speed[0]
    rect.top += speed[1]
    screen.fill((0,0,0))
    screen.blit(logo, rect)
    pygame.display.update()
    clock.tick(fps)