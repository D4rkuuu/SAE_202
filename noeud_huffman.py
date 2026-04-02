import sys
import os
import unicodedata as uni
import noeud_binaire as nb

class Huffman(nb.NoeudBinaire):

    def __init__(self, s, es, gauche, droit):
        """(s) est la chaîne de caratère et (es) est 
        le poids de la concaténation (s), 
        - valeur devient un tuple 
        - (s) position 0 plus le calcule de la concaténation 
        - (es) position 1 avec le calcule du poids totale."""
        super().__init__((s,es), gauche, droit)
        self.s = s
        self.es = es

    @staticmethod
    def compter_lettres(texte):
        compteur_lettres = {}

        for i in texte:
            compteur_lettres[i] = compteur_lettres.get(i, 0) + 1

        return compteur_lettres
