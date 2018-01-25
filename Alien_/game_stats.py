class Gamestats():

    """跟踪游戏中的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # 游戏刚启动时出于活跃状态
        self.game_active = False

    def reset_stats(self):
        """初始化游戏运行期间可能变化的统计信息"""
        self.ship_left = self.ai_settings.ship_limit
