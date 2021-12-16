import sys
import pygame
from settings import Settings
from ship import Ship #引用类
import game_functions as gf #引用模块

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Aline Invasion")
    
    ship = Ship(screen)

    while True:
        gf.check_event(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship) 

run_game()