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
    def __init__(self, valeur : str | None = None, gauche : 'NoeudBinaire | None' = None, droit : 'NoeudBinaire | None' = None):
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

    def hauteur(self,):
        if self.arbre_vide():
            return 0
        if self.__gauche is not None:           # Si le sous arbre gauche n'est pas vide
            h_gauche = self.__gauche.hauteur()  # Alors, réutiliser la méthode hauteur sur le sous arbre gauche
        else:
            h_gauche = 1
        if self.__droit is not None:            # Si le sous arbre droit n'est pas vide
            h_droit = self.__droit.arbre_vide() # Alors, réutiliser la méthode hauteur sur le sous arbre droit
        else:
            h_droit = 1
        return 1 + max(h_gauche, h_droit)       # Rajoute 1(la racine) à la hauteur du sous arbre ayant la plus grande hauteur