import pygame.ftfont
from pygame.sprite import Group


from ship import Ship


class Scoreboard():
    """Show score of game"""

    def __init__(self, ai_settings, screen, stats):
        """initialize score and relative property"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Set character of showing score
        self.text_color = (30, 30, 30)
        self.font = pygame.ftfont.SysFont(None, 48)

        # Prepare to initialize image of score
        self.prep_score()
        self.prep_highest_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Transform score into image"""
        rounded_score = round(self.stats.score, 0)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)

        # Place the image
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = (self.screen_rect.right - 20)
        self.score_rect.top = 20

    def prep_highest_score(self):
        """Transform highest score into image"""
        highest_score = round(self.stats.highest_score, 0)
        highest_score_str = "{:,}".format(highest_score)
        self.highest_score_image = (self.font.render(highest_score_str,
                                    True,  self.text_color,
                                    self.ai_settings.bg_color))

        # Place the image
        self.highest_score_image_rect = self.highest_score_image.get_rect()
        self.highest_score_image_rect.right = self.screen_rect.centerx
        self.highest_score_image_rect.top = 20

    def prep_level(self):
        """Into image"""
        self.level_image =(self.font.render(str(self.stats.level), True,
                           self.text_color, self.ai_settings.bg_color))

        # Place image
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.right = self.screen_rect.right - 20
        self.level_image_rect.top = self.score_rect.bottom + 5

    def show_score(self):
        """Show the image of score"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highest_score_image,
                         self.highest_score_image_rect)
        self.screen.blit(self.level_image, self.level_image_rect)
        # Draw ships
        self.ships.draw(self.screen)

    def prep_ships(self):
        """Show ships left"""
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
