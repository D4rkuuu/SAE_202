import sys
import os
import unicodedata as uni
import noeud_binaire as nb

class Huffman(nb.NoeudBinaire):

    def __init__(self, s, es, gauche, droit):
        """(s) est la chaîne de caractère et (es) est
        le poids de la concaténation (s), 
        - valeur devient un tuple 
        - (s) position 0 plus le calcule de la concaténation 
        - (es) position 1 avec le calcule du poids total."""
        super().__init__((s,es), gauche, droit)
        self.s = s
        self.es = es

    @staticmethod
    def compter_lettres(texte):
        compteur_lettres = {}

        for i in texte:
            compteur_lettres[i] = compteur_lettres.get(i, 0) + 1

        return compteur_lettres

    @staticmethod
    def lettres_noeuds(noeuds):
        while len(noeuds) > 1:
            noeuds.sort(key=lambda x: x.es)

            gauche = noeuds.pop(0)
            droit = noeuds.pop(0)

            nouveau = Huffman(
                gauche.s + droit.s,gauche.es + droit.es, gauche,droit
            )

            noeuds.append(nouveau)

        return noeuds[0]

    def __repr__(self):
        return f"({self.s}, {self.es})"

    #def arbre_huffman(self,noeuds):

    @staticmethod
    def ascii_vers_base2(text):
        res = ""
        for c in text:
            res += format(ord(c), "08b")
        return res