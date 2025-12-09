from ..Project.towers import FriendlyTower
import pygame

def test_is_towers():
    '''Test for confirming that--once a friendly tower is created--it is actually "alive"!'''
    screen = pygame.display.set_mode(
    (100, 100)) #have to create a pseudo screen and whatnot for test to run
    pygame.display.set_caption("CatWar")
    pygame.display.flip()
    tower = FriendlyTower((50, 450))
    assert tower._alive #should be alive after being created!
