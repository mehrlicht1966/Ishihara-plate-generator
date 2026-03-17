import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

class IshiharaPlateGenerator:
    def __init__(self, size=(100, 100), dot_color=(0.2, 0.6, 0.2), bg_color=(1, 1, 1)):
        self.size = size
        self.dot_color = dot_color
        self.bg_color = bg_color

    def create_plate(self, displayed_number):
        # Set plate background color
        plate = np.ones((self.size[0], self.size[1], 3)) * np.array(self.bg_color)

        # Define dot parameters
        num_dots = 500
        dot_radius = 3

        for _ in range(num_dots):
            y = np.random.randint(0, self.size[0])
            x = np.random.randint(0, self.size[1])

            # If within the area for the number, change dot color
            if self.is_in_number_area(x, y, displayed_number):
                plate[y-dot_radius:y+dot_radius, x-dot_radius:x+dot_radius] = np.array(self.dot_color)

        return plate

    def is_in_number_area(self, x, y, number):
        # Simplified function to check if coordinates fall within the area of the number
        # This would typically be more complex and involve the number's actual pixels
        return (number == "1" and (30 < x < 70) and (30 < y < 70))

    def display_plate(self, plate):
        plt.imshow(plate)
        plt.axis('off')
        plt.show()

if __name__ == '__main__':
    generator = IshiharaPlateGenerator()
    plate = generator.create_plate(displayed_number='1')
    generator.display_plate(plate)