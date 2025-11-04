import pygame

class CatCharacters(pygame.sprite.Sprite):
    '''Overall class for managing cat sprites'''
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

 

class GlockCat(CatCharacters):
    def __init__(self, pos):
        img = "Project/images/cat_glock.png"
        super().__init__(pos, img)
        self._alive = True #apparently alive is alr a name of somthign
        self.is_attacked = False
        self.is_attacking = False
        self.hp = 100
        self.damage = 10
     
        
        #I get it now, SUPER pushes STUFF up to the parent class to be used


class EnemyCat(CatCharacters):
    def __init__(self, pos):
        img = "Project/images/enemy_cat_glock.png" # literally just has red eyebrows (for now...)
        super().__init__(pos, img)
        self._alive = True
        self.is_attacked = False
        self.is_attacking = False
        self.hp = 100
        self.damage = 10
     