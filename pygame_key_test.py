import pygame
pygame.init()
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key), end="\t\t")
