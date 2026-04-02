import sys
import os
import unicodedata as uni
import noeud_binaire as nb

class Huffman(nb.NoeudBinaire):

    def __init__(self, s, es, gauche=None, droit=None):
        """(s) est la chaîne de caractère et (es) est
        le poids de la concaténation (s), 
        - valeur devient un tuple 
        - (s) position 0 plus le calcule de la concaténation 
        - (es) position 1 avec le calcule du poids total."""
        super().__init__((s,es), gauche, droit)
        self.s = s
        self.es = es

    def get_s(self):
        return self.s
    def get_es(self):
        return self.es
    def set_s(self, s):
        self.s = s
    def set_es(self, es):
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
    def ascii_vers_base2(text):
        res = ""
        for c in text:
            res += format(ord(c), "08b")
        return res

    def codes_huffman(self, code="", dico={}):
        # Si c'est une feuille (pas d'enfants)
        if self.get_gauche()   is None and self.get_droit()  is None:
            dico[self.s] = code
        else:
            # Aller à gauche -> on ajoute 0
            if self.get_gauche()  :
                self.get_gauche().codes_huffman(code + "0", dico)
            # Aller à droite -> on ajoute 1
            if self.get_droit() :
                self.get_droit().codes_huffman(code + "1", dico)

        return dico
