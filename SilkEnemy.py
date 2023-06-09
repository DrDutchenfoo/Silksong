import pygame
screen_width = 1200
screen_height = 600
gravity = 0.4


class Enemy1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Enemy1, self).__init__()
        self.image = pygame.Surface((25, 20))
        self.image.fill((10, 10, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1
        self.direction = 'R'
        self.velocity = 0
        self.knockback = 'L'
        self.hit = 'N'
        self.wait = 0
        self.health = 3

    def update(self, dt):

        self.velocity += gravity

        if self.rect.left < 0:
            self.rect.left = 0
            self.direction = 'R'
        elif self.rect.right > screen_width:
            self.rect.right = screen_width
            self.direction = 'L'

        if self.direction == 'R':
            self.speed = 2
        if self.direction == 'L':
            self.speed = -2
        self.rect.move_ip(self.speed, 0)

        if self.hit == 'Y':
            self.wait += 1
            if self.wait == 20:
                self.hit = 'N'
                self.wait = 0
            if self.knockback == 'L':
                self.rect.move_ip(-4, -3)
            if self.knockback == 'R':
                self.rect.move_ip(4, -3)

        self.rect.move_ip(0, self.velocity * dt)
