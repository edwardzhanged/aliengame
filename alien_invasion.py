
import pygame
from ship import Ship
from pygame.sprite import Group

from setting import Settings
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    bg_color=(230,230,230)

    ship=Ship(ai_settings,screen)
    bullets=Group()

    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,bullets)
        # for event in pygame.event.get():
        #     if event.type==pygame.QUIT:
        #         sys.exit()
        # screen.fill(bg_color)
        # ship.blitme()
        # pygame.display.flip()
run_game()