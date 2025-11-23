class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics and read the all-time high score from a file."""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False  # 游戏是否正在进行

        # 尝试从文件读取历史最高分
        try:
            with open('high_score.txt') as f:
                self.high_score = int(f.read())
        except (FileNotFoundError, ValueError):
            # 文件不存在或内容错误时，最高分设为0
            self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        # 注意：self.high_score 不在这里重置
