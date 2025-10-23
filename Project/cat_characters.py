import pygame

class CatCharacters(pygame.sprite.Sprite):
    '''Overall class for managing cat sprites'''
    def __init__(self, pos, img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect(center=pos)


class GlockCat(CatCharacters):
    def __init__(self, pos):
        img = "Project/images/cat_glock.png"
        super().__init__(pos, img)
        self._alive = True #apparently alive is alr a name of somthign
        self.hp = 100
        self.damage = 10
        
        #I get it now, SUPER pushes STUFF up to the parent class to be used
