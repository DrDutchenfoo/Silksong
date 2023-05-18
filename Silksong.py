import pygame
from SilkPlayer import Player
from tiles import Tile
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
)
pygame.init()
screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Hollow Knight: Silksong')
clock = pygame.time.Clock()

player = Player(50, 50)
tile = pygame.sprite.Group()
tile.add(Tile(0, 500, screen_width, 100))
tile.add(Tile(screen_width / 2, 400, 120, 180))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    collisions = pygame.sprite.spritecollide(player, tile, False)
    if collisions:
        print("collision!")
        for til in collisions:
            if player.rect.colliderect(til.rect):
                if player.rect.left < til.rect.right and player.rect.right > til.rect.right:
                    player.rect.left = til.rect.right
                elif player.rect.right > til.rect.left and player.rect.left < til.rect.left:
                    player.rect.right = til.rect.left
                elif player.rect.top < til.rect.bottom and player.rect.bottom > til.rect.bottom:
                    player.rect.top = til.rect.bottom
                elif player.rect.bottom > til.rect.top and player.rect.top < til.rect.top:
                    player.rect.bottom = til.rect.top
    screen.fill((80, 0, 10))
    tile.draw(screen)
    screen.blit(player.image, player.rect)
    pygame.display.flip()

pygame.quit()
