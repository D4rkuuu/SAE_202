import sys
import os
import unicodedata

import unicodedata as uni
import noeud_binaire as nb

class Huffman(nb.NoeudBinaire):
    nb_NoeudHuffman = 0

    def __init__(self, s, es, gauche=None, droit=None):
        """(s) est la chaîne de caractère et (es) est
        le poids de la concaténation (s), 
        - valeur devient un tuple 
        - (s) position 0 plus le calcule de la concaténation 
        - (es) position 1 avec le calcule du poids total."""
        super().__init__((s,es), gauche, droit)
        self.s = s
        self.es = es
        Huffman.nb_NoeudHuffman += 1

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

        return list(compteur_lettres.items())

    @staticmethod
    def lettres_noeuds(liste_tuples):
        noeuds = []
        for lettre, poids in liste_tuples:
            noeuds.append(Huffman(lettre, poids, None, None)) # Création de feuille

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

    def codes_huffman(self, code="", liste_codes=None):
        if liste_codes is None:
            liste_codes = [] # Crée une liste vide pour éviter que les résultats s'accumulent sur plusieurs arbres

        if self.feuille():
            liste_codes.append((self.s, code))
        else:
            # Aller à gauche -> on ajoute 0
            if self.get_gauche()  :
                self.get_gauche().codes_huffman(code + "0", liste_codes)
            # Aller à droite -> on ajoute 1
            if self.get_droit() :
                self.get_droit().codes_huffman(code + "1", liste_codes)

        return liste_codes

    @staticmethod
    def texte_to_code(texte,code_huffman):
        new_texte = ""
        for i in texte:
            for a,b in code_huffman:
                if i == a:
                    new_texte += b
        return new_texte

    @staticmethod
    def enlever_accents(texte):
        texte_normalise = unicodedata.normalize('NFD', texte)
        texte_sans_accents = ''.join(
            c for c in texte_normalise
            if unicodedata.category(c) != 'Mn'
        )
        return texte_sans_accents





