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
        """Renvoi True si l'arbre admet un sous-arbre gauche"""
        if self.__gauche is not None:
            return True
        return False
    def admet_sad(self):
        """Renvoi True si l'arbre admet un sous-arbre droit"""
        if self.__droit is not None:
            return True
        return False
    def feuille(self):
        """Renvoi True si l'arbre est une feuille"""
        if self.__gauche and self.__droit is None:
            return True
        return False
    def arbre_vide(self):
        """Renvoi True si l'arbre tout les attributs de la feuille vaut None"""
        if self.__valeur and self.__gauche and self.__droit is  None:
            return True
        return False
    def admet_un_sa(self):
        """Renvoi True si l'arbre admet seulement un sous-arbre"""
        if self.__droit is not None or self.__gauche is not None:
            return True
        return False

    def hauteur(self):
        """Renvoi la hauteur d'un noeud binaire.
        A utiliser pour la racine.
        Attention, on compte la racine comme étant le (premier étage)
        """
        if self.arbre_vide():
            return 0
        if self.__gauche is not None:  # Si le sous arbre gauche n'est pas vide
            h_gauche = self.__gauche.hauteur()  # Alors, réutiliser la méthode hauteur sur le sous arbre gauche
        else:
            h_gauche = 1       # Vaut 0 si c'est une feuille
        if self.__droit is not None:  # Si le sous arbre droit n'est pas vide
            h_droit = self.__droit.hauteur()  # Alors, réutiliser la méthode hauteur sur le sous arbre droit
        else:
            h_droit = 1         # Vaut 0 si c'est une feuille
        return 1 + max(h_gauche,h_droit) # Rajoute 1(la racine) à la hauteur du sous arbre ayant la plus grande hauteur"

    def __str__(self):
        """
        Appelle la méthode privée _afficher_arbre pour afficher l'arbre
        """
        print("Affichage de la forme de l'arbre:")
        return self._afficher_arbre(niveau=0) #Niveau = 0 pour que ça soit bien aligné

    def _afficher_arbre(self, niveau):
        """Gère l'affichage de l'arbre """
        affiche = str(self.get_valeur())
        tab = "    " * (niveau)

        # SAG
        if self.admet_sag():
            affiche += "\n" + tab + "|-->" + self.__gauche._afficher_arbre(niveau + 1)
        elif self.admet_un_sa():
            affiche += "\n" + tab + "|-->"  # Garde un espace vide si seul le côté droit existe

        # SAD
        if self.admet_sad():
            affiche += "\n" + tab + "|-->" + self.__droit._afficher_arbre(niveau + 1)
        elif self.admet_un_sa():
            affiche += "\n" + tab + "|-->"  # Garde un espace vide si seul le côté gauche existe

        return affiche