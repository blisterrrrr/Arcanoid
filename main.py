import time
from random import randint
from math import sin, cos

import pyray
from raylib import colors


class Ball:
    speed_x = 5
    speed_y = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, ball_texture):
        pyray.draw_texture(ball_texture, self.x, self.y, colors.WHITE)

    def move(self, screen_w, screen_h, panel_x):
        if self.x <= 10:
            self.speed_x = 5
        if self.y <= 10:
            self.speed_y = 5
        if self.x >= screen_w - 100:
            self.speed_x = -5
        if self.y >= screen_h - 100:
            self.speed_y = -5

        if self.y >= screen_h - 145 and panel_x - 50 <= self.x <= panel_x + 200:
            self.speed_y = -5

        self.x += self.speed_x
        self.y += self.speed_y


def main():
    # bc = int(input('Введи количество шаров: '))
    bc = 3
    angle = randint(0, 360)
    width = 1000
    height = 600
    panel_x = int(width / 2 - 100)
    print(angle)

    ball_list = [Ball(randint(0, width - 100), randint(0, height - 100)) for e in range(bc)]

    pyray.init_window(width, height, 'balls')
    ball = pyray.load_image('basketball.png')
    ball_texture = pyray.load_texture_from_image(ball)
    pyray.unload_image(ball)
    while not pyray.window_should_close():
        pyray.begin_drawing()
        pyray.clear_background(colors.BLACK)
        for e in ball_list:
            e.draw(ball_texture)
        pyray.draw_rectangle(panel_x, height - 45, 200, 30, colors.GREEN)
        pyray.end_drawing()

        for e in ball_list:
            e.move(width, height, panel_x)

        time.sleep(0.01)

        if pyray.is_key_down(pyray.KeyboardKey.KEY_A):
            panel_x -= 5 if panel_x > 10 else 0
        elif pyray.is_key_down(pyray.KeyboardKey.KEY_D):
            panel_x += 5 if panel_x < 790 else 0

    pyray.close_window()
    pyray.unload_texture(ball_texture)


if __name__ == '__main__':
    main()
