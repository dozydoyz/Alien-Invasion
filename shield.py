import pygame
from pygame.sprite import Sprite

class Shield(Sprite):
    """护盾是一个砖块，只能被敌方子弹摧毁，有两点生命值"""

    def __init__(self, ai_game, x, y):
        """创建护盾砖块"""
        super().__init__()
        self.screen = ai_game.screen
        self.color = (0, 255, 0)  # 绿色护盾
        self.width = 100
        self.height = 20
        self.rect = pygame.Rect(x, y, self.width, self.height)

        self.hit_points = 4  # 护盾生命值，4颗子弹摧毁

    def hit(self):
        """护盾被子弹击中，减少生命值"""
        self.hit_points -= 1
        if self.hit_points <= 0:
            self.kill()  # 如果生命值为0，移除护盾

    def draw(self):
        """在屏幕上绘制护盾"""
        pygame.draw.rect(self.screen, self.color, self.rect)
