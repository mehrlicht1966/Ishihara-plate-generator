import numpy as np
from PIL import Image
import random

class IshiharaPlate:
    def __init__(self, size=(400, 400), dot_radius=15):
        self.size = size
        self.dot_radius = dot_radius
        self.image = Image.new('RGB', self.size, (255, 255, 255))

    def generate_pattern(self, number_of_dots=100, color_blind_type='deuteranopia'):
        colors = self.get_colors(color_blind_type)
        for _ in range(number_of_dots):
            x = random.randint(0, self.size[0])
            y = random.randint(0, self.size[1])
            color = random.choice(colors)
            self.draw_dot(x, y, color)

    def draw_dot(self, x, y, color):
        for i in range(-self.dot_radius, self.dot_radius):
            for j in range(-self.dot_radius, self.dot_radius):
                if i**2 + j**2 <= self.dot_radius**2:
                    if 0 <= x+i < self.size[0] and 0 <= y+j < self.size[1]:
                        self.image.putpixel((x+i, y+j), color)

    def get_colors(self, color_blind_type):
        if color_blind_type == 'deuteranopia':
            return [(255, 0, 0), (0, 0, 255)]  # Example colors for testing
        return [(0, 255, 0), (255, 255, 0)]  # Normal colors

    def save(self, file_path):
        self.image.save(file_path)


if __name__ == '__main__':
    plate = IshiharaPlate()
    plate.generate_pattern()
    plate.save('ishihara_plate.png')
