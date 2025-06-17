import pygame
import sys

pygame.init()
screen=pygame.display.set_mode((400,500))
pygame.display.set_caption("pygameで描画してみる")

x,y = 175,225
width,height = 50,50
velocity = 5

running=True
while running:
    pygame.time.delay(50)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= velocity
    if keys[pygame.K_RIGHT]:
        x += velocity
    if keys[pygame.K_UP]:
        y -= velocity
    if keys[pygame.K_DOWN]:
        y += velocity
        
    screen.fill((255,255,255))
    pygame.draw.rect(screen,(0,0,255),(x,y,width,height))
    pygame.display.update()
    
pygame.quit() 
