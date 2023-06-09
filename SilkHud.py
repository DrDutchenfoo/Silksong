import pygame


class Health(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Health, self).__init__()
        self.image = pygame.Surface((35, 40))
        self.image.fill((200, 200, 200))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

