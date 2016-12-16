from robosim import *
import robosim
import random

print("---==[ Fonction pour connaitre la valeur d'un pixel ]==---")
print("getpixel\n\n")

def init(filename=None):
    path1 = 'SpriteSheet-32x32/'
    path2 = '/home/personne/Code/pySpriteWorld/SpriteSheet-32x32/'

    robosim.init('vide')
    if filename is None:
        filename = 'star.png'

    try:
        s = pygame.image.load(path1+filename)
    except:
        s = pygame.image.load(path2+filename)

    game.layers['bg2'].add( MySprite('fond',None,0,0,[s]))
    game.layers['bg2'].draw(game.background)
    while True:
        x , y = random.randint(0,512),random.randint(0,512)
        if set_position(x,y):
            break
    oriente(random.randint(0,360))
    av();av();av()



def getpixel(x=None,y=None):
    """
    usage1: getpixel(x,y)
    renvoie la valeur (en nuance de gris entre 0 et 255) du pixel correspondant
    usage2: getpixel()
    renvoie la valeur (en nuance de gris entre 0 et 255) du pixel sous le robot
    """
    assert (x is None and y is None) or (x is not None and y is not None), "lisez l'aide de cette fonction"
    if x is None:
        x,y= position(entiers=True)
    return int( sum( game.background.get_at((x,y))[:3]  ) / 3 )




sujet="""
-----------------------------------------------------------------------------
Le but de ce TP est de localiser le robot (en simulation d'abord) sans utiliser
la fonction "position".


Vous utiliserez en particulier la fonction getpixel. (voir l'aide)
Initialement, le robot est placé au hazard dans la fenetre
-----------------------------------------------------------------------------



1) Detection statique de position
* construisez une liste faite de milliers de positions aleatoires [(3,23),(501,83),...]
  chacune de ces position est une "hypothese" quant a la position reelle du robot
* faites une fonction qui affiche a l'ecran des points rouges (avec la fonction circle)
  a chaque position de la liste passee en parametre
* faites une fonction "filtrage(L)" qui prend la liste L de positions aleatoires,
  qui examine la valeur des pixels sous le robot,
  qui examine la valeur des pixels en chacune de ces positions,
  et qui renvoie les seuls positions de la liste qui dont les pixels correspondent a ceux sous le robot
* affichez a l'ecran les points rouges correspondant aux positions possibles

2) Detection dynamique de position
* construisez une liste faite de milliers de positions aleatoires et d'orientation [(3,23,45),(501,83,330),...]

vous allez maintenant deplacer le robot ET les position+orientation de la liste simultaneement
* ecrivez une fonction qui fasse avancer de 1 pixel chaque triple de la liste, dans la direction qui est la sienne
* faites avancer le robot en ligne droite sur 50 pixels, et faites de meme avec les triplets de la liste
* utilisez la fonction filtrage 50 fois de suite pour eliminer les triplets qui ne correspondent pas aux observations

Filtrage probabiliste
* ecrivez une fonction "filtrage_probabiliste", qui elimine de la liste les triplets
  qui ne correspondent pas aux observations avec une probabilite de 1/10.
* relancez votre code avec filtrage_probabiliste

Deplacements et Rotations
* faites en sorte que le robot (et les triplets) puissent tourner sur eux-meme maintenant

Maintenir le nombre d'hypothese constant
* on souhaite que la liste ait toujours le meme nombre de triplets. Quand on elimine un triplet, rajoutez-en un tire au hazard
* ajoutez une "duree de vie" a chaque triplet, pour voir quels triplets qui ont survecu le plus longtemps

Comptage des erreurs
* ajoutez un champs "nombre d'erreur" a chaque tuple. Ce champs est incremente de 1 a chaque fois qu'un tuple n'est pas consistent avec les observations
* ecrivez une fonction "filtrage_k_erreurs" qui enleve les tuple dont le nombre d'erreurs depasse un certain seuil

Ajout de Bruit
* Pour simuler le vrai robot, on va rajouter du bruit aux Deplacements
* creez une fonction avBruit() qui avance d'un nombre de pixels compris entre 0.9 et 1.1

"""
