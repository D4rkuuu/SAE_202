import sys
import os
from typing import Optional

import unicodedata as uni

class NoeudBinaire:
    """
    Classe NoeudBinaire
        Permet de créer un noeud binaire de manière récurssive
    Attributs:
    - valeur(Integer) : la valeur du noeud courant
    - gauche(NoeudBinaire) : le sous-arbre gauche
    - droit(NoeudBinaire) : le sous-arbre droit
    """
    nb_NoeudBinaire = 0

    def __init__(self, valeur : int | None = None, gauche : 'NoeudBinaire | None' = None, droit : 'NoeudBinaire | None' = None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit
        NoeudBinaire.nb_NoeudBinaire += 1