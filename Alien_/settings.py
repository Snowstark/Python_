class Settings():
    """存储外星人入侵的所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_limit = 2
        self.ship_speed_factor = 1

        # 子弹设计
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 80, 60, 60
        self.bullets_allowed = 3
        self.bullet_speed_factor = 3

        # 外星人设计
        self.fleet_drop_speed_factor = 10
        self.alien_speed_factor = 1
        self.fleet_direction = 1

        # 游戏难度系数
        self.speedup_scale = 1.3

    def initialize_dynamic_settings(self):
        """初始化游戏动态参数"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale





