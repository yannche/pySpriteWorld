"""
Global constants
"""

# Colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)

ALL_LAYERS = ["bg1","bg2","obstacles","ramassable","eye_candy","joueur","en_hauteur"]
ALL_LAYERS_SET = set(ALL_LAYERS)

NON_BG_LAYERS = [l for l in ALL_LAYERS if l not in ["bg1","bg2"]]
