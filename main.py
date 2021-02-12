# coding=utf-8
import weapon
import ammo
import magazine

bullets = [
    ammo.Ammo_9x18(),
    ammo.Ammo_9x18(),
    ammo.Ammo_9x18(),
    ammo.Ammo_9x18(),
    ammo.Ammo_9x18(),
    ammo.Ammo_9x18(),
    ammo.Ammo_9x18(),
    ammo.Ammo_9x18(),
    ammo.Ammo_9x18(),
    ammo.Ammo_9x18(),
    ammo.Ammo_9x18(),
    ammo.Ammo_9x18(),
    ammo.Ammo_9x18(),
    ammo.Ammo_9x18(),
    ammo.Ammo_9x18()
]

myPistol = weapon.P90(ammo.Ammo_9x18(), 1.1, magazine.Magazine_9x18_15(bullets), None)

print 'Nome: ' + myPistol.name + "\n" \
      + 'Tipo: ' + str(myPistol.type) + "\n" \
      + 'Peso: ' + str(myPistol.weight) + ' kg' + "\n" \
      + 'Acessórios: ' + str(myPistol.attachments) + "\n" \
      + 'Munição: ' + myPistol.ammo.name + "\n" \
      + 'Carregador: ' + myPistol.magazine.name + "\n"

print 'chackMagazine - ' + str(myPistol.checkMagazine())

myPistol.shot()
print 'shot'

print 'chackMagazine - ' + str(myPistol.checkMagazine())
