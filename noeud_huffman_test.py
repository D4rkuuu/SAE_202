from noeud_huffman import Huffman
import os
import sys

print("-----------------------------------Test fonctionnalités noeud binaire")
import noeud_binaire as nb

g = nb.NoeudBinaire('G', None, None) # Arbre de valeur 'G', sans sous-arbre (feuille)
# Arbre de valeur 'F'. Sous-arbre gauche : g. Pas sous-arbre droit.
f = nb.NoeudBinaire('F', g, None)
# Arbre de valeur 'E'. Pas de sous-arbre gauche. Sous-arbre droit : f
e = nb.NoeudBinaire('E', None, f)
d = nb.NoeudBinaire('D', None, None) # Arbre de valeur 'D', sans sous-arbres (feuille)
c = nb.NoeudBinaire('C', None, None) # Arbre de valeur 'C', sans sous-arbres (feuille)
# Arbre de valeur 'B', sous-arbre gauche : c. Sous-arbre droit : d.
b = nb.NoeudBinaire('B', c, d)
# Arbre de valeur 'A', sous-arbre gauche : b. Sous-arbre droit : e.
a = nb.NoeudBinaire('A', b, e)

print(a) # Affichage de la forme de l'arbre
print("Nombre de noeuds présent dans l'arbre:", nb.NoeudBinaire.nb_NoeudBinaire)
print("Hauteur de l'arbre:", a.hauteur()) # La hauteur de l'arbre ayant pour origine A




print("\n\n-----------------------------------Test fonctionnalités noeud huffman")

import noeud_huffman as nh

texte = Huffman.enlever_accents("éàè")

print(f"Texte à encoder : {texte}")

print("\n------------Étape 1 — Effectif de chaque caractère du texte")
liste_tuples = nh.Huffman.compter_lettres(texte) # Génère les tuples (Caractère, effectif)
liste_tuples_triee = sorted(liste_tuples, key=lambda x: x[1], reverse=True) # Trie la liste dans l'ordre décroissant des effectifs

print ("Liste des binômes (Caractère, effectif) :",liste_tuples_triee)    # Affiche la liste de tuples (Caractère, effectif)

print(nh.Huffman.ascii_vers_base2(texte))

print("\n------------Étape 2 — Construction de l’arbre de Huffman")
arbreHuffman = nh.Huffman.lettres_noeuds(liste_tuples) # Construit l'arbre
print (arbreHuffman)                                   # Affiche l'arbre
print("Nombre de noeuds présent dans l'arbre:", nh.Huffman.nb_NoeudHuffman)
print("Hauteur de l'arbre:", arbreHuffman.hauteur())


# Génération des codes pour l'encodage
codes = arbreHuffman.codes_huffman()

# Affichage des codes
print("\nListe des codes de Huffman du texte:", codes)

# Affichage du texte en base 2 et encodé
print(f"Texte en base 2  : {Huffman.ascii_vers_base2(texte)}")
print(f"Encodage Huffman : {Huffman.texte_to_code(texte,codes)}")
