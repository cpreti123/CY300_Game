import pygame

class Towers(pygame.sprite.Sprite):
    '''Overall class for managing tower sprites'''
    def __init__(self, pos, img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect(center=pos)


    def attack(self, target):
        current_time = pygame.time.get_ticks()
        if not hasattr(self, 'last_attack_time'):
            self.last_attack_time = 0
            self.attack_cooldown = 500  
        if current_time - self.last_attack_time >= self.attack_cooldown:
            if target._alive:
                target.hp -= self.damage
                self.is_attacking = True
                target.is_attacked = True
                self.last_attack_time = current_time  
                if target.hp <= 0:
                    target._alive = False
                    target.kill()


class FriendlyTower(Towers):
    friendly_tower_hp = 500
    friendly_tower_dmg = 20
    def __init__(self, pos):
        img = "project/images/gem_image.png"
        super().__init__(pos, img)
        self._alive = True 
        self.is_attacked = False
        self.is_attacking = False
        self.hp = self.friendly_tower_hp
        self.damage = self.friendly_tower_dmg


class EnemyTower(Towers):
    enemy_tower_hp = 500
    enemy_tower_dmg = 20
    def __init__(self, pos):
        img = "placeholder_image.txt"
        super().__init__(pos, img)
        self._alive = True 
        self.is_attacked = False
        self.is_attacking = False
        self.hp = self.enemy_tower_hp
        self.damage = self.enemy_tower_dmg
