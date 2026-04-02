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

    @staticmethod
    def generer_codes(noeud, code="", codes=None):
        if codes is None:
            codes = {}

        # feuille
        if noeud.get_gauche() is None and noeud.get_droit() is None:
            codes[noeud.get_valeur()[0]] = code
            return codes

        # gauche = 0
        if noeud.get_gauche():
            Huffman.generer_codes(noeud.get_gauche(), code + "0", codes)

        # droite = 1
        if noeud.get_droit():
            Huffman.generer_codes(noeud.get_droit(), code + "1", codes)

        return codes

    #def arbre_huffman(self,noeuds):