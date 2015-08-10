from gameclass import Game
from spritebuilder import SpriteBuilder
import pygame

direction = (1,0)

def gauche():
    global direction
    direction = (direction[1],-direction[0])
    update_n_draw()

def droite():
    global direction
    direction = (-direction[1],direction[0])
    update_n_draw()

def avance():
    global direction,game
    d = game.player.rect.width
    game.player.try_dx = d*direction[0]
    game.player.try_dy = d*direction[1]
    update_n_draw()
    return game.player.rect != game.player.previous_rect

def ramasse():
    global game
    o = game.player.ramasse(game.groupDict)
    update_n_draw()
    return o

def depose():
    global game
    o = game.player.depose(game.groupDict)
    update_n_draw()
    return o

def cherche():
    global game
    o = game.player.cherche_ramassable(game.groupDict)
    update_n_draw()
    return o


def update_n_draw():
    global game
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            pygame.quit()
            quit()

    game.update()
    game.draw()
    pygame.time.wait(200)



game = Game('data/gardenofdelight.json',SpriteBuilder)
update_n_draw()
