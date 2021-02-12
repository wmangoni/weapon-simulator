# coding=utf-8
class Weapon:
    def __init__(self, name, ammo, weight, magazine, attachments=None):
        self.name = name
        self.ammo = ammo
        self.weight = weight
        self.magazine = magazine
        self.attachments = attachments

    def reload(self, mag):
        self.magazine = mag

    def shot(self):
        self.magazine.bullets.pop()

    def checkMagazine(self):
        return len(self.magazine.bullets)


class Pistol(Weapon):
    type = 'Pistol'


class Submachine(Weapon):
    type = 'Submachine'


class P90(Submachine):
    def __init__(self, attachments, ammo, magazine, weight):
        Submachine.__init__(self, "P90", attachments, ammo, magazine, weight)
