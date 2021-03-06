from __future__ import absolute_import, print_function, unicode_literals
from gameclass import Game,check_init_game_done
from spritebuilder import SpriteBuilder
from players import Player
from sprite import MovingSprite
from ontology import Ontology
from itertools import chain
import pygame
import glo

"""
    Ce fichier est specifique au sprite dans le monde discret (e.g. tiles 32x32),
    Il contient aussi les commandes de base (tournegauche, avance...)
"""


class GardenSpriteBuilder(SpriteBuilder):
    """ classe permettant d'afficher le personnage sous 4 angles differents
    """
    def basicPlayerFactory(self,tileid,x=0.0,y=0.0):
        imglist = [self.sheet[i, j] for i, j in ((10, 0), (8, 0), (9, 0), (11, 0))]
        p = Player("joueur", tileid, x, y, imglist)
        if tileid is not None and tileid[0] in [10, 8, 9, 11]:
            p.translate_sprite(0, 0, 90 * [10, 8, 9, 11].index(tileid[0]))
        return p

#############################################################################

game = Game()


def rempli_panier_de_citrouilles(n=3):
    for i in range(n):
        game.player.inventory.add( game.spriteBuilder.basicSpriteFactory('ramassable',(10,12),x=0,y=0) )

def init(_boardname=None):
    global player,game
    name = _boardname if _boardname is not None else 'gardenofdelight'
    game = Game('Cartes/' + name + '.json', GardenSpriteBuilder)
    game.O = Ontology(True, 'SpriteSheet-32x32/tiny_spritesheet_ontology.csv')
    game.populate_sprite_names(game.O)
    game.fps = 60  # frames per second
    game.mainiteration()
    player = game.player
    if _boardname in ['planter_enclos','panier_plein']:
        rempli_panier_de_citrouilles(100)


@check_init_game_done
def tournegauche(p=None):
    p = player if p is None else p
    p.translate_sprite(0, 0, -90)
    game.mainiteration()

@check_init_game_done
def tournedroite(p=None):
    p = player if p is None else p
    p.translate_sprite(0, 0, 90)
    game.mainiteration()

@check_init_game_done
def avance(p=None):
    p = player if p is None else p
    p.forward(p.rect.width)
    game.mainiteration()
    if ( p.cherche_mortel(game.layers) ):
        import time
        print('####################')
        print('####  Game Over ####')
        print('####################')
        time.sleep(2)
        pygame.quit()
        quit()
    return p.position_changed()

@check_init_game_done
def ramasse(p=None):
    p = player if p is None else p
    o = p.ramasse(game.layers)
    game.mainiteration()
    return game.O.firstname(o)

@check_init_game_done
def obstacle(p=None):
    p = player if p is None else p
    p.forward(p.rect.width)
    hors = game.mask.out_of_screen(p)
    coll = game.mask.collision_blocking_player(p)
    p.resume_to_backup()
    return hors or coll != []

@check_init_game_done
def depose(nom=None,p=None):
    def _filtre(o): return nom in game.O.names(o) + [None]

    p = player if p is None else p
    o = p.depose(game.layers, _filtre)
    game.mainiteration()
    return game.O.firstname(o)

@check_init_game_done
def cherche(nom=None,p=None):
    def _filtre(o): return nom in game.O.names(o) + [None]

    p = player if p is None else p
    o = p.cherche_ramassable(game.layers, _filtre)
    game.mainiteration()
    return game.O.firstname(o)


tg, td, av, ra, dp, ch, reset, ob = tournegauche, tournedroite, avance, ramasse, depose, cherche, init, obstacle
