# Alien Invasion

一款基于《Python Crash Course (3rd Edition)》示例的射击游戏。加入了外星人子弹、护盾与最高分持久化等扩展功能，提升对抗性与可玩性。

## 目录

- 简介
- 新增功能
- 运行环境与安装
- 快速上手（运行）
- 操作说明（按键）
- 项目结构

## 新增功能

- 外星人子弹：外星人能随机向下发射子弹。
- 护盾系统：屏幕下方布置护盾单元（每个护盾有4点生命值），可抵挡外星人子弹。
- 最高分持久化：游戏会在本地保存并读取最高分，退出时自动写入。

## 运行环境与依赖

- Python 3.x
- pygame

安装依赖：

```powershell
pip install pygame
```

## 快速上手（在 Windows PowerShell）

1. 打开 PowerShell，切换到项目根目录（包含 `alien_invasion.py`）：

```powershell
cd 'path/to/project/Alien'  # 将此路径替换为你的项目根目录
```

2. 启动游戏：

```powershell
python alien_invasion.py
```

## 操作说明

- ← / →  : 控制飞船左右移动
- Space  : 发射子弹
- Q      : 退出游戏

## 项目结构（主要文件与说明）

- `alien_invasion.py`  : 游戏主入口
- `settings.py`       : 游戏设置（屏幕、速度、颜色等）
- `game_stats.py`     : 游戏统计
- `scoreboard.py`     : 分数显示与格式化
- `ship.py`           : 玩家飞船类
- `alien.py`          : 外星人类与移动逻辑
- `bullet.py`         : 玩家子弹逻辑
- `alien_bullet.py`   : 外星人子弹（新增）  
- `shield.py`         : 护盾实现（新增）
- `high_score.txt`    : 存储最高分的文本文件
- `images/`           : 游戏使用的图片资源
