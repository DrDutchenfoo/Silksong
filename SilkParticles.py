import random
import pygame

colour = random.randrange(240, 255)
gravity = 0.4


class Hurt(pygame.sprite.Sprite):
    def __init__(self, x, y, d):
        super(Hurt, self).__init__()
        self.image = pygame.Surface((3, 3))
        self.image.fill((colour, colour, colour))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = 0
        self.speed = random.randint(1, 6)
        self.healthspeed = random.randint(-5, 5)
        self.dashspeed = random.randint(1, 8)
        self.dashjump = random.randint(1, 2)
        self.jump = random.randint(1, 4)
        self.direction = d
        self.lifespan = 50
        self.count = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    def update(self, dt):

        self.velocity += gravity

        self.lifespan -= 1

        if self.direction == 1:
            self.rect.move_ip(self.speed, -self.jump)
            if self.lifespan == 0:
                self.kill()
        if self.direction == 2:
            self.rect.move_ip(-self.speed, -self.jump)
            if self.lifespan == 0:
                self.kill()
        if self.direction == 0:
            self.rect.move_ip(self.healthspeed, -self.jump)
            if self.lifespan == 30:
                self.kill()

        if self.direction == 3:
            self.rect.move_ip(self.dashspeed, 0)
            if self.lifespan == 47:
                self.kill()
        elif self.direction == 4:
            self.rect.move_ip(-self.dashspeed, 0)
            if self.lifespan == 47:
                self.kill()

        self.rect.move_ip(0, self.velocity * dt)


class EnemyDeath(pygame.sprite.Sprite):
    def __init__(self, x, y, d):
        super(EnemyDeath, self).__init__()
        self.image = pygame.Surface((3, 3))
        self.image.fill((255, 20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = 0
        self.speed = random.randint(2, 6)
        self.speed2 = random.randint(-3, 3)
        self.jump = random.randint(1, 3)
        self.jump2 = random.randint(1, 4)
        self.direction = d
        self.lifespan = 50

    def update(self, dt):

        self.velocity += gravity

        self.lifespan -= 1

        if self.direction == 1:
            self.rect.move_ip(self.speed, -self.jump)
            if self.lifespan == 0:
                self.kill()
        if self.direction == 2:
            self.rect.move_ip(-self.speed, -self.jump)
            if self.lifespan == 0:
                self.kill()
        if self.direction == 3:
            self.rect.move_ip(self.speed2, -self.jump2)
            if self.lifespan == 0:
                self.kill()

        self.rect.move_ip(0, self.velocity * dt)
