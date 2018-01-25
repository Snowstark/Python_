import pygame.ftfont


class Button():

    def __init__(self, ai_settings, screen, msg):
        """初始化按钮属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮的属性和其他相关信息
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.ftfont.SysFont(None, 48)

        # 创建按钮的rect，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 只创建一次标签按钮
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将msg渲染为图像，并使其居中"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        # 这里rect指的是按钮，将字体image与按钮组合
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # 绘制按钮及文本
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


