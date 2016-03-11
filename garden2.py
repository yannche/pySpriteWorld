# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 00:08:25 2016

@author: personne
"""
import gardenworld
import random
gardenworld.init('garden2')
player = gardenworld.game.player
fs= 0

herbes = set([(11, 10), (11, 11), (9, 10), (9, 11), (9, 12), (9, 13), (9, 14), (10, 11), (10, 9), (7, 11), (7, 12), (7, 13), (7, 14), (11, 7), (10, 8), (11, 8), (8, 10), (8, 11), (11, 9), (8, 14)])
pots = {(3,12):1000.0,(4,9):2000.0}
teleporteurs = [(12,2),(6,6)]


def _oriente_et_av(a):
    player.translate_sprite(player.x,player.y,a,relative=False)
    if position() in herbes:
        if random.random() < 0.8:
            gardenworld.game.mainiteration( _frameskip = fs )
            return False

    r = gardenworld.av()
    gardenworld.game.mainiteration( _frameskip = fs )
    return r

def speedup():
    global fs
    fs = 100

@gardenworld.check_init_game_done
def haut():
    return _oriente_et_av(90*3)
    
@gardenworld.check_init_game_done
def bas():
    return _oriente_et_av(90)
    
@gardenworld.check_init_game_done
def gauche():
    return _oriente_et_av(90*2)
    
@gardenworld.check_init_game_done
def droite():
    return _oriente_et_av(0)

@gardenworld.check_init_game_done
def position():
    return player.get_rowcol()

@gardenworld.check_init_game_done
def etat():
    i,j = player.get_rowcol()
    return i*16+j

@gardenworld.check_init_game_done
def ramasse():
    if position() == teleporteurs[1]:
        player.set_rowcol(*teleporteurs[0])
        gardenworld.game.mainiteration( _frameskip = fs )
        return 0.0

    if position() in pots:
        recomp = pots[position()]
        player.set_rowcol(14,12)
        gardenworld.game.mainiteration( _frameskip = fs )
        return recomp
    return 0.0
