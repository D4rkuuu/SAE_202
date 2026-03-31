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

# Constructeur
    def __init__(self, valeur : int | None = None, gauche : 'NoeudBinaire | None' = None, droit : 'NoeudBinaire | None' = None):
        self.__valeur = valeur
        self.__gauche = gauche
        self.__droit = droit
        NoeudBinaire.nb_NoeudBinaire += 1

# Getters/Setters
    def get_valeur(self):
        return self.__valeur

    def get_gauche(self):
        return self.__gauche

    def get_droit(self):
        return self.__droit

    def set_valeur(self, valeur):
        self.__valeur = valeur

    def set_gauche(self, gauche):
        self.__gauche = gauche

    def set_droit(self, droit):
        self.__droit = droit

# Méthodes
    def admet_sag(self):
        if self.__gauche is not None:
            return True
        return False
    def admet_sad(self):
        if self.__droit is not None:
            return True
        return False
    def feuille(self):
        if self.__gauche and self.__droit is None:
            return True
        return False
    def arbre_vide(self):
        if self.__valeur and self.__gauche and self.__droit is  None:
            return True
        return False