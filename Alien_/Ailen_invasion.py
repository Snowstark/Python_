
import pygame

from settings import Settings
from ship import Ship
from alien import Alien
import game_function as gf
from pygame.sprite import Group
from game_stats import Gamestats
from button import Button


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height
    ))
    pygame.display.set_caption("Alien Invasion")

    # 创建一个play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于统计的实例
    stats = Gamestats(ai_settings)

    # 创建一个外星人
    alien = Alien(ai_settings,screen)

    # 设置背景色
    bg_color = (230,230,230)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets, stats, play_button, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, play_button, stats)
        if stats.game_active:
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens)
            gf.update_aliens(ai_settings, aliens, ship, stats, screen, bullets)
            ship.update()


run_game()
