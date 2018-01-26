import sys

import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_events(event, ai_settings, screen, ship, bullets, stats, aliens, sb):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p:
        start_game(stats, aliens, ship, bullets, ai_settings, screen, sb)


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_play_button(stats, play_button, mouse_x, mouse_y, aliens, ship, bullets, ai_settings, screen, sb):
    """单击图标开始游戏"""
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        start_game(stats, aliens, ship, bullets, ai_settings, screen, sb)


def check_events(ai_settings, screen, ship, bullets, stats, play_button, aliens, sb):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets, stats, aliens, sb)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN and not stats.game_active:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y, aliens, ship, bullets, ai_settings, screen, sb)


def update_screen(ai_settings, screen, ship, aliens, bullets, play_button, stats, sb):
    """更新屏幕上的图像，并切换到新屏幕"""

    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # 当游戏处于非活跃状态，创建button按钮
    if not stats.game_active:
        play_button.draw_button()

    # Draw scoreboard
    sb.show_score()

    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, bullets, aliens, stats, sb):
    """子弹的相关管理
    :rtype: object
    """
    # 更新子弹位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    check_bullets_aliens_collisions(bullets, aliens, ai_settings, screen, ship, stats, sb)
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def check_bullets_aliens_collisions(bullets, aliens, ai_settings, screen, ship, stats, sb):
    # 检查是否有子弹命中
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_score * len(aliens)
            sb.prep_score()
    # 检查外星人是否被全部消灭
    # 若全部被消灭，则创建新的外星人群
    if 0 == len(aliens):
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)
        stats.level += 1
        sb.prep_level()
    # Check score
    check_high_score(stats, sb)


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed_factor
    ai_settings.fleet_direction *= -1


def check_fleet_edges(ai_settings, aliens):
    """检查外星人是否位于边界位置"""
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def update_aliens(ai_settings, aliens, ship, stats, screen, bullets, sb):
    """检查是否有外星人位于边界位置并更新外星人人群中的所有外星人位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)

    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb)


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb):
    """响应被外星人撞到的飞船"""
    # 如果有剩余飞船将ship_left减去1
    if stats.ship_left > 1:
        
        stats.ship_left -= 1
        sb.prep_ships()

        # 清空外星人与子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并重置飞船位置
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂停
        sleep(0.5)
        
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有到限制，就发射一颗子弹"""
    # 创建一颗子弹并加入编组
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    """创建外星人群"""
    # 计算
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并加入该行"""
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    alien = Alien(ai_settings, screen)
    number_alien_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  alien.rect.height)

    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(ai_settings, screen, aliens, alien_number,
                         row_number)


def get_number_rows(ai_settings,ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height)
                         - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb):
    """检查是否有外星人到达屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 失去一次机会
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)
            break


def start_game(stats, aliens, ship, bullets, ai_settings, screen, sb):

    # 重置
    stats.reset_stats()
    stats.game_active = True
    ai_settings.initialize_dynamic_settings()

    # 清除残局
    aliens.empty()
    bullets.empty()

    # 创建新的一局
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

    # 隐藏光标
    pygame.mouse.set_visible(False)

    # Flesh
    sb.prep_score()
    sb.prep_level()
    sb.prep_ships()


def check_high_score(stats, sb):
    """Prepare for the highest score"""
    if stats.score > stats.highest_score:
        stats.highest_score = stats.score
        sb.prep_highest_score()
