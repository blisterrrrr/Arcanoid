from abc import ABC, abstractmethod
import Assets.BaseBlock as BaseB


class Brick(BaseB.B):
    hp = 2
    exp = 1
    boom = False
    ch_pl = 0.2

    def is_b(self, string):
        if string == "Brick":
            return True


class Tnt(BaseB.B):
    hp = 1
    exp = -1
    boom = True
    ch_pl = 0.0

    def is_b(self, string):
        if string == "Tnt":
            return True


class Block(BaseB.B):
    hp = 4
    exp = 2
    boom = False
    ch_pl = 0.4

    def is_b(self, string):
        if string == "Block":
            return True
