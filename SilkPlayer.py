import pygame
from pygame.locals import (
    K_z,
    K_x,
    K_c,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
)
screen_width = 1200
screen_height = 600
gravity = 0.2


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self).__init__()
        self.image = pygame.Surface((20, 30))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 4
        self.jump = 7
        self.velocity = 1
        self.MaxVelocity = 30
        self.direction = 'R'
        self.dash = 0
        self.dashing = 0
        self.on_ground = 'N'
        self.hit = 'N'
        self.iframes = 0
        self.knockback = 'L'
        self.can_jump = 'N'
        self.spawn = 'N'

    def update(self, pressed_keys, dt):

        self.velocity += gravity * (self.velocity / 2)
        self.jump -= gravity

        if self.velocity > self.MaxVelocity:
            self.velocity = self.MaxVelocity

        if self.jump < 0:
            self.jump = 0

        if self.dash > 0:
            self.dash = self.dash - 1

        if self.hit == 'Y':
            self.dashing = 0
            self.speed = 4

        if self.hit == 'N' and (self.on_ground == 'Y' and ((pressed_keys[K_SPACE] and self.dash == 0) or self.dashing > 1)):
            self.speed = 10
            self.velocity = 1
            self.dashing += 1
            if self.direction == 'R':
                self.rect.move_ip(self.speed, 0)
            elif self.direction == 'L':
                self.rect.move_ip(-self.speed, 0)
            if self.dashing == 10:
                self.dash = 20
                self.dashing = 0
                self.speed = 4
                self.on_ground = 'N'

        if self.hit == 'N' and self.can_jump == 'Y' and pressed_keys[K_c] and self.dashing == 0:
            self.rect.move_ip(0, -self.jump)
            self.can_jump = 'Y'
        if self.hit == 'N' and pressed_keys[K_LEFT] and self.dashing == 0:
            self.rect.move_ip(-self.speed, 0)
            self.direction = 'L'
        if self.hit == 'N' and pressed_keys[K_RIGHT] and self.dashing == 0:
            self.rect.move_ip(self.speed, 0)
            self.direction = 'R'

        if not pressed_keys[K_c]:
            self.can_jump = 'N'

        self.rect.move_ip(0, self.velocity * dt)

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height

        if self.hit == 'Y':
            self.iframes += 1
            if self.iframes == 30:
                self.hit = 'N'
                self.iframes = 0
            if self.knockback == 'L':
                self.rect.move_ip(-3, -4)
            if self.knockback == 'R':
                self.rect.move_ip(3, -4)

        if self.spawn == 'Y':
            self.spawn = 'N'
        if pressed_keys[K_z]:
            self.spawn = 'Y'


class Attack(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Attack, self).__init__()
        self.image = pygame.Surface((30, 4))
        self.image.fill((80, 80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.swing = 'N'
        self.can_swing = 0
        self.swinging = 0

    def update(self, pressed_keys):

        if self.can_swing > 0:
            self.can_swing -= 1

        if self.swinging > 0:
            self.swing = 'Y'
            self.swinging += 1
            self.can_swing = 1
            if self.swinging == 15:
                self.can_swing = 15
                self.swinging = 0
                self.kill()
                self.swing = 'N'

        if self.can_swing == 0 and pressed_keys[K_x]:
            self.swinging = 1
