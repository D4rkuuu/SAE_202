import sys
import os
import unicodedata as uni
import noeud_binaire as nb

class Huffman(nb):
    def __init__(self, gauche, droit):
        """(s) est la chaîne de caratère et (es) est 
        le poids de la concaténation (s), 
        - valeur devient un tuple 
        - (s) position 0 plus le calcule de la concaténation 
        - (es) position 1 avec le calcule du poids totale."""
        
        s = gauche.valeur[0] + droit.valeur[0]
        es = gauche.valeur[1] + droit.valeur[1]
        
        super().__init_((s, es), gauche, droit)
        
       