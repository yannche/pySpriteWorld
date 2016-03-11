# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 00:45:54 2016

@author: personne
"""

from garden2 import *
import random
import numpy as np

speedup()


pr = np.zeros(shape=(512,5,512),dtype=float)

for i in range(5000):
    act = random.choice(range(5))

    p = etat()
    fonctions = [haut,bas,gauche,droite,ramasse]
    fonctions[act]()
    p2 = etat()
    
    pr[p,act,p2] += 1

for p in range(256):
    for a in range(5):
        if sum(pr[p,a] ) > 0:
            pr[p,a] /= sum( pr[p,a] )

