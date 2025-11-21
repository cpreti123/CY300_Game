from ..Project.settings import Settings


def test_is_gems_amount_200():
    '''Test that the starting gem amount is 200.'''
    settings = Settings()
    assert settings.gems == 200 

def test_start_level_greater_than_zero_and_int():
    '''Test for making sure start level is positive integer.'''
    settings = Settings()
    assert settings.start_level > 0 and type(settings.start_level) == int
