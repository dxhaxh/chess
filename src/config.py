import pygame
import os
from sound import Sound
from theme import Theme

class Config:
    def __init__(self):
        self.themes=[]
        self._addThemes()
        self.index = 0
        self.activeTheme=self.themes[self.index]
        self.moveSound = Sound(os.path.join('misc/sounds/move.wav'))
        self.captureSound = Sound(os.path.join('misc/sounds/capture.wav'))
    
    def changeTheme(self):
        self.index+=1
        self.index=self.index%len(self.themes)
        self.activeTheme = self.themes[self.index]

    def _addThemes(self):
        green = Theme((234, 235, 200), (119, 154, 88), (244, 247, 116), (172, 195, 51), '#C86464', '#C84646')
        brown = Theme((235, 239, 166), (165, 117, 80), (245, 234, 100), (209, 185, 59), '#C86464', '#C84646')
        blue = Theme((229, 228, 200), (60, 95, 135), (123, 187, 227), (43, 119, 191), '#C86464', '#C84646')
        gray = Theme((120, 119, 118), (86, 85, 84), (99, 126, 143), (82, 102, 128), '#C86464', '#C84646')
        pink = Theme((255, 194, 227), (235, 52, 152), (244, 247, 116), (172, 195, 51), '#65cfb6', '#50a18e')

        self.themes=[green, brown, blue, gray, pink]