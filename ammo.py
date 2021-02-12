# coding=utf-8
class Ammo:
    def __init__(self, name, speed):
        self.name = name

        # speed in m/s
        self.speed = speed


class Ammo_9x18(Ammo):
    def __init__(self):
        Ammo.__init__(self, "9x18", 385)
