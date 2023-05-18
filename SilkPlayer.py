import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
)
screen_width = 1200
screen_height = 600


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self).__init__()
        self.image = pygame.Surface((20, 30))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height
