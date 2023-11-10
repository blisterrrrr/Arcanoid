from abc import ABC, abstractmethod


class B(ABC):
    @abstractmethod
    def is_b(self, string):
        pass

    def touch(self, x_b, y_b, ball_x, ball_y, flx, fly, ball_texture, count):
        exp = 0
        if (x_b + 74 <= int(ball_x) == x_b + 76 or int(ball_x) == x_b - ball_texture.width) and y_b <= int(ball_y) <= y_b + 25:
            flx *= -1
            self.hp -= 1
            if self.hp == 0:
                exp += self.exp
                count += 1
        if (y_b + 24 <= int(ball_y) <= y_b + 26 or int(ball_y) == y_b - ball_texture.height) and x_b <= int(ball_x) <= x_b + 75:
            fly *= -1
            self.hp -= 1
            if self.hp == 0:
                exp += self.exp
                count += 1
        if exp != 0:
            return flx, fly, count, exp, True
        return flx, fly, count, exp, False
