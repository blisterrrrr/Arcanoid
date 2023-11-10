from random import randint
import pyray
from abc import ABC, abstractmethod
from raylib import colors
import Assets.CustomBlock as CustomB




def main():
    # text data
    width = 800
    height = 600
    pyray.init_window(width, height, "HI MEN or MOMEN")
    font = pyray.load_font_ex('comic_sans_ms.ttf', 68, None, 0)
    t = "DO YOU WANT"
    p = "TO PLAY"
    y = "YES"
    f = 0
    i = 0
    # main code
    while not pyray.window_should_close():
        keys = []
        while value := pyray.get_key_pressed():
            keys.append(value)
        if pyray.is_key_down(pyray.KeyboardKey.KEY_SPACE):
            f = 1
        # draw back
        pyray.begin_drawing()
        pyray.clear_background(colors.BLACK)
        pyray.draw_text_ex(font, '{}'.format(t), pyray.Vector2(150, 60), 80, 1, colors.WHITE)
        pyray.draw_text_ex(font, '{}'.format(p), pyray.Vector2(180, 180), 100, 1, colors.WHITE)
        if not f:
            pyray.draw_rectangle_lines(
                300, 300, 200, 100,
                colors.WHITE)
            pyray.draw_text_ex(font, '{}'.format(y), pyray.Vector2(315, 310), 90, 1, colors.WHITE)
        pyray.end_drawing()
        if f:
            pyray.draw_rectangle(
                300, 300, 200, 100,
                colors.WHITE)
            pyray.draw_text_ex(font, '{}'.format(y), pyray.Vector2(315, 310), 90, 1, colors.BLACK)
            i += 1
        if i == 1000:
            pyray.close_window()
            # blocks
            block = []
            for m in range(5):
                b = []
                for n in range(10):
                    k = randint(0, 1000)
                    if k <= 5:
                        b.append(0)
                    if 5 < k <= 650:
                        b.append(CustomB.Brick())
                    if 650 < k <= 700:
                        b.append(CustomB.Tnt())
                    if 700 < k <= 1000:
                        b.append(CustomB.Block())
                block.append(b)
                print(b)
            print(block)
            bx = 10
            by = 50

            i = 0
            exp = 0
            flag = 1
            # text data
            font = pyray.load_font_ex('comic_sans_ms.ttf', 68, None, 0)

            # ball data
            width = 800
            height = 600
            pyray.init_window(width, height, "Hello")
            ball = pyray.load_image('basketball.png')
            ball_texture = pyray.load_texture_from_image(ball)
            pyray.unload_image(ball)
            flx = 1
            fly = 1
            speed_ball = 0.2
            count = 0

            # vector data
            vec_x = randint(0, 800)
            vec_y = randint(0, 600)
            rad = ((vec_x - width // 2 - ball_texture.width // 2) ** 2 + (
                    vec_y - height // 2 - ball_texture.height // 2) ** 2) ** 0.5
            cos_x = round((vec_x - width // 2 - ball_texture.width // 2) / rad, 6)
            sin_x = round((vec_y - height // 2 - ball_texture.height // 2) / rad, 6)

            # rectangle data
            rec_width = 180
            rec_height = 5
            rec_x = width // 2 - rec_width // 2
            rec_y = height - rec_height - 5
            tx = 1
            ball_x = width // 2 - ball_texture.width // 2
            ball_y = height // 2 - ball_texture.height // 2

            # rec_l = 1
            # rec_r = 1
            # main code
            while not pyray.window_should_close():
                # if platform
                keys = []
                while value := pyray.get_key_pressed():
                    keys.append(value)
                if pyray.is_key_down(pyray.KeyboardKey.KEY_A):
                    if rec_x >= tx:
                        rec_x -= tx
                if pyray.is_key_down(pyray.KeyboardKey.KEY_D):
                    if rec_x <= width - tx - rec_width:
                        rec_x += tx

                # if ball
                if int(ball_x) <= 0 or int(ball_x) >= width - ball_texture.width:
                    flx *= -1
                if int(ball_y) <= 0:
                    fly *= -1
                if (rec_x - ball_texture.width <= int(ball_x) <= rec_x + rec_width
                        and int(ball_y) == rec_y - ball_texture.height):
                    fly *= -1

                # geometry
                if flx == 1:
                    ball_x += speed_ball * cos_x
                if fly == 1:
                    ball_y += speed_ball * sin_x
                if flx == -1:
                    ball_x -= speed_ball * cos_x
                if fly == -1:
                    ball_y -= speed_ball * sin_x

                # draw back
                pyray.begin_drawing()
                if flag:
                    pyray.clear_background(colors.BLACK)
                    pyray.draw_text_ex(font, '{}'.format(count), pyray.Vector2(width // 2 - 20, 10), 32, 1,
                                       colors.WHITE)
                    pyray.draw_text_ex(font, '{}'.format(exp), pyray.Vector2(width // 2 + 20, 10), 32, 1, colors.WHITE)

                    # draw figures
                    pyray.draw_line_ex(
                        pyray.Vector2(width / 2, height / 2),
                        pyray.Vector2(vec_x, vec_y),
                        3, colors.BLACK)
                    if i // 2:
                        pyray.draw_texture(ball_texture,
                                           int(ball_x), int(ball_y),
                                           colors.WHITE)

                    pyray.draw_rectangle(
                        int(rec_x), rec_y, rec_width, rec_height,
                        colors.YELLOW)

                    # draw blocks
                    for m in range(5):
                        for n in range(10):
                            if block[m][n] == 0:
                                bx += 78
                            else:
                                flx, fly, count, ep, yes_no = block[m][n].touch(bx, by, ball_x, ball_y, flx, fly,
                                                                                ball_texture, count)
                                exp += ep
                                if block[m][n].hp > 0 and not yes_no:
                                    if block[m][n].is_b("Brick"):
                                        pyray.draw_rectangle(
                                            bx, by, 75, 25,
                                            colors.BROWN)
                                        bx += 78
                                    if block[m][n].is_b("Tnt"):
                                        pyray.draw_rectangle(
                                            bx, by, 75, 25,
                                            colors.RED)
                                        bx += 78
                                    if block[m][n].is_b("Block"):
                                        pyray.draw_rectangle(
                                            bx, by, 75, 25,
                                            colors.GRAY)
                                        bx += 78
                                    if block[m][n].boom:
                                        if n != 0 and block[m][n - 1] != 0:
                                            block[m][n - 1].hp = 0
                                        if n != 9 and block[m][n - 1] != 0:
                                            block[m][n + 1].hp = 0
                                        if m != 0 and block[m][n - 1] != 0:
                                            block[m - 1][n].hp = 0
                                        if m != 4 and block[m][n - 1] != 0:
                                            block[m + 1][n].hp = 0

                        by += 28
                        bx = 10
                    bx = 10
                    by = 50
                # crash
                if ball_y > 1000:
                    break
                if int(ball_y) >= height:
                    flag = 0
                    pyray.clear_background(colors.BLACK)
                    pyray.draw_text_ex(font, '{}'.format(count), pyray.Vector2(width // 2 - 70, 100), 64, 1,
                                       colors.WHITE)
                    pyray.draw_text_ex(font, '{}'.format(exp), pyray.Vector2(width // 2 + 70, 100), 64, 1, colors.WHITE)
                    pyray.draw_text_ex(font, 'GAME OVER', pyray.Vector2(width // 2 - 175, height // 2), 68, 2,
                                       colors.WHITE)
                    tx = 0
                # end draw
                pyray.end_drawing()
                i += 1
                speed_ball += 0.000001

            pyray.unload_texture(ball_texture)
            pyray.close_window()
    pyray.close_window()


if __name__ == '__main__':
    main()
