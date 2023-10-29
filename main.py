import datetime

import pyray
from raylib import colors


def main():
    # Инициализация окна
    window_width = 800
    window_height = 600
    pyray.init_window(window_width, window_height, 'Hello, raylib')
    pyray.set_exit_key(pyray.KeyboardKey.KEY_F8)
    pyray.set_target_fps(120)

    # Инициализация глобальных переменных
    scene_index = 0
    scene_changed = True
    background_color = colors.BLACK

    # Инициализация сцены 0 (menu)
    scene_0_button_new_geometry = pyray.Rectangle(window_width / 2 - 100 / 2, window_height / 2 - 10 - 50, 100, 50)
    scene_0_button_exit_geometry = pyray.Rectangle(window_width / 2 - 100 / 2, window_height / 2 + 10, 100, 50)

    motion_seconds = 3
    motion_start = datetime.datetime.now()
    motion_now = datetime.datetime.now()
    percent_completed = 0
    line_color = colors.WHITE

    # Инициализация сцены 1 (game)
    ball_image = pyray.load_image('basketball.png')
    ball_texture = pyray.load_texture_from_image(ball_image)
    pyray.unload_image(ball_image)
    del ball_image

    max_collision_count = 5

    collision_text_format = 'Collisions: {}/' + str(max_collision_count)

    ball_0_position = pyray.Vector2(10, 10)
    ball_0_shift = [1, 1]
    ball_1_position = pyray.Vector2(500, 100)
    ball_1_shift = [-1, 1]
    ball_2_position = pyray.Vector2(400, 500)
    ball_2_shift = [-1, -1]
    collision_count = 0

    # Инициализация сцены 2 (gameover)
    max_wait_seconds = 3
    wait_seconds = 0
    gameover_text_format = 'Game over ({}/{})'.format('{}', max_wait_seconds)
    open_scene_datetime = datetime.datetime.now()

    # Основной цикл программы
    while not pyray.window_should_close():

        # Действия, выполняемые при первом появлении сцены на экране
        if scene_changed:
            scene_changed = False
            if scene_index == 0:  # menu
                motion_start = datetime.datetime.now()
                motion_now = datetime.datetime.now()
                percent_completed = 0
            elif scene_index == 1:  # game
                ball_0_position = pyray.Vector2(10, 10)
                ball_0_shift = [1, 1]
                ball_1_position = pyray.Vector2(500, 100)
                ball_1_shift = [-1, 1]
                ball_2_position = pyray.Vector2(400, 500)
                ball_2_shift = [-1, -1]
                collision_count = 0
            elif scene_index == 2:  # gameover
                open_scene_datetime = datetime.datetime.now()

        # Обработка событий различных сцен (при каждом кадре)
        if not scene_changed:
            if scene_index == 0:  # menu
                if pyray.gui_button(scene_0_button_new_geometry, 'New game'):
                    scene_changed = True
                    scene_index = 1
                if pyray.gui_button(scene_0_button_exit_geometry, 'Exit'):
                    pyray.close_window()
                    exit(0)
            elif scene_index == 1:  # game
                if pyray.is_key_down(pyray.KeyboardKey.KEY_ESCAPE):
                    scene_changed = True
                    scene_index = 0
            elif scene_index == 2:  # gameover
                if pyray.is_key_down(pyray.KeyboardKey.KEY_ESCAPE):
                    scene_changed = True
                    scene_index = 0

        # Обработка логики работы сцен (при каждом кадре)
        if not scene_changed:
            if scene_index == 0:  # menu
                motion_now = datetime.datetime.now()
                delta = (motion_now - motion_start)
                ms = delta.seconds * 1000000 + delta.microseconds
                percent_completed = min(1.0, ms / (motion_seconds * 1000000))
            elif scene_index == 1:  # game
                # Движение мячиков
                ball_0_position.x += ball_0_shift[0]
                ball_0_position.y += ball_0_shift[1]
                ball_1_position.x += ball_1_shift[0]
                ball_1_position.y += ball_1_shift[1]
                ball_2_position.x += ball_2_shift[0]
                ball_2_position.y += ball_2_shift[1]

                # Отражение от стенок
                if ball_0_position.x < 0 or ball_0_position.x + ball_texture.width > window_width:
                    ball_0_shift[0] *= -1
                if ball_0_position.y < 0 or ball_0_position.y + ball_texture.height > window_height:
                    ball_0_shift[1] *= -1
                if ball_1_position.x < 0 or ball_1_position.x + ball_texture.width > window_width:
                    ball_1_shift[0] *= -1
                if ball_1_position.y < 0 or ball_1_position.y + ball_texture.height > window_height:
                    ball_1_shift[1] *= -1
                if ball_2_position.x < 0 or ball_2_position.x + ball_texture.width > window_width:
                    ball_2_shift[0] *= -1
                if ball_2_position.y < 0 or ball_2_position.y + ball_texture.height > window_height:
                    ball_2_shift[1] *= -1

                # Обработка коллизий
                ball_0_center = pyray.Vector2(ball_0_position.x + ball_texture.width / 2,
                                              ball_0_position.y + ball_texture.height / 2)
                ball_0_radius = ball_texture.width / 2
                ball_1_center = pyray.Vector2(ball_1_position.x + ball_texture.width / 2,
                                              ball_1_position.y + ball_texture.height / 2)
                ball_1_radius = ball_texture.width / 2
                ball_2_center = pyray.Vector2(ball_2_position.x + ball_texture.width / 2,
                                              ball_2_position.y + ball_texture.height / 2)
                ball_2_radius = ball_texture.width / 2
                if pyray.check_collision_circles(ball_0_center, ball_0_radius, ball_1_center, ball_1_radius):
                    ball_0_shift, ball_1_shift = ball_1_shift, ball_0_shift
                    collision_count += 1
                if pyray.check_collision_circles(ball_0_center, ball_0_radius, ball_2_center, ball_2_radius):
                    ball_0_shift, ball_2_shift = ball_2_shift, ball_0_shift
                    collision_count += 1
                if pyray.check_collision_circles(ball_1_center, ball_1_radius, ball_2_center, ball_2_radius):
                    ball_1_shift, ball_2_shift = ball_2_shift, ball_1_shift
                    collision_count += 1

                # Переключение сцен при достижении нужного количества коллизий
                if collision_count == max_collision_count:
                    scene_changed = True
                    scene_index = 2

            elif scene_index == 2:  # gameover
                now = datetime.datetime.now()
                wait_seconds = (now - open_scene_datetime).seconds

                # Переключение сцен при достижении нужного количества секунд (микросекунд)
                if wait_seconds == max_wait_seconds:
                    scene_changed = True
                    scene_index = 0

        # Обработка отрисовки различных сцен (при каждом кадре)
        if not scene_changed:
            pyray.begin_drawing()
            pyray.clear_background(background_color)

            if scene_index == 0:  # menu
                # четыре анимированные линии (две кнопки уже отрисовались)
                pyray.draw_line_ex(pyray.Vector2(100, 100), pyray.Vector2(100 + 600 * percent_completed, 100),
                                   4, line_color)
                pyray.draw_line_ex(pyray.Vector2(700, 100), pyray.Vector2(700, 100 + 400 * percent_completed, ),
                                   4, line_color)
                pyray.draw_line_ex(pyray.Vector2(700, 500), pyray.Vector2(700 - 600 * percent_completed, 500),
                                   4, line_color)
                pyray.draw_line_ex(pyray.Vector2(100, 500), pyray.Vector2(100, 500 - 400 * percent_completed),
                                   4, line_color)
            elif scene_index == 1:  # game
                pyray.draw_texture_v(ball_texture, ball_0_position, colors.WHITE)
                pyray.draw_texture_v(ball_texture, ball_1_position, colors.WHITE)
                pyray.draw_texture_v(ball_texture, ball_2_position, colors.WHITE)
                pyray.draw_text(collision_text_format.format(collision_count), 10, 10, 78, colors.WHITE)
            elif scene_index == 2:  # gameover
                pyray.draw_text(gameover_text_format.format(wait_seconds), 100, 250, 78, colors.RED)

            pyray.end_drawing()

    pyray.unload_texture(ball_texture)
    pyray.close_window()
    exit(0)


if __name__ == '__main__':
    main()
