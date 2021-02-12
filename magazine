# coding=utf-8
class Magazine:
    def __init__(self, name, capacity, bullets):
        self.name = name
        self.capacity = capacity
        self.bullets = bullets

        if len(bullets) > self.capacity:
            raise Exception("O carregador não pode ter mais que {} balas".format(self.capacity))


class Magazine_9x18_15(Magazine):
    def __init__(self, bullets):
        Magazine.__init__(self, "9x18_15", 15, bullets)
