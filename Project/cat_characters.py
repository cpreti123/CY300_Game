import pygame

class CatCharacters(pygame.sprite.Sprite):
    '''Overall class for managing cat sprites!'''
    def __init__(self, pos):
        cat_glock_png = "Project/cat_glock.png"
        super().__init__()
        self.image = pygame.image.load(cat_glock_png).convert_alpha()
        self.rect = self.image.get_rect(center=pos)