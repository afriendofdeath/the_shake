import os
import pygame
import pytest


os.environ['SDL_VIDEODRIVER'] = 'dummy'
os.environ['SDL_AUDIODRIVER'] = 'dummy'


@pytest.fixture(autouse=True)
def init_pygame():
    """Инициализирует Pygame перед тестом."""
    pygame.init()
    pygame.display.set_mode((640, 480))

    yield

    pygame.quit()
