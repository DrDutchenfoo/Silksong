import random
import pygame
import time
from SilkParticles import Hurt, EnemyDeath
from SilkPlayer import Player, Attack
from SilkEnemy import Enemy1
from tiles import Tile
from SilkHud import Health
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
attack = Attack(player.rect.x, player.rect.y)

health = Health(10, 10)
HX = 10
mask = pygame.sprite.Group()
for i in health.health:
    mask.add(Health(HX, 10))
    HX += 45

ouch = Hurt(0, 0, 0)
particle = pygame.sprite.Group()

enemies = pygame.sprite.Group()
enemy = Enemy1(400, 480)
enemies.add(enemy)

tile = pygame.sprite.Group()
tile.add(Tile(0, 500, screen_width, 100))

tile.add(Tile(0, 250, 120, 350))
tile.add(Tile(0, 250, 200, 40))
tile.add(Tile(0, 250, 140, 60))
tile.add(Tile(120, 450, 250, 150))

tile.add(Tile(700, 400, 100, 200))
tile.add(Tile(680, 420, 20, 180))
tile.add(Tile(800, 440, 30, 160))

running = True
while running:
    X = player.rect.x
    Y = player.rect.y
    EX = enemy.rect.x
    EY = enemy.rect.y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    pressed_keys = pygame.key.get_pressed()

    if player.direction == 'R':
        attack.rect.x = X + 10
        attack.rect.y = Y + 15
    if player.direction == 'L':
        attack.rect.x = X - 20
        attack.rect.y = Y + 15
    dt = clock.tick(60) / 30

    attack.update(pressed_keys)

    player.update(pressed_keys, dt)
    enemies.update(dt)
    particle.update(dt)

    pcollisions = pygame.sprite.spritecollide(player, tile, False)
    if pcollisions:
        for til in pcollisions:
            if player.rect.colliderect(til.rect):
                if player.rect.top < til.rect.bottom and player.rect.bottom > til.rect.bottom:
                    player.rect.top = til.rect.bottom
                if player.rect.bottom > til.rect.top and player.rect.top < til.rect.top:
                    player.rect.bottom = til.rect.top
                    player.velocity = 1
                    player.jump = 11
                    player.on_ground = 'Y'
                    player.can_jump = 'Y'
                if player.rect.left < til.rect.right and player.rect.right > til.rect.right:
                    player.rect.left = til.rect.right
                if player.rect.right > til.rect.left and player.rect.left < til.rect.left:
                    player.rect.right = til.rect.left
    ecollisions = pygame.sprite.spritecollide(enemy, tile, False)
    if ecollisions:
        for til in ecollisions:
            if enemy.rect.colliderect(til.rect):
                if enemy.rect.top < til.rect.bottom and enemy.rect.bottom > til.rect.bottom:
                    enemy.rect.top = til.rect.bottom
                elif enemy.rect.bottom > til.rect.top and enemy.rect.top < til.rect.top:
                    enemy.rect.bottom = til.rect.top
                    enemy.velocity = 0
                elif enemy.rect.left < til.rect.right and enemy.rect.right > til.rect.right:
                    enemy.rect.left = til.rect.right
                    enemy.direction = 'R'
                elif enemy.rect.right > til.rect.left and enemy.rect.left < til.rect.left:
                    enemy.rect.right = til.rect.left
                    enemy.direction = 'L'

    screen.fill((80, 0, 10))
    tile.draw(screen)
    mask.draw(screen)

    if attack.swing == 'Y':
        screen.blit(attack.image, attack.rect)
        if enemy.hit == 'N' and pygame.sprite.spritecollideany(attack, enemies):
            enemy.hit = 'Y'
            enemy.health -= 1
            if attack.rect.x < enemy.rect.x:
                enemy.knockback = 'R'
                edirection = 1
            if attack.rect.x > enemy.rect.x:
                enemy.knockback = 'L'
                edirection = 2
            for p in ouch.count:
                particle.add(EnemyDeath(random.randint(EX, EX + 25), random.randint(EY, EY + 10), edirection))
    else:
        attack.kill()

    if enemy.health == 0 and enemy.alive():
        for p in ouch.count:
            particle.add(EnemyDeath(random.randint(EX, EX + 25), random.randint(EY, EY + 5), 3))
        enemy.kill()

    screen.blit(player.image, player.rect)

    if enemy.alive():
        screen.blit(enemy.image, enemy.rect)
        enemies.draw(screen)

    particle.draw(screen)

    if player.hit == 'N' and pygame.sprite.spritecollideany(player, enemies):
        health.health.pop(0)
        mask.remove(mask)
        HX = 10
        for m in health.health:
            mask.add(Health(HX, 10))
            HX += 45
        for p in ouch.count:
            particle.add(Hurt(random.randint(HX, HX + 20), random.randint(10, 30), 0))
        time.sleep(0.2)
        player.hit = 'Y'
        player.velocity = 1
        if player.rect.x < enemy.rect.x:
            player.knockback = 'L'
            pdirection = 1
        if player.rect.x > enemy.rect.x:
            player.knockback = 'R'
            pdirection = 2
        for p in ouch.count:
            particle.add(Hurt(random.randint(X, X + 20), random.randint(Y, Y + 20), pdirection))

    if player.dashing > 0:
        if player.direction == 'L':
            pdirection = 3
        elif player.direction == 'R':
            pdirection = 4
        for p in ouch.count:
            particle.add(Hurt(X + 10, Y + 15, pdirection))

    if player.spawn == 'Y':
        enemies.add(enemy)

    if 0 not in health.health:
        print('Game over')
        running = False

    pygame.display.flip()

pygame.quit()
