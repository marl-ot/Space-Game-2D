import sys
import pygame
import game_functions as gf

from settings import Settings
from ship import Ship


# Основная функция игры
def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Создание корабля.
    ship = Ship(screen)
    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши.
        gf.check_events(ship)
        # При каждом проходе цикла перерисовывается экран.
        # Прорисовка корабля.
        ship.update()
        # Отображение последнего прорисованного экрана.
        gf.update_screen(ai_settings, screen, ship)


run_game()