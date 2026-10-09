"""
Brick: a single brick with configurable type and durability.
"""

import pygame


class Brick:
    NORMAL = "normal"
    STRONG = "strong"
    UNBREAKABLE = "unbreakable"

    COLORS = {
        NORMAL: (200, 90, 90),
        STRONG: (230, 180, 60),
        UNBREAKABLE: (100, 100, 110),
    }

    HITS = {
        NORMAL: 1,
        STRONG: 3,
        UNBREAKABLE: None,
    }

    def __init__(self, x, y, width, height, brick_type=NORMAL):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.brick_type = brick_type
        self.hits_remaining = self.HITS[brick_type]
        self.color = self.COLORS[brick_type]

    @property
    def is_breakable(self):
        return self.brick_type != self.UNBREAKABLE

    def get_rect(self):
        return pygame.Rect(int(self.x), int(self.y), self.width, self.height)